from flask import Blueprint, request, render_template
from utils import search_for_posts, view_bookmarks


search_blueprint = Blueprint("search", __name__)


@search_blueprint.route("/search")
def search():
    '''Вьюшка, каторая переправляет на страницу поиска.'''
    return render_template("search_page.html")

@search_blueprint.route("/search/")
def search_posts():
    '''Вьюшка, которая ищет и показывает посты по ключевому слову.'''
    s = request.args["s"]
    posts = search_for_posts(s)
    bookmarks = view_bookmarks()
    return render_template("search.html", word=s, posts=posts, bookmarks=bookmarks)


