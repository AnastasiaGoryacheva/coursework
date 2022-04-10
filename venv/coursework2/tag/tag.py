import logging
from flask import Blueprint, request, render_template
from utils import search_for_posts, view_bookmarks

logging.basicConfig(encoding="utf-8", level=logging.INFO)
tag_blueprint = Blueprint("tag", __name__)


@tag_blueprint.route("/tag/<tagname>")
def post_with_tag(tagname):
    """Вьюшка, которая показывает посты с определенным тэгом"""
    tag = f"#{tagname}"
    post = search_for_posts(tag)
    bookmarks = view_bookmarks()
    logging.info(f"Запрошена страница постов с тэгом {tag}")
    return render_template("tag.html", posts=post, tag=tag, bookmarks=bookmarks)