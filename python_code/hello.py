from tkinter import *
root=Tk()
entry=Entry(root).pack()
def click(): 
	e=entry.get()
	label=Label(root,text=e*73.9)
	label.pack()	
button=Button(root,text ="inr into usd ", command=click)
button.pack()
root.mainloop()