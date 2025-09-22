from sqlalchemy import Table, Integer, Column, MetaData,DECIMAL,DateTime,ForeignKey,func
from ..connectiontodb import connection_to_db
from ..connectiontodb import connection_str

metadata = MetaData()

connected = connection_to_db(connection_str)
commandes_table = Table(
    'commandes', metadata,
    Column('id', Integer, primary_key=True),
    Column('client_id', ForeignKey('clients.id')),
    Column('date_commande', DateTime(timezone=True), server_default=func.now(), nullable=False),
    Column('total', DECIMAL(precision=5, scale=2))
)

metadata.create_all(connected)

print("Table 'clients' créée avec succès")
