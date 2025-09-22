from sqlalchemy import Table, Integer, String, Column, MetaData
from ..connectiontodb import connection_to_db
from ..connectiontodb import connection_str

metadata = MetaData()

connected = connection_to_db(connection_str)
clients = Table(
    "cliensdts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nom", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("telephone", String, nullable=True),
)

metadata.create_all(connected)

print("Table 'clients' créée avec succès")
