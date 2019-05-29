import tkinter as tk
from tkinter import messagebox
mainWindow = tk.Tk()
mainWindow.title("calculator")


First_Number = tk.Label(mainWindow, text="first number")
First_Number.pack()
First_Number_Value = tk.Entry(mainWindow)
First_Number_Value.pack()

Second_Number = tk.Label(mainWindow, text="second number")
Second_Number.pack()
Second_Number_Value = tk.Entry(mainWindow)
Second_Number_Value.pack()

heading_label3 = tk.Label(mainWindow, text=" operator")
heading_label3.pack()

Addition = tk.Button(mainWindow, text="+", command=lambda: add())
Addition.pack()
Minus = tk.Button(mainWindow, text="-", command=lambda: minus())
Minus.pack()
Multiplication = tk.Button(mainWindow, text="*", command=lambda: mul())
Multiplication.pack()
Division = tk.Button(mainWindow, text="/", command=lambda: divide())
Division.pack()

Result_Label = tk.Label(mainWindow, text="result is", pady=10, padx= 20)
Result_Label.pack()


def add():
    first, second = takeValueInput()
    name = first+second
    Result_Label.config(text="OPERATION RESULT IS" + str(name))


def minus():
    first, second = takeValueInput()
    name = first - second
    Result_Label.config(text="OPERATION RESULT IS" + str(name))


def mul():
    first, second = takeValueInput()
    name = first * second
    Result_Label.config(text="OPERATION RESULT IS" + str(name))


def divide():

    first, second = takeValueInput()
    if(second==0):
        messagebox.showerror("error", "second no. cannot be zero")
    else:
        name = first / second
        Result_Label.config(text="OPERATION RESULT IS"+str(name))

def takeValueInput():
    first = First_Number_Value.get()
    second = Second_Number_Value.get()
    try:
        first = int(first)
        second = int(second)
        return first, second
    except ValueError:
        if(len(First_Number_Value.get()) == 0) or (len(Second_Number_Value.get() == 0)):
            messagebox.showerror("Error", "please enter something")
        else:
            messagebox.showerror("Error", "enter integer value")
        quit(0)


mainWindow.mainloop()
