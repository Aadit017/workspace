from tkinter import *


class Calculator:

    def __init__(self, title):
        self.title = title
        self.first_num = None
        self.current_operation = None
        self.in_result = False

    def clear(self):
        self.entry.delete(0, END)
        self.first_num = None
        self.current_operation = None
        self.in_result = None

    def addition(self, new_num):
        if self.in_result:
            self.entry.delete(0, END)
            self.in_result = False
            self.current_operation = "+"
            return None
            
        self.entry.delete(0, END)
        if self.first_num == None:
            self.first_num = int(new_num)
        else:
            self.first_num += int(new_num)
        self.current_operation = "+"

    
    def subtract(self, new_num):
        if self.in_result:
            self.entry.delete(0, END)
            self.in_result = False
            self.current_operation = "-"
            return None
            
        self.entry.delete(0, END)
        if self.first_num == None:
            self.first_num = int(new_num)
        else:
            self.first_num -= int(new_num)
        self.current_operation = "-"

    def divide(self, new_num):
        if self.in_result:
            self.entry.delete(0, END)
            self.in_result = False
            self.current_operation = "/"
            return None
            
        self.entry.delete(0, END)
        if self.first_num == None:
            self.first_num = int(new_num)
        else:
            self.first_num /= int(new_num)
        self.current_operation = "/"
    
    def multiply(self, new_num):
        if self.in_result:
            self.entry.delete(0, END)
            self.in_result = False
            self.current_operation = "*"
            return None
            
        self.entry.delete(0, END)
        if self.first_num == None:
            self.first_num = int(new_num)
        else:
            self.first_num *= int(new_num)
        self.current_operation = "*"

    def get_result(self, current_num):
        self.entry.delete(0, END)
        if self.first_num == None:
            self.entry.insert(0, "Error Please Enter a number!")
            return None
        if self.current_operation == "+":
            self.first_num = self.first_num + int(current_num)
            self.entry.insert(0, str(self.first_num))
            self.in_result = True
        elif self.current_operation == "*":
            self.first_num = self.first_num * int(current_num)
            self.entry.insert(0, str(self.first_num))
            self.in_result = True
        elif self.current_operation == "-":
            self.first_num = self.first_num - int(current_num)
            self.entry.insert(0, str(self.first_num))
            self.in_result = True
        elif self.current_operation == "/":
            self.first_num = self.first_num / int(current_num)
            self.entry.insert(0, str(self.first_num))
            self.in_result = True
        else:
            self.entry.insert(0, "Unknown Expression")
        

    def button_add(self, number):
        self.entry.insert(END,number)

    def setup(self):
        self.root = Tk()
        self.root.title(self.title)
        self.entry=Entry(self.root,width=50,borderwidth=5)
        self.entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
        self.button_1=Button(self.root,text="1",padx=40,pady=20,command=lambda: self.button_add(1))
        self.button_2=Button(self.root,text="2",padx=40,pady=20,command=lambda: self.button_add(2))
        self.button_3=Button(self.root,text="3",padx=40,pady=20,command=lambda: self.button_add(3))
        self.button_4=Button(self.root,text="4",padx=40,pady=20,command=lambda: self.button_add(4))
        self.button_5=Button(self.root,text="5",padx=40,pady=20,command=lambda: self.button_add(5))
        self.button_6=Button(self.root,text="6",padx=40,pady=20,command=lambda: self.button_add(6))
        self.button_7=Button(self.root,text="7",padx=40,pady=20,command=lambda: self.button_add(7))
        self.button_8=Button(self.root,text="8",padx=40,pady=20,command=lambda: self.button_add(8))
        self.button_9=Button(self.root,text="9",padx=40,pady=20,command=lambda: self.button_add(9))
        self.button_0=Button(self.root,text="0",padx=40,pady=20,command=lambda: self.button_add(0))
        self.button_ad=Button(self.root,text='+',padx=39,pady=20, command=lambda: self.addition(self.entry.get()))
        self.button_mul=Button(self.root,text="*",padx=40,pady=20,command=lambda: self.multiply(self.entry.get()))
        self.button_sub=Button(self.root,text="-",padx=40,pady=20,command=lambda: self.subtract(self.entry.get()))
        self.button_div=Button(self.root,text="/",padx=40,pady=20,command=lambda: self.divide(self.entry.get()))
        self.button_equal=Button(self.root,text='=',padx=95,pady=20, command=lambda: self.get_result(self.entry.get()))
        self.button_clear=Button(self.root,text='clear',padx=141.5,pady=10,command=self.clear) 

        self.retranslate_ui()

    def retranslate_ui(self):
        # grid being set 
        self.button_1.grid(row=1,column=0)
        self.button_2.grid(row=1,column=1)
        self.button_4.grid(row=2,column=0)
        self.button_5.grid(row=2,column=1)
        self.button_6.grid(row=2,column=2)
        self.button_7.grid(row=3,column=0)
        self.button_8.grid(row=3,column=1)
        self.button_9.grid(row=3,column=2)
        self.button_ad.grid(row=4,column=0)
        self.button_mul.grid(row=1, column=2)
        self.button_sub.grid(row=1, column=3)
        self.button_div.grid(row=2, column=3)
        self.button_equal.grid(row=4,column=1,columnspan=1)
        self.button_0.grid(row=4, column=2, columnspan=1)
        self.button_clear.grid(row=5, column=0,columnspan=4)



    def start(self):
        self.root.mainloop()



def main():
    c = Calculator("Hello")
    c.setup()
    c.start()


if __name__ == "__main__":
    main()
