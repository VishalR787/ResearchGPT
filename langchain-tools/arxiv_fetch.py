import arxiv

def fetch_papers(topic: str, max_results=5):
    search = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
    )
    results = []
    for r in search.results():
        results.append({
            "title": r.title,
            "authors": [a.name for a in r.authors],
            "year": r.published.year,
            "pdf_url": r.pdf_url,
            "summary": r.summary,
        })
    return results
