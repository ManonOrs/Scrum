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