import tkinter as tk
from tkinter import messagebox


class Vendedor:

    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    @staticmethod
    def verificar_edad(edad):

        if edad < 0 or edad > 120:
            raise ValueError(
                "La edad no puede ser negativa ni mayor a 120"
            )

        if edad <= 18:
            raise ValueError(
                "El vendedor debe ser mayor a 18 años"
            )

    def imprimir(self):

        return (
            f"Nombre: {self.nombre}\n"
            f"Apellidos: {self.apellidos}\n"
            f"Edad: {self.edad} años"
        )


def crear_vendedor():

    try:

        nombre = txt_nombre.get()
        apellidos = txt_apellidos.get()
        edad = int(txt_edad.get())

        Vendedor.verificar_edad(edad)

        vendedor = Vendedor(
            nombre,
            apellidos,
            edad
        )

        resultado.delete("1.0", tk.END)
        resultado.insert(
            tk.END,
            vendedor.imprimir()
        )

    except ValueError as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


def limpiar():

    txt_nombre.delete(0, tk.END)
    txt_apellidos.delete(0, tk.END)
    txt_edad.delete(0, tk.END)

    resultado.delete("1.0", tk.END)



ventana = tk.Tk()
ventana.title("Registro de Vendedor")
ventana.geometry("450x350")
ventana.resizable(False, False)

tk.Label(
    ventana,
    text="Nombre:"
).place(x=30, y=30)

txt_nombre = tk.Entry(
    ventana,
    width=30
)

txt_nombre.place(x=150, y=30)

tk.Label(
    ventana,
    text="Apellidos:"
).place(x=30, y=70)

txt_apellidos = tk.Entry(
    ventana,
    width=30
)

txt_apellidos.place(x=150, y=70)

tk.Label(
    ventana,
    text="Edad:"
).place(x=30, y=110)

txt_edad = tk.Entry(
    ventana,
    width=30
)

txt_edad.place(x=150, y=110)

btn_crear = tk.Button(
    ventana,
    text="Crear vendedor",
    width=15,
    command=crear_vendedor
)

btn_crear.place(x=90, y=160)

btn_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    width=15,
    command=limpiar
)

btn_limpiar.place(x=240, y=160)

resultado = tk.Text(
    ventana,
    width=40,
    height=6
)

resultado.place(x=50, y=220)

ventana.mainloop()
