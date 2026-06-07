import pandas as pd
import matplotlib.pyplot as plt


def show_statistics():

    try:
        df = pd.read_csv(
            "data/weather_history.csv"
        )

        print("\n===== WEATHER ANALYSIS =====")

        print(
            f"Average Temp: "
            f"{df['temperature'].mean():.2f} °C"
        )

        print(
            f"Highest Temp: "
            f"{df['temperature'].max():.2f} °C"
        )

        print(
            f"Lowest Temp: "
            f"{df['temperature'].min():.2f} °C"
        )

    except:
        print("No data available.")


def city_filter(city):

    try:
        df = pd.read_csv(
            "data/weather_history.csv"
        )

        result = df[
            df["city"].str.lower()
            == city.lower()
        ]

        print(result)

    except:
        print("No records found.")


def plot_temperature_trend():

    try:
        df = pd.read_csv(
            "data/weather_history.csv"
        )

        plt.figure(figsize=(10, 5))

        plt.plot(
            df.index,
            df["temperature"],
            marker="o"
        )

        plt.title(
            "Temperature Trend"
        )

        plt.xlabel("Record")
        plt.ylabel("Temperature °C")

        plt.grid(True)

        plt.show()

    except:
        print("No data available.")