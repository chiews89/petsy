from flask import Blueprint, request
from flask_login import login_required, current_user
from app.forms import ReviewForm, EditReviewForm
from app.models import Review, db
from datetime import datetime

review_routes = Blueprint('reviews', __name__)


@review_routes.route('')
def get_reviews():
    reviews = Review.query.all()
    return {'reviews': [review.to_dict() for review in reviews]}


@review_routes.route('/new', methods=["POST"])
@login_required
def add_reviews():
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_review = Review(
            buyer_id = current_user.id,
            review = form.data['review'],
            rating = form.data['rating'],
            product_id = form.data['product_id'],
            created_at = datetime.now(),
            updated_at = datetime.now(),
        )
        db.session.add(new_review)
        db.session.commit()
        return new_review.to_dict()
    return {'message': 'sucess'}


@review_routes.route('/<int:id>', methods=["PUT"])
@login_required
def edit_reviews(id):
    form = EditReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        edit = Review.query.get(id)
        edit.buyer_id = current_user.id
        edit.review = form.data['review']
        edit.rating = form.data['rating']
        # edit.product_id = form.data['product_id']
        edit.created_at = form.data['created_at']
        edit.updated_at = datetime.now()
        db.session.add(edit)
        db.session.commit()
        return edit.to_dict()
    return {'message': "Success"}


@review_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_reviews(id):
    review_to_delete = Review.query.get(id)
    db.session.delete(review_to_delete)
    db.session.commit()
    return {'message': 'Success'}
