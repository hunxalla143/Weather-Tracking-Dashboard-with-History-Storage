import time

from modules.weather_api import get_weather
from modules.storage import save_weather
from modules.storage import load_history

from modules.utils import display_weather

from modules.alerts import weather_alert

from modules.analytics import (
    show_statistics,
    city_filter,
    plot_temperature_trend
)


def get_weather_menu():

    city = input(
        "\nEnter City Name: "
    ).strip()

    data = get_weather(city)

    if not data:
        return

    display_weather(data)

    save_weather(data)

    alerts = weather_alert(data)

    if alerts:

        print("\nWEATHER ALERTS")

        for alert in alerts:
            print(f"⚠ {alert}")


def view_history():

    history = load_history()

    if history.empty:
        print("No History Available")
        return

    print(history)


def analysis_menu():

    while True:

        print("""
1. Statistics
2. Filter By City
3. Temperature Trend
4. Back
""")

        choice = input("Choice: ")

        if choice == "1":
            show_statistics()

        elif choice == "2":
            city = input(
                "Enter City: "
            )
            city_filter(city)

        elif choice == "3":
            plot_temperature_trend()

        elif choice == "4":
            break


def multi_city_tracking():

    cities = input(
        "Enter cities separated by commas: "
    )

    city_list = [
        city.strip()
        for city in cities.split(",")
    ]

    for city in city_list:

        data = get_weather(city)

        if data:

            display_weather(data)

            save_weather(data)


def auto_refresh():

    city = input("City: ")

    interval = int(
        input("Refresh interval (seconds): ")
    )

    try:

        while True:

            data = get_weather(city)

            if data:

                display_weather(data)

                save_weather(data)

            time.sleep(interval)

    except KeyboardInterrupt:

        print("\nStopped.")


def menu():

    while True:

        print("""
====================================
 WEATHER TRACKING DASHBOARD
====================================

1. Get Weather
2. View History
3. Analyze Data
4. Multi-City Tracking
5. Auto Refresh
6. Exit
""")

        choice = input(
            "Enter Choice: "
        )

        if choice == "1":
            get_weather_menu()

        elif choice == "2":
            view_history()

        elif choice == "3":
            analysis_menu()

        elif choice == "4":
            multi_city_tracking()

        elif choice == "5":
            auto_refresh()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()