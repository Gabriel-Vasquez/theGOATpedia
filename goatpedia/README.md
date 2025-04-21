# README.md

# 🐐 GOATPEDIA

**GOATPEDIA** is a fully automated, AI-powered compendium of the Greatest Of All Time individuals across every field imaginable—real, absurd, forgotten, and immortal.

This project reads a list of prompts, uses OpenAI's GPT to generate lore-rich entries, and compiles them into a beautifully formatted Markdown archive and PDF book.

---

## 🚀 Features

- Input prompts via CSV (`data/prompts.csv`)
- Auto-generates Markdown entries using GPT
- Consolidates all entries into a single `.md` and `.pdf`
- Fully configurable and extensible

---

## 📁 Folder Structure
```
goatpedia/
├── data/                  # Prompt CSVs
├── entries/               # Output files
├── utils/                 # Core scripts
├── assets/                # (Optional) PDF/cover images
├── config.py              # API keys and settings
├── generate_pdf.py        # Convert Markdown to PDF
├── requirements.txt       # Dependencies
└── README.md              # You're reading it
```

---

## ⚙️ Setup

1. Clone the repo
2. Add your OpenAI API key to `config.py`
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Populate `data/prompts.csv`
5. Generate entries:
```bash
python utils/generator.py
```
6. Convert to PDF:
```bash
python generate_pdf.py
```

---

## 🧠 Example CSV Input
```csv
question,category,tags
Who is the GOAT of prestidigitation?,Artisans,magic,illusion
Who is the GOAT of surviving two atomic bombs?,History,war,luck
```

---

## 📖 Output Example
```markdown
---
title: "Dai Vernon – GOAT of Prestidigitation"
category: "Artisans"
tags: ["magic", "illusion"]
---

## Field: Artisans
**GOAT**: Dai Vernon  
**Known for**: Fooling Houdini, mentoring generations of magicians  
**Legacy**: Elevated card magic to high art  
**Signature Move or Quote**: "Confusion is not magic."  
**GOATness Index**: 97
```

---

## 📜 License
MIT. Use it. Remix it. Make weird books with it.

---

**Created by [Gabriel Vasquez](https://github.com/Gabriel-Vasquez)** . For the love of GOATs everywhere.