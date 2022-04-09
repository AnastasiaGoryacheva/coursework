from flask import Blueprint, request, render_template
from utils import search_for_posts, view_bookmarks

tag_blueprint = Blueprint("tag", __name__)


@tag_blueprint.route("/tag/<tagname>")
def post_with_tag(tagname):
    '''Вьюшка, которая показывает посты с определенным тэгом'''
    tag = f"#{tagname}"
    post = search_for_posts(tag)
    bookmarks = view_bookmarks()
    return render_template("tag.html", posts=post, tag=tag, bookmarks=bookmarks)