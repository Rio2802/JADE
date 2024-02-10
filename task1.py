import requests

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"
    querystring = {
        "location": city,
        "format": "json",
        "u": "f"
    }
    headers = {
        "X-RapidAPI-Key": "db49b0079amshec40358b0ec4568p1c9f55jsn0a3fee6c5c38",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com" 
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise error for bad response status
        data = response.json()  # Parse JSON response

        location = data.get("location")
        if location:
            print(f"Weather information for {location.get('city')}, {location.get('country')}:")

        current_observation = data.get("current_observation")
        if current_observation:
            temperature = current_observation.get("condition", {}).get("temperature")
            condition = current_observation.get("condition", {}).get("text")
            print(f"The current temperature is {temperature}°F with {condition}.")

            atmosphere = current_observation.get("atmosphere")
            if atmosphere:
                humidity = atmosphere.get("humidity")
                print(f"The humidity is {humidity}%.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    temp_city("Mumbai")
