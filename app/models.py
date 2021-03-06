from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from sqlalchemy import Table

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    def check_password(self, password):
        return check_password_hash(self.password, password)

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    privilage = db.Column(db.String(50), nullable=False)
    reviews_by_user = db.relationship("Review", back_populates="user_review")


class Muscle(db.Model):
    __tablename__ = "muscles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(50), nullable=False, unique=True)

    workoutplans = db.relationship("WorkoutPlan", back_populates="muscle")


class WorkoutPlan(db.Model):
    __tablename__ = "workoutplans"

    id = db.Column(db.Integer, primary_key=True)
    muscle_id = db.Column(db.Integer, db.ForeignKey(
        "muscles.id"), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(300))

    muscle = db.relationship("Muscle", back_populates="workoutplans")
    exercises = db.relationship("Exercise", back_populates="workoutplan")
    reviews = db.relationship("Review", back_populates="workoutplan_review")


class Exercise(db.Model):
    __tablename__ = "exercises"
    id = db.Column(db.Integer, primary_key=True)
    workoutplan_id = db.Column(db.Integer, db.ForeignKey(
        "workoutplans.id"), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200))
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(200))

    workoutplan = db.relationship("WorkoutPlan", back_populates="exercises")


class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    workoutplan_id = db.Column(db.Integer, db.ForeignKey(
        "workoutplans.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)
    review = db.Column(db.String(300))

    workoutplan_review = db.relationship(
        "WorkoutPlan", back_populates="reviews")
    user_review = db.relationship("User", back_populates="reviews_by_user")
