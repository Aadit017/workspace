# hello if you came through the story

from tkinter import * 
root=Tk()
f_num=None
math=None
#  not required here root.geometry()
root.title("calculator")
entry=Entry(root,width=50,borderwidth=5)#,fg="grey",bg="black")
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
#entry.insert(0,int(0))
def button_add(number):
    current=entry.get()
    entry.delete (0,END)
    entry.insert(0,str(current)+str(number))
def clear(): 
    entry.delete(0,END)
def addition(): 
    first_number=entry.get()
    global f_num, math 
    f_num=int(first_number)
    math="addition"
    entry.delete(0,END)
def subtraction(): 
    first_number=entry.get()
    global f_num, math 
    f_num=int(first_number)
    math="subtraction"
    entry.delete(0,END)
def multi(): 
    first_number=entry.get()
    global f_num, math 
    f_num=int(first_number)
    math="multiply"
    entry.delete(0,END)
def divide(): 
    first_number=entry.get()
    global f_num, math 
    f_num=int(first_number)
    math="division"
    entry.delete(0,END)
def equal_button(): 
    second_number=entry.get()
    entry.delete(0,END)
    if math == "addition": 
        entry.insert(0,f_num+int(second_number))
    elif math== "subtraction": 
        entry.insert(0,f_num-int(second_number))
    elif math== "multiply":
        entry.insert(0,f_num*int(second_number))
    else : 
        entry.insert(0,f_num/int(second_number))  
def clear(): 
    entry.delete(0,END)
    
# buttons <--
button_1=Button(root,text="1",padx=40,pady=20,command=lambda: button_add(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_add(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: button_add(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: button_add(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda: button_add(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: button_add(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: button_add(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: button_add(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda: button_add(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda: button_add(0))
button_ad=Button(root,text='+',padx=36.23333,pady=20,command=addition)
button_su=Button(root,text="-",padx=38,pady=20,command=subtraction)
button_mu=Button(root,text="*",padx=37.5,pady=20,command=multi)
button_di=Button(root,text="/",padx=37.5,pady=20,command=divide)
button_equal=Button(root,text='=',padx=88,pady=20,command=equal_button)
button_clear=Button(root,text='clear',padx=174,pady=10,command=clear)

# grid being set 
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_ad.grid(row=1,column=3)
button_su.grid(row=2,column=3)
button_mu.grid(row=3,column=3)
button_di.grid(row=4,column=3)
button_equal.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=5, column=0,columnspan=4)

# ---x----x----x---
root.mainloop()
# ---x----x----x---
