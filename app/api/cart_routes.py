from flask import Blueprint
from flask_login import login_required
from app.models import Shopping_Cart

cart_routes = Blueprint('shopping_cart', __name__)


@cart_routes.route('')
@login_required
def get_cart():
    cart = Shopping_Cart.query.all()
    return cart


@cart_routes.route('/new', methods=["POST"])
@login_required
def add_cart():
    ##add form
    ##query
    return None


@cart_routes.route('/<int:id>', methods=["PUT"])
@login_required
def edit_cart():
    ##edit form
    ##query
    return None


@cart_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_cart():
    ##delete
    return None

@cart_routes.route('/clear/<int:id>', methods=["DELETE"])
@login_required
def delete_all_cart():
    ##delete
    return None
