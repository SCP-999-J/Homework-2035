from tkinter import *
from tkinter import messagebox
def button_1():
    messagebox.showinfo('Результат +', int(a.get())+int(b.get()))
def button_2():
    messagebox.showinfo('Результат -', int(a.get())-int(b.get()))
def button_3():
    messagebox.showinfo('Результат *', int(a.get())*int(b.get()))
def button_4():
    messagebox.showinfo('Результат /', int(a.get())/int(b.get()))
def button_5():
    messagebox.showinfo('Результат //', int(a.get())//int(b.get()))
def button_6():
    messagebox.showinfo('Результат %', int(a.get())%int(b.get()))
root=Tk()
root.title('Калькулятор')
root.geometry('500x300')
a=Entry(root, width=10,  bg='gray', fg='white', font='consolas')
a.pack()
b=Entry(root, width=10,  bg='gray', fg='white', font='consolas')
b.pack()
q=Button(root, text='+', width=10, height=2, bg='gray', fg='black', command=button_1).pack()
w=Button(root, text='-', width=10, height=2, bg='gray', fg='black', command=button_2).pack()
e=Button(root, text='*', width=10, height=2, bg='gray', fg='black', command=button_3).pack()
r=Button(root, text='/', width=10, height=2, bg='gray', fg='black', command=button_4).pack()
t=Button(root, text='//', width=10, height=2, bg='gray', fg='black', command=button_5).pack()
y=Button(root, text='%', width=10, height=2, bg='gray', fg='black', command=button_6).pack()
root.mainloop()
