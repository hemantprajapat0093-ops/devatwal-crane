import json

p = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(p, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if "btn-tech-primary" in line and "Content" in line:
            obj = json.loads(line)
            for tc in obj.get('tool_calls', []):
                args = tc.get('function', {}).get('arguments', {})
                content = args.get('Content', '')
                if 'btn-tech-primary' in content:
                    print(f"Found btn-tech-primary in tool call at line {idx}!")
                    with open(r"C:\Users\heman\Desktop\devatwal-crane-service\found_prev_style.css", "w", encoding="utf-8") as out:
                        out.write(content)
                    break
