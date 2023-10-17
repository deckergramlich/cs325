#Decker Gramlich
#CS325
#poject 3 - main

#main function that inputs the website url and outputs its text and comments into different files

import sys
from module_1.download_content import download_content
from module_2.save_content_to_file import save_content_to_file
from module_3.extract_comments import extract_comments

if len(sys.argv) != 2:
    print("Usage: python main.py <URL>")
    sys.exit(1)

url = sys.argv[1]

#calls first module, which extracts the text from the website
content = download_content(url)

#calls second module, which outputs the text in a file
save_content_to_file(content, "data/raw/output.txt") #note the path to the 'raw' folder

#calls third module, which extracts the comments from the text
comments = extract_comments(content)

#calls second module, again, which outputs the comments in a file
save_content_to_file(comments, "data/processed/comments.txt") #note the path to the 'processed' folder