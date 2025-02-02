import tkinter as tk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# widgets
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

canvas.create_rectangle((
    50, 20, 100, 200),
    fill = 'red',
    width = 2,
    dash = (1,5,1,1),
    outline = 'green')

canvas.create_polygon(0,0, 100,200, 300,50, fill = 'yellow')
canvas.create_oval(200, 0, 100, 100, fill = 'black')
canvas.create_line(0, 0, 300, 200, fill = 'blue')

# events

# run
window.mainloop()