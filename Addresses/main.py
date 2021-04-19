from tkinter import *
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title('Batman')
root.iconbitmap('images/batman.ico')
root.geometry('360x700')

# Database

# Create DB or Connect to one
conn = sqlite3.connect('addres_book.db')

# Create Cursor
cursor = conn.cursor()

# Tables
'''
cursor.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode text
    )
    """)
'''
# Update Func
def update():
    conn = sqlite3.connect('addres_book.db')
    cursor = conn.cursor()
    record_id = select_boxes.get()

    cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
                   {
                       'first':f_entry_editor.get(),
                       'last':l_entry_editor.get(),
                       'address':address_editor.get(),
                       'city':city_editor.get(),
                       'state':state_editor.get(),
                       'zipcode':zipcode_editor.get(),

                       'oid':record_id
                   })


    conn.commit()
    conn.close()
    editor.destroy()

# Edit Record
def edit():
    global editor
    editor = Tk()
    editor.title('Edit A Record')
    editor.iconbitmap('C:/Users/ti.infra/desktop/python/Tkinter Course/Addresses/images/batman.ico')
    editor.geometry('360x200')
    conn = sqlite3.connect('addres_book.db')
    cursor = conn.cursor()
    record_id = select_boxes.get()
    cursor.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records = cursor.fetchall()

    # Globals
    global f_entry_editor
    global l_entry_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create Entry Boxes
    f_entry_editor = Entry(editor, width=30)
    f_entry_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_entry_editor = Entry(editor, width=30)
    l_entry_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)


    # Create Entry Text Boxes
    f_name_label_editor = Label(editor, text='First Name')
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text='Last Name')
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text='Address')
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text='City')
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text='State')
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text='Zipcode')
    zipcode_label_editor.grid(row=5, column=0)


    for record in records:
        f_entry_editor.insert(0, record[0])
        l_entry_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Save Button
    save_button = Button(editor, text='Save Changes', command=update)
    save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=120)

    conn.commit()
    conn.close()



# Delete Record
def delete():
    conn = sqlite3.connect('addres_book.db')
    cursor = conn.cursor()
    cursor.execute('DELETE from addresses WHERE oid= ' + select_boxes.get())

    conn.commit()
    conn.close()

# Submit function to database
def submit():
    # Create DB or Connect to one
    conn = sqlite3.connect('addres_book.db')
    # Create Cursor
    cursor = conn.cursor()
    # Insert Into Table
    cursor.execute("INSERT INTO addresses VALUES(:f_entry, :l_entry, :address, :city, :state, :zipcode)",
                   {
                       'f_entry':f_entry.get(),
                       'l_entry':l_entry.get(),
                       'address':address.get(),
                       'city':city.get(),
                       'state':state.get(),
                       'zipcode':zipcode.get()
                   })


    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear Text
    f_entry.delete(0, END)
    l_entry.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)
    state.delete(0, END)

def query():
    # Create DB or Connect to one
    conn = sqlite3.connect('addres_book.db')
    # Create Cursor
    cursor = conn.cursor()
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    print_records = ''
    for record in records:
        print_records += record[0] + ' ' + record[1] + "\t\t" + str(record[6]) + "\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

# Create Entry Boxes
f_entry = Entry(root, width=30)
f_entry.grid(row=0, column=1, padx=20, pady=(10, 0))
l_entry = Entry(root, width=30)
l_entry.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
select_boxes = Entry(root, width=30)
select_boxes.grid(row=9, column=1)


# Create Entry Text Boxes
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)
select_boxes_label = Label(root, text='Select ID')
select_boxes_label.grid(row=9, column=0)


# Create Submit Button
submit_button = Button(root, text='Add Record To Database', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_button = Button(root, text='Show Records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create a Delete Button

delete_button = Button(root, text='Delete Record', command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# Create an Update Button

edit_button = Button(root, text='Edit Record', command=edit)
edit_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
