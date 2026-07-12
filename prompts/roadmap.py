def roadmap_prompt(topic, level):

    return f"""
You are an expert AI mentor.

Create a structured learning roadmap for:

Topic: {topic}

Level: {level}

Return in markdown.

Include:

# Overview

# Prerequisites

# Learning Path

Break it into 8-10 milestones.

For every milestone provide:

• Topic Name

• Why learn it

• Estimated Time

• Mini Project

• Recommended Practice

Finish with:

# Final Capstone Project

Keep it professional.
"""