import requests


def get_weather(city):
    """
    Fetch weather data from wttr.in
    """

    try:
        city = city.strip()

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if response.status_code != 200:
            print("Unable to fetch weather.")
            return None

        data = response.json()

        current = data["current_condition"][0]

        weather_data = {
            "city": city.title(),
            "temperature": float(current["temp_C"]),
            "humidity": int(current["humidity"]),
            "condition": current["weatherDesc"][0]["value"],
            "wind_speed": float(current["windspeedKmph"])
        }

        return weather_data

    except requests.exceptions.ConnectionError:
        print("No Internet Connection.")
        return None

    except requests.exceptions.Timeout:
        print("Request Timeout.")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None