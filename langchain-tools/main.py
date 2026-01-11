import json
from arxiv_fetch import fetch_papers
from pdf_download import download_pdf
from pdf_parse import extract_text
from to_json import paper_to_json

TOPIC = input("Enter research topic:")

papers = fetch_papers(TOPIC, max_results=3)
outputs = []

for p in papers:
    pdf_path = download_pdf(p["pdf_url"])
    text = extract_text(pdf_path)
    outputs.append(paper_to_json(p, text))

with open("data/papers.json", "w", encoding="utf-8") as f:
    json.dump(outputs, f, indent=2)

print("Saved data/papers.json")
