from flask import Flask, render_template, request
from predictor import predict_congestion

app = Flask(__name__)

# Sample traffic trend data for graph
traffic_times = ["8AM", "9AM", "10AM", "11AM", "12PM", "1PM", "2PM"]
traffic_values = [120, 200, 340, 300, 450, 380, 260]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predictor", methods=["GET", "POST"])
def predictor():

    result = None

    if request.method == "POST":
        bikes = int(request.form["bikes"])
        cars = int(request.form["cars"])
        buses = int(request.form["buses"])
        trucks = int(request.form["trucks"])

        result = predict_congestion(bikes, cars, buses, trucks)

    return render_template(
        "predictor.html",
        result=result,
        times=traffic_times,
        values=traffic_values
    )


if __name__ == "__main__":
    app.run(debug=True)