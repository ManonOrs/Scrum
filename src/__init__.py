from src.table import Table
from src.orderer import Ordered

table1 = Table(14, 4, 'occupée', 3)

orderer1 = Ordered(15, 14, 'Billy')

table1.add_order(orderer1)
table1.show_table_infos()
