import os
import requests


def get_article_from_github(path_to_article):
    query_url = f'{os.getenv("GITHUB_URL")}/{path_to_article}.md'
    article = requests.get(query_url)
    return article.text


def get_json_menu_from_github():
    query_url = f'{os.getenv("GITHUB_URL")}/menu.json'
    article = requests.get(query_url)
    return article.text
