import logging
from flask import Blueprint, request, render_template, redirect
from utils import get_post_by_pk, save_post_in_bookmarks, view_bookmarks

logging.basicConfig(encoding="utf-8", level=logging.INFO)
bookmarks_blueprint = Blueprint("bookmarks", __name__)

bookmarks = view_bookmarks()


@bookmarks_blueprint.route("/bookmarks/add/<int:id>/")
def save_post(id):
    """Вьюшка, которая добавляет пост в закладки и переправляет на главную страницу."""
    post = get_post_by_pk(id)
    if post not in bookmarks:
        bookmarks.append(post)
    save_post_in_bookmarks(bookmarks)
    logging.info("Запрошено добавление поста в закладки")
    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/remove/<int:id>/")
def delete_post(id):
    """Вьюшка, которая удаляет пост из закладок и переправляет на главную страницу."""
    post = get_post_by_pk(id)
    if post in bookmarks:
        bookmarks.remove(post)
    save_post_in_bookmarks(bookmarks)
    logging.info("Запрошено удаление поста из закладок")
    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/")
def open_bookmarks():
    """Вьюшка, которая показывает закладки, то есть сохраненные посты"""
    logging.info("Страница с закладками запрошена")
    return render_template("bookmarks.html", bookmarks=bookmarks)