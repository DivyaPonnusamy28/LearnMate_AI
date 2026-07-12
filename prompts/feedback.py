def feedback_prompt(topic, answer):

    return f"""
You are an AI tutor.

Topic:
{topic}

Student Answer:
{answer}

Evaluate the answer.

Provide:

1. Score out of 10
2. Strengths
3. Mistakes
4. Correct Answer
5. Suggestions to improve
"""