import requests


def get_article_from_github(path_to_article):
<<<<<<< HEAD
    query_url = f'https://raw.githubusercontent.com/Tserewara/blog-posts/master/{path_to_article}.md'
=======
    query_url = f'{os.getenv("GITHUB_URL")}/{path_to_article}.md'
>>>>>>> 4d06ab165f6a0261be82ac0ff100c5ebc0658b40
    article = requests.get(query_url)
    return article.text


def get_json_menu_from_github():
<<<<<<< HEAD
    query_url = 'https://raw.githubusercontent.com/Tserewara/blog-posts/master/menu.json'
=======
    query_url = f'{os.getenv("GITHUB_URL")}/menu.json'
>>>>>>> 4d06ab165f6a0261be82ac0ff100c5ebc0658b40
    article = requests.get(query_url)
    return article.text
