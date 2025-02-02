import tkinter as tk
from tkinter import ttk
from turtledemo.penrose import start

# window
window = tk.Tk()
window.title('Slider')

# slider
scale_int = tk.IntVar(value = 15)
scale = ttk.Scale(
    window,
    command = lambda value: print(scale_int.get()),
    from_ = 0,
    to = 25,
    orient = 'horizontal',
    variable = scale_int)

scale.pack()

# progress bar
progress = ttk.Progressbar(
    window,
    variable = scale_int,
    maximum = 25,
    orient = 'horizontal',
    mode = 'determinate',
    length = 400)

progress.pack()

# exercise
ex_int = tk.IntVar(value = 0)

ex_bar = ttk.Progressbar(
    window,
    variable = ex_int,
    maximum = 100,
    orient = 'vertical')

ex_bar.pack()
ex_bar.start()

label = ttk.Label(window, textvariable= ex_int)
label.pack()

ex_slide = ttk.Scale(
    window,
    variable = ex_int,
    from_ = 0,
    to = 100)

ex_slide.pack()



# run
window.mainloop()