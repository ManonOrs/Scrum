class Table:
    table_number = 0
    seats = 0
    status = 'libre'
    clients = 0
    orders = []

    def __init__(self, table_number, seats, status, clients):
        self.table_number = table_number
        self.seats = seats
        self.status = status
        self.clients = clients

    def set_status(self, status):
        self.status = status

    def add_clients(self, clients_number):
        self.clients = self.clients + clients_number

    def remove_client(self, clients_number):
        self.clients = self.clients - clients_number

    def add_order(self, order):
        self.orders.append(order)

    def remove_order(self, order):
        self.orders.remove(order)

    def show_table_infos(self):
        print('Numéro de table:' + str(self.table_number))
        print('Nombre de sièges:' + str(self.seats))
        print('Status:' + str(self.status))
        print('Nombre de clients:' + str(self.clients))
        print('Nombre de commande:' + str(len(self.orders)))
        if not self.orders:
            print('Auccune commande a cette table')
        else:
            for order in self.orders:
                print('Commande N°' + str(order.numero) + ' au nom de: ' + str(order.name))
                print('Les plats:')
                if order.plats:
                    for plat in order.plats:
                        print('- ' + plat)
