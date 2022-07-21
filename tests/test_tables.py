import pytest
from src import Table


def test_init_table():
    table = Table(table_number=14, seats=4, status='occupé', clients=3)

    assert table.table_number == 14
    assert table.seats == 4
    assert table.status == 'occupé'
    assert table.clients == 3
    assert table.orders == []


def test_add_orders(order):
    table = Table(table_number=14, seats=4, status='occupé', clients=3)
    orders = table.orders
    table.add_order(order)
    assert table.orders == orders.append(order)


def test_add_client():
    table = Table(table_number=14, seats=6, status='occupé', clients=3)
    table.add_clients(2)
    assert table.clients == 5


def test_remove_client():
    table = Table(table_number=14, seats=6, status='occupé', clients=5)
    table.remove_client(2)
    assert table.clients == 3
