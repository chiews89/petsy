from .db import db

class Category(db.Model):
  __tablename__ = 'categories'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)

  products = db.relationship('Product', back_populates='category')

  def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'products': [product.to_dict() for product in self.products]
        }

  def to_dict_with_limit(self):
        return {
            'id': self.id,
            'name': self.name,
            'products': [product.to_dict() for product in self.products[0:5]]
        }
