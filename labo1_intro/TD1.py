"""

Créer une classe « Serpent » qui possède les caractéristiques suivantes :
* Longueur
* Couleur
* Vitesse
* Venimeux
Elle possèdera également les méthodes suivantes :

* ‘afficherInfo()’, pour afficher les différentes infos de l’objet
* ‘seDeplacer()’, pour permettre à l’objet de se déplacer dans une direction
* ‘manger()’, pour définir que le serpent a mangé. 

"""

class Serpent:
    longueur : float
    couleur : str
    vitesse : int
    venimeux : bool

    def __init__(self, longueur:float, couleur:str, vitesse:int, venimeux:bool):
        self.longueur = longueur
        self.couleur = couleur
        self.vitesse = vitesse
        self.venimeux = venimeux

    def afficherInfo(self):
        print(
            "bonjour fdp, les caractéristiques du serpent sont:\n",
            f"L : {self.longueur}\n",
            f"Color : {self.couleur}\n",
            f"C : {self.vitesse}\n",
            f"V : {self.venimeux}\n")

    def seDeplacer(self, direction):
        print(f"le serpent se déplace dans la direction '{direction}'")

    def manger(self):
        self.longueur +=1
        print(f"the serpent grew and is now {self.longueur} m long")

def main():
    snek = Serpent(1,"yhfedhfhvfjd",6,0)
    snek.afficherInfo()
    snek.seDeplacer("droite")
    snek.manger()
if __name__ == "__main__":
    main()
