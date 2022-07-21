from src.table import Table

table1 = Table(14, 4, 'occupée', 3)

table1.add_order('commande1')
table1.add_order('commande2')
table1.add_order('commande3')
table1.show_table_infos()