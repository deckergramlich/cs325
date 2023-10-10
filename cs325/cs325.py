#Decker Gramlich
#CS325

import requests
import sys
import re

#project 1:
if len(sys.argv) != 2:
    print("Usage: python proj.py <URL>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)

content = response.text

file = open("output.txt", "w")
file.write(content)
file.close()

#project 2:
comments = re.findall("<div class=\"md\">(.*?)</div>", content)

file = open("comments.txt", "w")
for comment in comments:
    file.write(comment + "\n")
file.close()