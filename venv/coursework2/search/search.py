import logging
from flask import Blueprint, request, render_template
from utils import search_for_posts, view_bookmarks

logging.basicConfig(encoding="utf-8", level=logging.INFO)
search_blueprint = Blueprint("search", __name__)


@search_blueprint.route("/search")
def search():
    '''Вьюшка, каторая переправляет на страницу поиска.'''
    logging.info("Запрошено перенаправление на страницу поиска постов")
    return render_template("search_page.html")

@search_blueprint.route("/search/")
def search_posts():
    '''Вьюшка, которая ищет и показывает посты по ключевому слову.'''
    s = request.args["s"]
    posts = search_for_posts(s)[:10]
    bookmarks = view_bookmarks()
    logging.info(f"Поиск постов по слову: {s}")
    return render_template("search.html", word=s, posts=posts, bookmarks=bookmarks)


