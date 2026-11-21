
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api")
def get_students():

    with open("data.json", "r") as file:
        students = json.load(file)

    return jsonify(students)


if __name__ == "__main__":
    app.run(debug=True)
