import requests

from dotenv import load_dotenv

from urllib.parse import urlparse

import os

import argparse


def shorten_link(headers, users_url):
    headers = {
        "Authorization": f"Bearer {api_bitly_token}"
    }
    url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {
        "long_url": users_url
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(headers, users_url):
    headers = {
        "Authorization": f"Bearer {apy_bitly_token}"
    }
    parsed_url = urlparse(users_url)
    url_without_scheme = f"{parsed_url.netloc}{parsed_url.path}"
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{url_without_scheme}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(headers, users_url):    
    headers = {
        "Authorization": f"Bearer {api_bitly_token}"
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{users_url}'
    response = requests.get(url, headers=headers)
    return response.ok


if __name__ == "__main__":
    load_dotenv()
    api_bitly_token = os.environ['API_BITLY_TOKEN']
    parser = argparse.ArgumentParser(
        description='сокращает ссылку'
    )
    parser.add_argument('users_url', help='ссылка пользователя')
    args = parser.parse_args()

    try:
        if is_bitlink(api_bitly_token, args.users_url):
            print(count_clicks(api_bitly_token, args.users_url))
        else:
            print(shorten_link(api_bitly_token, args.users_url))

    except requests.exceptions.HTTPError as error:
        print('ошибка неверная ссылка', error)

