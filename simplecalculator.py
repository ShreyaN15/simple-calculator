from tkinter import *
root=Tk()
root.title("calculator")
e=Entry(root,bg="black",fg="white",borderwidth=5,width=40)
e.grid(row=0,column=0,columnspan=3)
#e.insert(0,"")
def click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    
def buadd():
   #first_number=e.get()
   global fir_num
   global math
   math="add"
   fir_num=int(e.get())
   e.delete(0,END)
    
def busub():
      
   global fir_num
   global math
   math="sub"
   #e.delete(0,END)
   #e.insert(0,"-")
   first_number=e.get()
   fir_num=int(first_number)
   e.delete(0,END)
    
def bumul():
   #first_number=e.get()
   global fir_num
   global math
   math="mul"
   fir_num=int(e.get())
   e.delete(0,END)
    
def budiv():
   #first_number=e.get()
   global fir_num
   global math
   math="div"
   fir_num=int(e.get())
   e.delete(0,END)
   
def buclear():
    e.delete(0,END)
    

def buequal():
    sec_number=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,int(fir_num)+int(sec_number))
    if math=="sub":
        e.insert(0,int(fir_num)-int(sec_number))
    if math=="div":
        e.insert(0,int(fir_num)/int(sec_number))
    if math=="mul":
        e.insert(0,int(fir_num)*int(sec_number))

    
but_1=Button(root,text="1",padx=40,pady=20,command=lambda:click(1),fg="white",bg="blue")
but_2=Button(root,text="2",padx=40,pady=20,command=lambda:click(2),fg="white",bg="blue")
but_3=Button(root,text="3",padx=40,pady=20,command=lambda:click(3),fg="white",bg="blue")
but_4=Button(root,text="4",padx=40,pady=20,command=lambda:click(4),fg="white",bg="blue")
but_5=Button(root,text="5",padx=40,pady=20,command=lambda:click(5),fg="white",bg="blue")
but_6=Button(root,text="6",padx=40,pady=20,command=lambda:click(6),fg="white",bg="blue")
but_7=Button(root,text="7",padx=40,pady=20,command=lambda:click(7),fg="white",bg="blue")
but_8=Button(root,text="8",padx=40,pady=20,command=lambda:click(8),fg="white",bg="blue")
but_9=Button(root,text="9",padx=40,pady=20,command=lambda:click(9),fg="white",bg="blue")
but_0=Button(root,text="0",padx=40,pady=20,command=lambda:click(0),fg="white",bg="blue")
but_add=Button(root,text="+",padx=39,pady=20,command=buadd,fg="blue",bg="white")

but_sub=Button(root,text="-",padx=40.5,pady=20,command=busub,fg="blue",bg="white")
but_mul=Button(root,text="*",padx=40,pady=20,command=bumul,fg="blue",bg="white")
but_div=Button(root,text="/",padx=40,pady=20,command=budiv,fg="blue",bg="white")
but_clear=Button(root,text="clear",padx=78,pady=20,command=buclear,fg="blue",bg="white")
but_equal=Button(root,text="=",padx=85.5,pady=20,command=buequal,fg="blue",bg="white")

but_1.grid(row=3,column=0)
but_2.grid(row=3,column=1)
but_3.grid(row=3,column=2)
but_4.grid(row=2,column=0)
but_5.grid(row=2,column=1)
but_6.grid(row=2,column=2)
but_7.grid(row=1,column=0)
but_8.grid(row=1,column=1)
but_9.grid(row=1,column=2)
but_0.grid(row=4,column=0)
but_add.grid(row=5,column=0)
but_sub.grid(row=6,column=0)
but_mul.grid(row=6,column=1)
but_div.grid(row=6,column=2)
but_clear.grid(row=4,column=1,columnspan=2)
but_equal.grid(row=5,column=1,columnspan=2)

root.mainloop()

