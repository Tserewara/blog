import json
from flask import Flask, render_template
from utils.fetch_github import get_json_menu_from_github, get_article_from_github
from utils.markdown_converter import convert_markdown_to_html


app = Flask(__name__)


@app.route('/')
def home():
    menu_string = get_json_menu_from_github()
    menu = json.loads(menu_string)
    return render_template('index.html', menu=menu)

@app.route("/<path:path_to_article>")
def index(path_to_article):
    article = get_article_from_github(path_to_article)
    post_markdown = convert_markdown_to_html(article)
    return render_template('post.html', post_markdown=post_markdown)
    # return post_markdown



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
