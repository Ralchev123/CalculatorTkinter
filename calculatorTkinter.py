import tkinter as tk
from tkinter import ttk

counter = 0
number_1 = -1
number_2 = -1
operation = 0
result = 0
global number_label
global result_label
global what_operation

def number_becomity (number_reg):
    global number_1, counter, operation, number_label, result_label, number_2
    if operation == 0:
        if counter == 0:
            number_1 = number_reg
            counter = counter + 1
            number_label = tk.Label(root, text = number_1, font = ("Arial", 20))
            number_label.place(relx = 0.35, rely = 0.02)
        else:
            number_1 = number_1 * 10 + number_reg
            number_label = tk.Label(root, text = number_1, font = ("Arial", 20))
            number_label.place(relx = 0.35, rely = 0.02)

    if operation == 1:
        if counter == 0:
            number_2 = number_reg
            counter = counter + 1
            number_label = tk.Label(root, text = number_2, font = ("Arial", 20))
            number_label.place(relx = 0.35, rely = 0.02)
        else:
            number_2 = number_2 * 10 + number_reg
            number_label = tk.Label(root, text = number_2, font = ("Arial", 20))
            number_label.place(relx = 0.35, rely = 0.02)


def operation_used(opera_reg):
    global number_1, counter, operation, result, number_label, result_label, what_operation
    if opera_reg == 1:
        what_operation = 1
        number_label.destroy()
        oper_label = tk.Label(root, text = "+", font = ("Arial", 20))
        oper_label.place(relx = 0.35, rely = 0.02)
        operation = 1
    if opera_reg == 2:
        what_operation = 2
        number_label.destroy()
        oper_label = tk.Label(root, text = "-", font = ("Arial", 20))
        oper_label.place(relx = 0.35, rely = 0.02)
        operation = 1
    if opera_reg == 3:
        what_operation = 3
        number_label.destroy()
        oper_label = tk.Label(root, text = "*", font = ("Arial", 20))
        oper_label.place(relx = 0.35, rely = 0.02)
        operation = 1
    if opera_reg == 4:
        what_operation = 4
        number_label.destroy()
        oper_label = tk.Label(root, text = "/", font = ("Arial", 20))
        oper_label.place(relx = 0.35, rely = 0.02)
        operation = 1

    if opera_reg == 0:

        if what_operation == 1:
            result = number_1 + number_2

        if what_operation == 2:
            result = number_1 - number_2

        if what_operation == 3:
            result = number_1 * number_2

        if what_operation == 4:
            if number_2 == 0:
                popup = tk.Toplevel(root)
                popup.title("CANT DEVIDE BY ZERO")
                popup.geometry("200x300")
            result = number_1 / number_2


        number_label.destroy()
        result_label = tk.Label(root, text = result, font = ("Arial", 20))
        result_label.place(relx = 0.35, rely = 0.02)
        operation = 0 
         
        
        
    counter = 0
        




root = tk.Tk()
root.geometry("600x800")
root.title("Calculator")

button_1 = tk.Button(root, text = "1", font=("Arial", 15), width = 3, height = 3, bg = 'red', activebackground="green", command = lambda: number_becomity(1))
button_1.place(relx = 0.13, rely = 0.4)


button_2 = tk.Button(root, text = "2", font=("Arial", 15), width = 3, height = 3, bg = 'red', activebackground="green", command = lambda: number_becomity(2))
button_2.place(relx = 0.24, rely = 0.4)

button_3 = tk.Button(root, text = "3", font=("Arial", 15), width = 3, height = 3, bg = 'red', activebackground="green", command = lambda: number_becomity(3))
button_3.place(relx = 0.35, rely = 0.4)

button_4 = tk.Button(root, text = "4", font=("Arial", 15), width = 3, height = 3, bg = 'red', activebackground="green", command = lambda: number_becomity(4))
button_4.place(relx = 0.46, rely = 0.4)

button_5 = tk.Button(root, text = "5", font=("Arial", 15), width = 3, height = 3, bg = 'red', activebackground="green", command = lambda: number_becomity(5))
button_5.place(relx = 0.13, rely = 0.51)

button_6 = tk.Button(root, text = "6", font=("Arial", 15), width = 3, height = 3, bg = 'red', activebackground="green", command = lambda: number_becomity(6))
button_6.place(relx = 0.24, rely = 0.51)

button_7 = tk.Button(root, text = "7", font=("Arial", 15), width = 3, height = 3, bg = 'red', activebackground="green", command = lambda: number_becomity(7))
button_7.place(relx = 0.35, rely = 0.51)

button_8 = tk.Button(root, text = "8", font=("Arial", 15), width = 3, height = 3, bg = 'red', activebackground="green", command = lambda: number_becomity(8))
button_8.place(relx = 0.46, rely = 0.51)

button_9 = tk.Button(root, text = "9", font=("Arial", 15), width = 3, height = 3, bg = 'red', activebackground="green", command = lambda: number_becomity(9))
button_9.place(relx = 0.13, rely = 0.62)

button_0 = tk.Button(root, text = "0", font=("Arial", 15), width = 3, height = 3, bg = 'red', activebackground="green", command = lambda: number_becomity(0))
button_0.place(relx = 0.24, rely = 0.62)

button_equal = tk.Button(root, text = "=", font=("Arial", 15), width = 9, height = 3, bg = 'orange', activebackground="green", command=lambda: operation_used(0))
button_equal.place(relx = 0.35, rely = 0.62)

button_plus = tk.Button(root, text = "+", font=("Arial", 15), width = 3, height = 3, bg = 'orange', activebackground="green", command=lambda: operation_used(1))
button_plus.place(relx = 0.57, rely = 0.4)

button_minus = tk.Button(root, text = "-", font=("Arial", 15), width = 3, height = 3, bg = 'orange', activebackground="green", command=lambda: operation_used(2))
button_minus.place(relx = 0.57, rely = 0.51)

button_times = tk.Button(root, text = "x", font=("Arial", 15), width = 3, height = 3, bg = 'orange', activebackground="green", command=lambda: operation_used(3))
button_times.place(relx = 0.57, rely = 0.62)

button_divide = tk.Button(root, text = "/", font=("Arial", 15), width = 3, height = 3, bg = 'orange', activebackground="green", command=lambda: operation_used(4))
button_divide.place(relx = 0.68, rely = 0.4)



root.mainloop()