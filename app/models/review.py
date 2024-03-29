from .db import db, environment, SCHEMA, add_prefix_for_prod


class Review(db.Model):
    __tablename__ = 'reviews'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    buyer = db.relationship('User', back_populates='review')
    product = db.relationship('Product', back_populates='review')

    def to_dict(self):
        return {
            'id': self.id,
            'buyer_id': self.buyer_id,
            'product_id': self.product_id,
            'username': self.buyer.username if self.buyer else None,
            'review': self.review,
            'rating': self.rating,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
