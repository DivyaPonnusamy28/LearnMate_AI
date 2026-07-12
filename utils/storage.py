import json
import os

FILE = "user_data.json"


def load_data():

    if not os.path.exists(FILE):

        return {
            "quiz_scores": [],
            "topics": [],
            "sessions": 0
        }

    with open(FILE) as f:

        return json.load(f)


def save_data(data):

    with open(FILE, "w") as f:

        json.dump(data, f, indent=4)