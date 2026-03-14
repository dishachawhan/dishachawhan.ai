import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model():

    # Load traffic dataset
    data = pd.read_csv("traffic_data.csv")

    # Create congestion label
    # 1 = congestion, 0 = normal traffic
    data["congestion"] = data["vehicles"].apply(lambda x: 1 if x > 250 else 0)

    # Input feature
    X = data[["vehicles"]]

    # Output label
    y = data["congestion"]

    # Create model
    model = LogisticRegression()

    # Train model
    model.fit(X, y)

    return model