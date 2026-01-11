import os
import requests

def download_pdf(url: str, out_dir="data/pdfs"):
    os.makedirs(out_dir, exist_ok=True)
    filename = url.split("/")[-1] + ".pdf"
    path = os.path.join(out_dir, filename)
    r = requests.get(url, timeout=30)
    with open(path, "wb") as f:
        f.write(r.content)
    return path
