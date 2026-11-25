import json

path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
with open(path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx == 265:
            obj = json.loads(line)
            print("Keys:", obj.keys())
            print("Type:", obj.get('type'))
            print("Tool calls length:", len(obj.get('tool_calls', [])))
            # check if there's content or tool_calls
            if 'content' in obj:
                print("Content preview:", str(obj['content'])[:200])
