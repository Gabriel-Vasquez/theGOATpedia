import os

structure = [
    "goatpedia/data",
    "goatpedia/entries",
    "goatpedia/utils",
    "goatpedia/assets"
]

files = {
    "goatpedia/data/prompts.csv": "question,category,tags\nWho is the GOAT of prestidigitation?,Artisans,magic,illusion",
    "goatpedia/entries/generated_entries.md": "",
    "goatpedia/config.py": "# Add your OpenAI key here\nOPENAI_API_KEY = 'your-api-key'\nMODEL_NAME = 'gpt-4'",
    "goatpedia/generate_pdf.py": "# PDF generator logic goes here\n",
    "goatpedia/requirements.txt": "openai\npandas\nmarkdown2\npdfkit\njinja2",
    "goatpedia/README.md": "# GOATPEDIA\nThe official archive of the greatest humans (and goats) in every imaginable field.",
    "goatpedia/utils/generator.py": "# Entry generator logic goes here\n"
}

for folder in structure:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("GOATPEDIA structure created.")
