import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')

# combobox
items = ('Ice Cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
combo['values'] = items
combo.pack()

# spin
spin = tk.Spinbox(window)
spin.pack()
spin['values'] = items

# run
window.mainloop()