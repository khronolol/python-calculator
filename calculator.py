from tkinter import *
import math

window = Tk()
window.geometry("340x440")
window.resizable(0,0)
window.title("calculator")

displaystr = StringVar()
expression = ""
operators = []
nums = []

def btnclick(item):
    global expression
    global displaystr
    
    if item == "." and "." in displaystr.get():
        return
    
    if item == "pi":
        expression += str(math.pi)
    else:
        expression += str(item)
        
    try:
        displaystr.set(expression)
    except AttributeError:
        try: 
            displaystr = expression
        except: return
        
        equation = equation.join(expression)
        print(equation)
   
# i ltierally have no idea how to backspace so only clearing
def clear():
    global expression
    global displaystr
    global nums
    global operators
    
    if displaystr == "":
        return
    displaystr.set("")
    expression = ""
    operators.clear()
    nums.clear()
    print("cleared")
    
def backspace():
    global expression
    global displaystr

    expression = expression[:-1]
    displaystr.set(expression)
    
def setoperator(op):
    global expression
    global displaystr
    global nums
    global operators
    equation = ""
    
    try:
        nums.append(expression)
        operators.append(op)
        expression = ""
    except ValueError:
        try:
            nums.append(float(expression))
            operators.append(op)
            expression = ""
        except ValueError: return
        
    for i,v in enumerate(nums):
        try:
            equation = "".join((equation,str(v+operators[i])))
        except IndexError:
            try:
                equation = "".join((equation,str(v)))
            except: return
    
    try:
        displaystr.set(op)
    except AttributeError:
        try: 
            displaystr = op
        except: return
    
def solve():
    global expression
    global displaystr
    global nums
    global operators
    equation = ""
    
    if expression != "":
        nums.append(expression)
    
    if len(nums) == len(operators): 
        print("must have an integer after an operator")
        return
            
    for i,v in enumerate(nums):
        try:
            equation = "".join((equation,str(v+operators[i])))
        except IndexError:
            try:
                equation = "".join((equation,str(v)))
            except: return
    try:
        answer = eval(equation)
    except: return
    print(equation+"="+str(answer))
    displaystr.set(str(answer))
    expression = str(answer)
    operators.clear()
    nums.clear()
    
            
display = Frame(window, width = 340, height = 70, bd = 0, highlightbackground = "black", highlightthickness = 1,)
display.pack(side = TOP)

input_field = Label(display, font = ('arial',16,'bold'), textvariable = displaystr, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns = Frame(window, width = 340, height = 370, bg = "#ccc")
btns.pack()

# numbers
button1 = Button(btns, text = "7", height = 4, width = 8, command = lambda: btnclick(7))
button1.grid(row = 0, column = 0, padx = 1, pady = 1)
button2 = Button(btns, text = "8", height = 4, width = 8, command = lambda: btnclick(8))
button2.grid(row = 0, column = 1, padx = 1, pady = 1)
button3 = Button(btns, text = "9", height = 4, width = 8, command = lambda: btnclick(9))
button3.grid(row = 0, column = 2, padx = 1, pady = 1)
button4 = Button(btns, text = "4", height = 4, width = 8, command = lambda: btnclick(4))
button4.grid(row = 1, column = 0, padx = 1, pady = 1)
button5 = Button(btns, text = "5", height = 4, width = 8, command = lambda: btnclick(5))
button5.grid(row = 1, column = 1, padx = 1, pady = 1)
button6 = Button(btns, text = "6", height = 4, width = 8, command = lambda: btnclick(6))
button6.grid(row = 1, column = 2, padx = 1, pady = 1)
button7 = Button(btns, text = "1", height = 4, width = 8, command = lambda: btnclick(1))
button7.grid(row = 2, column = 0, padx = 1, pady = 1)
button8 = Button(btns, text = "2", height = 4, width = 8, command = lambda: btnclick(2))
button8.grid(row = 2, column = 1, padx = 1, pady = 1)
button9 = Button(btns, text = "3", height = 4, width = 8, command = lambda: btnclick(3))
button9.grid(row = 2, column = 2, padx = 1, pady = 1)
button0 = Button(btns, text = "0", height = 4, width = 8, command = lambda: btnclick(0))
button0.grid(row = 3, column = 0, padx = 1, pady = 1)
buttonpi = Button(btns, text = "π", height = 4, width = 8, command = lambda: btnclick("pi"))
buttonpi.grid(row = 5, column = 0, padx = 1, pady = 1)


# operators
buttondiv = Button(btns, text = "/", height = 4, width = 8, command = lambda: setoperator("/"))
buttondiv.grid(row = 0, column = 3, padx = 1, pady = 1)
buttonmult = Button(btns, text = "*", height = 4, width = 8, command = lambda: setoperator("*"))
buttonmult.grid(row = 1, column = 3, padx = 1, pady = 1)
buttonadd = Button(btns, text = "+", height = 4, width = 8, command = lambda: setoperator("+"))
buttonadd.grid(row = 2, column = 3, padx = 1, pady = 1)
buttonsub = Button(btns, text = "-", height = 4, width = 8, command = lambda: setoperator("-"))
buttonsub.grid(row = 3, column = 3, padx = 1, pady = 1)
buttonsolve = Button(btns, text = "=", height = 4, width = 8, command = lambda: solve())
buttonsolve.grid(row = 3, column = 2, padx = 1, pady = 1)

# other buttons
buttonclear = Button(btns, text = "Clear", height = 4, width = 8, command = lambda: clear())
buttonclear.grid(row = 1, column = 4, padx = 1, pady = 1)
buttonback = Button(btns, text = "⌫", height = 4, width = 8, command = lambda: backspace())
buttonback.grid(row = 0, column = 4, padx = 1, pady = 1)
buttonpoint = Button(btns, text = ".", height = 4, width = 8, command = lambda: btnclick("."))
buttonpoint.grid(row = 3, column = 1, padx = 1, pady = 1)

window.mainloop()