import pytest
from app import app
import json

keys_posts = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

def test_api():
    response = app.test_client().get("/api/posts")
    assert response.status_code == 200
    assert type(response.json) == list
    for post in response.json:
        assert post.keys() == keys_posts


def test_api_post():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    assert type(response.json) == dict
    post = response.json
    assert post.keys() == keys_posts