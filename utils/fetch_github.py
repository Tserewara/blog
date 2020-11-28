import requests


def get_article_from_github(path_to_article):
    query_url = f'https://raw.githubusercontent.com/Tserewara/blog-posts/master/{path_to_article}.md'
    article = requests.get(query_url)
    return article.text


def get_json_menu_from_github():
    query_url = 'https://raw.githubusercontent.com/Tserewara/blog-posts/master/menu.json'
    article = requests.get(query_url)
    return article.text
