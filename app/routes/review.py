from flask import Blueprint,  request, jsonify, redirect
from ..models import db, Review
from app import app

bp = Blueprint('reviews', __name__, url_prefix='')

# register


@bp.route('/postreview', methods=['POST'])
def register_user():
    data = request.json
    new_review = Review(
        user_id=data["user_id"],
        workoutplan_id=data["workoutplan_id"],
        review=data["review"],
    )
    db.session.add(new_review)
    db.session.commit()
    review = {}
    review[new_review.id] = {
        "id": new_review.id,
        "review": new_review.review,
        "user": new_review.user_review.username
    }
    return {"review": review}
