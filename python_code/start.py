from tkinter import *
root=Tk()
def click(): 
    f=open('sample.txt','a')
    f.write(entry.get())
    f.write('\n')
    f.close()
    entry.delete(0,END)
button=Button(root,text="click me", command=click)
entry=Entry(root)
entry.pack()
button.pack()
root.mainloop()