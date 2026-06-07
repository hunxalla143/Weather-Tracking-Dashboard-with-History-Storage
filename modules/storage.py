import os
import json
import pandas as pd
from datetime import datetime

CSV_FILE = "data/weather_history.csv"
JSON_FILE = "data/weather_history.json"


def save_weather(data):

    os.makedirs("data", exist_ok=True)

    data["timestamp"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    df = pd.DataFrame([data])

    if os.path.exists(CSV_FILE):
        df.to_csv(
            CSV_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(CSV_FILE, index=False)

    save_json(data)


def save_json(record):

    history = []

    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as file:
                history = json.load(file)
        except:
            history = []

    history.append(record)

    with open(JSON_FILE, "w") as file:
        json.dump(history, file, indent=4)


def load_history():

    if not os.path.exists(CSV_FILE):
        return pd.DataFrame()

    return pd.read_csv(CSV_FILE)