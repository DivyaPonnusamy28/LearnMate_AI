def study_plan_prompt(topic, level, days, hours):

    return f"""
You are an expert study planner.

Create a professional study schedule.

Topic : {topic}

Difficulty : {level}

Available Days : {days}

Hours Per Day : {hours}

Return in Markdown.

For every day provide:

# Day 1

Topics

Objectives

Practice Tasks

Mini Quiz

Estimated Time

Repeat until Day {days}

Finally include

Revision Day

Resources

Interview Preparation

Final Mini Project
"""