import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x500')
window.title('')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = 'button')
btn.pack()

# events
window.bind('<Control-KeyPress-a>', lambda event: print('an event'))

# exercise
text.bind('<Shift-MouseWheel>', lambda event: print('mousewheel'))
# run
window.mainloop()