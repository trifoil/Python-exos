#hellloworld

print("hello")

#déclaration de classe

class MaPremiereClasse:
    pass

#instanciation d'un objet

PremierObjet = MaPremiereClasse()

#ajout d'un constructeur

class MaDeuxiemeClasse:
    def __init__(self):
        print("MaDeuxiemeClasse initialisée")

#instanciation de la 2e classe

MonDeuxiemeObjet = MaDeuxiemeClasse()

#ajout d'un attribut

class MaTroisiemeClasse:
    def __init__(self):
        print("hi, I'm Dave")
        self.stack_list = [2,7,6,6]

#instanciation de la 3e classe

MonTroisiemeObjet = MaTroisiemeClasse()
print (MonTroisiemeObjet.stack_list)        #afficher l'attribut stacklist

#ajout d'un attribut privé et getter (accesseur)

class Ma4EClasse:
    def __init__(self):
        print("Hi I'm Hal")
        self.__stack_list = [2,7,8,4]
    def stackGetter(self):
        return self.__stack_list

#instanciation de la 4e classe

Mon4EObjet = Ma4EClasse()
#print(Mon4EObjet.stack_list)    ne marche pas car attribut privé
print ()
print (Mon4EObjet.stackGetter())

#mise en place de setter (mutateur)

class Ma5EmeClasse:
    def __init__(self):
        print("inited")
        self.variablePrincipale = 3
    def variableSetter(self, valeur):
        self.variablePrincipale = valeur
    def variableGetter(self):
        return self.variablePrincipale

Mon5EObjet = Ma5EmeClasse()
print (Mon5EObjet.variableGetter())
Mon5EObjet.variableSetter(7)
print(Mon5EObjet.variableGetter())

#mise en place de property

class Ma6EmeClasse:
    def __init__(self):
        self.variablePrincipale = 0
    @property
    def variablePrincipale(self):
        print("retourne la valeur depuis le getter")
        return self._variablePrincipale

    @variablePrincipale.setter
    def variablePrincipale(self, valeur):
        print("modif de la variable depuis le setter")
        self._variablePrincipale = valeur

Mon6EObjet = Ma6EmeClasse()

print(Mon6EObjet.variablePrincipale)
Mon6EObjet.variablePrincipale = 7
print(Mon6EObjet.variablePrincipale)

#Pour les attributs privés on utilise __ au début du nom de la méthode
#(et pas à la fin) et la méthode est toujours retrouvable sur le modèle
#de _NomDeLaClasse__NomDeLaMethode


