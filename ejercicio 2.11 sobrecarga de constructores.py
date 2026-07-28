

class ArticuloCientifico:

    # Constructor principal
    def __init__(self, nombre, autor,
                 palabras_claves=None,
                 publicacion=None,
                 anio=None,
                 resumen=None):

        self.nombre = nombre
        self.autor = autor
        self.palabras_claves = palabras_claves
        self.publicacion = publicacion
        self.anio = anio
        self.resumen = resumen

    # Constructor 1
    @classmethod
    def constructor1(cls, nombre, autor):

        return cls(nombre, autor)

    # Constructor 2 (invoca al primero)
    @classmethod
    def constructor2(cls, nombre, autor,
                     palabras_claves,
                     publicacion,
                     anio):

        articulo = cls.constructor1(nombre, autor)

        articulo.palabras_claves = palabras_claves
        articulo.publicacion = publicacion
        articulo.anio = anio

        return articulo

    # Constructor 3 (invoca al segundo)
    @classmethod
    def constructor3(cls, nombre,
                     autor,
                     palabras_claves,
                     publicacion,
                     anio,
                     resumen):

        articulo = cls.constructor2(
            nombre,
            autor,
            palabras_claves,
            publicacion,
            anio
        )

        articulo.resumen = resumen

        return articulo

    # Método para imprimir

    def imprimir(self):

        print("========== ARTÍCULO CIENTÍFICO ==========")
        print("Título:", self.nombre)
        print("Autor:", self.autor)
        print("Palabras claves:", self.palabras_claves)
        print("Publicación:", self.publicacion)
        print("Año:", self.anio)
        print("Resumen:", self.resumen)




def main():

    articulo = ArticuloCientifico.constructor3(
        "Programación Orientada a Objetos en Python",
        "Andrés Miguel Olivero Carrascal",
        "Python, POO, Clases",
        "Revista Ingeniería",
        2026,
        "Este artículo presenta los conceptos básicos de la programación orientada a objetos utilizando Python."
    )

    articulo.imprimir()




if __name__ == "__main__":
    main()
