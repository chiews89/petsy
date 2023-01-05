from flask import Blueprint, request
from flask_login import current_user
from app.models import Product, db
from app.forms import ProductForm, EditProductForm
from datetime import datetime

product_routes = Blueprint("products", __name__)

@product_routes.route("")
def get_products():

    products = Product.query.all()
    return {"products": [product.to_dict() for product in products]}


@product_routes.route("/<int:id>")
def get_product_by_id(id):

    product = Product.query.get(id)
    return product.to_dict()

@product_routes.route('/new', methods=['POST'])
# @login_required
def add_product():
    form = ProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_product = Product(
            seller_id = current_user.id,
            name = form.data['name'],
            image_url = form.data['image_url'],
            description = form.data['description'],
            price = form.data['price'],
            category_id = int(form.data['category_id']),
            created_at = datetime.now(),
            updated_at = datetime.now(),
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product.to_dict()
    return {'message': "Success"}

@product_routes.route('/<int:id>/edit', methods=['PUT'])
# @login_required
def edit_product(id):
    form = EditProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        edit = Product.query.get(id)
        edit.seller_id = current_user.id
        edit.name = form.data['name'],
        edit.image_url = form.data['image_url'],
        edit.description = form.data['description'],
        edit.price = form.data['price'],
        edit.category_id = int(form.data['category_id']),
        edit.created_at = form.data['created_at'],
        edit.updated_at = datetime.now(),
        db.session.add(edit)
        db.session.commit()
        return edit.to_dict()
    return {'message': "Success"}

@product_routes.route('/delete/<int:id>', methods=['DELETE'])
# @login_required
def delete_product(id):
    product_delete = Product.query.get(id)
    db.session.delete(product_delete)
    db.session.commit()
    return {'message': "Success"}
