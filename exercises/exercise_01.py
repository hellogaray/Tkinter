import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button was pressed')

def print_hello_func():
    print('hello')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk widgets
label = ttk.Label(window, text = 'This is a test')
label.pack()

# tk widgets
text = (tk.Text(window))
text.pack()

# ttk entry
entry = ttk.Entry(window)
entry.pack()

#exercise
exercise_label = ttk.Label(window, text ='My Label')
exercise_label.pack()

button = tk.Button(window, text = 'A button', command = button_func)
button.pack()


#exercise
# exercise_button = ttk.Button(window, text = 'Print Hello', command = print_hello_func)
exercise_button = ttk.Button(window, text = 'Print Hello', command = lambda: print('hello'))
exercise_button.pack()

# run
window.mainloop()