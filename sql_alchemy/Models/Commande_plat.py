from sqlalchemy import Table, Integer, String, Column, MetaData,ForeignKey
from ..connectiontodb import connection_to_db
from ..connectiontodb import connection_str

metadata = MetaData()

connected = connection_to_db(connection_str)


commandes_plats_table = Table(
    'commandes_plats', metadata,
    Column('commandes_id', ForeignKey('commandes.id')),
    Column('plat_id', ForeignKey('plats.id')),
    Column('quantite', Integer)
)

metadata.create_all(connected)

print("Table 'clients' créée avec succès")
