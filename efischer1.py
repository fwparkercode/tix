# Record Keeping Functions/Portion

# Recordkeeping portion:
# Your app will have the following features:
#   - Records class in separate file from __main__
#   - a ledger to permanently record each purchase (date,movie,time,tickets)
#   - a record to permanently record total purchase for each day and showing
#   - both record and ledger kept as csv files
#   - function(s) and/or method(s) to "claim" tickets
#   - checks to ensure no more than 10 tickets per showing
#   - checks to ensure no more than 20 tickets per day
#   - ledger and record are updated after each purpose

# pull in all stuff out of file, put it in list, see that there are no violations
# function for pulling in data, for purchase, functions for doing checks
# ledger is a recording of all actions (every time a purchase is made add it to the ledger)
# Have 2 files, working doc and one thats permanent
# Be careful about reading and writing
# commit, update, merge, push

import csv
import os.path

# Checking the file and opeining it
def filecheck():
    try:
        file = open("ledger.csv" , "r")
    except IOError:
        print("This file does not exist")
        file = open("ledger.csv" , "w")
        file.close()
        file = open("ledger.csv" , "r")
    return file

# Creating a list out of the contents of the file
def create_list():
    file = filecheck()
    movie_data = []
    reader = csv.reader(file, delimiter = ',')
    for line in reader:
        movie_data.append(line)
    return movie_data

# Main function
def purchase(date, movie, time, quantity):
    file = filecheck()
    movie_data = create_list()
    print(movie_data)
    showings = check_showings(movie_data)
    daily = check_per_day(movie_data, date)
    file.close()
    file = open("ledger.csv" , "a")
    print(showings)
    if (showings + quantity) <= 10 and (daily + quantity) <=20:
        file.write(date +"," + movie +"," + time +"," + str(quantity) + "\n")
        return("Confirmed!")
    if showings + quantity > 10:
        return("Purchase denied, no tickets left in this showing")
    if daily + quantity > 20:
        return("Purchase denied, no tickets left today. ")

# Check #1: Checking and limiting the showings per movie
def check_showings(movie_data):
    showings = 0
    for i in range(len(movie_data)):
        if movie_data[i][1] == movie_data[i][1]:
            showings += int(movie_data[i][3])
    if showings == 10:
        print("Limit reached, tickets for this showing are no longer available")
    return showings

# Check #2: Checking and limiting the showings per day
def check_per_day(movie_data, date):
    sum_daily = 0
    for i in range(len(movie_data)):
        if movie_data[i][0] == date:
            sum_daily += int(movie_data[i][3])
    return sum_daily

# Program loop
if __name__== "__main__":
    purchase("5/9", " Guardians of the Galaxy", " 8:00", 4)

