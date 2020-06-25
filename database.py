from app.models import Review, User, Muscle, WorkoutPlan, Exercise
from app import app, db
from dotenv import load_dotenv
load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    muscles = [
        Muscle(name="Chest", description="Pectoralis Major"),
        Muscle(name="Legs", description="Hamstrings, Thights, and calves"),
    ]

    for muscle in muscles:
        db.session.add(muscle)

    db.session.commit()
