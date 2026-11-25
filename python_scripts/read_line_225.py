import json

p = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(p, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx in [225, 227]:
            obj = json.loads(line)
            print(f"Line {idx} keys: {obj.keys()}")
            for k in ['content', 'tool_calls']:
                if k in obj:
                    print(f"Line {idx} {k}: {str(obj[k])[:300]}")
