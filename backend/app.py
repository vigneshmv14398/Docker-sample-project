from flask import Flask, request, jsonify
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)
r = redis.Redis(host="redis", port=6379, db=0)

@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    choice = data.get("choice")
    if choice not in ["cats", "dogs"]:
        return jsonify({"error": "Invalid choice"}), 400
    r.incr(choice)
    return jsonify({"message": f"Vote for {choice} added!"})

@app.route("/results", methods=["GET"])
def results():
    cats = int(r.get("cats") or 0)
    dogs = int(r.get("dogs") or 0)
    return jsonify({"cats": cats, "dogs": dogs})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
