from app.models import Review, User, Muscle, WorkoutPlan, Exercise
from app import app, db
from dotenv import load_dotenv
load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    muscles = [
        Muscle(name="Chest", description="Upper body. Includes workouts involving upper to lower portion of the chest and shoulders as well."),
        Muscle(name="Leg", description="Lower Body. Includes workouts involving hamstrings, quadriceps, thighs, glutes, and calves."),
        Muscle(name="Arm", description="Upper body. Includes workouts involving biceps, triceps, and forearms."),
        Muscle(name="Abs", description="Core body. Includes workouts that interact with the abdominal muscle leading to a strong core/balance."),
        Muscle(name="Back", description="Upper body. Includes workouts involving upper to lower back that help support a stable spine."),
    ]

    for muscle in muscles:
        db.session.add(muscle)

    db.session.commit()

    workoutplans = [
        WorkoutPlan(name="Chest Pump", muscle_id=1, description=""),
        WorkoutPlan(name="BodyWeight Chest", muscle_id=1, description=""),
        WorkoutPlan(name="Chest Strength", muscle_id=1, description=""),
        WorkoutPlan(name="Thigh/Quad Burner", muscle_id=2, description=""),
        WorkoutPlan(name="Leg Strength", muscle_id=2, description=""),
        WorkoutPlan(name="Squat Master", muscle_id=2, description=""),
        WorkoutPlan(name="Bicep Blaster", muscle_id=3, description=""),
        WorkoutPlan(name="Killer Arm", muscle_id=3, description=""),
        WorkoutPlan(name="Stable Core", muscle_id=4, description=""),
        WorkoutPlan(name="Six Pack Shred", muscle_id=4, description=""),
        WorkoutPlan(name="Deadlift Master", muscle_id=5, description=""),
        WorkoutPlan(name="Wings", muscle_id=5, description=""),
    ]

    for workoutplan in workoutplans:
        db.session.add(workoutplan)

    db.session.commit()

    exercises = [
        Exercise(name="Bench Press", workoutplan_id=1,
                 sets=4, reps=8, difficulty=Beginner),
        Exercise(name="Chest Fly", workoutplan_id=1,
                 sets=3, reps=12, difficulty=Intermediate),
        Exercise(name="Incline Bench Press", workoutplan_id=1,
                 sets=3, reps=6, difficulty=Advanced),
        Exercise(name="BodyWeight Push-Ups", workoutplan_id=1,
                 sets=3, reps=10, difficulty=Beginner),
        Exercise(name="Push-Ups", workoutplan_id=2,
                 sets=3, reps=10, difficulty=Beginner),
        Exercise(name="Chest Dips", workoutplan_id=2,
                 sets=3, reps=10, difficulty=Intermediate),
        Exercise(name="Wide Grip Push-Ups", workoutplan_id=2,
                 sets=3, reps=8, difficulty=Advanced),
        Exercise(name="Band Chest Fly", workoutplan_id=2,
                 sets=3, reps=12, difficulty=Intermediate),
        Exercise(name="Bench Press", workoutplan_id=3,
                 sets=4, reps=5, difficulty=Beginner),
        Exercise(name="Close Grip Bench Press", workoutplan_id=3,
                 sets=2, reps=8, difficulty=Intermediate),
        Exercise(name="Decline DB Press", workoutplan_id=3,
                 sets=3, reps=10, difficulty=Advanced),
        Exercise(name="Incline DB Press", workoutplan_id=3,
                 sets=4, reps=6, difficulty=Advanced),
        Exercise(name="Squat", workoutplan_id=4, sets=3,
                 reps=12, difficulty=Intermediate),
        Exercise(name="Leg Press", workoutplan_id=4,
                 sets=4, reps=8, difficulty=Beginner),
        Exercise(name="Leg Lunges", workoutplan_id=4,
                 sets=3, reps=10, difficulty=Advanced),
        Exercise(name="Goblin Squat", workoutplan_id=4,
                 sets=3, reps=8, difficulty=Intermediate),
        Exercise(name="Squat", workoutplan_id=5, sets=4,
                 reps=5, difficulty=Intermediate),
        Exercise(name="Leg Press", workoutplan_id=5,
                 sets=3, reps=8, difficulty=Beginner),
        Exercise(name="Leg Curls", workoutplan_id=5,
                 sets=3, reps=10, difficulty=Intermediate),
        Exercise(name="Leg Extension", workoutplan_id=5,
                 sets=3, reps=10, difficulty=Intermediate),
        Exercise(name="Squat", workoutplan_id=6, sets=4,
                 reps=10, difficulty=Intermediate),
        Exercise(name="Goblin Squat", workoutplan_id=6,
                 sets=3, reps=12, difficulty=Intermediate),
        Exercise(name="Front Squat", workoutplan_id=6,
                 sets=4, reps=8, difficulty=Advanced),
        Exercise(name="DB Squat", workoutplan_id=6,
                 sets=3, reps=10, difficulty=Beginner),
        Exercise(name="Barbell Curl", workoutplan_id=7,
                 sets=3, reps=12, difficulty=Intermediate),
        Exercise(name="DB Curl", workoutplan_id=7,
                 sets=3, reps=15, difficulty=Beginner),
        Exercise(name="Hammer Curl", workoutplan_id=7,
                 sets=3, reps=15, difficulty=Intermediate),
        Exercise(name="Cable Curl", workoutplan_id=7,
                 sets=3, reps=10, difficulty=Intermediate),
        Exercise(name="DB Curls", workoutplan_id=8,
                 sets=3, reps=12, difficulty=Beginner),
        Exercise(name="Tricep Extension", workoutplan_id=8,
                 sets=3, reps=15, difficulty=Beginner),
        Exercise(name="Hammer Curls", workoutplan_id=8,
                 sets=3, reps=10, difficulty=Intermediate),
        Exercise(name="Skull Crushes", workoutplan_id=8,
                 sets=3, reps=8, difficulty=Advanced),
        Exercise(name="Crunches", workoutplan_id=9,
                 sets=3, reps=25, difficulty=Beginner),
        Exercise(name="Mountain Climbers", workoutplan_id=9,
                 sets=3, reps=15, difficulty=Intermediate),
        Exercise(name="Knee Touches", workoutplan_id=9,
                 sets=3, reps=12, difficulty=Advanced),
        Exercise(name="Crunches", workoutplan_id=10,
                 sets=4, reps=20, difficulty=Beginner),
        Exercise(name="Toe Touches", workoutplan_id=10,
                 sets=4, reps=15, difficulty=Intermediate),
        Exercise(name="Leg Lifts", workoutplan_id=10,
                 sets=4, reps=15, difficulty=Intermediate),
        Exercise(name="Deadlift", workoutplan_id=11,
                 sets=4, reps=6, difficulty=Intermediate),
        Exercise(name="Sumo Deadlift", workoutplan_id=11,
                 sets=4, reps=6, difficulty=Advanced),
        Exercise(name="Romanian Deadlift", workoutplan_id=11,
                 sets=3, reps=10, difficulty=Advanced),
        Exercise(name="Deadlift", workoutplan_id=12,
                 sets=4, reps=8, difficulty=Intermediate),
        Exercise(name="Lat Pulldown", workoutplan_id=12,
                 sets=3, reps=12, difficulty=Intermediate),
        Exercise(name="One Arm Row", workoutplan_id=12,
                 sets=3, reps=12, difficulty=Beginner),
    ]

    for exercise in exercises:
        db.session.add(exercise)

    db.session.commit()
