import pytest
from app import app

keys_posts = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

def test_api():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    for post in response.json:
        assert post.keys() == keys_posts


def test_api_post():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    for post in response.json:
        assert post.keys() == keys_posts