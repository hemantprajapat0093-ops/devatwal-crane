p = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(p, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if "btn-tech-primary" in line:
            print(f"Line {idx} mentions btn-tech-primary")
