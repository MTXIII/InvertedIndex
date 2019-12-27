from tkinter import *
import InvertedIndex as bck

print(bck)
print(dir(bck))

HeadFont = ('sfprodisplay', 20, 'bold')
LARGE_FONT = ("Verdana", 12, 'bold')
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

def open():
	top = Toplevel()
	searching = 'Occurences of the term: ' + Term.get()
	lbl = Label(top, text=searching, width = 40, font = LARGE_FONT)
	lbl.pack()
	listbox = Listbox(top)
	listbox.pack()

	# for line in bck.index_lookup_query(Term.get()):
	for line in bck.index_lookup_query(Term.get()):
		listbox.insert(END, line)


#create the tkinter window.
root = Tk()
root.geometry('300x85')
# frame = Frame(root, width=100, height=15, bg='white')
# frame.pack()

# to rename the title of the root
root.title("Term Search")

#Label for entry box.
Label(root, text = "Enter search term:", font = LARGE_FONT).pack() 


# Entry box.
Term = Entry(root, width=30)
Term.pack(side = TOP)
# Term.insert(0,"Enter the term to search for:")
# Term.grid(row = 0, column = 0) 


# Search button.
search_for = "Searching for " + Term.get()
b1 = Button(root, text = "Search!", bg = 'grey', fg = "red", width = 15, command = open)
b1.pack()
# b1.grid(row = 1, column = 0) #'fg or foreground' is for coloring the contents (buttons)


mainloop()
