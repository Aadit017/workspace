from tkinter import *
root=Tk()
e=Entry(root)
# default text in the entry area ---e.insert(0,"insert your name")
e.pack()
def click(): 
    label=Label(root,text="Hello "+e.get())
    label.pack()
    e.delete(0,END)
button=Button(root,text="submit",command=click)
button.pack()
root.mainloop()