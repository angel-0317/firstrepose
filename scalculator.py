from tkinter import*
import math
import parser
import tkinter.messagebox 

root = Tk()
root.title("Scientific Calculator")
root.resizable(width=False, height = False)
root.geometry("400x492+460+40")

Mainframe = Frame(root, bd=20, pady=2, relief =RIDGE)
calFrame = Frame(root, bd=20, pady=2, relief =RIDGE)
calFrame.grid()
#=======================================================

class Calc():
    def _init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
#=======================================================
added_value = Calc

txtResult = Entry(calFrame, font = ("arial",16,"bold"),bg="darkgreen", bd=30, width=26, justify=RIGHT)
txtResult.grid(row=0, column=0, columnspan= 4, pady=1)
txtResult.insert(0, "0")
#=======================================================
numbericButton = "789456123"
i = 0
btn = []
for j in range(2,5):
    for q in range(3):
        btn.append(Button(calFrame, width=6, height=2, font=("arial",16,"bold"),bd=4,
        text=numbericButton[i]))
        btn[i].grid(row =j, column=q, pady=1)
        btn[i]["command"] = lambda X = numbericButton[i]:added_value
        i+= 1
#=======================================================

btn0=Button(calFrame, text="0", width = 6,height=2, font=("arial",16,"bold",),bd=4, 
bg="grey").grid(row = 5, column=0, pady=1)

btnDiv=Button(calFrame, text=chr(247), width = 6,height=2, font=("arial",16,"bold",),bd=4, 
bg="grey").grid(row = 5, column=3, pady=1)

btnMult=Button(calFrame, text=chr(42), width = 6,height=2, font=("arial",16,"bold",),bd=4, 
bg="grey").grid(row = 4, column=3, pady=1)

btnSub=Button(calFrame, text=chr(45), width = 6,height=2, font=("arial",16,"bold",),bd=4, 
bg="grey").grid(row = 3, column=3, pady=1)

btnDot=Button(calFrame, text=chr(183), width = 6,height=2, font=("arial",16,"bold",),bd=4, 
bg="grey").grid(row = 5, column=1, pady=1)

btnAdd=Button(calFrame, text=chr(43), width = 6,height=2, font=("arial",16,"bold",),bd=4, 
bg="grey").grid(row = 2, column=3, pady=1)

btnPM=Button(calFrame, text=chr(177), width = 6,height=2, font=("arial",16,"bold",),bd=4, 
bg="grey").grid(row = 1, column=3, pady=1)

btnBack=Button(calFrame, width = 6,height=2, font=("arial",16,"bold",),bd=4, text="<=" ,
bg="grey").grid(row = 1, column=0, pady=1)

btnClearEntry=Button(calFrame, text=chr(67) + chr(69), width = 6,height=2, font=("arial",16,"bold",),bd=4, 
bg="grey").grid(row = 1, column=1, pady=1)

btnClear=Button(calFrame, text=chr(67), width = 6,height=2, font=("arial",16,"bold",),bd=4, 
bg="grey").grid(row = 1, column=2, pady=1)

btnEquals=Button(calFrame, text=chr(61), width = 6,height=2, font=("arial",16,"bold",),bd=4, 
bg="grey").grid(row = 5, column=2, pady=1)
#=======================================================
meubar = Menu(calFrame)

filemenu = Menu(meubar, tearoff=0)
meubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "Standard")
filemenu.add_command(label = "Scientific")
filemenu.add_separator()
filemenu.add_command(label = "Exit")

root.config(menu = meubar)
root.mainloop()

