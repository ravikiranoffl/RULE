import difflib
from datetime import date, timedelta
from utils import read_file, write_file, hash_text
import json

today = date.today()
yesterday = today - timedelta(days=1)

today_str = today.isoformat()
yesterday_str = yesterday.isoformat()

today_path = f"data/google/privacy_policy/raw/{today_str}.txt"
yesterday_path = f"data/google/privacy_policy/raw/{yesterday_str}.txt"

today_text = read_file(today_path)
yesterday_text = read_file(yesterday_path)

today_hash = hash_text(today_text)
yesterday_hash = hash_text(yesterday_text)

changed = today_hash != yesterday_hash

meta = {
    "date": today_str,
    "changed": changed,
    "hash": today_hash
}

write_file(
    f"data/google/privacy_policy/meta/{today_str}.json",
    json.dumps(meta, indent=2)
)

if not changed:
    print("[SKIP] No change detected")
    exit()

diff = difflib.unified_diff(
    yesterday_text.splitlines(),
    today_text.splitlines(),
    lineterm=""
)

diff_text = "\n".join(diff)

write_file(
    f"data/google/privacy_policy/diff/{today_str}.diff",
    diff_text
)

print("[OK] Diff created")
