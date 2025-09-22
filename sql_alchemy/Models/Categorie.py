from sqlalchemy import Table, Integer, String, Column, MetaData
from ..connectiontodb import connection_to_db
from ..connectiontodb import connection_str

metadata = MetaData()

connected = connection_to_db(connection_str)
categories_table = Table(
    'categories', metadata,
    Column('id', Integer, primary_key=True),
    Column("name", String(50), nullable=False)
)

metadata.create_all(connected)

print("Table 'categorie' créée avec succès")
