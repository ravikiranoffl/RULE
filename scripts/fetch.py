import requests
from bs4 import BeautifulSoup
from datetime import date
from utils import write_file

URL = "https://policies.google.com/privacy"

today = date.today().isoformat()

def clean(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    return soup.get_text(separator="\n", strip=True)

res = requests.get(URL, timeout=20)
text = clean(res.text)

path = f"data/google/privacy_policy/raw/{today}.txt"
write_file(path, text)

print("[OK] Google policy fetched")
