import random
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Generate random weather data
def generateWeatherData(n: int) -> list[tuple[int, str, str, str]]:
    cities = ['Tokyo', 'Osaka', 'Nagoya', 'Sapporo', 'Fukuoka', 'Kobe', 'Kyoto', 'Yokohama', 'Sendai', 'Hiroshima']
    weather_data = []
    for i in range(n):
        temperature = random.randint(-30, 50)  # Random temperature between -30 and 50 degrees Celsius
        condition = random.choice(['Sunny', 'Rainy', 'Cloudy', 'Snowy'])
        city = random.choice(cities)
        time = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d %H:%M:%S')
        weather_data.append((temperature, condition, city, time))
    return weather_data

# Insertion Sort implementation
def insertionSort(arr: list[tuple[int, str, str, str]]) -> tuple[list[tuple[int, str, str, str]], int]:
    operations = 0
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            operations += 1
            if arr[j][0] < arr[j - 1][0]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr, operations

# Generate and sort weather data
weather_data = generateWeatherData(100)
sorted_weather_data, operations = insertionSort(weather_data)

# Print sorted weather data
for data in sorted_weather_data:
    print(data)

# Plot the number of operations
plt.figure(figsize=(10, 6))
plt.plot(range(1, 101), [data[0] for data in sorted_weather_data], marker='o', linestyle='-', color='b')
plt.title('Sorted Weather Data')
plt.xlabel('Index')
plt.ylabel('Temperature')
plt.grid(True)
plt.show()

# Verify stability
is_stable = True
for i in range(1, len(sorted_weather_data)):
    if sorted_weather_data[i][0] == sorted_weather_data[i - 1][0]:
        if weather_data.index(sorted_weather_data[i]) < weather_data.index(sorted_weather_data[i - 1]):
            is_stable = False
            break

print(f"Insertion Sort is {'stable' if is_stable else 'not stable'}")
