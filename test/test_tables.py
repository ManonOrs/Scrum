import pytest
from src import Table


def test_init_table():
    table = Table(table_number=14, seats=4, status='occupé', clients=3)

    assert table.table_number == Table.table_number
    assert table.seats == Table.seats
    assert table.status == Table.status
    assert table.clients == Table.clients
    assert table.orders == []
