# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:59:49 2023

@author: MAX ASUS
"""

import tkinter as tk

window = tk.Tk()

window.title("my first GUI program")

window.geometry('300x300')

label = tk.Label(window,text="my GUI",bg="#06B",fg="#5FC")

label.pack()

entry = tk.Entry(window,width = 20)
entry.pack()

import tkinter.messagebox

def clickMe():
    tkinter.messagebox.showinfo(title='hint',message=' hurt')

#def clickMe2():
    #tkinter.messagebox.showinfo(title='error',message=' x')

button = tk.Button(window,text = "button",command = clickMe)
#button2 = tk.Button(window,text = "button2",command = clickMe2)
button.pack()

window.mainloop()



