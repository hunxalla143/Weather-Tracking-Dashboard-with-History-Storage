from tabulate import tabulate


def display_weather(data):

    table = [
        ["City", data["city"]],
        ["Temperature", f"{data['temperature']} °C"],
        ["Humidity", f"{data['humidity']} %"],
        ["Condition", data["condition"]],
        ["Wind Speed", f"{data['wind_speed']} km/h"]
    ]

    print()
    print(tabulate(table, tablefmt="grid"))