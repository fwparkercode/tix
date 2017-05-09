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

# start with a single movie on two days
# if name = main, call functions and see if the tests work
import csv
# commit, update, merge, push

def filecheck():
    try:
        file = open("ledger.csv" , "r")
    except IOError:
        print("This file does not exist")
    return file

def create_list():
    file = filecheck()
    movie_data = []
    reader = csv.reader(file, delimiter = ',')
    for line in reader:
        movie_data.append(line)
    return movie_data

# make a function that looks past the comma in the phrase Today, May 8
#make one ledger that you read from and append new data to the end of the list

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


    # bring in info from ledger (read from and append) √
    # if you can purchase, execute that and add to ledger √
    # if there is an error return it to the app but DO NOT add to ledger √

def check_showings(movie_data):
    showings = 0
    # Should I create a loop that when done is true it blocks the user from buying more tickets?
    # How should I do that?
    for i in range(len(movie_data)):
        if movie_data[i][1] == movie_data[i][1]:
            showings += int(movie_data[i][3])
    if showings == 10:
        print("Limit reached, tickets for this showing are no longer available")
    return showings


def check_per_day(movie_data, date):
    sum_daily = 0
    for i in range(len(movie_data)):
        if movie_data[i][0] == date:
            sum_daily += int(movie_data[i][3])
    return sum_daily

        #if len(total_daily_list) == 20:
            #print("You have reached your limit for ticket sales today, tickets today are no longer available")
        #if len(total_daily_list) == 15:
            #print("Only 5 more tickets are available to buy today.")
    # make a dummy ledger

def pull_data():
    # read/pull in data from marc's file
    # put it in a list (or multiple lists)
    # scan those lists using other functions
    pass

if __name__== "__main__":
    purchase("5/9", " Guardians of the Galaxy", " 8:00", 4)
    # make the strings above variables that are brought in from charlie's data
