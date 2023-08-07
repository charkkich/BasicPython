from tkinter import *
from tkinter import ttk,messagebox


gui = Tk()
gui.title("โปรแกรมคำนวณราคาขายทุเรียน")
gui.geometry("500x400")

bg = PhotoImage(file=r"C:\Users\User\Desktop\Learning\PythonGUI\fruit.png")
BG = Label(gui,image=bg)
BG.pack()

L1 = Label(gui,text="กรุณาป้อนจำนวนกิโลกรัมของทุเรียน",font=(NONE,20))
L1.pack()

v_quantity = StringVar()
E1 = ttk.Entry(gui,textvariable=v_quantity,font=(None,20),justify=LEFT)
E1.pack()
E1.focus()

def Cal():
    try:
        quan = float(v_quantity.get())
        price = quan * 30
        messagebox.showinfo("ราคาทุเรียน","ราคาของทุเรียน คือ {:.2f} บาท".format(price))
        v_quantity.set("")
        E1.focus()
    except:
        messagebox.showerror("โปรแกรมทำงานผิดพลาด","กรุณากรอกตัวเลข")
        v_quantity.set("")
        E1.focus()

B1 = ttk.Button(gui,text="คำนวณ",command=Cal)
B1.pack(ipadx=30,ipady=10,pady=5)


gui.mainloop()