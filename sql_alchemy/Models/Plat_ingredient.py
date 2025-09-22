from sqlalchemy import Table, Integer, String, Column, MetaData,ForeignKey,DECIMAL
from ..connectiontodb import connection_to_db
from ..connectiontodb import connection_str

metadata = MetaData()

connected = connection_to_db(connection_str)
plat_ingredients = Table(
    "plat_ingredients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("plat_id", ForeignKey("plats.id")),
    Column("ingredient_id", ForeignKey("ingredients.id")),
    Column("quantite_necessaire", DECIMAL(precision=5,scale=2)),
)

metadata.create_all(connected)

print("Table 'clients' créée avec succès")
