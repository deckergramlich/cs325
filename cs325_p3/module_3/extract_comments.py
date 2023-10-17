#Decker Gramlich
#CS325
#poject 3 - 3rd module

#takes the website text as input and separates the comments into text and outputs that text

import re

def extract_comments(content):
    comments = re.findall("<div class=\"md\">(.*?)</div>", content) #filters for the comments
    return comments #return comments