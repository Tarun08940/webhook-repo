from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime, timezone

app = Flask(__name__)

# MongoDB Atlas connection
MONGO_URI = "mongodb+srv://taruht08_db_user:ZTZgIUloDREhkQjU@cluster0.fl3bewr.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["github_events"]
events = db["events"]


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/webhook", methods=["POST"])
def webhook():
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.json

    data = {
        "author": None,
        "action": event_type,
        "from_branch": None,
        "to_branch": None,
        "timestamp": datetime.now(timezone.utc)
    }

    if event_type == "push":
        data["author"] = payload["pusher"]["name"]
        data["to_branch"] = payload["ref"].split("/")[-1]

    elif event_type == "pull_request":
        pr = payload["pull_request"]
        data["author"] = pr["user"]["login"]
        data["from_branch"] = pr["head"]["ref"]
        data["to_branch"] = pr["base"]["ref"]

    events.insert_one(data)
    return jsonify({"status": "saved"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    result = []

    for e in events.find().sort("timestamp", -1).limit(10):
        ts = e.get("timestamp")

        if isinstance(ts, datetime):
            ts = ts.strftime("%d %b %Y, %I:%M %p UTC")
        else:
            ts = ""

        result.append({
            "author": e.get("author", "Unknown"),
            "action": e.get("action", ""),
            "from_branch": e.get("from_branch", ""),
            "to_branch": e.get("to_branch", ""),
            "timestamp": ts
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
