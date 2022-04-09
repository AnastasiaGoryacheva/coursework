from flask import Blueprint, request, jsonify
from utils import get_posts_all, get_post_by_pk


api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/api/posts")
def posts_json():
    '''Вьюшка, которая возвращает все посты в виде json файла.'''
    data = get_posts_all()
    return jsonify(data)


@api_blueprint.route("/api/posts/<int:id>")
def post_id_json(id):
    '''Вьюшка, которая возвращает определенный пост в виде json файла.'''
    post = get_post_by_pk(id)
    return jsonify(post)

