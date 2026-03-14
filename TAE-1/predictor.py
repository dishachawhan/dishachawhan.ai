import pandas as pd

# Vehicle weights based on road impact
weights = {
    "bike": 1,
    "car": 2,
    "bus": 4,
    "truck": 5
}


def predict_congestion(bikes, cars, buses, trucks):

    total = bikes + cars + buses + trucks

    if total == 0:
        return "No Traffic Data"

    bike_ratio = bikes / total
    car_ratio = cars / total
    bus_ratio = buses / total
    truck_ratio = trucks / total

    score = (
        bike_ratio * weights["bike"] +
        car_ratio * weights["car"] +
        bus_ratio * weights["bus"] +
        truck_ratio * weights["truck"]
    )

    if score > 2.5:
        return "Heavy Congestion"
    elif score > 1.5:
        return "Moderate Traffic"
    else:
        return "Low Traffic"