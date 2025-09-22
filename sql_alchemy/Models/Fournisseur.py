from sqlalchemy import Table, Integer, String, Column, MetaData
from ..connectiontodb import connection_to_db
from ..connectiontodb import connection_str

metadata = MetaData()

connected = connection_to_db(connection_str)
clients = Table(
    "fournisseurs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nom", String, nullable=False),
    Column("contact", String, nullable=False, unique=True),
)

metadata.create_all(connected)

print("Table 'clients' créée avec succès")
