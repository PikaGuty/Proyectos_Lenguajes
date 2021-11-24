from tkinter import *
import random

from aa import aa

ventana=Tk()

btn1=Button(ventana,text='Sortear', command=lambda:aa.sortear(Canvas1,img1,img2,img3))
btn1.grid(column=0,row=0)

Canvas1=Canvas(ventana,width=300,height=500, bg="black")
Canvas1.grid(column=0,row=1)

img1=PhotoImage(file='Pokeball.png')
img2=PhotoImage(file='Pokeball[MX].png')
img3=PhotoImage(file='Pokeball2[MY].png')

Canvas1.create_image(50,100,image=img1,anchor="nw")

ventana.mainloop()

