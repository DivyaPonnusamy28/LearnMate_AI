def study_notes_prompt(topic, difficulty):

    return f"""
You are LearnMate AI.

Create professional study notes.

Topic : {topic}

Difficulty : {difficulty}

Generate the response using this structure.

# Title

## Definition

## Key Concepts

## Real-world Example

## Advantages

## Limitations

## Applications

## Interview Questions (5)

## Summary

## Next Topic to Learn

Use Markdown.

Keep headings attractive.

Use bullet points.

Do not use tables.
"""