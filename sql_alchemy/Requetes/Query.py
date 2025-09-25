from sqlalchemy import create_engine, Table,delete, Column,select, Integer,or_, insert,String, MetaData, DECIMAL, Text, ForeignKey, DateTime, func,desc,fetchall
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
stmt = (
    select(
        categories_table.c.name.label("categorie"),
        func.count(plats_table.c.id).label("nombre_plats")
    )
    .select_from(categories_table)  
    .join(plats_table, categories_table.c.id == plats_table.c.categorie_id, isouter=True)
    .group_by(categories_table.c.name)
    .order_by(categories_table.c.name)
)

with connected.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

# Afficher le prix moyen des plats par catégorie et le coût moyen des ingrédients par plat.

stmt = (
    select(
        categories_table.c.name.label("categorie"),
        func.avg(plats_table.c.prix).label("prix_moyen_plats")
    )
    .select_from(categories_table)
    .join(plats_table, categories_table.c.id == plats_table.c.categorie_id, isouter=True)
    .group_by(categories_table.c.name)
    .order_by(categories_table.c.name)
)

stmt = (
    select(
        plats_table.c.name.label("plat"),
        func.avg(plat_ingredients.c.quantite * ingredients_table.c.prix_unitaire).label("cout_moyen_ingredients")
    )
    .join(plat_ingredients, plats_table.c.id == plat_ingredients.c.plat_id)
.join(ingredients_table, plat_ingredients.c.ingredient_id == ingredients_table.c.id)
.group_by(plats_table.c.name)
.order_by(plats_table.c.name)
)

with connected.connect() as conn:
    print("moyen des plats par categorie :")
    for row in conn.execute(stmt):
        print(row)

    print(" cout moyen des ingredients par plat :")
    for row in conn.execute(stmt):
        print(row)

# Afficher le nombre de commandes par client, trié par ordre décroissant.

stmt = select(clients.c.name.label("clients"),func.count(commandes_table.c.id.label("clients"))
            .join(clients,commandes_table.c.client_id== clients.c.id)).group_by(clients.c.name)

with connected.connect() as conn:
    print("moyen des plats par categorie :")
    for row in conn.execute(stmt):
        print(row)

stmt = (
    select(
        clients.c.id,
        clients.c.name,
        func.count(commandes_table.c.id).label("nombre_commandes")
    )
    .join(commandes_table, clients.c.id == commandes_table.c.client_id)
    .group_by(clients.c.id,clients.c.name)
    .having(func.count(commandes_table.c.id) >2)
)

with connected.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

stmt = (
    select(
        plats_table.c.name.label("plat"),
        func.sum(commandes_table.c.quantite).label("total_quantite"),
        func.avg(avis_table.c.note).label("note_moyenne")
    )
    .join(commandes_table, plats_table.c.id == commandes_table.c.plat_id)
    .join(avis_table, plats_table.c.id == avis_table.c.plat_id, isouter=True)
    .group_by(plats_table.c.name)
    .having(func.sum(commandes_table.c.quantite) > 3)
    .order_by(func.sum(commandes_table.c.quantite).desc())
)


from datetime import date

stmt = (
    select(
        commandes_table.c.id.label("commande_id"),
        commandes_table.c.date,
        clients.c.name.label("client")
    )
    .join(clients, commandes_table.c.client_id == clients.c.id)
    .where(commandes_table.c.date.between(date(2025, 7, 1), date(2025, 9, 30)))
    .order_by(commandes_table.c.date)
)


query = select(func.max(commandes_table.c.date)).scalar_subquery()

stmt = (
    select(
        commandes_table.c.id.label("commande_id"),
        clients.c.name.label("client"),
        plats_table.c.name.label("plat"),
        commandes_plats_table.c.quantite
    )
    .join(clients, commandes_table.c.client_id == clients.c.id)
    .join(commandes_plats_table, commandes_table.c.id == commandes_plats_table.c.commande_id)
    .join(plats_table, commandes_plats_table.c.plat_id == plats_table.c.id)
    .order_by(commandes_table.c.date_commande,desc()).limit(1)
)
with connected.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

# Afficher les clients ayant passé une commande d’un montant supérieur à 150, avec leur numéro de téléphone.

stmt = (
    select(
        commandes_table.c.id.label("commande_id"),
        clients.c.name.label("client"),
        plats_table.c.name.label("plat"),
      #
    )
    .join(clients, commandes_table.c.client_id == clients.c.id)
    .join(commandes_plats_table, commandes_table.c.id == commandes_plats_table.c.commande_id)
    .join(plats_table, commandes_plats_table.c.plat_id == plats_table.c.id)
    .order_by(commandes_table.c.id).having(func.sum(plats_table.c.price * commandes_plats_table.c.quantite)>150)
)   

with connected.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

# Afficher les plats dont le coût total des ingrédients est supérieur à 50% du prix du plat.

stmt = (
    select(
        plats_table.c.name.label("plat"),
        plats_table.c.prix.label("prix_plat"),
        func.sum(plat_ingredients.c.quantite * ingredients_table.c.prix_unitaire).label("cout_ingredients")
    )
    .join(plat_ingredients, plats_table.c.id == plat_ingredients.c.plat_id)
    .join(ingredients_table, plat_ingredients.c.ingredient_id == ingredients_table.c.id)
    .group_by(plats_table.c.id, plats_table.c.name, plats_table.c.prix)
    .having(func.sum(plat_ingredients.c.quantite * ingredients_table.c.prix_unitaire) > 0.5 * plats_table.c.prix)
    .order_by(plats_table.c.name)
)

with connected.connect() as conn:
    for row in conn.execute(stmt):
        print(row)


# Ajouter un nouveau plat dans la catégorie "Végétarien" avec deux ingrédients.

with connected.connect() as conn:
    categorieID = conn.execute(
        select(categories_table.c.id).where(categories_table.c.nom == "Végétarien")
    ).scalar_one()

    result = conn.execute(
        insert(plats_table).values(nom="Salade fraiche", prix=80, id_categorie=categorieID).returning(plats_table.c.id)
    )
    plat_id = result.scalar_one()

    conn.execute(insert(ingredients_table), [
        {"plat_id": plat_id, "ingredient_id": 1, "quantite": 2},
        {"plat_id": plat_id, "ingredient_id": 3, "quantite": 1}
    ])

    conn.commit()
    

# Question 19 : Supprimer le client "Youssef El Khalfi", ses commandes et ses avis
with engine.begin() as conn:
    client_id = conn.execute(
        select(clients.c.id).where(clients.c.nom == "Youssef El Khalfi")
    ).scalar()

    if client_id:
        commande_ids = conn.execute(
            select(commandes_table.c.id).where(commandes_table.c.client_id == client_id)
        ).scalars().all()

        if commande_ids:
            conn.execute(
                commandes_plats_table.delete().where(
                    commandes_plats_table.c.commande_id.in_(commande_ids)
                )
            )

        conn.execute(avis_table.delete().where(avis_table.c.client_id == client_id))

        conn.execute(commandes_table.delete().where(commandes_table.c.client_id == client_id))

        conn.execute(clients.delete().where(clients.c.id == client_id))

        print(" Client et toutes ses données supprimés")
    else:
        print(" Client non trouvé")


# Afficher pour chaque client :
# Son nom
# Le nombre total de plats commandés
# Le montant total dépensé
# La note moyenne de leurs av
stmt = (
    select(
        clients.c.nom.label("client"),
        func.coalesce(func.sum(commandes_plats_table.c.quantite), 0).label("total_plats"),
        func.coalesce(func.sum(commandes_plats_table.c.quantite * plats_table.c.prix), 0).label("total_depense"),
        func.coalesce(func.avg(avis_table.c.note), 0).label("note_moyenne")
    )
    .select_from(clients)
    .outerjoin(commandes_table, clients.c.id == commandes_table.c.client_id)
    .outerjoin(commandes_plats_table, commandes_table.c.id == commandes_plats_table.c.commande_id)
    .outerjoin(plats_table, commandes_plats_table.c.plat_id == plats_table.c.id)
    .outerjoin(avis_table, clients.c.id == avis_table.c.client_id)
    .group_by(clients.c.id, clients.c.nom)
)

with connected.connect() as conn:
    rows = conn.execute(stmt).fetchall()
    for row in rows:
        print(row)
