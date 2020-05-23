
import json
with open("mariyam.txt", "r") as f:
    file = json.loads(f.read())["items"]
    for line in file :
        print(line["personEmail"]+ " :" + line["text"])