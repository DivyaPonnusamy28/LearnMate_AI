def flashcards_prompt(topic, difficulty):

    return f"""
You are an expert educator.

Generate exactly 10 flashcards.

Topic:
{topic}

Difficulty:
{difficulty}

Return ONLY JSON.

Example:

[
 {{
   "question":"What is AI?",
   "answer":"Artificial Intelligence is..."
 }},
 {{
   "question":"What is Machine Learning?",
   "answer":"Machine Learning is..."
 }}
]

No markdown.

No explanation.

No extra text.

Only JSON.
"""