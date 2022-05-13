from django.conf import settings

import redis

import requests


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
    return response.json()


def get_yandex_token(oauth_token: str = settings.YA_OAUTH_TOKEN) -> str:
    """Try get token value from redis.
    If it's not available, fetch token from yandex.
    Strange name i_am_token got from yandex."""

    r = redis.Redis(  # noqa VNE001
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=0,
    )

    if _is_redis_available(r):
        token = r.get('iamToken')
        #  TODO add check for token expiring.
        if token:
            return token.decode('utf-8')
        i_am_token = _fetch_yandex_token(oauth_token)
        token = i_am_token['iamToken']
        r.set('iamToken', token)
    else:
        i_am_token = _fetch_yandex_token(oauth_token)
        token = i_am_token['iamToken']
    return token


def translate_word(token: str, word: str, language_code: str = "ru") -> str:
    url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
    body = {
        "targetLanguageCode": language_code,
        "texts": [word],
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
    return response.json()["translations"]
