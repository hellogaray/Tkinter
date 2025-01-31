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

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))
combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

# spin
spin_int = tk.IntVar(value = 5)
spin = ttk.Spinbox(
    window,
    from_ = 3, to = 20,
    increment = 2,
    command = lambda: print(spin_int.get()),
    textvariable = spin_int)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
spin.pack()


# exercise
ex_letters = ('a', 'b', 'c', 'd', 'e')
ex_spin_value = tk.StringVar(value = ex_letters[0])
ex_spin = ttk.Spinbox(
    window,
    values = ex_letters,
    textvariable = ex_spin_value)
ex_spin.bind('<<Decrement>>', lambda event: print(ex_spin_value.get()))
ex_spin.pack()
# run
window.mainloop()