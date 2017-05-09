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

    url_list = [x['href'] for x in soup.findAll("a", {"class": "date-area"})]
    return date_list, url_list



# Movies
def pull_movies(url):

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")

    my_movies = [x.text.strip() for x in soup.findAll("a", {"class": "showtimes-movie-title"})]

    return my_movies




# Times
def pull_times(url,movie_index):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    my_times = []

    my_times_initial = [[y.text.strip() for y in x.findAll("time", {"class": "timeInfo"})] for x in soup.findAll("div", {"class": "showtimes-times"})]
    my_times.append(my_times_initial)

    return my_times_initial[movie_index]


if __name__ == "__main__":
    get_date()
    print(pull_movies("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage?date=5/9/2017"))
    print(pull_times("http://www.fandango.com/regalwebsterplace11_aaaxr/theaterpage?date=5/9/2017", 3))

