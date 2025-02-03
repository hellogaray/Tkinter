import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x500')
window.title('Frames and Parenting')

# frame
frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side = 'left')
frame.pack()

# master setting
label = ttk.Label(frame, text = 'Label in Frame')
label.pack()

#example
label12 = ttk.Label(window, text = 'Label outside frame')
label12.pack(side = 'left')

# exercise
ex_frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
ex_frame.pack_propagate(False)
ex_frame.pack(side = 'right')

ex_label = ttk.Label(ex_frame, text = 'Label')
ex_label.pack()

ex_button = ttk.Button(ex_frame, text = 'Button')
ex_button.pack()

ex_entry = ttk.Entry(ex_frame)
ex_entry.pack()

# run
window.mainloop()