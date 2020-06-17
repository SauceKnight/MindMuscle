from flask import Blueprint, request
from ..models import Muscle


bp = Blueprint("muscle", __name__, url_prefix="")


@bp.route("/<musclename>")
def get_workouts(musclename):
    muscle = Muscle.query.filter_by(name=musclename).first()
    workoutplans = []
    for plan in muscle.workoutplans:
        workoutplans.append(plan.id)
    data = {}
    data[muscle.id] = {
        "id": muscle.id,
        "name": muscle.name,
        "description": muscle.description,
        "workoutplans": workoutplans
    }
    return {"data": data}
