import json

candidates = []

def load_candidates_from_json(path):
    global candidates
    with open(path, encoding="utf-8") as file:
        candidates = json.load(file)
    return candidates


def get_candidate(candidate_id):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    candidates_ = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidates_.append(candidate)
    return candidates_



def get_candidates_by_skill(skill_name):
    candidates__ = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            candidates__.append(candidate)
    return candidates__
