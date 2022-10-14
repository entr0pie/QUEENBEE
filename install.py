import json
import os

your_name = input("[?] Name: ").strip()
git_profile = input("[?] Your GitHub profile page: ")

info = {"name": your_name, "github":git_profile}
json_info = json.dumps(info, indent=4)

try:
    os.mkdir("user-info")

except FileExistsError:
    pass

with open("user-info/info.json", "w") as json_file:
    json_file.write(json_info)
    json_file.close()

