from flask import Blueprint, request, jsonify, redirect
from ..models import db, User
from werkzeug.security import generate_password_hash
from app import app

bp = Blueprint('users', __name__, url_prefix='')

# register


@bp.route('/signup', methods=['POST'])
def register_user():
    data = request.json
    hashed_password = generate_password_hash(data["password"])
    new_user = User(
        username=data["username"],
        email=data["email"],
        password=hashed_password,
        privilage="trainer"
    )
    db.session.add(new_user)
    db.session.commit()
    return {"id": new_user.id, "username": new_user.username}

# # Login


@bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    print(data["username"])
    user = User.query.filter_by(username=data['username']).first()
    if user.check_password(data['password']):
        return {"id": user.id, "username": user.username, }
    else:
        return {'message': 'Invalid credentials'}, 401
