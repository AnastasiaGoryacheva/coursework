from flask import Blueprint, request, render_template
from functions import read_posts, upload_posts
import logging

logging.basicConfig(encoding="utf-8", level=logging.INFO)

UPLOAD_FOLDER = "uploads/images"

loader_blueprint = Blueprint("loader", __name__, url_prefix="/post", static_folder="static", template_folder="templates")

@loader_blueprint.route("/form/")
def loader():
    return render_template("post_form.html")


@loader_blueprint.route("/upload/", methods=["GET", "POST"])
def upload_post():
    try:
        file = request.files["picture"]
        filename = file.filename
        content = request.values["content"]
        posts = read_posts()
        new_post = {
            "pic": f"/uploads/images/{filename}",
            "content": content
        }
        posts.append(new_post)
        upload_posts(posts)
        file.save(f"uploads/images/{filename}")
        if filename.split(".")[-1] not in ["png", "jpeg"]:
            logging.info("Загруженный файл - не картинка")
    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла")
        return render_template("error.html")
    else:
        return render_template("post_uploaded.html", pic=f"/uploads/images/{filename}", content=content)


@loader_blueprint.route("/uploads/images/<path:path>")
def static_dir(path):
    return send_from_directory(UPLOAD_FOLDER, path)
