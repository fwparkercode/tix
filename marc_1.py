#Marc's file
# Beautiful Soup

import urllib.request
from bs4 import BeautifulSoup

url = "http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage?date=5%2f2%2f2017"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

def pull_dates():
    return []