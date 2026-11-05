import requests

URL = "http://127.0.0.1:5000/submit"
TEXT = ("Honestly I burned the toast again this morning, set off the smoke alarm, "
        "and my cat bolted under the couch like I had committed a crime. "
        "Third time this week. Not great.")

codes = []
for i in range(15):
    r = requests.post(URL, json={"text": TEXT, "creator_id": f"rotating_{i}"}, timeout=90)
    codes.append(r.status_code)
print(" ".join(map(str, codes)))