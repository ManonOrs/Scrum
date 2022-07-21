import orderer


def accueil():
    listMenu =["Nouvelle Commande","Modifier commande","Supprimer commande","Liste commande","Quitter"]
    selector = 1
    for menu in listMenu:
        print("["+str(selector)+"] "+ menu)
        selector = selector + 1
    print("\n")
    menu = input("Selection ? ")
    switchMenu(menu)

def switchMenu(menu):
    if menu == "1":
        name = input("name ? ")
        numero = input("numero ? ")
        table = input("table ? ")
        orderer.addOrdered(numero, table, name)
        accueil()

    if menu == "2":
        for ordered in orderer.tabOrdered:
            print("Commande N°" + numero + ", table N°" + table)
        numero = input("numero ? ")
        action = input("action ? ")
        orderer.modifyOrdered(numero, action)
        accueil()

    if menu == "3":
        name = input("name ?")
        numero = input("numero ?")
        table = input("table ?")
        orderer.deleteOrdered(numero)
        accueil()

    if menu == "4":
        for order in orderer.tabOrdered:
            print("Commande N°"+ order.numero + ", table N°" + order.table)
        print("\n")
        select = input("Selectionner une commande avec le numero pour voir\nla listes des menus de celle-ci.\nAppuyer sur 0 puis entrée pour retourner a l'accueil ")
        if select == "0":
            accueil()

