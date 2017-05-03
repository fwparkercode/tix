#Marc's file
# Beautiful Soup

import urllib.request
from bs4 import BeautifulSoup

# Dates
def get_date():

    url = "http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage?date=5%2f2%2f2017"

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")


    my_week_days = [x.text for x in soup.findAll("div", {"class": "date-week-day"})][:7]

    my_months = [x.text for x in soup.findAll("div", {"class": "date-month"})][:7]   # target a specific table

    my_day = [x.text for x in soup.findAll("div", {"class": "date-day"})][:7]

    date_list = []

    for i in range(len(my_week_days)):
        date_list.append(my_week_days[i]+", "+ my_months[i] + " " + my_day[i])
    print(date_list)

    url_list = [x['href'] for x in soup.findAll("a", {"class": "date-area"})]
    print(url_list)
    return date_list, url_list







# Movies




if __name__ == "__main__":
    get_date()





#rows = my_table.findAll("tr")









# Times






def pull_dates():
    return []