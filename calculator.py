import customtkinter as ctk
from tkinter import END
from PIL import Image

# Define the color for the '=' button
orange = '#bf5b19'

# Initialize the main application
app = ctk.CTk()

# Set the title and geometry of the window
app.title("Calculator")
app.geometry("400x650")
app.resizable(False, False)

# Load and set the new icon
app.iconbitmap('images/calculator.ico')

# Function to update the entry widget when a button is clicked
def button_click(item):
    current = entry.get()
    entry.delete(0, END)
    if current == 'Error':
        entry.insert(END, str(item))
    elif item == '%':
        # Calculate percentage
        try:
            result = float(current) / 100.0
            previous_display.delete(0, END)
            previous_display.insert(END, current + '% = ' + str(result))
            entry.insert(END, str(result))
        except Exception as e:
            entry.insert(END, "Error")
    else:
        entry.insert(END, current + str(item))

# Function to clear the entry widget
def clear_all(event=None):
    entry.delete(0, END)

# Function to delete the last character
def delete_last(event=None):
    current = entry.get()
    entry.delete(0, END)
    if current == 'Error':
        entry.delete(0, END)
    else:
        entry.insert(END, current[:-1])

# Function to evaluate the expression
def calcutaion(event=None):
    try:
        current = entry.get()
        if current != '':
            result = eval(current)
            # Clear the previous display entry and update with result
            previous_display.delete(0, END)
            previous_display.insert(END, current + ' = ' + str(result))
            # Clear the main entry and update with result
            entry.delete(0, END)
            entry.insert(END, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Create an entry widget for displaying the previous expression and result
previous_display = ctk.CTkEntry(app, width=390, height=120, font=("Arial", 24), justify='right')
previous_display.grid(row=0, column=0, columnspan=4, pady=(20, 5), padx=5)

# Create an entry widget for the current input and result
entry = ctk.CTkEntry(app, width=390, height=100, font=("Arial", 45), justify='right', border_color='#12d8db')
entry.grid(row=1, column=0, columnspan=4, pady=(0, 10), padx=5)

# Define the buttons with their text, row, and column positions
buttons = [
    ('C', 2, 0), ('%', 2, 1), ('DEL', 2, 2), ('/', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('x', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
    ('0', 6, 0), ('00', 6, 1), ('.', 6, 2), ('=', 6, 3),
]

# Load the image for the delete button
img = Image.open('images/delete.png')

# Add buttons to the grid with reduced padding
for (text, row, col) in buttons:
    if text == 'C':
        button = ctk.CTkButton(app, text=text, font=('default', 20), width=70, height=70, corner_radius=40, command=clear_all)
        app.bind('<Escape>', clear_all)
    elif text == 'DEL':
        button = ctk.CTkButton(app, text='', image=(ctk.CTkImage(img)), width=70, height=70, corner_radius=60, command=delete_last)
        app.bind('<BackSpace>', delete_last)
    elif text == '=':
        button = ctk.CTkButton(app, text=text, font=('default', 20), width=70, height=70, corner_radius=60, command=calcutaion, fg_color=orange)
        app.bind('<Return>', calcutaion)
    elif text == 'x':
        button = ctk.CTkButton(app, text=text, font=('default', 20), width=70, height=70, corner_radius=60, command=lambda t='*': button_click(t))
        app.bind('*', lambda event, t='*': button_click(t))
    else:
        button = ctk.CTkButton(app, text=text, font=('default', 20), width=70, height=70, corner_radius=60, command=lambda t=text: button_click(t))
        app.bind(text, lambda event, t=text: button_click(t))

    button.grid(row=row, column=col, padx=3, pady=3)  # Adjust padx and pady as needed

# Run the application
app.mainloop()
