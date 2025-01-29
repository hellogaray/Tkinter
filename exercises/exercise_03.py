import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')
# window
window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable
string_var = tk.StringVar()
string_var_2 = tk.StringVar(value = 'test')

# widgets
label = ttk.Label(window, text = "label", textvariable = string_var)
label.pack()

entry = ttk.Entry(window, textvariable = string_var)
entry.pack()

button = ttk.Button(window, text = 'button', command = button_func)
button.pack()

#excercise
field_01 = ttk.Entry(window, textvariable = string_var_2)
field_01.pack()

field_02 = ttk.Entry(window, textvariable = string_var_2)
field_02.pack()

exercise_label = ttk.Label(window, textvariable = string_var_2)
# run
window.mainloop()