import datetime

class Humain:
    def __init__(self):
        self.nom = "a"
        self.prenom = "a"
        self.anneeDeNaissance = 2005
        self.enfants = "a"

    def CalculerAge(self):
        print(datetime.date.today().year-self.anneeDeNaissance)
"""     def SePresenter(self):

    def ReconnaissanceParentale(self): """

theo = Humain()
theo.CalculerAge()