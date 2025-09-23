from sqlalchemy import create_engine, Table, Column,select, Integer,or_, String, MetaData, DECIMAL, Text, ForeignKey, DateTime, func,desc,fetchall
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
avis_table = Table(
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


# question 01
stmt = select(plats_table)

with connected.connect() as query :
    res = query.execute(stmt)
    # fetchPlats = res.fetchall()

for plat in res :
    print(plat)


# question 03

stmt = select(plats_table).order_by(plats_table.prix)

with connected.connect() as query :
    res = query.execute(stmt)
    fetchPlats = res.fetchall()

for plat in fetchPlats :
    print(plat)

# question 04

stmt = select(plats_table).where(plats_table.c.prix.between(30,80))

with connected.connect() as query :
    res = query.execute(stmt)
    fetchPlats = res.fetchall()

for plat in fetchPlats :
    print(plat)

    # question 05

stmt = select(plats_table).where(or_(plats_table.columns.name.like("S%"),plats_table.columns.name.like("P%")))

with connected.connect() as query :
    res = query.execute(stmt)
    fetchPlats = res.fetchall()

for plat in fetchPlats :
    print(plat)

#question 06

stmt = select(plats_table.c.name.label("plats"),categories_table.c.name.label("categories"),fournisseurs.c.name.label("fournisseurs")).join(
    categories_table,plats_table.c.categorie_id==categories_table.c.id).join(
        fournisseurs,ingredients_table.c.fournisseur_id ==fournisseurs.c.id).join(
            ingredients_table,plat_ingredients.c.ingredient_id == ingredients_table.c.id).distinct(
                plats_table.c.id).order_by(plats_table.c.id,desc(
                    plat_ingredients.c.quantite_necessaire))

with connected.connect() as plats :
   resultat =  plats.execute(stmt)
   for plat in resultat :
     print(plat)


# question 07

stmt = select(commandes_table.c.name.label("commendes"),clients.c.name.label("clients") ,func.sum(commandes_table.c.plat)).join(clients,commandes_table.c.client_id == clients.c.id).join(commandes_table,commandes_table.c.plat_id == commandes_plats_table.c.id).group_by(plat.c.id)

with connected.begin() as executeStmt :
    queryEx = executeStmt.execute(stmt)
    resultat = queryEx.fetchall()

    for plat in resultat:
        print(plat)

    
#question 8 

from sqlalchemy import select, func

stmt = (
    select(
        commandes_table.c.id.label("commande_id"),
        plats_table.c.name.label("plat"),
        commandes_plats_table.c.quantite.label("quantite_commande"),
        func.sum(plat_ingredients.c.quantite * ingredients_table.c.count_unitaire * commandes_plats_table.c.quantite)
            .label("cout_total")
    )
    .join(commandes_plats_table, commandes_table.c.id == commandes_plats_table.c.commande_id)
    .join(plats_table, commandes_plats_table.c.plat_id == plats_table.c.id)
    .join(plat_ingredients, plats_table.c.id == plat_ingredients.c.plat_id)
    .join(ingredients_table, plat_ingredients.c.ingredient_id == ingredients_table.c.id)
    .group_by(commandes_table.c.id, plats_table.c.name, commandes_plats_table.c.quantite)
    .order_by(commandes_table.c.id)
)

with connected.connect() as conn:
    for row in conn.execute(stmt):
        print(row)


#question 09 
# Afficher le nombre de plats pour chaque catégorie, y compris celles sans plats.

