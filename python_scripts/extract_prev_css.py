import json

p = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(p, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx == 261:
            obj = json.loads(line)
            for tc in obj.get('tool_calls', []):
                args = tc.get('function', {}).get('arguments', {})
                content = args.get('Content')
                if content and 'style.css' in args.get('Path', ''):
                    with open(r"C:\Users\heman\Desktop\devatwal-crane-service\reconstructed_prev_style.css", "w", encoding="utf-8") as out:
                        out.write(content)
                    print("Extracted style.css from line 261!")
