import whois
import json

with open('file.txt', "r") as f:
    web = f.read().split("\n")
    for item in web:
        res = whois.whois(item)
        with open(item, "w") as file:
            json.dump(res, file, indent=4, ensure_ascii=False)
