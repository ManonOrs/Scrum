entree = ["salade", "tomate", "fois gras"]
plat = ["boeuf bourgignon", "grattin de choux", "ragou de lapin"]
dessert = ["glace", "tarte", "gateau"]


selection = []
class menu:

    def __init__(self, numero):
        self.numero = numero
        self.plats = []

    def ajoutMenu(self, plat):
        self.plats.append(plat)

choix = "yes"
chiffre = 1

while choix == "yes":

    def commande():
        print("Voici la liste des entrées :")
        for lentree in entree:
            print(lentree)
        print("\n")

        print("Voici la liste des plats :")
        for lplat in plat:
            print(lplat)
        print("\n")

        print("Voici la liste des desserts :")
        for ldessert in dessert:
            print(ldessert)

        print("\n")

        global chiffre
        selection.append(menu(chiffre))
        chiffre = chiffre + 1

        print("votre numero de menu est " + str(selection[chiffre-2].numero))

        print("\n")

        choisir = input("choisi ton entrée \n")
        selection[chiffre-2].ajoutMenu(choisir)

        choisir = input("choisi ton plat \n")
        selection[chiffre-2].ajoutMenu(choisir)

        choisir = input("choisi ton dessert \n")
        selection[chiffre-2].ajoutMenu(choisir)

        print("\n")

        print("Voici votre menu :")
        for monMenu in selection[chiffre-2].plats:
            print(monMenu)

    print("\n")

    choix = input("souhaitez vous commander ? \n")
    if choix == "yes":
        commande()
    else:
        print("vous avez choisi de ne pas commander")

for Menu in selection:
    print("Voici les menus : " + str(Menu.numero))

