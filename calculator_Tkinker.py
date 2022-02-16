from ast import operator
from cgitb import text
from tkinter import *
import math


#Essential
root = Tk()


#Change BG color
root.configure(bg="#2d2d2d")
#Title
root.title("Roger Calculator")


#Calculator Input
calculator_input = Entry(root, width=70,borderwidth=5)
calculator_input.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
calculator_input.insert(0, "")


def button_click(text):
    global current
    current = calculator_input.get()
    calculator_input.delete(0, END)
    calculator_input.insert(0, str(current) + str(text))
    if text == "C":
        calculator_input.delete(0, END)
    elif text == "<--":
        delete_last = calculator_input.delete(calculator_input.index("end") -1)
        delete_last = calculator_input.delete(calculator_input.index("end") -1)
        delete_last = calculator_input.delete(calculator_input.index("end") -1)
        delete_last = calculator_input.delete(calculator_input.index("end") -1)


def operators(operator):
    first_number = calculator_input.get()
    global f_num
    f_num = int(first_number)
    global math
    math = operator
    if operator == "+":
        math = "+"
    elif operator == "-":
        math = "-"
    elif operator == "÷":
        math = "/"
    elif operator == "×":
        math = "*"
    elif operator == "√":
        math = "sqrt"
    elif operator == "x^2":
        math = "x^2"
    calculator_input.delete(0,END)

def button_equal():
    second_number = calculator_input.get()
    calculator_input.delete(0, END)
    global f_num
    global math
    if math == "+":
        calculator_input.insert(0, f_num + int(second_number))
    elif math == "-":
        calculator_input.insert(0, f_num - int(second_number))
    elif math == "/":
        calculator_input.insert(0, f_num / int(second_number))
    elif math == "*":
        calculator_input.insert(0, f_num * int(second_number))
    elif math == "sqrt":
        calculator_input.insert(0, math.sqrt(int(f_num)))
    elif math == "x^2":
        calculator_input.insert(0, f_num * f_num)
    



#button function
def button(text_button, padx_button, pady_button, row_button, column_button):
    my_button = Button(root, text=text_button, padx=padx_button, pady=pady_button, command=lambda :button_click(text_button), bg="#333333", fg="white")
    my_button.grid(row=row_button, column=column_button)


def button_operations(text_button, padx_button, pady_button, row_button, column_button):
    my_button = Button(root, text=text_button, padx=padx_button, pady=pady_button, command=lambda :operators(text_button), bg="#333333", fg="white")
    my_button.grid(row=row_button, column=column_button)


button(7, 40, 10, 1, 0)
button(8, 40, 10, 1, 1)
button(9, 40, 10, 1, 2)
button_operations("÷", 40, 10, 1, 3)
button("<--", 40, 10, 1, 4)
button("C", 47, 10, 1, 5)


button(4, 40, 10, 2, 0)
button(5, 40, 10, 2, 1)
button(6, 40, 10, 2, 2)
button_operations("×", 40, 10, 2, 3)
button("(", 48, 10, 2, 4)
button(")", 49, 10, 2, 5)


button(1, 40, 10, 3, 0)
button(2, 40, 10, 3, 1)
button(3, 40, 10, 3, 2)
button_operations("-", 42, 10, 3, 3)
button_operations("x^2", 37, 10, 3, 4)
button_operations("√", 47, 10, 3, 5)


button(0, 40, 10, 4, 0)
button(".", 42, 10, 4, 1)
button_operations("%", 37.5, 10, 4, 2)
button_operations("+", 37.5, 10, 4, 3)
equal_button = Button(root, text="=", padx=100, pady=10, command=button_equal, bg="#638600", fg="white")
equal_button.grid(row=4, column=4, columnspan=2)


#Essential
root.mainloop()