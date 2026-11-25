import json

p = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(p, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx in [189, 193, 225, 227, 261, 304]:
            obj = json.loads(line)
            for tc in obj.get('tool_calls', []):
                args = tc.get('function', {}).get('arguments', {})
                if 'style.css' in args.get('Path', ''):
                    print(f"Line {idx} wrote style.css with length {len(args.get('Content', ''))}")
                    with open(rf"C:\Users\heman\Desktop\devatwal-crane-service\prev_style_{idx}.css", "w", encoding="utf-8") as out:
                        out.write(args.get('Content', ''))
