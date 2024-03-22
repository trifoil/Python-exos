'''
TD 2
Créer une classe « Voiture » qui possède les caractéristiques suivantes :
* Couleur
* Vitesse
* Portes
* Marque
* Demarree ?
'''

class Voiture():
    couleur : str
    vitesse : int
    portes : int
    marque : str
    demarree : bool

    def __init__(self, couleur = "white", vitesse = 0, portes = 4, marque = "generic", demarree = False):
        self.couleur = couleur
        self.vitesse = vitesse
        self.portes = portes
        self.marque = marque
        self.demarree = demarree

def main():
    maVoiture = Voiture()
    print(maVoiture.marque)
    autreVoiture = Voiture(marque="hyundai")
    print(f"{autreVoiture.marque} +  {autreVoiture.demarree}")    

if __name__=="__main__":
    main()
