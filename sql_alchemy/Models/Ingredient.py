from sqlalchemy import Table, Integer, String, Column, MetaData,DECIMAL,ForeignKey
from ..connectiontodb import connection_to_db
from ..connectiontodb import connection_str

metadata = MetaData()

connected = connection_to_db(connection_str)
ingredients_table = Table(
    'ingredients', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('count_unitaire', DECIMAL(precision=5, scale=2)),
    Column("fournisseur_id",ForeignKey('fournisseurs.id'))
)

metadata.create_all(connected)

print("Table 'clients' créée avec succès")
