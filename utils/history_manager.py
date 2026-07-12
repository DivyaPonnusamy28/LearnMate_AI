import json
import os
from datetime import datetime

FILE_PATH = "data/history.json"


def save_history(topic, activity, difficulty, response):

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)

    with open(FILE_PATH, "r") as f:
        history = json.load(f)

    history.insert(0, {
        "topic": topic,
        "activity": activity,
        "difficulty": difficulty,
        "response": response,
        "time": datetime.now().strftime("%d %b %Y %I:%M %p")
    })

    with open(FILE_PATH, "w") as f:
        json.dump(history, f, indent=4)


def load_history():

    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        return json.load(f)