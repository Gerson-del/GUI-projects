import tkinter as tk
import math
calculation = ""

def add_to_calculation(symbol):
    global calculation
    if symbol == "sqrt":
        calculation += "sqrt("
    else:
        calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = ""
        if "sqrt" in calculation:  # Check if square root function is present in the calculation
            parts = calculation.split("sqrt(")  # Split calculation string by "sqrt("
            result += parts[0]  # Append the part before the square root function
            for part in parts[1:]:  # Iterate over the parts after "sqrt("
                number = float(part.split(")")[0])  # Extract the number inside square root function
                result += str(math.sqrt(number))  # Calculate square root and append to result
                result += part.split(")")[1]  # Append the rest of the calculation
        else:
            result = str(eval(calculation))  # Evaluate calculation as normal
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

def clear_last():
    global calculation
    if len(calculation) > 0:
        calculation = calculation[:-1]
        text_result.delete("end-2c", "end")

def glowing(event):
    # Gradually change the background color to simulate glowing effect
    for i in range(255):
        color = "#{:02x}{:02x}{:02x}".format(i + 80,255 - i, i)  # Custom color format
        event.widget.config(bg=color)
        event.widget.update()

root = tk.Tk()
root.geometry("300x350")

root.resizable(False, False)

text_result = tk.Text(root, height=3, width=16, font=("Arial", 24), bg="white")
text_result.grid(columnspan = 5)

#Añadamos color cuando colocas el cursor



#Button 1
btn_1 = tk.Button(root, text=1, command=lambda: add_to_calculation(1), width=5, font=("Arial", 14), bg="lightblue", fg="black")
btn_1.grid(row=3, column=1)
btn_1.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_1.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))
#Button 2
btn_2 = tk.Button(root, text = 2, command = lambda : add_to_calculation(2), width=5, font=("Arial", 14), bg="lightblue", fg="black")
btn_2.grid(row = 3, column = 2)
btn_2.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_2.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))
#Button 3
btn_3 = tk.Button(root, text = 3, command = lambda : add_to_calculation(3), width=5, font=("Arial", 14), bg="lightblue", fg="black")
btn_3.grid(row = 3, column = 3)
btn_3.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_3.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))
#Button 4
btn_4 = tk.Button(root, text = 4, command = lambda : add_to_calculation(4), width=5, font=("Arial", 14), bg="lightblue", fg="black")
btn_4.grid(row = 4, column = 1)
btn_4.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_4.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))
#Button 5
btn_5 = tk.Button(root, text = 5, command = lambda : add_to_calculation(5), width=5, font=("Arial", 14), bg="lightblue", fg="black")
btn_5.grid(row = 4, column = 2)
btn_5.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_5.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))
#Button 6
btn_6 = tk.Button(root, text = 6, command = lambda : add_to_calculation(6), width=5, font=("Arial", 14), bg="lightblue", fg="black")
btn_6.grid(row = 4, column = 3)
btn_6.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_6.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))
#Button 7
btn_7 = tk.Button(root, text = 7, command = lambda : add_to_calculation(7), width=5, font=("Arial", 14), bg="lightblue", fg="black")
btn_7.grid(row = 5, column = 1)
btn_7.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_7.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))
#Button 8
btn_8 = tk.Button(root, text = 8, command = lambda : add_to_calculation(8), width=5, font=("Arial", 14), bg="lightblue", fg="black")
btn_8.grid(row = 5, column = 2)
btn_8.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_8.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))
#Button 9
btn_9 = tk.Button(root, text = 9, command = lambda : add_to_calculation(9), width=5, font=("Arial", 14), bg="lightblue", fg="black")
btn_9.grid(row = 5, column = 3)
btn_9.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_9.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))
# Button 0
btn_0 = tk.Button(root, text=0, command=lambda: add_to_calculation(0), width=12, font=("Arial", 14), bg="lightblue", fg="black")
btn_0.grid(row=6, column=1, columnspan=2)  # Ocupa dos columnas
btn_0.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_0.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))

# Button .
btn_point = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14), bg="lightblue", fg="black")
btn_point.grid(row=6, column=3) 
btn_point.bind("<Enter>", lambda event: event.widget.config(bg="lightcyan"))
btn_point.bind("<Leave>", lambda event: event.widget.config(bg="lightblue"))

#Button +
btn_plus = tk.Button(root, text = "+", command = lambda : add_to_calculation("+"), width = 5, font = ("arial", 14), bg="white", fg="black")
btn_plus.grid(row = 5, column = 4)
btn_plus.bind("<Enter>", lambda event: event.widget.config(bg="Light Gray"))
btn_plus.bind("<Leave>", lambda event: event.widget.config(bg="white"))
#Button -
btn_minus = tk.Button(root, text = "-", command = lambda : add_to_calculation("-"), width = 5, font = ("arial", 14), bg="white", fg="black")
btn_minus.grid(row = 6, column = 4)
btn_minus.bind("<Enter>", lambda event: event.widget.config(bg="Light Gray"))
btn_minus.bind("<Leave>", lambda event: event.widget.config(bg="white"))

#Button *
btn_mult = tk.Button(root, text = "x", command = lambda : add_to_calculation("*"), width = 5, font = ("arial", 14), bg="white", fg="black")
btn_mult.grid(row = 4, column = 4)
btn_mult.bind("<Enter>", lambda event: event.widget.config(bg="Light Gray"))
btn_mult.bind("<Leave>", lambda event: event.widget.config(bg="white"))
#Button /
btn_div = tk.Button(root, text = "/", command = lambda : add_to_calculation("/"), width = 5, font = ("arial", 14), bg="white", fg="black")
btn_div.grid(row = 3, column = 4)
btn_div.bind("<Enter>", lambda event: event.widget.config(bg="Light Gray"))
btn_div.bind("<Leave>", lambda event: event.widget.config(bg="white"))
#Button sqrt

btn_sqrt = tk.Button(root, text="\u221A", command=lambda: add_to_calculation("sqrt"), width=5, font=("arial", 14), bg="white", fg="black")
btn_sqrt.grid(row=7, column=4)
btn_sqrt.bind("<Enter>", lambda event: event.widget.config(bg="Light Gray"))
btn_sqrt.bind("<Leave>", lambda event: event.widget.config(bg="white"))
#Parenthesis open "("
btn_open = tk.Button(root, text = "(", command = lambda : add_to_calculation("("), width = 5, font = ("arial", 14), bg="white", fg="black")
btn_open.grid(row = 2, column = 1)
btn_open.bind("<Enter>", lambda event: event.widget.config(bg="Light Gray"))
btn_open.bind("<Leave>", lambda event: event.widget.config(bg="white"))
#Parenthesis close ")"
btn_close = tk.Button(root, text = ")", command = lambda : add_to_calculation(")"), width = 5, font = ("arial", 14), bg="white", fg="black")
btn_close.grid(row = 2, column = 2)
btn_close.bind("<Enter>", lambda event: event.widget.config(bg="Light Gray"))
btn_close.bind("<Leave>", lambda event: event.widget.config(bg="white"))
#Botton C (Delete last element) (Tengo que crear una funcion para esto)

btn_clear = tk.Button(root, text = "C", command = clear_last, width = 5, font = ("arial", 14), bg="white", fg="black")
btn_clear.grid(row = 2, column = 3)
btn_clear.bind("<Enter>", lambda event: event.widget.config(bg="Light Gray"))
btn_clear.bind("<Leave>", lambda event: event.widget.config(bg="white"))
#Button =
btn_equal = tk.Button(root, text = "=", command = evaluate_calculation, width=18, font=("Arial", 14), bg="white", fg="black")
btn_equal.grid(row = 7, column = 1, columnspan=3)
btn_equal.bind("<Enter>", glowing)
btn_equal.bind("<Leave>", lambda event: event.widget.config(bg="white"))
#Button del
btn_del = tk.Button(root, text = "del", command = clear_field, width=5, font=("Arial", 14), bg="white", fg="black")
btn_del.grid(row = 2, column = 4)
btn_del.bind("<Enter>", lambda event: event.widget.config(bg="Light Gray"))
btn_del.bind("<Leave>", lambda event: event.widget.config(bg="white"))

# Bind for numbers
root.bind('1', lambda event: add_to_calculation(1))
root.bind('2', lambda event: add_to_calculation(2))
root.bind('3', lambda event: add_to_calculation(3))
root.bind('4', lambda event: add_to_calculation(4))
root.bind('5', lambda event: add_to_calculation(5))
root.bind('6', lambda event: add_to_calculation(6))
root.bind('7', lambda event: add_to_calculation(7))
root.bind('8', lambda event: add_to_calculation(8))
root.bind('9', lambda event: add_to_calculation(9))
root.bind('0', lambda event: add_to_calculation(0))

# Bind the keyboard input handling functions for operators
root.bind('+', lambda event: add_to_calculation("+"))
root.bind('-', lambda event: add_to_calculation("-"))
root.bind('*', lambda event: add_to_calculation("*"))
root.bind('/', lambda event: add_to_calculation("/"))

# Bind the special keywords
root.bind('<Return>', lambda event: evaluate_calculation())
root.bind('(', lambda event: add_to_calculation("("))
root.bind(')', lambda event: add_to_calculation(")"))
root.bind('c', lambda event: clear_field())
root.bind('<BackSpace>', lambda event: clear_last())
root.bind('<Return>', lambda event: evaluate_calculation())
root.bind('<Delete>', lambda event: clear_field())
root.bind('<Shift-6>', lambda event: add_to_calculation("^"))

root.mainloop()