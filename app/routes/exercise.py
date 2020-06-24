from flask import Blueprint, request
from ..models import Exercise, WorkoutPlan, Review


bp = Blueprint("exercise", __name__, url_prefix="")


@bp.route("/<workoutid>/exercises")
def get_workouts(workoutid):
    exercises = Exercise.query.filter_by(workoutplan_id=workoutid).all()
    reviews = Review.query.filter_by(
        workoutplan_id=workoutid).all()
    data = {}
    review_data = {}
    for exercise in exercises:
        data[exercise.id] = {
            "id": exercise.id,
            "name": exercise.name,
            "description": exercise.description,
            "sets": exercise.sets,
            "reps": exercise.reps,
            "difficulty": exercise.difficulty,
        }
    for user_review in reviews:
        review_data[user_review.id] = {
            "id": user_review.id,
            "review": user_review.review,
            "user": user_review.user_review.username
        }
    selectedWorkout = {}
    selectedWorkout["SelectedWorkout"] = workoutid
    return {"data": data, "review": review_data, "SelectedWorkout": selectedWorkout}
