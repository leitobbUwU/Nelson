from tkinter import *
from tkinter import messagebox

root=Tk()

def lleno():
    messagebox.showinfo("informacion",
                        f'Producto: {producto.get()}\nEl precio es: {precio.get()}\n La existencia es: {existencia.get()}')

producto=StringVar()
precio=StringVar()
existencia=StringVar()

Label(root, text="Nombre del producto").pack()
Entry(root, justify="center",textvariable=producto).pack()

Label(root, text="Precio").pack()
Entry(root, justify="center", textvariable=precio).pack()

Label(root, text="existencia").pack()
Entry(root, justify="center", textvariable=existencia).pack()

Button(root,text="Info",command=lleno).pack(side="left")

root.mainloop()