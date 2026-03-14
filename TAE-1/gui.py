import tkinter as tk
from predictor import predict_congestion

def check_traffic():
    try:
        vehicles = int(entry.get())

        prediction, probability = predict_congestion(vehicles)

        if prediction == 1:
            result_label.config(
                text=f"⚠ Congestion Expected\nProbability: {probability:.2f}",
                fg="red"
            )
        else:
            result_label.config(
                text=f"Traffic Normal\nProbability: {probability:.2f}",
                fg="green"
            )

    except ValueError:
        result_label.config(text="Please enter a valid number", fg="black")


window = tk.Tk()
window.title("Intelligent Traffic Congestion Predictor")
window.geometry("400x300")

title = tk.Label(window, text="Traffic Congestion Predictor", font=("Arial", 16))
title.pack(pady=10)

label = tk.Label(window, text="Enter number of vehicles:")
label.pack()

entry = tk.Entry(window)
entry.pack()

predict_button = tk.Button(window, text="Predict Traffic", command=check_traffic)
predict_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

window.mainloop()