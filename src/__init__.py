import json

from table import Table

from orderer import Ordered


# Return True if id existe in waiters.json
def connexion(id):
    with open('json/waiters.json') as f:
        data = json.load(f)
    for x in data:
        if id == x["id"]:
            return True
    return False


def get_orderer(orders):
    print("coucou")
    with open('json/orders.json') as order_json:
        data = json.load(order_json)
    for order in data:
        new_order = Ordered(order['numero'], order['table'], order['name'])
        if order['plats']:
            for plat in order['plats']:
                new_order.addPlat(plat)
        orders.append(new_order)


def get_tables(tables, orders):
    with open('json/tables.json') as tables_json:
        data = json.load(tables_json)
    for table in data:
        new_table = Table(table['table_number'], table['seats'], table['status'], table['clients'])
        if table['orders']:
            for order in table['orders']:
                new_table.add_order(order)
        elif orders:
            for order in orders:
                print(order.table)
                print(new_table.table_number)
                print("------------------")
                if order.table == new_table.table_number:
                    print("pass")
                    print("______________")
                    new_table.add_order(order)
        tables.append(new_table)


tables = []
orders = []

# connexion(1)
get_orderer(orders)
get_tables(tables, orders)
