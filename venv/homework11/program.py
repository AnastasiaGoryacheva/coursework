from flask import Flask, request, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

candidates = load_candidates_from_json("candidates.json")

@app.route("/")
def list_candidates():
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:id>")
def profile_candidate(id):
    candidate = get_candidate(id)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<name>")
def search_name(name):
    candidates_ = get_candidates_by_name(name)
    return render_template("search.html", candidates=candidates_, len_candidates=len(candidates_))


@app.route("/skill/<skill>")
def skill_search(skill):
    candidates__= get_candidates_by_skill(skill)
    return render_template("skill.html", candidates=candidates__, len_candidates=len(candidates__))


app.run()
