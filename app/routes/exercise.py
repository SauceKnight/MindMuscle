from flask import Blueprint, request
from ..models import Exercise


bp = Blueprint("workoutplan", __name__, url_prefix="")


@bp.route("/exercises")
def get_workouts(muscleid):
    exercises = Exercise.query.all()
    data = {}
    for exercise in exercises:
        data[exercise.id] = {
            "id": exercise.id,
            "name": exercise.name,
            "description": exercise.description,
        }
    return {"data": data}
