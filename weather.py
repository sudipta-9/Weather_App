def get_weather(location):
    # Static weather data (you can replace this with real data)
    weather_data = {
        "Kolkata": {
            "temperature": "25°C",
            "conditions": "Sunny",
            "humidity": "50%",
            "wind_speed": "10 km/h",
        },
        "New Delhi": {
            "temperature": "18°C",
            "conditions": "Partly Cloudy",
            "humidity": "60%",
            "wind_speed": "15 km/h",
        },
        "Bangalore": {
            "temperature": "30°C",
            "conditions": "Clear",
            "humidity": "45%",
            "wind_speed": "12 km/h",
        },
        "Mumbai": {
            "temperature": "28°C",
            "conditions": "Sunny",
            "humidity": "40%",
            "wind_speed": "8 km/h",
            }
    }
    return weather_data.get(location)

def main():
    print("Welcome to the Simple Weather App!")
    while True:
        location = input("Enter a city or location (or 'quit' to exit): ")
        if location.lower() == 'quit':
            print("Goodbye!")
            break

        weather_info = get_weather(location)
        if weather_info:
            print("\nWeather Information for", location)
            print("Temperature:", weather_info["temperature"])
            print("Conditions:", weather_info["conditions"])
            print("Humidity:", weather_info["humidity"])
            print("Wind Speed:", weather_info["wind_speed"])
        else:
            print(f"Weather information for '{location}' not found. Please enter a valid location.")

if __name__ == "__main__":
    main()
