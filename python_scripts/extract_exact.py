import json

p = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(p, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx == 225:
            obj = json.loads(line)
            css_content = obj['tool_calls'][0]['args']['Content']
            with open(r"C:\Users\heman\Desktop\devatwal-crane-service\recovered_style.css", "w", encoding="utf-8") as out:
                out.write(css_content)
            print(f"Extracted recovered_style.css, length: {len(css_content)}")
        elif idx == 227:
            obj = json.loads(line)
            html_content = obj['tool_calls'][0]['args']['Content']
            with open(r"C:\Users\heman\Desktop\devatwal-crane-service\recovered_index.html", "w", encoding="utf-8") as out:
                out.write(html_content)
            print(f"Extracted recovered_index.html, length: {len(html_content)}")
