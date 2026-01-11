def paper_to_json(meta, text):
    return {
        "title": meta["title"],
        "authors": meta["authors"],
        "year": meta["year"],
        "abstract": meta["summary"],
        "raw_text": text[:8000],  # cap for now
    }
