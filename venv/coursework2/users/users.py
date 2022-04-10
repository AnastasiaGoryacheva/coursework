import logging
from flask import Blueprint, request, render_template
from utils import get_posts_by_user, view_bookmarks

logging.basicConfig(encoding="utf-8", level=logging.INFO)
users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users/<username>/")
def posts_user(username):
    """Вьюшка, которая показывает все посты определенного пользователя"""
    posts = get_posts_by_user(username)
    bookmarks = view_bookmarks()
    logging.info(f"Запрошена страница пользователя {username}")
    return render_template("user-feed.html", posts=posts, bookmarks=bookmarks)

