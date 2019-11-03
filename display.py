"""
 A program that is updated with Funny and Famous quotes from Our favorite movies

Holds:

The Actual Quote
The Name of the Movie
Character Who Said the Quote
Actor who played The Character

User can 
- Add
- Delete
- Edit
- View All
- Search
- Close
"""

from tkinter import *
from backend import Database

database=Database("quotes.db")

window=Tk()
#window.minsize(500,500)
#window.maxsize(500,500)

def view_all():
    listbox.delete(0,END)
    for row in database.view():
        listbox.insert(END,row)


def search_for():
    listbox.delete(0,END)
    for row in database.search(quote_text.get(), movie_text.get(), character_text.get(), actor_text.get()):
        listbox.insert(END,row)

def add_entry():
    database.insert(quote_text.get(), movie_text.get(), character_text.get(), actor_text.get())
    listbox.delete(0,END)
    listbox.insert(END, (quote_text.get(), movie_text.get(), character_text.get(), actor_text.get()))


def get_selected_row(event):
    try:
        global selected_tuple
        index=listbox.curselection()[0]
        selected_tuple=listbox.get(index)
        quote_entry.delete(0,END)
        quote_entry.insert(END, selected_tuple[1])
        movie_entry.delete(0,END)
        movie_entry.insert(END,selected_tuple[2])
        character_entry.delete(0,END)
        character_entry.insert(END, selected_tuple[3])
        actor_entry.delete(0,END)
        actor_entry.insert(END, selected_tuple[4])
    except IndexError:
        pass


def delete_command():
    database.delete(selected_tuple[0])
    view_all()

def update_command():
    database.edit(selected_tuple[0], quote_text.get(), movie_text.get(), character_text.get(), actor_text.get())
    view_all()

#TITLE
title_label = Label(window, text="QUOTEBOOK", justify=CENTER, fg = "Gray13", font = "Helvetica 30 bold italic", bg="White Smoke")
title_label.grid(row=0, column=0, columnspan=3 ,sticky=NSEW, pady=16)

#QUOTE

quote_label = Label(window, text="Quote", fg = "Black", bg="White Smoke")
quote_label.grid(row=1, column=0, padx=20)

quote_text = StringVar()
quote_entry = Entry(window, textvariable = quote_text)
quote_entry.grid(row=1, column=1, padx=20)

#MOVIE

movie_label = Label(window, text="Movie", fg = "Black", bg="White Smoke")
movie_label.grid(row=2, column=0, padx=20)

movie_text = StringVar()
movie_entry = Entry(window, textvariable = movie_text)
movie_entry.grid(row=2, column=1, padx= 20)

#CHARACTER

character_label = Label(window, text="Character", fg = "Black", bg="White Smoke")
character_label.grid(row=3, column=0, padx=20)

character_text = StringVar()
character_entry = Entry(window, textvariable = character_text)
character_entry.grid(row=3, column=1, padx=20)

#ACTOR

actor_label = Label(window, text="Actor", fg = "Black", bg="White Smoke")
actor_label.grid(row=4, column=0, padx=20)

actor_text = StringVar()
actor_entry = Entry(window, textvariable = actor_text)
actor_entry.grid(row=4, column=1, padx=20)

#LISTBOX

listbox = Listbox(window, height=4, width=20)
listbox.grid(row=6,column=0, rowspan= 6, columnspan=2, sticky=NSEW, padx=20, pady=20)

listbox.bind('<<ListboxSelect>>', get_selected_row)

#SCROLLBAR

sb = Scrollbar(window)
sb.grid(row=8, column=2, padx=10, pady=20, sticky=W)
sb.configure(command=listbox.yview)
#BUTTONS

#VIEW ALL BTN

view_button = Button(window, text="View All", width=7, command=view_all)
view_button.grid(row=1, column=2, padx=20)

#ADD BTN
view_button = Button(window, text="Add", width=7, command=add_entry)
view_button.grid(row=2, column=2, padx=20)

#DELETE BTN
view_button = Button(window, text="Delete", width=7, command=delete_command)
view_button.grid(row=3, column=2, padx=20)

#EDIT BTN
view_button = Button(window, text="Edit", width=7, command=update_command)
view_button.grid(row=4, column=2, padx=20)

#SEARCH BUTTON
search_button = Button(window, text="Search", width=7, command=search_for)
search_button.grid(row=5, column=2, padx=20)

#LAUNCH CONFIG

window.configure(background="White Smoke")
window.title("QuoteBook")
window.wm_title("QuoteBook")
window.mainloop()
