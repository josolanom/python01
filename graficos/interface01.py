import tkinter as tk
from tkinter import messagebox

ventana=tk.Tk()
ventana.title ="Ingreso de Clientes"
ventana.geometry('900x500')
ventana.resizable(False,False)
ventana.configure(background='beige')

def Mensaje1(): messagebox.showinfo("Titulo","No te preocupes es solo un ejemplo!")
btn1 = tk.Button(ventana, text="Txt btn 1", command=Mensaje1 )
btn1.place(x=100,y=200)


ventana.mainloop()