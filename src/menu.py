import src.orderer

def menu():
    listMenu =["Nouvelle Commande","Modifier commande","Supprimer commande","Liste menu"]
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
        src.orderer.addOrdered(numero, table, name)
        menu()

    if menu == "2":
        for ordered in src.orderer.tabOrdered:
            print("Commande N°" + numero + ", table N°" + table)
        numero = input("numero ? ")
        action = input("action ? ")
        src.orderer.modifyOrdered(numero, action)
        menu()

    if menu == "3":
        name = input("name ?")
        numero = input("numero ?")
        table = input("table ?")
        src.orderer.deleteOrdered(numero)
        menu()

    if menu == "4":
        for order in src.orderer.tabOrdered:
            print("Commande N°"+ order.numero)
        select = input("Selectionner une commande avec le numero pour voir\nla listes des menus de celle-ci.\nAppuyer sur 0 puis entrée pour retourner a l'accueil ")
        if select == 0:
            menu()

menu()   