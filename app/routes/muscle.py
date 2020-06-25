from flask import Blueprint, request
from ..models import Muscle


bp = Blueprint("muscle", __name__, url_prefix="")


@bp.route("/<muscleid>")
def get_workouts(muscleid):
    muscle = Muscle.query.filter_by(id=muscleid).first()
    workoutplans = {}
    workoutIds = []
    for plan in muscle.workoutplans:
        workoutplans[plan.name] = {
            "id": plan.id, "name": plan.name, "description": plan.description}
        workoutIds.append(plan.name)
    data = {}
    data = {
        "id": muscle.id,
        "name": muscle.name,
        "description": muscle.description,
        "workoutplans": workoutIds
    }
    return {"data": data, "WorkoutPlans": workoutplans}
