from flask import Blueprint, request
from ..models import Exercise


bp = Blueprint("exercise", __name__, url_prefix="")


@bp.route("/<workoutid>/exercises")
def get_workouts(workoutid):
    exercises = Exercise.query.filter_by(workoutplan_id=workoutid).all()
    data = {}
    for exercise in exercises:
        data[exercise.id] = {
            "id": exercise.id,
            "name": exercise.name,
            "description": exercise.description,
            "sets": exercise.sets,
            "reps": exercise.reps
        }
    return {"data": data}
