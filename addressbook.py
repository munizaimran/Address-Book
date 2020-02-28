from tkinter import *
import sqlite3
root  = Tk()

root.title("Address Book")
heading = Label(text = "ADDRESS BOOK\n", font = ("bold", 15))
heading.grid(column = 2, row = 0)
root.geometry("300x300")

conn = sqlite3.connect('addressbook.db')
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer,
		p_number integer
		)""")'''

def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('addressbook.db')
	# Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode, :p_number)",
			{
				'f_name': e.get(),
				'l_name': e2.get(),
				'address': e3.get(),
				'city': e4.get(),
				'state': e5.get(),
				'zipcode': e6.get(),
				'p_number': e7.get()
			})


	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

	# Clear The Text Boxes
	e.delete(0, END)
	e2.delete(0, END)
	e3.delete(0, END)
	e4.delete(0, END)
	e5.delete(0, END)
	e6.delete(0, END)
	e7.delete(0, END)


Label1 = Label(root, text = "   Fisrt Name: ")
Label1.grid(column = 0, row = 1)
e = Entry(root)
e.grid(column = 2, row = 1)

Label2 = Label(root, text = "   Last Name: ")
Label2.grid(column = 0, row = 2)
e2 = Entry(root)
e2.grid(column = 2, row = 2)

Label3 = Label(root, text = "   Address: ")
Label3.grid(column = 0, row =3)
e3 = Entry(root)
e3.grid(column = 2, row = 3)

Label4 = Label(root, text = "   City: ")
Label4.grid(column = 0, row = 4)
e4 = Entry(root)
e4.grid(column = 2, row = 4)

Label5 = Label(root, text = "   State: ")
Label5.grid(column = 0, row = 5)
e5 = Entry(root)
e5.grid(column = 2, row = 5)

Label6 = Label(root, text = "   Zip Code: ")
Label6.grid(column = 0, row = 6)
e6 = Entry(root)
e6.grid(column = 2, row = 6)

Label7 = Label(root, text = "   Phone Number: ")
Label7.grid(column = 0, row = 7)
e7 = Entry(root)
e7.grid(column = 2, row = 7)

Label8 = Label(root, text = "\n")
Label8.grid(column= 2, row =8)

Button1 = Button(root, text = "Submit", command=submit)
Button1.grid(column= 2, row =9)

root.mainloop()