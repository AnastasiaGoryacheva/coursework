import logging
from flask import Blueprint, request, render_template
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, get_post_by_tags, view_bookmarks

logging.basicConfig(encoding="utf-8", level=logging.INFO)
post_blueprint = Blueprint("post", __name__)


@post_blueprint.route("/")
def upload_posts():
    """Вьюшка, которая показывает ленту, то есть все посты."""
    all_posts = get_posts_all()
    bookmarks = view_bookmarks()
    logging.info("Главная страница запрошена")
    return render_template("index.html", posts=all_posts, bookmarks=bookmarks)


@post_blueprint.route("/posts/<int:id>/")
def open_post(id):
    """Вьюшка, которая показывает определенный пост"""
    post = get_post_by_pk(id)
    content = get_post_by_tags(post["content"])
    comment_post = get_comments_by_post_id(id)
    bookmarks = view_bookmarks()
    logging.info("Страница выбранного поста запрошена")
    return render_template("post.html", comments=comment_post, post=post, content=content, bookmarks=bookmarks)


