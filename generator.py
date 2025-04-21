import openai
import pandas as pd
from config import OPENAI_API_KEY, MODEL_NAME

openai.api_key = OPENAI_API_KEY

TEMPLATE = """
You are an expert chronicler of GOATPEDIA, a compendium of the Greatest Of All Time (GOATs) across all fields.

Your job is to answer this question directly:
"{question}"

Provide a compelling, respectful, and humorous Markdown entry in the following format. Focus entirely on the question. Do not use or rely on any extra metadata.

Include a clear answer at the start in the form:
**The GOAT of [field] is: [Name] 🐐**

Then continue with the structured entry:

---
title: "{title}"
category: "(to be inferred by GPT)"
---

## Field: {title}
**GOAT**: [Name]  
**Known for**: [Summary]  
**Legacy**: [Cultural or historical impact]  
**Signature Move or Quote**: [Optional but funny if possible]  
**GOATness Index**: [Score out of 100]

Finish with a short, legendary closing line.
"""

def format_prompt(question):
    return TEMPLATE.format(
        question=question,
        title=question.replace("Who is the GOAT of ", "").replace("?", "").title()
    )

def generate_entry(question):
    prompt = format_prompt(question)
    print("🧪 Prompt preview:\n", prompt[:300], "...\n")

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
            try:
                print(f"\n⏳ Asking: {row['question']}")
                entry = generate_entry(row['question'])
                if entry.strip():
                    f.write(entry + "\n\n")
                    print("✅ Entry written.")
                else:
                    print(f"⚠️ Empty response for: {row['question']}")
            except Exception as e:
                import traceback
                print("❌ Error during GPT call:")
                traceback.print_exc()

if __name__ == "__main__":
    main()
