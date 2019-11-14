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

class Window(object):

    def __init__(self, window):

        self.window=window()
        self.window.title("QuoteBook")
        self.window.wm_title("QuoteBook")
        self.window.configure(background="White Smoke")


        #TITLE
        title_label = Label(window, text="QUOTEBOOK", justify=CENTER, fg = "Gray13", font = "Helvetica 30 bold italic", bg="White Smoke")
        title_label.grid(row=0, column=0, columnspan=3 ,sticky=NSEW, pady=16)

        #QUOTE

        quote_label = Label(window, text="Quote", fg = "Black", bg="White Smoke")
        quote_label.grid(row=1, column=0, padx=20)

        self.quote_text = StringVar()
        self.quote_entry = Entry(window, textvariable = self.quote_text)
        self.quote_entry.grid(row=1, column=1, padx=20)

        #MOVIE

        movie_label = Label(window, text="Movie", fg = "Black", bg="White Smoke")
        movie_label.grid(row=2, column=0, padx=20)

        self.movie_text = StringVar()
        self.movie_entry = Entry(window, textvariable = self.movie_text)
        self.movie_entry.grid(row=2, column=1, padx= 20)

        #CHARACTER

        character_label = Label(window, text="Character", fg = "Black", bg="White Smoke")
        character_label.grid(row=3, column=0, padx=20)

        self.character_text = StringVar()
        self.character_entry = Entry(window, textvariable = self.character_text)
        self.character_entry.grid(row=3, column=1, padx=20)

        #ACTOR

        actor_label = Label(window, text="Actor", fg = "Black", bg="White Smoke")
        actor_label.grid(row=4, column=0, padx=20)

        self.actor_text = StringVar()
        self.actor_entry = Entry(window, textvariable = self.actor_text)
        self.actor_entry.grid(row=4, column=1, padx=20)

        #LISTBOX

        self.listbox = Listbox(window, height=4, width=20)
        self.listbox.grid(row=6,column=0, rowspan= 6, columnspan=2, sticky=NSEW, padx=20, pady=20)

        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)

        #SCROLLBAR

        sb =Scrollbar(window)
        sb.grid(row=8, column=2, padx=10, pady=20, sticky=W)
        sb.configure(command=self.listbox.yview)
        #BUTTONS

        #VIEW ALL BTN

        view_button = Button(window, text="View All", width=7, command=self.view_all)
        view_button.grid(row=1, column=2, padx=20)

        #ADD BTN
        view_button = Button(window, text="Add", width=7, command=self.add_entry)
        view_button.grid(row=2, column=2, padx=20)

        #DELETE BTN
        view_button = Button(window, text="Delete", width=7, command=self.delete_command)
        view_button.grid(row=3, column=2, padx=20)

        #EDIT BTN
        view_button = Button(window, text="Edit", width=7, command=self.update_command)
        view_button.grid(row=4, column=2, padx=20)

        #SEARCH BUTTON
        search_button = Button(window, text="Search", width=7, command=self.search_for)
        search_button.grid(row=5, column=2, padx=20)


        def view_all(self):
            self.listbox.delete(0,END)
            for row in database.view():
                self.listbox.insert(END,row)


        def search_for(self):
            self.listbox.delete(0,END)
            for row in database.search(self.quote_text.get(), self.movie_text.get(), self.character_text.get(), self.actor_text.get()):
                self.listbox.insert(END,row)

        def add_entry(self):
            database.insert(self.quote_text.get(), self.movie_text.get(), self.character_text.get(), self.actor_text.get())
            self.listbox.delete(0,END)
            self.listbox.insert(END, (self.quote_text.get(), self.movie_text.get(), self.character_text.get(), self.actor_text.get()))


        def get_selected_row(self, event):
            try:
                index=self.listbox.curselection()[0]
                self.selected_tuple=listbox.get(index)
                self.quote_entry.delete(0,END)
                self.quote_entry.insert(END, self.selected_tuple[1])
                self.movie_entry.delete(0,END)
                self.movie_entry.insert(END,self.selected_tuple[2])
                self.character_entry.delete(0,END)
                self.character_entry.insert(END, self.selected_tuple[3])
                self.actor_entry.delete(0,END)
                self.actor_entry.insert(END, self.selected_tuple[4])
            except IndexError:
                pass


        def delete_command(self):
            database.delete(self.selected_tuple[0])
            view_all()

        def update_command(self):
            database.edit(self.selected_tuple[0], self.quote_text.get(), self.movie_text.get(), self.character_text.get(), self.actor_text.get())
            view_all()

window=Tk()
Window(window)
window.mainloop()
