from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Calculator")
root.resizable(False,False)
root.configure(bg="#17161b")

#label
lbl_result=Label(root,height=2,width=20,text="",font=("arial", 20, "bold"))
lbl_result.pack()

#frame
frame=Frame(root,height=300,width=350,bg="#2a2d36")
frame.pack()


calculation=""

def show(value):
    global calculation
    calculation+=value
    lbl_result.config(text=calculation)

def clear():
    global calculation
    calculation=""
    lbl_result.config(text=calculation)
    
def calculate():
    global calculation
    result=""
    if calculation!="":
        try:
            result=eval(calculation)
        except:
            result="error"
            calculation=""
    lbl_result.config(text=result)

#calculator_icon
Image_icon=PhotoImage(file="C:/Users/Sujata Sarkar/OneDrive/Desktop/10310245.png")
root.iconphoto(False,Image_icon)

#all_button
Button(root,text="C",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=5,y=100)
Button(root,text="/",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("/")).place(x=95,y=100)
Button(root,text="%",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("%")).place(x=185,y=100)
Button(root,text="*",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("*")).place(x=275,y=100)

Button(root,text="7",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("7")).place(x=5,y=150)
Button(root,text="8",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("8")).place(x=95,y=150)
Button(root,text="9",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("9")).place(x=185,y=150)
Button(root,text="-",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("-")).place(x=275,y=150)

Button(root,text="4",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("4")).place(x=5,y=200)
Button(root,text="5",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("5")).place(x=95,y=200)
Button(root,text="6",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("6")).place(x=185,y=200)
Button(root,text="+",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("+")).place(x=275,y=200)

Button(root,text="1",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("1")).place(x=5,y=250)
Button(root,text="2",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("2")).place(x=95,y=250)
Button(root,text="3",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("3")).place(x=185,y=250)
Button(root,text="=",width=5,height=3,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:calculate()).place(x=275,y=250)

Button(root,text="0",width=12,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("0")).place(x=5,y=300)
Button(root,text=".",width=5,height=1,font=("arial",16,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show(".")).place(x=185,y=300)


root.mainloop()
