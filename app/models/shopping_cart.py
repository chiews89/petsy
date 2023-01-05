from .db import db, environment, SCHEMA, add_prefix_for_prod
from .cart_product import cart_products


class Shopping_Cart(db.Model):
    __tablename__ = 'shopping_carts'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    products = db.relationship(
        'Product', secondary=cart_products, back_populates='shopping_cart')

    def to_dict(self):
        return {
            'id': self.id,
            'buyer_id': self.buyer_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
