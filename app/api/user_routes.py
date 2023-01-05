from flask import Blueprint
from flask_login import login_required, current_user
from app.models import User

user_routes = Blueprint('users', __name__)


@user_routes.route('')
@login_required
def users():
    user = User.query.get(current_user.id)
    return user.to_dict()
