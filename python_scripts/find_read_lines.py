import json

path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if "Showing lines 1-150 of 1178" in line:
            print(f"Found line {idx} with lines 1-150!")
