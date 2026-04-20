import json
from datetime import date
from utils import read_file, write_file
import os

today = date.today().isoformat()

meta_path = f"data/google/privacy_policy/meta/{today}.json"
diff_path = f"data/google/privacy_policy/diff/{today}.diff"

if not os.path.exists(meta_path):
    exit()

meta = json.loads(read_file(meta_path))

if not meta["changed"]:
    print("[SKIP] No change to analyze")
    exit()

diff_text = read_file(diff_path)

prompt = f"""
Analyze this policy change:

{diff_text[:4000]}

Return JSON:
- summary
- change_type
- risk_level
- topics
- user_impact
"""

def fake_llm(prompt):
    return json.dumps({
        "summary": "Minor update to data usage language",
        "change_type": "modification",
        "risk_level": "low",
        "topics": ["data_usage"],
        "user_impact": "Minimal impact on users"
    })

result = json.loads(fake_llm(prompt))

output = {
    "date": today,
    "entity": "Google",
    "document": "privacy_policy",
    **result
}

write_file(
    f"data/google/privacy_policy/processed/{today}.json",
    json.dumps(output, indent=2)
)

print("[OK] Analysis complete")
