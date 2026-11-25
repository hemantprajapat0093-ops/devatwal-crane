import json

path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if "public/index.html" in line:
            obj = json.loads(line)
            step = obj.get('step_index')
            tc_names = [tc.get('function', {}).get('name') for tc in obj.get('tool_calls', [])]
            print(f"Line {idx}, step {step}, tools: {tc_names}")
