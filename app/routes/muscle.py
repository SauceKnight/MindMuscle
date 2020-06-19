from flask import Blueprint, request
from ..models import Muscle


bp = Blueprint("muscle", __name__, url_prefix="")


@bp.route("/<musclename>")
def get_workouts(musclename):
    muscle = Muscle.query.filter_by(name=musclename).first()
    workoutplans = {}
    workoutIds = []
    for plan in muscle.workoutplans:
        workoutplans[plan.id] = {
            "id": plan.id, "name": plan.name, "description": plan.description}
        workoutIds.append(plan.id)
    data = {}
    data[muscle.id] = {
        "id": muscle.id,
        "name": muscle.name,
        "description": muscle.description,
        "workoutplans": workoutIds
    }
    return {"data": data, "WorkoutPlans": workoutplans}
