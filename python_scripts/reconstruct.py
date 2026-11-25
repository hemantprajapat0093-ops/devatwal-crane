import json, re

path = r"C:\Users\heman\.gemini\antigravity-cli\brain\4864e298-07a5-436c-ad5f-3371b3bb3f27\.system_generated\logs\transcript_full.jsonl"
lines_to_read = [275, 277, 279, 281, 283, 285]

all_code = []

with open(path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx in lines_to_read:
            obj = json.loads(line)
            content = obj.get('content', '')
            # The content has format:
            # Showing lines X-Y of 1178
            # 1: ...
            # 2: ...
            # Let's extract code lines
            lines = content.split('\n')
            for l in lines:
                m = re.match(r'^\s*(\d+):\s?(.*)$', l)
                if m:
                    line_num = int(m.group(1))
                    line_text = m.group(2)
                    all_code.append((line_num, line_text))

all_code.sort(key=lambda x: x[0])
# Deduplicate lines by line_num
dedup = []
seen = set()
for num, text in all_code:
    if num not in seen:
        seen.add(num)
        dedup.append(text)

with open(r"C:\Users\heman\Desktop\devatwal-crane-service\reconstructed_prev_index.html", "w", encoding="utf-8") as out:
    out.write("\n".join(dedup))

print(f"Successfully reconstructed previous index.html with {len(dedup)} lines!")
