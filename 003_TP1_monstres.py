class Monstre:
    def __init__(self, c="test"):
        self.race = c

robin = Monstre()

print(robin.race)

florent = Monstre("shit")

print(florent.race)

