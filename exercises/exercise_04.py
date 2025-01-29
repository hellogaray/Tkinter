import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# button
def button_func():
    print('a basic button')

button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(window, text = 'button', command = button_func, textvariable = button_string)
button.pack()

# checkbox_1
check_var_1 = tk.IntVar(value = 10)
checkbox_1 = ttk.Checkbutton(
    window,
    text = 'checkbox 1',
    command = lambda: print(check_var_1.get()),
    variable = check_var_1,
    onvalue = 10,
    offvalue = 5)
checkbox_1.pack()

# checkbox_2
check_var_2 = tk.StringVar()
checkbox_2 = ttk.Checkbutton(
    window,
    text = 'checkbox 2',
    command = lambda: check_var_1.set(5),
    variable = check_var_2,)
checkbox_2.pack()

# radio_button_1
radio_var = tk.StringVar()
radio_button_1 = ttk.Radiobutton(
    window,
    text = 'Radio button 1',
     value = 'radio 1',
     variable = radio_var,
     command = lambda: print(radio_var.get()))
radio_button_1.pack()

# radio_button_2
radio_button_2 = ttk.Radiobutton(
    window,
    text = 'Radio button 2',
    value = 'radio 2')
radio_button_2.pack()





# exercise

def radio_func():
    print(check_button_1.get())
    check_button_1.set(False)

#data
radio_var_ex = tk.StringVar()
check_button_1 = tk.IntVar()

# widgets
radio_button_a = ttk.Radiobutton(
    window,
    text = 'Radio Button a',
    value = 'a',
    variable = radio_var_ex,
    command = radio_func)

radio_button_b = ttk.Radiobutton(
    window,
    text = 'Radio Button b',
    value = 'b',
    variable = radio_var_ex,
    command = radio_func)

check_button = ttk.Checkbutton(
    window,
    text = 'Check Button',
    variable = check_button_1,
    command = lambda: print(radio_var_ex.get()))
# layout
radio_button_a.pack()
radio_button_b.pack()
check_button.pack()

# run
window.mainloop()