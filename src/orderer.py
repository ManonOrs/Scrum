tabOrdered = []
class Ordered:

    def __init__(self,  numero, table, name):
        self.name = name
        self.numero = numero
        self.plats = [] 
        self.table = table 

    def addPlat(self, plats):
        self.plats.append(plats)
        print("\n" + plats + " ajouté \n")

    def deletePlat(self, plat, indiceOrdered):
        indicePlat = -1
        for plt in tabOrdered[indiceOrdered].plats:
            indicePlat = indicePlat + 1
            if plt == plat:
                del tabOrdered[indiceOrdered].plats[indicePlat]
        print(plat + " supprimé")

def addOrdered(numero, table, name):
    addingOrdered = Ordered(numero, table, name)
    tabOrdered.append(addingOrdered)

def deleteOrdered(numero):
    indiceOrdered = -1
    for ordered in tabOrdered:
        indiceOrdered = indiceOrdered + 1
        if ordered.numero == numero:
            del tabOrdered[indiceOrdered]

def modifyOrdered(numero, action):
    indiceOrdered = -1
    for ordered in tabOrdered:
        indiceOrdered = indiceOrdered + 1
        if ordered.numero == numero:
            if action == "delete":
                for plt in tabOrdered[indiceOrdered].plats:
                    print(plt)
                plat = input("Quel est le plat à supprimer ? ")
                tabOrdered[indiceOrdered].deletePlat(plat, indiceOrdered)
                

            if action == "add":
                for plt in tabOrdered[indiceOrdered].plats:
                    print(plt)
                print("\n")
                plat = input("Quel est le plat ajouter ? ")
                tabOrdered[indiceOrdered].addPlat(plat)

       


#addOrdered(25, 4, "Guy")
#deleteOrdered(10)
#modifyOrdered(1, "delete")