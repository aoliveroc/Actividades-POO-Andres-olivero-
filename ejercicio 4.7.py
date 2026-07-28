from abc import ABC, abstractmethod



class Animal(ABC):

    @abstractmethod
    def getNombreCientifico(self):
        pass

    @abstractmethod
    def getSonido(self):
        pass

    @abstractmethod
    def getAlimentos(self):
        pass

    @abstractmethod
    def getHabitat(self):
        pass




class Canido(Animal):
    pass




class Felino(Animal):
    pass




class Perro(Canido):

    def getNombreCientifico(self):
        return "Canis lupus familiaris"

    def getSonido(self):
        return "Ladrido"

    def getAlimentos(self):
        return "Carnívoro"

    def getHabitat(self):
        return "Doméstico"




class Lobo(Canido):

    def getNombreCientifico(self):
        return "Canis lupus"

    def getSonido(self):
        return "Aullido"

    def getAlimentos(self):
        return "Carnívoro"

    def getHabitat(self):
        return "Bosque"




class Leon(Felino):

    def getNombreCientifico(self):
        return "Panthera leo"

    def getSonido(self):
        return "Rugido"

    def getAlimentos(self):
        return "Carnívoro"

    def getHabitat(self):
        return "Pradera"




class Gato(Felino):

    def getNombreCientifico(self):
        return "Felis silvestris catus"

    def getSonido(self):
        return "Maullido"

    def getAlimentos(self):
        return "Ratones"

    def getHabitat(self):
        return "Doméstico"




def main():

    animales = [
        Perro(),
        Lobo(),
        Leon(),
        Gato()
    ]

    for animal in animales:

        print("--------------------------------")
        print("Nombre científico :", animal.getNombreCientifico())
        print("Sonido            :", animal.getSonido())
        print("Alimentación      :", animal.getAlimentos())
        print("Hábitat           :", animal.getHabitat())


if __name__ == "__main__":
    main()
