import pytest
from src import Table


def test_init_table():
    table = Table(table_number=14, seats=4, status='occupé', clients=3)

    assert table.table_number == 14
    assert table.seats == 4
    assert table.status == 'occupé'
    assert table.clients == 3
    assert table.orders == []


def test_1():
    assert 1 == 12


def test_add_orders():
    table = Table(table_number=14, seats=4, status='occupé', clients=3)
    table.add_order('commande 1')
    assert table.orders == ['commande 1']


def test_add_client():
    table = Table(table_number=14, seats=6, status='occupé', clients=3)
    table.add_clients(2)
    assert table.clients == 5


def test_remove_client():
    table = Table(table_number=14, seats=6, status='occupé', clients=5)
    table.remove_client(2)
    assert table.clients == 3
