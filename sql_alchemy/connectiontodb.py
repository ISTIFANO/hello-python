from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DECIMAL, Text, ForeignKey, DateTime, func
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

connection_str = f'postgresql://{user}:{password}@{host}:{port}/{database}'

def connection_to_db(conn):
    try:
        engine = create_engine(conn)
        conn = engine.connect()
        conn.close()
        return engine
    except Exception as err:
        return err

connected = connection_to_db(connection_str)
metadata = MetaData()

clients = Table(
    "clients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nom", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("telephone", String, nullable=True),
)


categories_table = Table(
    'categories', metadata,
    Column('id', Integer, primary_key=True),
    Column("name", String(50), nullable=False)
)

fournisseurs = Table(
    "fournisseurs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nom", String, nullable=False),
    Column("contact", String, nullable=False, unique=True),
)

plats_table = Table(
    'plats', metadata,
    Column('id', Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column('price', DECIMAL(precision=10, scale=2)),
    Column('description', Text),
    Column('category_id', ForeignKey('categories.id'))
)

commandes_table = Table(
    'commandes', metadata,
    Column('id', Integer, primary_key=True),
    Column('client_id', ForeignKey('clients.id')),
    Column('date_commande', DateTime(timezone=True), server_default=func.now(), nullable=False),
    Column('total', DECIMAL(precision=5, scale=2))
)

commandes_plats_table = Table(
    'commandes_plats', metadata,
    Column('commandes_id', ForeignKey('commandes.id')),
    Column('plat_id', ForeignKey('plats.id')),
    Column('quantite', Integer)
)

ingredients_table = Table(
    'ingredients', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('count_unitaire', DECIMAL(precision=5, scale=2))
)
ingredients_table = Table(
    'avis', metadata,
    Column('id', Integer, primary_key=True),
    Column('client_id', ForeignKey("clients.id")),
    Column('plat_id ', ForeignKey("plats.id")),
    Column('note',Integer),
    Column("commentaire",Text,nullable=True),
    Column("data_avis",DateTime(timezone=True),nullable=False)
    
)
plat_ingredients = Table(
    "plat_ingredients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("plat_id", ForeignKey("plats.id")),
    Column("ingredient_id", ForeignKey("ingredients.id")),
    Column("quantite_necessaire", DECIMAL(precision=5,scale=2)),
)

metadata.create_all(connected)
print("Tables created successfully")

