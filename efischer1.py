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

ledger = []

def purchase():
    # if you can purchase, execute that and add to ledger
    # if there is an error return it to the app but DO NOT add to ledger
    pass

def check_showings():
    pass

def check_per_day():
    # make a dummy ledger
    pass

def pull_data():
    # read/pull in data from marc's file
    # put it in a list (or multiple lists)
    # scan those lists using other functions
    pass

