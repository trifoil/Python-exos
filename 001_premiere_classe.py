""" class Volume :
    def __init__(self):
        self.__facesamount = 6
        self.__name = "cube"

    def setFacesAmount(self):
        self.__facesamount = input("\nEntrer le nombre de faces : ")

    def setName(self):
        self.__name = input("\nPut ya dick in there : ")

    def getName(self):
        print(self.__name)
    
    def getFacesAmount(self):
        print(self.__facesamount) """

class Serpent :
    def __init__(self, lo, co, vi, ve):
        self.Longueur = lo
        self.Couleur = co
        self.Vitesse = vi
        self.Venimeux = ve
    
    def afficherInfo(self):
        print("Longueur : " + str(self.Longueur) +
              "\nCouleur : " + str(self.Couleur) + 
              "\nVitesse : " +str(self.Vitesse)+"\n")

    def seDeplacer(self):
        
anaconda = Serpent(1,2,3,4)
anaconda.afficherInfo()

boule = Volume()



""" boule.setName()
boule.setFacesAmount()
boule.__name ="pute"
boule.getName()
boule.getFacesAmount() """