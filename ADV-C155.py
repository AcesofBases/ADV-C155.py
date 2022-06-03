# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 20:35:02 2022

@author: Ace
"""

from tkinter import *
import random
root=Tk()

root.title("Dictionary's")
root.geometry("500x500")
root.configure(background="pink")



dictionary= [
    "marroon1","lawn green","magenta2","purple1","springgreen2","chocolate1","deep pink","cyan"    
    ]
    
def ran():
   random_col=random.randint(0,7)
   random_colour= dictionary[random_col]
   root.configure(background=random_colour)

btn=Button(root,text="See Value Of Mutable",command=ran,)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()