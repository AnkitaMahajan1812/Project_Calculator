from tkinter import *
import tkinter as TK
import math
# Define the main window

cal = Tk()
cal.title('Calculator')
operator = ""
Text_Input = StringVar()


text_Display = Entry(cal, font=('arial', 20), textvariable=Text_Input, bd=8, insertwidth=6, bg="white", justify='right')
text_Display.grid(columnspan=4)

# funcation when a button is clicked

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    Text_Input.set(operator)

# funcation to clear the display

def btnClearDisplay():
    global operator
    operator = ""
    Text_Input.set("")

# funcation for backspace

def btnBackspace():
    global operator
    operator = operator[:-1]
    Text_Input.set(operator)
    
# function to the equal button

def btnEqualsInput():
    global operator
    try:
        result = str(eval(operator))
        Text_Input.set(result)
        operator = result  
    except:
        Text_Input.set("Error")
        operator = ""

 # function for Percentage button
   
def btnPercentage():
    global operator
    try:
        result = str(eval(operator + "/100"))
        Text_Input.set(result)
        operator = result  
    except:
        Text_Input.set("Error")
        operator = "" 

 #function for Square Root button
   

def btnSquareRoot():
    global operator
    try:
        result = math.sqrt(float(operator))
        Text_Input.set(str(result))
        operator = str(result)  
    except:
        Text_Input.set("Error")
        operator = "" 


# Create Number buttons

Button(cal, padx=12, pady=12, bd=8, fg="black", font=('arial', 18, 'bold'),
       text="C", command=btnClearDisplay).grid(row=1, column=0)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 15, 'bold'),
       text="←", command=btnBackspace).grid(row=1, column=2)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 15, 'bold'),
       text="%", command=btnPercentage).grid(row=1, column=3)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 15, 'bold'),
       text="√", command=btnSquareRoot).grid(row=1, column=1)



Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="7", command=lambda: btnClick(7)).grid(row=2, column=0)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="8", command=lambda: btnClick(8)).grid(row=2, column=1)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="9", command=lambda: btnClick(9)).grid(row=2, column=2)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="+", command=lambda: btnClick("+")).grid(row=2, column=3)

Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="4", command=lambda: btnClick(4)).grid(row=3, column=0)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="5", command=lambda: btnClick(5)).grid(row=3, column=1)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="6", command=lambda: btnClick(6)).grid(row=3, column=2)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="-", command=lambda: btnClick("-")).grid(row=3, column=3)

Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="1", command=lambda: btnClick(1)).grid(row=4, column=0)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="2", command=lambda: btnClick(2)).grid(row=4, column=1)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="3", command=lambda: btnClick(3)).grid(row=4, column=2)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="*", command=lambda: btnClick("*")).grid(row=4, column=3)

Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text=".", command=lambda: btnClick(".")).grid(row=5, column=0)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="0", command=lambda: btnClick(0)).grid(row=5, column=1)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="=", command=btnEqualsInput).grid(row=5, column=2)
Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
       text="/", command=lambda: btnClick("/")).grid(row=5, column=3)


# function call

cal.mainloop()
