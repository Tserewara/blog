import os
import requests


TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {'Authorization': f'token {TOKEN}'}


def get_article_from_github(path_to_article):
    query_url = f'{os.getenv("GITHUB_URL")}/{path_to_article}.md'
    article = requests.get(query_url, headers=HEADERS)
    return article.text


def get_json_menu_from_github():
    query_url = f'{os.getenv("GITHUB_URL")}/menu.json'
    article = requests.get(query_url, headers=HEADERS)
    return article.text
