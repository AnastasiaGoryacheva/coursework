import json
from json import JSONDecodeError

POST_JSON = "data/data.json"
COMMENTS_JSON = "data/comments.json"
BOOKMARKS_JSON = "data/bookmarks.json"

all_posts = []

def get_posts_all():
    """Выгружает данные постов из json файла."""
    try:
        global all_posts
        with open(POST_JSON, encoding="utf-8") as file:
            all_posts = json.load(file)
        return all_posts
    except FileNotFoundError:
        return "Файл отсутствует или поврежден"
    except JSONDecodeError:
        return "Файл не удается преобразовать"


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя."""
    posts_user = []
    for post in all_posts:
        if post["poster_name"].lower() == user_name.lower():
            posts_user.append(post)
    return posts_user


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста."""
    try:
        with open(COMMENTS_JSON, encoding="utf-8") as file:
            all_comments = json.load(file)
            comments_post = []
            for comment in all_comments:
                if comment["post_id"] == post_id:
                    comments_post.append(comment)
        return comments_post
    except FileNotFoundError:
        return "Файл отсутствует или поврежден"
    except JSONDecodeError:
        return "Файл не удается преобразовать"


def search_for_posts(query):
    """Возвращает список постов по ключевому слову."""
    found_posts = []
    for post in all_posts:
        if query.lower() in post["content"].lower():
            found_posts.append(post)
    return found_posts


def get_post_by_pk(pk):
    """Возвращает пост по идентифицирующему номеру."""
    for post in all_posts:
        if post["pk"] == pk:
            return post


def get_post_by_tags(content):
    """Возвращает текст поста с активными тэгами."""
    content = content.split()
    new_content = []
    for word in content:
        if "#" in word:
            w =  word.replace(word, f'<a href="/tag/{word[1:].lower()}">{word}</a>')
            new_content.append(w)
        else:
            new_content.append(word)
    return " ".join(new_content)


def save_post_in_bookmarks(posts):
    """Записывает закладки в json файл."""
    try:
        with open(BOOKMARKS_JSON, "w", encoding="utf-8") as file:
            json.dump(posts, file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        return "Файл отсутствует или поврежден"
    except JSONDecodeError:
        return "Файл не удается преобразовать"


def view_bookmarks():
    """Выгружает закладки из json файла."""
    try:
        with open(BOOKMARKS_JSON, encoding="utf-8") as file:
            posts = json.load(file)
        return posts
    except FileNotFoundError:
        return "Файл отсутствует или поврежден"
    except JSONDecodeError:
        return "Файл не удается преобразовать"
