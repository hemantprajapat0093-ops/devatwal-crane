import os
import sqlite3
import shutil

chrome_hist = os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data\Default\History")
temp_p = os.path.join(r"C:\Users\heman\Desktop\devatwal-crane-service\python_scripts", "temp_token_time.db")

shutil.copy2(chrome_hist, temp_p)
conn = sqlite3.connect(temp_p)
cursor = conn.cursor()
cursor.execute("SELECT url, title, datetime(last_visit_time/1000000-11644473600, 'unixepoch', 'localtime') as visit_time FROM urls WHERE url LIKE '%tokens%' ORDER BY last_visit_time DESC LIMIT 10")
rows = cursor.fetchall()
for url, title, t in rows:
    print(f"[{t}] {url} | {title}")
conn.close()
os.remove(temp_p)
