def notes_prompt(topic, difficulty):

    return f"""
You are an expert teacher.

Create professional study notes.

Topic:
{topic}

Difficulty:
{difficulty}

Return in Markdown.

Include:

# Definition

# Objectives

# Key Concepts

# Important Points

# Advantages

# Limitations

# Real-world Applications

# Interview Questions

# Common Mistakes

# Revision Notes

# Summary
"""