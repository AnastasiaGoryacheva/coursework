import json

POST_PATH = "posts.json"


def read_posts():
    with open(POST_PATH, encoding="utf-8") as file:
        posts = json.load(file)
        return posts


def upload_posts(posts):
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4, ensure_ascii=False)

