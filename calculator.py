import tkinter as tk

def on_button_click(char):
    """
    Appends the character of the pressed button to the display.
    """
    # Using the global variable 'expression' to store the input
    global expression
    expression = expression + str(char)
    # Updating the text in the display
    equation.set(expression)

def clear_display():
    """
    Clears the entire expression in the display.
    """
    # Using the global variable 'expression' and resetting it
    global expression
    expression = ""
    # Setting the display text to empty
    equation.set("")

def calculate_result():
    """
    Calculates the result of the expression in the display.
    Uses eval() to evaluate the string expression, with error handling.
    """
    # Using the global variable 'expression'
    global expression
    try:
        # The eval function evaluates the passed string as a Python expression
        # and returns the result.
        total = str(eval(expression))
        equation.set(total)
        # Set the expression to the result for further calculations
        expression = total
    except:
        # Handling errors like division by zero or syntax errors
        equation.set(" error ")
        expression = ""

# --- GUI Setup ---
if __name__ == "__main__":
    # Create the main window
    window = tk.Tk()
    window.title("Simple Calculator")
    window.geometry("300x400")
    window.configure(bg="#f0f0f0") # Light grey background

    # Global variable for the expression string
    expression = ""

    # StringVar to hold the text for the display
    equation = tk.StringVar()

    # Create the display Entry widget
    display = tk.Entry(window, textvariable=equation, font=('Arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
    equation.set('0') # Initialize display with '0'

    # --- Button Creation and Layout ---
    # Define button properties for a consistent look
    button_props = {
        'font': ('Arial', 14),
        'fg': 'black',
        'bg': '#e0e0e0', # A slightly darker grey for buttons
        'relief': 'raised',
        'bd': 3,
        'width': 5,
        'height': 2
    }

    # Creating and placing buttons in a grid
    # Row 1
    tk.Button(window, text='7', **button_props, command=lambda: on_button_click(7)).grid(row=1, column=0)
    tk.Button(window, text='8', **button_props, command=lambda: on_button_click(8)).grid(row=1, column=1)
    tk.Button(window, text='9', **button_props, command=lambda: on_button_click(9)).grid(row=1, column=2)
    tk.Button(window, text='/', **button_props, bg='#ff9f43', command=lambda: on_button_click('/')).grid(row=1, column=3) # Operator color

    # Row 2
    tk.Button(window, text='4', **button_props, command=lambda: on_button_click(4)).grid(row=2, column=0)
    tk.Button(window, text='5', **button_props, command=lambda: on_button_click(5)).grid(row=2, column=1)
    tk.Button(window, text='6', **button_props, command=lambda: on_button_click(6)).grid(row=2, column=2)
    tk.Button(window, text='*', **button_props, bg='#ff9f43', command=lambda: on_button_click('*')).grid(row=2, column=3)

    # Row 3
    tk.Button(window, text='1', **button_props, command=lambda: on_button_click(1)).grid(row=3, column=0)
    tk.Button(window, text='2', **button_props, command=lambda: on_button_click(2)).grid(row=3, column=1)
    tk.Button(window, text='3', **button_props, command=lambda: on_button_click(3)).grid(row=3, column=2)
    tk.Button(window, text='-', **button_props, bg='#ff9f43', command=lambda: on_button_click('-')).grid(row=3, column=3)

    # Row 4
    tk.Button(window, text='0', **button_props, command=lambda: on_button_click(0)).grid(row=4, column=0)
    tk.Button(window, text='.', **button_props, command=lambda: on_button_click('.')).grid(row=4, column=1)
    tk.Button(window, text='+', **button_props, bg='#ff9f43', command=lambda: on_button_click('+')).grid(row=4, column=2)
    tk.Button(window, text='C', **button_props, bg='#f55', command=clear_display).grid(row=4, column=3) # Clear button color

    # Row 5 (Equals Button)
    tk.Button(window, text='=', **button_props, bg='#28a745', command=calculate_result).grid(row=5, column=0, columnspan=4, sticky='nsew', padx=10, pady=10) # Equals button spans all columns

    # Start the GUI event loop
    window.mainloop()
