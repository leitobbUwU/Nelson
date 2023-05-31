from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("300x200")
root.title("Login")

usuario="Admin"
contra="Admin"

def Validacion():
    if usu.get()==usuario and cont.get()==contra:
        ventana2=Toplevel()
        ventana2.geometry("300x200")
        ventana2.title("Cajero")
        
        def transaccion():
            resultado.set(saldo - float(importe.get()))
            messagebox.showinfo("Transaccion realizada",f'La transacción se realizó correctamente y el saldo en la cuenta destino es: {importe.get()}' )
        
        saldo=5000
        
        Label(ventana2, text="Numero de cuenta origen").pack()
        Entry(ventana2, justify="center").pack()
        
        Label(ventana2, text="Numero de cuenta destino").pack()
        Entry(ventana2, justify="center").pack()
        
        importe=IntVar()
        resultado=StringVar()
        
        Label(ventana2, text="Importe").pack()
        Entry(ventana2, justify="center",textvariable=importe).pack()
        
        Button(ventana2,text="Realizar Transaccion",command=transaccion).pack(side="left")
    else:
        messagebox.showerror("Datos incorrectos", "Verifica tus credenciales ;)")
        
        
def borrar():
    usu.set("") 
    cont.set("")

usu=StringVar()
cont=StringVar()

Label(root, text="Usuario").pack()
Entry(root, justify="center",textvariable=usu).pack()

Label(root, text="Contraseña").pack()
Entry(root, justify="center", show="*", textvariable=cont).pack()

Button(root,text="Login",command=Validacion).pack(side="left")
Button(root,text="Limpiar",command=borrar).pack(side="left")

root.mainloop()