#  1.import tkinter
# from tkinter import*
# anjali=Tk()
# # anjali.title("this is me")

# anjali.mainloop()
#2============================================GUI APPLICATION===============================
# 2.import tkinter as tk
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
# app=App()   
# app.mainloop()

#3===========================================MESSAGEBOX USING TKINTER=========================
# from tkinter import*
# from tkinter import messagebox
# top=Tk()
# top.title("whatsapp")
# top.geometry("700x500")
# def anjali98():
#     msg=messagebox.showinfo("whatsapp","all correct")
# B=Button(top,text="submit",background="black",foreground="white",command=anjali98)
# B.place(x=50,y=50)
# top.mainloop()
##4==========================================canvas===============================================
from tkinter import*
from tkinter import messagebox
top=Tk()
top.geometry("400x400")
top.title("my coord")
def anj():
    msg=messagebox.showinfo("hey tkinter","all correct")
B=Button(top,text="next",command=anj)
B.place(x=70,y=80)
c=Canvas(top,background="pink",height=400,width=400)
coord=100,200,300,400
# arc=c.create_arc(coord,start=0,extent=450,fill="white")
oval=c.create_oval(coord,fill="white")

c.pack()
top.mainloop()