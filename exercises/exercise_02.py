import tkinter as tk
from logging import disable
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get()

    #update label
    # label.config(text = 'Some Other Text')
    label['text'] = entry_text
    entry['state'] = 'disabled'

def reverse_func():
    label['text'] = "Some Text"
    entry['state'] = 'enabled'

# window
window = tk.Tk()
window.title('Getting and Setting Widgets')

# widgets
label = tk.Label(window, text = "Some Text")
label.pack()

entry = ttk.Entry(window)
entry.pack()

button = tk.Button(window, text = "The button", command = button_func)
button.pack()

# exercise
exercise_button = tk.Button(window, text = 'Reverse', command = reverse_func)
exercise_button.pack()

# run
window.mainloop()