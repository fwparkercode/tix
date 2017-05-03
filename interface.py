'''
(150pts, 75pts for your section, 75pts for overall app)
Your client's organization provides discount movie tickets as a benefit to
its employees and families.
You are tasked with creating a desktop app to track discount movie tickets
obtained through their program.

The client requires the following specifics for the app:
Tickets can be to any movie at Regal Webster Place 11 on any day or time.
Tickets may only be purchased to a showing in the next 7 days.
Only six tickets are allowed per employee for a single "purchase".
Only 10 tickets are allowed for an individual showing of a film (same theater/time).
Your organization cannot sell more than 20 tickets for any single day.

This assignment will require extensive use of tkinter, beautifulSoup,
and writing to and reading from files.

You will be working as a team of 3 students collaboratively on github.
You will create at least three python files for this app.
Each student will be responsible for one file.
One .py file will handle the tkinter GUI (this will be the __main__).
One .py file will handle all web scraping using BeautifulSoup.
One .py file will handle data storage to track and record all purchases.

Tkinter file:
Your app will have the following features
- App class
- __name__ == "__main__":
- imports Webscraping and Recordkeeping modules/libraries
- an OptionMenu to choose the date of your visit
- an OptionMenu to choose your movie
- Radiobuttons or OptionMenu to choose your time
- A SpinBox to choose the number of tickets to purchase
- A purchase button to buy/record your ticket purchase.
- A popup message widget to verify your purchase
- After a purchase is made, you will be able to start over.
- Proper formatting (font, colors, sticky, width, layout)

BeautifulSoup portion:
Your app will have the following features:
- Web scraping functions in separate file from __main__
- Scrapes available dates from Fandango website (next 7 days)
- Scrapes available links (href) to those dates
- Scrapes available movies for the date selected
- Scrapes available times for the movie and date
- Creates lists out of all of the above items for use in the app

Recordkeeping portion:
Your app will have the following features:
- Records class in separate file from __main__
- a ledger to permanently record each purchase (date,movie,time,tickets)
- a record to permanently record total purchase for each day and showing
- both record and ledger kept as csv files
- function(s) and/or method(s) to "claim" tickets
- checks to ensure no more than 10 tickets per showing
- checks to ensure no more than 20 tickets per day
- ledger and record are updated after each purpose

IF your team has a 4th member:
Your app will create a printable ticket following the purchase.
This ticket will have date, show, time, and number of tickets.

All team members will make appropriate pull requests and merges to github.
'''
import marc_1
from tkinter import *
from tkinter import font


class App():
    def __init__(self, master):
        self.title_font = font.Font(family="Times", size=20, weight=font.BOLD)
        self.title = Label(master, text="Discount Movie Tickets",font=self.title_font, bg="black", fg="white")
        self.title.grid(row=1, column=1, columnspan=2, sticky="e" + "w")

        self.date = StringVar()
        self.date_list = marc_1.get_date()[0]
        self.date.set(marc_1.get_date()[0][0])
        self.url_list = marc_1.get_date()[1]
        #marc_1.get_movies(url_list[self.date_list.find(self.date.get()])
        self.date_menu = OptionMenu(master, self.date, *self.date_list)
        self.date_menu.grid(column=2, row=2)
        self.date_label = Label(master, text="Select a date:")
        self.date_label.grid(row=2, column=1)

        self.movie = StringVar()
        self.movie.set("                    ")
        self.movie_list = ["testingmovie", "testingmovie2"] #RUN MARC'S FUNC'''
        self.movie_menu = OptionMenu(master, self.movie, *self.movie_list)
        self.movie_menu.grid(row=3, column=2, sticky="w")
        self.movie_label = Label(master, text="Select a movie:")
        self.movie_label.grid(row=3, column=1)

        self.time = StringVar()
        self.time.set("        ")
        self.time_list = ["9:30", "8:30", "10:10", "11:45"] #RUN MARCS FUNC
        self.time_menu = OptionMenu(master, self.time, *self.time_list)
        self.time_menu.grid(row=4, column=2, sticky="w")
        self.time_label = Label(master, text="Select a time:")
        self.time_label.grid(row=4, column=1)

        self.ticket_quant = IntVar()
        self.ticket_quant.set(0)
        self.ticket_quant_list = [0,1,2,3,4,5,6]  #RUN ELIZA'S FUNCTION HERE
        self.ticket_quant_menu = OptionMenu(master, self.ticket_quant, *self.ticket_quant_list)
        self.ticket_quant_menu.grid(row=5, column=2, sticky="w")
        self.ticket_label = Label(master, text="Quantity:")
        self.ticket_label.grid(row=5, column=1)

        label_text = StringVar()
        self.response_label = Label(master, textvariable=label_text)

        self.purchase_button = Button(master, text="Purchase", command=lambda:purchase(self, self.response_label, self.date.get(), self.movie.get(), self.time.get(), str(self.ticket_quant.get())))
        self.purchase_button.grid(row=6, column=1, columnspan=2)

        def purchase(self, label, date, movie, time, quantity):
            '''RUN ELIZA'S FUNCTION'''
            label_text.set("Thank you for your purchase!\n Receipt:\nDate: " + str(date) + "\nMovie: " + str(movie) + "\nTime: " + str(time) + "\nQuantity: " + str(quantity))
            label.grid(row=7, column=1, columnspan=2)
            self.date.set("")
            self.movie.set("")
            self.time.set("")
            self.ticket_quant.set(0)




if __name__ == "__main__":
    root = Tk()
    root.title("Discount Movie Tickets")
    my_app = App(root)
    root.mainloop()
