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
import efischer1


def resize_menu(input_list, menu):
    max_length = len(max(input_list, key=len))
    menu.config(width=int(max_length * .8 + 4))


def change_movies(input_list, master, movie, menu, date_list, date, url_list, time_list, time_menu, time, movie_list):
    input_list = marc_1.pull_movies(url_list[date_list.index(date.get())])
    app.movie_list = input_list # look at this
    movie_list = input_list
    menu.grid_remove()
    movie.set("-Select-")
    menu = OptionMenu(master, movie, *input_list, command=lambda x: change_time(time_list, master, time_menu, time, movie, url_list, date_list, date, movie_list))
    menu.grid(row=3, column=2, sticky="w")
    #resize_menu(input_list, menu)
    change_time(time_list, master, time_menu, time, movie, url_list, date_list, date, movie_list)


def change_time(time_list, master, time_menu, time, movie, url_list, date_list, date, movie_list):
    if movie.get() != "-Select-":
        time_list = marc_1.pull_times(url_list[date_list.index(date.get())], movie_list.index(movie.get()))
        app.time_list = time_list
        time_menu.grid_remove()
        time.set("-Select-")
        time_menu = OptionMenu(master, time, *time_list)
        time_menu.grid(row=4, column=2, sticky='w')
        #resize_menu(time_list, time_menu)
    else:
        time_list = ["-Select-"]  # PUT MARC'S FUNC HERE
        app.time_list = time_list
        time_menu.grid_remove()
        time.set("-Select-")
        time_menu = OptionMenu(master, time, *time_list)
        time_menu.grid(row=4, column=2, sticky='w')

class App():
    def __init__(self, master):
        self.title_font = font.Font(family="Times", size=20, weight=font.BOLD)
        self.title = Label(master, text="Discount Movie Tickets",font=self.title_font, bg="black", fg="white")
        self.title.grid(row=1, column=1, columnspan=2, sticky="e" + "w")

        self.date = StringVar()

        self.date_list = marc_1.get_date()[0]
        self.date.set(marc_1.get_date()[0][0])
        self.date.set("-Select-")
        self.url_list = marc_1.get_date()[1]
        '''Line below has a lambda input b/c it was broken without one'''
        self.date_menu = OptionMenu(master, self.date, *self.date_list, command=lambda x: change_movies(self.movie_list, master, self.movie, self.movie_menu, self.date_list, self.date, self.url_list, self.time_list, self.time_menu, self.time, self.movie_list))
        self.date_menu.grid(column=2, row=2)
        resize_menu(self.date_list, self.date_menu)
        self.date_label = Label(master, text="Select a date:")
        self.date_label.grid(row=2, column=1)

        self.movie = StringVar()
        self.movie.set("-Select-")
        self.movie_list = ["-Select-"]

        self.movie_menu = OptionMenu(master, self.movie, *self.movie_list, command=lambda x: change_time(self.time_list, master, self.time_menu, self.time, self.movie.get(), self.url_list, self.date_list, self.date, self.movie_list))
        self.movie_menu.grid(row=3, column=2, sticky="w")
        self.movie_label = Label(master, text="Select a movie:")
        self.movie_label.grid(row=3, column=1)

        self.time = StringVar()
        self.time.set("-Select-")
        self.time_list = ["-Select-"]
        self.time_menu = OptionMenu(master, self.time, *self.time_list)
        self.time_menu.grid(row=4, column=2, sticky="w")
        self.time_label = Label(master, text="Select a time:")
        self.time_label.grid(row=4, column=1)

        self.ticket_quant = IntVar()
        self.ticket_quant.set(0)
        self.ticket_quant_list = [0,1,2,3,4,5,6]  # RUN ELIZA'S FUNCTION HERE
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
            response = efischer1.purchase(date, movie, time, int(quantity))
            if response == "Confirmed!":
                label_text.set("Thank you for your purchase!\n Receipt:\nDate: " + str(date) + "\nMovie: " + str(movie) + "\nTime: " + str(time) + "\nQuantity: " + str(quantity))
            else:
                label_text.set(response)
            label.grid(row=7, column=1, columnspan=2)
            self.date.set(self.date_list[0])
            self.movie.set("-Select-")
            self.time.set("-Select-")
            self.ticket_quant.set(0)

#[:len(time)-1]
#[date.find(",") + 1:]
if __name__ == "__main__":
    root = Tk()
    root.title("Discount Movie Tickets")
    app = App(root)
    root.mainloop()