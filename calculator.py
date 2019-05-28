import tkinter as tk

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
Division = tk.Button(mainWindow, text="/", command=lambda:devide())
Division.pack()

Result_Label = tk.Label(mainWindow, text="result is", pady=10, padx= 20)
Result_Label.pack()


def add():
    first = int(First_Number_Value.get())
    second = int(Second_Number_Value.get())
    name = first+second
    Result_Label.config(text="OPERATION RESULT IS" + str(name))


def minus():
    first = int(First_Number_Value.get())
    second = int(Second_Number_Value.get())
    name = first - second
    Result_Label.config(text="OPERATION RESULT IS" + str(name))


def mul():
    first = int(First_Number_Value.get())
    second = int(Second_Number_Value.get())
    name = first * second
    Result_Label.config(text="OPERATION RESULT IS" + str(name))


def divide():
    first = int(First_Number_Value.get())
    second = int(Second_Number_Value.get())
    name = first / second
    Result_Label.config(text="OPERATION RESULT IS"+str(name))


mainWindow.mainloop()
