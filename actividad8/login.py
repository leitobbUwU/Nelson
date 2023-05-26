from tkinter import *
from tkinter import messagebox

root=Tk()

usuario="alumno"
contra="sistemas2023"

def Validacion():
    if usu.get()==usuario and cont.get()==contra:
        messagebox.showinfo("Exito", "Usuario Correcto")
    else:
        messagebox.showerror("Error", "Usuario incorrecto")
        
usu=StringVar()
cont=StringVar()

Label(root, text="Usuario").pack()
Entry(root, justify="center",textvariable=usu).pack()

Label(root, text="Contraseña").pack()
Entry(root, justify="center", textvariable=cont).pack()

Button(root,text="Login",command=Validacion).pack(side="left")

root.mainloop()