import json

path = r"C:\Users\heman\Desktop\devatwal-crane-service\find_read_lines.py"
# Let's search transcript_full.jsonl for style.css writes
p = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(p, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if "style.css" in line and "write_file" in line:
            print(f"Line {idx} has write_file for style.css")
