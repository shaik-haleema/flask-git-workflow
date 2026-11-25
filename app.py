

from flask import Flask, jsonify, render_template
from flask import Flask, jsonify, render_template, request
from db import collection

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


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():

    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    todo_item = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(todo_item)

    return "To-Do item saved successfully!"



if __name__ == "__main__":
    app.run(debug=True)
