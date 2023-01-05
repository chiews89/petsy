from flask import Blueprint
from app.models import Product, Category

home_route = Blueprint("home", __name__)

@home_route.route("")
def products():
  home_products = Product.query.all()
  return {"products": [product.to_dict() for product in home_products]}

def categories():
  home_categories = Category.query.all()
  return {"categories": [category.to_dict() for category in home_categories]}
