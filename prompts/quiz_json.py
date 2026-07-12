def quiz_json_prompt(topic, difficulty):

    return f"""
You are LearnMate AI.

Generate exactly 5 multiple-choice questions.

Topic: {topic}

Difficulty: {difficulty}

Return ONLY valid JSON.

[
    {{
        "question":"Question",
        "options":[
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "answer":0,
        "explanation":"Explanation"
    }}
]

Rules:
- Generate exactly 5 questions.
- Exactly 4 options.
- answer must be 0,1,2 or 3.
- explanation should be 2-3 sentences.
- Do NOT return markdown.
- Do NOT write ```json.
- Return ONLY JSON.
"""