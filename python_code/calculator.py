# if you came here from my story 
# please help me in finishing this calcultor


from tkinter import * 
root=Tk()
#  not required here root.geometry()
root.title("calculator")
entry=Entry(root,width=50,borderwidth=5)
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_add(number):
  
    entry.insert(0,number)
def clear(): 
    entry.delete(0,END)
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
button_ad=Button(root,text='+',padx=39,pady=20)
button_equal=Button(root,text='=',padx=95,pady=20)
def clear(): 
    entry.delete(0,END)
button_clear=Button(root,text='clear',padx=141.5,pady=10,command=clear)
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
button_ad.grid(row=4,column=0)
button_equal.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=5, column=0,columnspan=4)

root.mainloop()
