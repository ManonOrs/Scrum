tabOrdered = []
class Ordered:

    def __init__(self,  numero):
        self.numero = numero
        self.plats = []    

    def addPlat(self, plats):
        self.plats.append(plats)

def addOrdered(numero):
    addingOrdered = Ordered(numero)
    tabOrdered.append(addingOrdered)


addOrdered(1)

tabOrdered[0].addPlat('gratin')
print(tabOrdered[0].plats)
