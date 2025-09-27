from app import app, db
from models import User, Habit, HabitLog, Challenge, UserChallenge

# Run everything inside the app context
with app.app_context():
    # Drop all tables and recreate
    db.drop_all()
    db.create_all()

    # -------- Users --------
    user1 = User(name="Alice", email="alice@example.com", password="password123")
    user2 = User(name="Bob", email="bob@example.com", password="password456")
    db.session.add_all([user1, user2])
    db.session.commit()

    # -------- Habits --------
    habit1 = Habit(user_id=user1.id, title="Morning Jog", description="Jog every morning", frequency="daily", start_date="2025-09-27")
    habit2 = Habit(user_id=user2.id, title="Read Book", description="Read 30 minutes", frequency="daily", start_date="2025-09-27")
    db.session.add_all([habit1, habit2])
    db.session.commit()

    # -------- Habit Logs --------
    log1 = HabitLog(habit_id=habit1.id, date="2025-09-27", status="done", note="Felt great!")
    log2 = HabitLog(habit_id=habit2.id, date="2025-09-27", status="not done", note="Too tired")
    db.session.add_all([log1, log2])
    db.session.commit()

    # -------- Challenges --------
    chal1 = Challenge(title="30-Day Fitness", description="Complete daily workouts for 30 days", start_date="2025-09-01", end_date="2025-09-30")
    chal2 = Challenge(title="Reading Challenge", description="Read 5 books in a month", start_date="2025-09-01", end_date="2025-09-30")
    db.session.add_all([chal1, chal2])
    db.session.commit()

    # -------- User Challenges --------
    uc1 = UserChallenge(user_id=user1.id, challenge_id=chal1.id, progress=10)
    uc2 = UserChallenge(user_id=user2.id, challenge_id=chal2.id, progress=20)
    db.session.add_all([uc1, uc2])
    db.session.commit()

    print("🌱 Database seeded successfully!")
