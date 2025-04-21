import openai
import pandas as pd
from config import OPENAI_API_KEY, MODEL_NAME

openai.api_key = OPENAI_API_KEY

TEMPLATE = """
You are an expert chronicler of GOATPEDIA, a compendium of the Greatest of All Time (GOATs) across all fields.

Write a compelling, respectful, and humorous entry answering the question:
"{question}"

Respond in Markdown format with the following structure:
---
title: "{title}"
category: "{category}"
tags: [{tags}]
---

## Field: {category}
**GOAT**: [Name]  
**Known for**: [Summary]  
**Legacy**: [Cultural or historical impact]  
**Signature Move or Quote**: [Optional but funny if possible]  
**GOATness Index**: [Score out of 100]

End with a short, epic or hilarious line like a Hall of Fame induction.
"""

def format_prompt(question, category, tags):
    return TEMPLATE.format(
        question=question,
        title=question.replace("Who is the GOAT of ", "").replace("?", "").title(),
        category=category,
        tags=", ".join([f'\"{t.strip()}\"' for t in tags.split(",")])
    )

def generate_entry(question, category, tags):
    prompt = format_prompt(question, category, tags)
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85
    )
    return response.choices[0].message['content']

def main():
    df = pd.read_csv("./data/prompts.csv")
    with open("./entries/generated_entries.md", "a", encoding="utf-8") as f:
        for _, row in df.iterrows():
            entry = generate_entry(row['question'], row['category'], row['tags'])
            f.write(entry + "\n\n")
            print(f"Added entry: {row['question']}")

if __name__ == "__main__":
    main()