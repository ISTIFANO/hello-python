from sqlalchemy import Table, Integer, String, Column, MetaData,DECIMAL,Text,ForeignKey
from ..connectiontodb import connection_to_db
from ..connectiontodb import connection_str

metadata = MetaData()

connected = connection_to_db(connection_str)
plats_table = Table(
    'plats', metadata,
    Column('id', Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column('price', DECIMAL(precision=10, scale=2)),
    Column('description', Text),
    Column('category_id', ForeignKey('categories.id'))
)

metadata.create_all(connected)

print("Table 'plats' créée avec succès")
