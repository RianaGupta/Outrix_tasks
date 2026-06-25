import tkinter as tk 
import requests


root=tk.Tk()
root.configure(bg="lightblue")
root.title("Weather App")
root.geometry("700x700")
title=tk.Label(root,text="Weather App" ,bg="black", fg="#4FC3F7", font=("arial",16,"bold","italic"))
title.pack(pady=40)


def get_weather():
    print("Button clicked")
    city = city_entry.get()
    # print(city)
   
    API_KEY = "8a1dfd782f21e3b9574134863e34d59d"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get("cod") != 200:
        result_label.config(text="City not found!")
    
    # print(data)
    
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]


    emoji = "🌤"
    if "clear" in condition:
        emoji = "☀️"

    elif "cloud" in condition:
        emoji = "☁️"

    elif "rain" in condition:
        emoji = "🌧"

    elif "thunderstorm" in condition:
        emoji = "⛈"

    elif "snow" in condition:
        emoji = "❄️"

    elif "mist" in condition:
        emoji = "🌫"

    print("TEMP =", temp)
    print("HUMIDITY =", humidity)
    print("CONDITION =", condition)

    result_label.config(
        text=f"{emoji}{condition}\nTemperature: {temp}°C\nHumidity: {humidity}%"
    )
city_entry = tk.Entry(root,width=30,font=("Arial",14),bg="#1E1E1E",fg="white")
city_entry.pack(pady=30)

button=tk.Button(root,text="Get Weather" , command=get_weather,bg="#4FC3F7",
    fg="black",
    font=("Arial", 11, "bold"))
button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    bg="lightblue",
    fg="white",
    font=(20)
)
result_label.pack(pady=10)

root.mainloop()
