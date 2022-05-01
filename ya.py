import requests
from environs import Env


def get_ya_token(oauth_token: str) -> dict:
    """Get iamToken and expiresAt from yandex.
    iamToken is active 24 hours, after this time it's necessary to get new.
    """
    iam_token_url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    response = requests.post(
        url=iam_token_url, json={"yandexPassportOauthToken": env('YA_OAUTH_TOKEN')}
    )
    response.raise_for_status()
    return response.json()


def translate_word(token: str, word: str, language_code: str = "ru") -> str:
    url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
    body = {
        "targetLanguageCode": language_code,
        "texts": [word],
        "folderId": env('FOLDER_ID'),
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


if __name__ == "__main__":
    env = Env()
    env.read_env()
    print(translate_word(token=env('IAMTOKEN'), word="Decrease", language_code='ru'))
