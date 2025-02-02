import random
import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# data
first_names =['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# widget
table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First name')
table.heading('last', text = 'Last name')
table.heading('email', text = 'Email')
table.pack(fill = 'both', expand = True)

# insert values into a table
# table.insert(parent = '', index = 0, values = ('John', 'Doe', 'email@meial.com'))

for i in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f'{last}{first}@email.com'
    data = (first, last, email)

    table.insert(parent = '', index = i, values = data)

# events
def item_select(_):
    for row in table.selection():
        print(table.item(row)['values'])

table.bind('<<TreeviewSelect>>', item_select)

def delete_items(_):
    for row in table.selection():
        print(f'{table.item(row)['values']} was delete')
        table.delete(row)

# Delete on Mac
table.bind('<BackSpace>', delete_items)
# Delete on PC
table.bind('<Delete>', delete_items)

# run
window.mainloop()