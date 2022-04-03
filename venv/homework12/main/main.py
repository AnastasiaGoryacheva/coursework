from flask import Blueprint, request, render_template
import logging
from functions import read_posts

logging.basicConfig(encoding="utf-8", level=logging.INFO)

main_blueprint = Blueprint("main", __name__, template_folder="templates")

@main_blueprint.route("/")
def main():
    return render_template("index.html")


@main_blueprint.route("/search/")
def search_posts():
    s = request.args["s"]
    logging.info(f"Выполняется поиск слова: {s}")
    post = []
    for word in read_posts():
        if s.lower() in word["content"].lower():
            post.append(word)
    return render_template("post_list.html", word=s, post=post)

