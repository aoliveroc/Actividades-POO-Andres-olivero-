import tkinter as tk
import math




class Figura:
    pass




class Cilindro(Figura):

    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return math.pi * self.radio**2 * self.altura

    def superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)




class Esfera(Figura):

    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        return (4/3) * math.pi * self.radio**3

    def superficie(self):
        return 4 * math.pi * self.radio**2




class Piramide(Figura):

    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def volumen(self):
        return (self.base**2 * self.altura) / 3

    def superficie(self):
        area_base = self.base**2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral




ventana = tk.Tk()
ventana.title("Figuras")
ventana.geometry("400x150")
ventana.resizable(False, False)




def ventana_cilindro():

    v = tk.Toplevel()
    v.title("Cilindro")
    v.geometry("300x230")
    v.resizable(False, False)

    tk.Label(v, text="Radio (cms):").place(x=20, y=30)
    txt_radio = tk.Entry(v)
    txt_radio.place(x=120, y=30)

    tk.Label(v, text="Altura (cms):").place(x=20, y=70)
    txt_altura = tk.Entry(v)
    txt_altura.place(x=120, y=70)

    resultado_volumen = tk.Label(v, text="")
    resultado_volumen.place(x=20, y=150)

    resultado_superficie = tk.Label(v, text="")
    resultado_superficie.place(x=20, y=180)

    def calcular():

        radio = float(txt_radio.get())
        altura = float(txt_altura.get())

        c = Cilindro(radio, altura)

        resultado_volumen.config(
            text="Volumen (cm3): {:.2f}".format(c.volumen())
        )

        resultado_superficie.config(
            text="Superficie (cm2): {:.2f}".format(c.superficie())
        )

    tk.Button(v, text="Calcular", width=15, command=calcular).place(x=80, y=110)


def ventana_esfera():

    v = tk.Toplevel()
    v.title("Esfera")
    v.geometry("300x220")
    v.resizable(False, False)

    tk.Label(v, text="Radio (cms):").place(x=20, y=40)
    txt_radio = tk.Entry(v)
    txt_radio.place(x=120, y=40)

    resultado_volumen = tk.Label(v, text="")
    resultado_volumen.place(x=20, y=140)

    resultado_superficie = tk.Label(v, text="")
    resultado_superficie.place(x=20, y=170)

    def calcular():

        radio = float(txt_radio.get())

        e = Esfera(radio)

        resultado_volumen.config(
            text="Volumen (cm3): {:.2f}".format(e.volumen())
        )

        resultado_superficie.config(
            text="Superficie (cm2): {:.2f}".format(e.superficie())
        )

    tk.Button(v, text="Calcular", width=15, command=calcular).place(x=80, y=90)


def ventana_piramide():

    v = tk.Toplevel()
    v.title("Pirámide")
    v.geometry("320x260")
    v.resizable(False, False)

    tk.Label(v, text="Base (cms):").place(x=20, y=30)
    txt_base = tk.Entry(v)
    txt_base.place(x=130, y=30)

    tk.Label(v, text="Altura (cms):").place(x=20, y=70)
    txt_altura = tk.Entry(v)
    txt_altura.place(x=130, y=70)

    tk.Label(v, text="Apotema (cms):").place(x=20, y=110)
    txt_apotema = tk.Entry(v)
    txt_apotema.place(x=130, y=110)

    resultado_volumen = tk.Label(v, text="")
    resultado_volumen.place(x=20, y=190)

    resultado_superficie = tk.Label(v, text="")
    resultado_superficie.place(x=20, y=220)

    def calcular():

        base = float(txt_base.get())
        altura = float(txt_altura.get())
        apotema = float(txt_apotema.get())

        p = Piramide(base, altura, apotema)

        resultado_volumen.config(
            text="Volumen (cm3): {:.2f}".format(p.volumen())
        )

        resultado_superficie.config(
            text="Superficie (cm2): {:.2f}".format(p.superficie())
        )

    tk.Button(v, text="Calcular", width=15, command=calcular).place(x=90, y=150)




tk.Button(
    ventana,
    text="Cilindro",
    width=12,
    command=ventana_cilindro
).place(x=30, y=50)

tk.Button(
    ventana,
    text="Esfera",
    width=12,
    command=ventana_esfera
).place(x=145, y=50)

tk.Button(
    ventana,
    text="Pirámide",
    width=12,
    command=ventana_piramide
).place(x=260, y=50)




ventana.mainloop()
