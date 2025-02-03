import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x500')
window.title('Tab Widget')

# widgets
notebook = ttk.Notebook(window)

#tab 1
tab1 = ttk.Frame(notebook)
label = ttk.Label(tab1, text = 'Text in tab 1')
label.pack()
button = ttk.Button(tab1, text = 'Button in tab 1')
button.pack()

# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = 'Text in tab 2')
label2.pack()
button2 = ttk.Button(tab2, text = 'Button in tab 2')
button2.pack()

notebook.add(tab1, text = 'Tab 1')
notebook.add(tab2, text = 'Tab 2')
notebook.pack()

# exercise tab
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text = 'Tab 3')

ex_btn = ttk.Button(tab3, text = 'button 1')
ex_btn.pack()

ex_btn2 = ttk.Button(tab3, text = 'button 2')
ex_btn2.pack()

ex_label = ttk.Label(tab3, text = 'Label')
ex_label.pack()

# run
window.mainloop()