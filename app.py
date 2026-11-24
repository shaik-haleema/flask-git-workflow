
from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/api")
def get_students():

    with open("data.json", "r") as file:
        students = json.load(file)

    return jsonify(students)

@app.route("/todo")
def todo():
    return render_template("todo.html")


if __name__ == "__main__":
    app.run(debug=True)
