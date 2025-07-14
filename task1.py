import requests
import matplotlib.pyplot as plt

API_KEY = "your_api_key_here"  
CITY = "Mumbai"

url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

temps = []
times = []

for entry in data['list'][:8]: 
    temps.append(entry['main']['temp'])
    times.append(entry['dt_txt'])

plt.figure(figsize=(10, 5))
plt.plot(times, temps, marker='o', linestyle='-', color='blue')
plt.title(f"Weather Forecast for {CITY}")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
