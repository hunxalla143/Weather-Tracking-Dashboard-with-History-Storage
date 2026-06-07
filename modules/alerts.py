def weather_alert(record):

    alerts = []

    condition = record["condition"].lower()

    if "rain" in condition:
        alerts.append("Rain Alert")

    if "storm" in condition:
        alerts.append("Storm Warning")

    if record["temperature"] > 40:
        alerts.append("Extreme Heat Warning")

    if record["temperature"] < 5:
        alerts.append("Cold Weather Warning")

    return alerts