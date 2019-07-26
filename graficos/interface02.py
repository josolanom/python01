import tkinter as tk
from tkinter import messagebox

ventana=tk.Tk()
ventana.title ="Ingreso de Clientes"
ventana.geometry('900x500')
ventana.resizable(False,False)
ventana.configure(background='beige')


frame = LabelFrame(ventana,text="Registrando un nuevo producto")
frame.grid(row=0,colum=0,columspan=3,pady=20)

Label(frame, text="Código").grid(row=1,colum=0)
codigo=Entry(frame)
codigo.grid(row=1,colum=1)



ventana.mainloop()