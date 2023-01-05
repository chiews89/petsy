from .db import db, environment, SCHEMA, add_prefix_for_prod

cart_products = db.Table(
    'cart_products',
    db.Column('shopping_cart_id', db.Integer, db.ForeignKey(
        add_prefix_for_prod('shopping_carts.id')), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey(
        add_prefix_for_prod('products.id')), primary_key=True)
)
if environment == "production":
    cart_products.schema = SCHEMA
