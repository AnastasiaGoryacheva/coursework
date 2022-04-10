import pytest
from utils import *


def test_get_posts_all():

    posts = get_posts_all()
    assert posts != None, "ошибка при выгрузке данных"


def test_get_posts_by_user():

    post_user = get_posts_by_user("sasha")[0]["poster_name"]
    assert post_user != None, "ошибка при выводе определенного пользователя"
    assert post_user == "sasha", "ошибка при выводе определенного пользователя"


def test_get_comments_by_post_id():

    comments_post = get_comments_by_post_id(1)
    assert comments_post != None, "ошибка при выводе комментариев к посту"
    assert comments_post[0]["post_id"] == 1, "ошибка при выводе комментариев к посту"

def test_search_for_posts():

    post_search = search_for_posts("суп")
    assert post_search != None, "ошибка при выводе постов по ключевому слову"
    assert post_search[0]["pk"] == 1, "ошибка при выводе постов по ключевому слову"


def test_get_post_by_pk():

    post_by_pk = get_post_by_pk(1)
    assert post_by_pk != None, "ошибка при выводе поста по идентифицирующему номеру"
    assert post_by_pk["pk"] == 1, "ошибка при выводе поста по идентифицирующему номеру"

def test_get_post_by_tags():

    post_by_tags = get_post_by_tags("текст с #тэгами")
    assert post_by_tags != None, "ошибка при выводе текста поста с живыми тэгами"


def test_save_post_in_bookmarks():

    save_post_in_bookmarks("текст")
    bookmarks = view_bookmarks()
    assert bookmarks != None, "ошибка при сохранении данных"


def test_view_bookmarks():

    bookmarks = view_bookmarks()
    assert bookmarks != None, "ошибка при выгрузке данных"