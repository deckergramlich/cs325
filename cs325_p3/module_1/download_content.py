#Decker Gramlich
#CS325
#poject 3 - 1st module

#expects url as an input, outputs the text of the website

import requests

def download_content(url):
    
    response = requests.get(url)
    return response.text #outputs the text from the website