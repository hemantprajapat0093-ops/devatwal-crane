import json

path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx == 265:
            obj = json.loads(line)
            for tc in obj.get('tool_calls', []):
                args = tc.get('function', {}).get('arguments', {})
                content = args.get('Content')
                if content:
                    with open(r"C:\Users\heman\Desktop\devatwal-crane-service\previous_index.html", "w", encoding="utf-8") as out:
                        out.write(content)
                    print(f"Extracted previous_index.html from line 265, length: {len(content)}")
                    break
