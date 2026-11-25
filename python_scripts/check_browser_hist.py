import os
import sqlite3
import shutil

# Chrome or Edge History
edge_hist = os.path.expanduser(r"~\AppData\Local\Microsoft\Edge\User Data\Default\History")
chrome_hist = os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data\Default\History")

for name, p in [("Edge", edge_hist), ("Chrome", chrome_hist)]:
    if os.path.exists(p):
        temp_p = os.path.join(r"C:\Users\heman\Desktop\devatwal-crane-service\python_scripts", f"temp_{name}_hist.db")
        try:
            shutil.copy2(p, temp_p)
            conn = sqlite3.connect(temp_p)
            cursor = conn.cursor()
            cursor.execute("SELECT url, title, last_visit_time FROM urls WHERE url LIKE '%github.com%' ORDER BY last_visit_time DESC LIMIT 20")
            rows = cursor.fetchall()
            print(f"--- Recent GitHub URLs in {name} ---")
            for url, title, t in rows:
                print(f" {url} | {title}")
            conn.close()
            os.remove(temp_p)
        except Exception as e:
            print(f"Error reading {name} history: {e}")
