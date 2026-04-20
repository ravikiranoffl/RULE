name: RULE Google Tracker

on:
  schedule:
    - cron: "0 2 * * *"
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - uses: actions/setup-python@v4
        with:
          python-version: 3.10

      - run: pip install -r requirements.txt

      - run: python scripts/fetch.py
      - run: python scripts/diff.py
      - run: python scripts/analyze.py

      - name: Commit data
        run: |
          git config --global user.name "rule-bot"
          git config --global user.email "bot@rule.ai"
          git add .
          git commit -m "RULE update" || echo "No changes"
          git push
