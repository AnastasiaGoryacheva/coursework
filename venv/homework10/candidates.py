from flask import Flask
import json

with open("candidates.json", encoding = "utf-8") as file:
    candidates = json.load(file)

app = Flask(__name__)

@app.route("/")
def making_list():
    list_candidates = "<pre>"
    for candidate in candidates:
        list_candidates += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n\n"
    list_candidates += "</pre>"
    return list_candidates


@app.route("/candidate/<int:id>")
def profile(id):
    number_candidate = candidates[id-1]
    profile_candidate = f"<img src = {number_candidate['picture']}></img>"
    profile_candidate += "<pre>"
    profile_candidate += f"{number_candidate['name']}\n{number_candidate['position']}\n{number_candidate['skills']}\n\n"
    profile_candidate += "</pre>"
    return profile_candidate


@app.route("/skills/<skill>")
def skill_candidate(skill):
    skill_lower = skill.lower()
    skills_candidate = "<pre>"
    for candidate in candidates:
        skills_lower = candidate['skills'].lower().split(", ")
        if skill_lower in skills_lower:
            skills_candidate += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n\n"
    skills_candidate += "</pre>"
    return skills_candidate

app.run()