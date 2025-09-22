from sqlalchemy import create_engine, Table, Column, Integer, String, DECIMAL, Text, ForeignKey, DateTime, MetaData, insert, func
from datetime import datetime, timedelta
import random
import os

# ----------------- Configuration -----------------
# Directly write credentials here or use environment variables
DB_USER = "postgres"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "sql_Alchemy"

connection_str = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(connection_str)
metadata = MetaData()

# ----------------- Table Definitions -----------------
clients = Table(
    "clients", metadata,
    Column("id", Integer, primary_key=True),
    Column("nom", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("telephone", String, nullable=True),
)

categories = Table(
    "categories", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False)
)

fournisseurs = Table(
    "fournisseurs", metadata,
    Column("id", Integer, primary_key=True),
    Column("nom", String, nullable=False),
    Column("contact", String, nullable=False, unique=True)
)

plats = Table(
    "plats", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("price", DECIMAL(10,2)),
    Column("description", Text),
    Column("category_id", ForeignKey("categories.id"))
)

commandes = Table(
    "commandes", metadata,
    Column("id", Integer, primary_key=True),
    Column("client_id", ForeignKey("clients.id")),
    Column("date_commande", DateTime(timezone=True), server_default=func.now(), nullable=False),
    Column("total", DECIMAL(5,2))
)

commandes_plats = Table(
    "commandes_plats", metadata,
    Column("commandes_id", ForeignKey("commandes.id")),
    Column("plat_id", ForeignKey("plats.id")),
    Column("quantite", Integer)
)

ingredients = Table(
    "ingredients", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("count_unitaire", DECIMAL(5,2))
)

avis = Table(
    "avis", metadata,
    Column("id", Integer, primary_key=True),
    Column("client_id", ForeignKey("clients.id")),
    Column("plat_id", ForeignKey("plats.id")),
    Column("note", Integer),
    Column("commentaire", Text, nullable=True),
    Column("date_avis", DateTime(timezone=True), nullable=False)
)

plat_ingredients = Table(
    "plat_ingredients", metadata,
    Column("id", Integer, primary_key=True),
    Column("plat_id", ForeignKey("plats.id")),
    Column("ingredient_id", ForeignKey("ingredients.id")),
    Column("quantite_necessaire", DECIMAL(5,2))
)

# ----------------- Drop and Create Tables -----------------
metadata.drop_all(engine)
print("✅ All tables dropped")

metadata.create_all(engine)
print("✅ All tables created")

# ----------------- Insert Fake Data -----------------
with engine.connect() as conn:
    # Clients
    clients_data = [
        ("Aamir El Amiri", "aamir@gmail.com", "0609117393"),
        ("Sara Bensaid", "sara@gmail.com", "0612345678"),
        ("Youssef Ahmed", "youssef@gmail.com", "0623456789"),
        ("Laila Omar", "laila@gmail.com", "0634567890"),
        ("Hassan Idrissi", "hassan@gmail.com", "0645678901")
    ]
    for nom, email, tel in clients_data:
        conn.execute(insert(clients).values(nom=nom, email=email, telephone=tel))

    # Categories
    categories_data = ["Entrées", "Plats principaux", "Desserts", "Boissons"]
    for name in categories_data:
        conn.execute(insert(categories).values(name=name))

    # Fournisseurs
    fournisseurs_data = [
        {"nom": "Fournisseur A", "contact": "contactA@email.com"},
        {"nom": "Fournisseur B", "contact": "contactB@email.com"},
        {"nom": "Fournisseur C", "contact": "contactC@email.com"},
    ]
    for f in fournisseurs_data:
        conn.execute(insert(fournisseurs).values(**f))

    # Plats (use category_id 1-4 from categories)
    plats_data = [
        ("Pizza Margherita", 45.00, "Pizza avec sauce tomate, mozzarella et basilic.", 2),
        ("Poulet Rôti", 70.00, "Poulet rôti aux herbes.", 2),
        ("Tarte aux pommes", 30.00, "Tarte sucrée aux pommes caramélisées.",3),
        ("Coca-Cola", 15.00, "Boisson gazeuse rafraîchissante.", 4),
    ]
    for name, price, desc, cat_id in plats_data:
        conn.execute(insert(plats).values(name=name, price=price, description=desc, category_id=cat_id))

    # Commandes
    commandes_data = [
        {"client_id": 1, "date_commande": datetime.now() - timedelta(days=3), "total": 120.00},
        {"client_id": 2, "date_commande": datetime.now() - timedelta(days=2), "total": 85.00},
        {"client_id": 3, "date_commande": datetime.now() - timedelta(days=1), "total": 150.00},
    ]
    for cmd in commandes_data:
        conn.execute(insert(commandes).values(**cmd))

    # Commandes_Plats
    commandes_plats_data = [
        (1, 1, 2),
        (1, 2, 1),
        (2, 1, 1),
        (2, 3, 2),
        (3, 2, 3),
    ]
    for cmd_id, plat_id, quant in commandes_plats_data:
        conn.execute(insert(commandes_plats).values(commandes_id=cmd_id, plat_id=plat_id, quantite=quant))

    # Ingredients
    ingredients_data = [
        ("Tomate", 5.0),
        ("Fromage", 3.5),
        ("Poulet", 8.0),
        ("Lait", 2.5),
        ("Oignon", 1.0)
    ]
    for name, count in ingredients_data:
        conn.execute(insert(ingredients).values(name=name, count_unitaire=count))

    # Avis
    avis_data = [
        (1, 1, 5, "Excellent plat!", datetime.now()),
        (2, 2, 4, "Très bon goût!", datetime.now() - timedelta(days=1)),
        (3, 3, 3, "Correct mais peut mieux faire", datetime.now() - timedelta(days=2))
    ]
    for client_id, plat_id, note, comment, date_avis in avis_data:
        conn.execute(insert(avis).values(client_id=client_id, plat_id=plat_id, note=note, commentaire=comment, date_avis=date_avis))

    # Plat_Ingredients
    plat_ingredients_data = [
        (1, 1, 2.0),
        (1, 2, 1.5),
        (2, 3, 3.0),
        (3, 4, 2.5)
    ]
    for plat_id, ing_id, quant in plat_ingredients_data:
        conn.execute(insert(plat_ingredients).values(plat_id=plat_id, ingredient_id=ing_id, quantite_necessaire=quant))

print("✅ All fake data inserted successfully!")
