import tkinter as tk
from tkinter import messagebox
import math



class Notas:

    def __init__(self, notas):
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def desviacion(self):
        prom = self.promedio()

        suma = 0
        for nota in self.notas:
            suma += (nota - prom) ** 2

        return math.sqrt(suma / len(self.notas))

    def mayor(self):
        return max(self.notas)

    def menor(self):
        return min(self.notas)




def calcular():

    try:
        notas = [
            float(txt_nota1.get()),
            float(txt_nota2.get()),
            float(txt_nota3.get()),
            float(txt_nota4.get()),
            float(txt_nota5.get())
        ]

        estudiante = Notas(notas)

        lbl_promedio.config(
            text="Promedio = {:.2f}".format(estudiante.promedio())
        )

        lbl_desviacion.config(
            text="Desviación estándar = {:.2f}".format(estudiante.desviacion())
        )

        lbl_mayor.config(
            text="Valor mayor = {}".format(estudiante.mayor())
        )

        lbl_menor.config(
            text="Valor menor = {}".format(estudiante.menor())
        )

    except:
        messagebox.showerror("Error", "Ingrese valores válidos")


def limpiar():

    txt_nota1.delete(0, tk.END)
    txt_nota2.delete(0, tk.END)
    txt_nota3.delete(0, tk.END)
    txt_nota4.delete(0, tk.END)
    txt_nota5.delete(0, tk.END)

    lbl_promedio.config(text="")
    lbl_desviacion.config(text="")
    lbl_mayor.config(text="")
    lbl_menor.config(text="")




ventana = tk.Tk()
ventana.title("Notas")
ventana.geometry("350x420")
ventana.resizable(False, False)




tk.Label(ventana, text="Nota 1:", font=("Arial", 10, "bold")).place(x=40, y=40)
txt_nota1 = tk.Entry(ventana, width=20)
txt_nota1.place(x=140, y=42)

tk.Label(ventana, text="Nota 2:", font=("Arial", 10, "bold")).place(x=40, y=80)
txt_nota2 = tk.Entry(ventana, width=20)
txt_nota2.place(x=140, y=82)

tk.Label(ventana, text="Nota 3:", font=("Arial", 10, "bold")).place(x=40, y=120)
txt_nota3 = tk.Entry(ventana, width=20)
txt_nota3.place(x=140, y=122)

tk.Label(ventana, text="Nota 4:", font=("Arial", 10, "bold")).place(x=40, y=160)
txt_nota4 = tk.Entry(ventana, width=20)
txt_nota4.place(x=140, y=162)

tk.Label(ventana, text="Nota 5:", font=("Arial", 10, "bold")).place(x=40, y=200)
txt_nota5 = tk.Entry(ventana, width=20)
txt_nota5.place(x=140, y=202)




btn_calcular = tk.Button(
    ventana,
    text="Calcular",
    width=10,
    command=calcular
)

btn_calcular.place(x=60, y=250)

btn_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    width=10,
    command=limpiar
)

btn_limpiar.place(x=180, y=250)




lbl_promedio = tk.Label(ventana, text="", font=("Arial", 10))
lbl_promedio.place(x=40, y=310)

lbl_desviacion = tk.Label(ventana, text="", font=("Arial", 10))
lbl_desviacion.place(x=40, y=340)

lbl_mayor = tk.Label(ventana, text="", font=("Arial", 10))
lbl_mayor.place(x=40, y=370)

lbl_menor = tk.Label(ventana, text="", font=("Arial", 10))
lbl_menor.place(x=40, y=400)




ventana.mainloop()
