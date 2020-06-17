from flask import Blueprint, request
from ..models import WorkoutPlan


bp = Blueprint("workoutplan", __name__, url_prefix="")


@bp.route("/<muscleid>/workoutplans")
def get_workouts(muscleid):
    workoutplans = WorkoutPlan.query.filter_by(muscle_id=muscleid).all()
    data = {}
    for workout in workoutplans:
        data[workout.id] = {
            "id": workout.id,
            "name": workout.name,
            "description": workout.description,
            "muscle": workout.muscle.name
        }
    return {"data": data}
