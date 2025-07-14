import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Your WeatherAPI key
API_KEY = "52865262be93419ab35171024251407"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

# List of cities to fetch weather data for
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]

# Lists to store weather data
temperatures = []
humidities = []
conditions = []

# Fetch weather data for each city
for city in cities:
    params = {
        "key": API_KEY,
        "q": city
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temperatures.append(data["current"]["temp_c"])
        humidities.append(data["current"]["humidity"])
        conditions.append(data["current"]["condition"]["text"])
    else:
        print(f"Failed to fetch data for {city}: {data.get('error', {}).get('message', 'Unknown error')}")

# Plot 1: Temperature Bar Graph
plt.figure(figsize=(10, 6))
sns.barplot(x=cities, y=temperatures, palette="coolwarm")
plt.title("City-wise Temperature (°C)", fontsize=14)
plt.ylabel("Temperature (°C)")
plt.xlabel("City")
plt.tight_layout()
plt.show()

# Plot 2: Humidity Bar Graph
plt.figure(figsize=(10, 6))
sns.barplot(x=cities, y=humidities, palette="Blues")
plt.title("City-wise Humidity (%)", fontsize=14)
plt.ylabel("Humidity (%)")
plt.xlabel("City")
plt.tight_layout()
plt.show()

# Plot 3: Weather Condition Pie Chart
from collections import Counter

condition_counts = Counter(conditions)
labels = list(condition_counts.keys())
sizes = list(condition_counts.values())

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Weather Condition Distribution", fontsize=14)
plt.axis('equal')
plt.show()
