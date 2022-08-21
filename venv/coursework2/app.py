from flask import Flask
from post.post import post_blueprint
from search.search import search_blueprint
from users.users import users_blueprint
from api.api import api_blueprint
from tag.tag import tag_blueprint
from bookmarks.bookmarks import bookmarks_blueprint


app = Flask(__name__)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.config['JSON_AS_ASCII'] = False


if __name__ == "__main__":
    app.run()
