from datetime import datetime, timezone

from dateutil.parser import ParserError, parse

from django.conf import settings

import redis

import requests


def get_hours_before_expired(expire_date: str) -> float | int:
    """Format of expire_date: '2022-05-14T20:32:09.801350141Z'.
    Return hours left before expire_date.
    Return 0 if parsing failed."""
    try:
        expire = parse(expire_date)
        delta = expire - datetime.now(timezone.utc)
        return delta.seconds // 3600
    except (ParserError, TypeError):
        return 0


def _is_redis_available(redis_instance: redis.Redis) -> bool:
    """Check redis is connected."""
    try:
        return redis_instance.ping()
    except redis.ConnectionError:
        return False


def _fetch_yandex_token(oauth_token: str) -> dict:
    """Fetch iamToken and expiresAt from yandex.
    iamToken is active 24 hours, after this time it's necessary to get new.
    """

    iam_token_url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    response = requests.post(
        url=iam_token_url,
        json={"yandexPassportOauthToken": oauth_token},
    )
    response.raise_for_status()
    # FIXME Add handler what to do if yandex is unavailable
    return response.json()


def get_yandex_token(oauth_token: str = settings.YA_OAUTH_TOKEN) -> str:
    """Try get token value from redis.
    If it's not available, fetch token from yandex.
    Strange name i_am_token got from yandex."""

    r = redis.Redis(  # noqa VNE001
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        decode_responses=True,
        db=0,
    )

    if _is_redis_available(r):
        token = r.get('iamToken')
        expires_at = r.get('iamToken_expires_at')
        if token is None or get_hours_before_expired(expires_at) > 6:
            token_response = _fetch_yandex_token(oauth_token)
            token = token_response['iamToken']
            expires_at = token_response['expiresAt']
            r.set('iamToken', token)
            r.set('iamToken_expires_at', expires_at)
    else:
        token_response = _fetch_yandex_token(oauth_token)
        print('Fetch token')
        token = token_response['iamToken']
    return token


def translate_phrase(token: str, phrase: str, language_code: str = "ru") -> str:
    url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
    body = {
        "targetLanguageCode": language_code,
        "texts": [phrase],
        "folderId": settings.FOLDER_ID,
    }

    response = requests.post(
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        url=url,
        json=body,
    )
    if response.ok:
        return response.json()["translations"]

    return response.json()
