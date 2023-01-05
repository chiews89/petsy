from .db import db

cart_products = db.Table(
    'cart_products',
    db.Column('shopping_cart_id', db.Integer, db.ForeignKey('shopping_carts.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)
