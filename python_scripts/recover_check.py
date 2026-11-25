import json

path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if "public/index.html" in line and "write_file" in line:
            obj = json.loads(line)
            print(f"Match at line {idx}, step: {obj.get('step_index')}")
            # check tool calls
            for tc in obj.get('tool_calls', []):
                if tc.get('function', {}).get('name') == 'write_file':
                    args = tc['function']['arguments']
                    p = args.get('Path') or args.get('path')
                    if p and 'index.html' in p:
                        print(f"Found index.html write in line {idx}")
