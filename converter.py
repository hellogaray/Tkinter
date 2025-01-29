import tkinter as tk
import ttkbootstrap as ttk

def convert():
    try:
        # Get the input value as float for better handling of decimals
        mile_input = float(entry_int.get())
        km_output = mile_input * 1.609344
        output_string.set(f"{km_output:.2f} km")  # Format to 2 decimal places
    except ValueError:
        output_string.set("Invalid input! Please enter a number.")

# Create window with 'darkly' theme
window = ttk.Window(themename = 'darkly')
window.title("Miles to Kilometers Converter")
window.geometry("300x150")

# Title Label
title_label = ttk.Label(window,
                        text = "Miles To Kilometers",
                        font = 'Calibri 16 bold')
title_label.pack(pady = 10)

# Input Frame
input_frame = ttk.Frame(window)
entry_int = tk.StringVar()  # Use StringVar for flexibility with both int and float
entry = ttk.Entry(input_frame,
                  textvariable = entry_int,
                  font = 'Calibri 14',
                  width = 10)
button = ttk.Button(input_frame,
                    text = "Convert",
                    command = convert, style = "primary.TButton")

# Arrange input and button in a row
entry.pack(side = 'left', padx = 5)
button.pack(side = 'left', padx = 5)
input_frame.pack(pady = 10)

# Output Label
output_string = tk.StringVar()
output_label = ttk.Label(window,
                         textvariable = output_string,
                         font = 'Calibri 14 bold',
                         foreground = "white")
output_label.pack(pady = 10)

# Run the window
window.mainloop()
