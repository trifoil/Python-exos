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

class Anaconda(Serpent):
        
anaconda = Serpent(1,2,3,4)
anaconda.afficherInfo()

boule = Volume()


