from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, User, Habit, HabitLog, Challenge, UserChallenge

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init extensions
db.init_app(app)
CORS(app)
migrate = Migrate(app, db)


# -------- HELPERS --------
def user_to_dict(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }

def habit_to_dict(habit):
    return {
        "id": habit.id,
        "user_id": habit.user_id,
        "title": habit.title,
        "description": habit.description,
        "frequency": habit.frequency,
        "start_date": habit.start_date
    }

def habitlog_to_dict(log):
    return {
        "id": log.id,
        "habit_id": log.habit_id,
        "date": log.date,
        "status": log.status,
        "note": log.note
    }

def challenge_to_dict(chal):
    return {
        "id": chal.id,
        "title": chal.title,
        "description": chal.description,
        "start_date": chal.start_date,
        "end_date": chal.end_date
    }

def userchallenge_to_dict(uc):
    return {
        "id": uc.id,
        "user_id": uc.user_id,
        "challenge_id": uc.challenge_id,
        "progress": uc.progress
    }


# -------- ROUTES --------
@app.route("/users", methods=["GET","POST"])
def users():
    if request.method == "GET":
        return jsonify([user_to_dict(u) for u in User.query.all()])
    data = request.json
    user = User(name=data["name"], email=data["email"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user_to_dict(user)), 201


@app.route("/habits", methods=["GET","POST"])
def habits():
    if request.method == "GET":
        return jsonify([habit_to_dict(h) for h in Habit.query.all()])
    data = request.json
    habit = Habit(
        user_id=data["user_id"],
        title=data["title"],
        description=data.get("description"),
        frequency=data["frequency"],
        start_date=data["start_date"]
    )
    db.session.add(habit)
    db.session.commit()
    return jsonify(habit_to_dict(habit)), 201


@app.route("/habits/<int:id>", methods=["PATCH","DELETE"])
def habit_detail(id):
    habit = Habit.query.get_or_404(id)
    if request.method == "PATCH":
        data = request.json
        habit.title = data.get("title", habit.title)
        habit.description = data.get("description", habit.description)
        habit.frequency = data.get("frequency", habit.frequency)
        habit.start_date = data.get("start_date", habit.start_date)
        db.session.commit()
        return jsonify(habit_to_dict(habit))
    else:
        db.session.delete(habit)
        db.session.commit()
        return jsonify({"message": "Habit deleted"})


@app.route("/habit-logs", methods=["GET","POST"])
def habit_logs():
    if request.method == "GET":
        return jsonify([habitlog_to_dict(l) for l in HabitLog.query.all()])
    data = request.json
    log = HabitLog(
        habit_id=data["habit_id"],
        date=data["date"],
        status=data["status"],
        note=data.get("note")
    )
    db.session.add(log)
    db.session.commit()
    return jsonify(habitlog_to_dict(log)), 201


@app.route("/challenges", methods=["GET","POST"])
def challenges():
    if request.method == "GET":
        return jsonify([challenge_to_dict(c) for c in Challenge.query.all()])
    data = request.json
    chal = Challenge(
        title=data["title"],
        description=data.get("description"),
        start_date=data["start_date"],
        end_date=data["end_date"]
    )
    db.session.add(chal)
    db.session.commit()
    return jsonify(challenge_to_dict(chal)), 201


@app.route("/user-challenges", methods=["GET","POST"])
def user_challenges():
    if request.method == "GET":
        return jsonify([userchallenge_to_dict(uc) for uc in UserChallenge.query.all()])
    data = request.json
    uc = UserChallenge(
        user_id=data["user_id"],
        challenge_id=data["challenge_id"],
        progress=data.get("progress", 0)
    )
    db.session.add(uc)
    db.session.commit()
    return jsonify(userchallenge_to_dict(uc)), 201


@app.route("/user-challenges/<int:id>", methods=["PATCH"])
def update_user_challenge(id):
    uc = UserChallenge.query.get_or_404(id)
    data = request.json
    uc.progress = data.get("progress", uc.progress)
    db.session.commit()
    return jsonify(userchallenge_to_dict(uc))

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email, password=password).first()
    if user:
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        }), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

# -------- RUN --------
if __name__ == "__main__":
    app.run(debug=True)
