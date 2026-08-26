import tkinter as tk
from tkinter import messagebox
import requests



API_KEY = "58ff4d11b02b37d1178c9a9e6cf82512"

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"




def get_weather():

    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a city name."
        )
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        current_data = requests.get(
            CURRENT_URL,
            params=params,
            timeout=10
        ).json()

        forecast_data = requests.get(
            FORECAST_URL,
            params=params,
            timeout=10
        ).json()


        if current_data["cod"] != 200:
            messagebox.showerror(
                "Error",
                current_data["message"]
            )
            return



        temperature = current_data["main"]["temp"]
        humidity = current_data["main"]["humidity"]
        wind = current_data["wind"]["speed"]
        pressure = current_data["main"]["pressure"]

        precipitation = forecast_data["list"][0]["pop"] * 100



        temperature_label.config(
            text=f"Temperature : {temperature:.1f} °C"
        )

        humidity_label.config(
            text=f"Humidity : {humidity}%"
        )

        wind_label.config(
            text=f"Wind Speed : {wind:.1f} m/s"
        )

        pressure_label.config(
            text=f"Pressure : {pressure} hPa"
        )

        precipitation_label.config(
            text=f"Precipitation : {precipitation:.0f}%"
        )


    except requests.exceptions.ConnectionError:

        messagebox.showerror(
            "Error",
            "No internet connection."
        )

    except requests.exceptions.Timeout:

        messagebox.showerror(
            "Error",
            "Request timed out."
        )

    except Exception:

        messagebox.showerror(
            "Error",
            "Unable to retrieve weather data."
        )



window = tk.Tk()

window.title("Weather Application")

window.geometry("450x330")

window.resizable(False, False)
icon_imge = tk.PhotoImage(file="icon.png")
window.iconphoto(True,icon_imge)





BG = "#DFF6FF"
ENTRY_COLOR = "#FFFFFF"
BUTTON_COLOR = "#457EC4"
BUTTON_ACTIVE = "#93C5FD"


window.config(bg=BG)



title = tk.Label(
    window,
    text="Weather Application",
    font=("Arial", 18, "bold"),
    bg=BG,
    fg="#0F172A"
)

title.grid(
    row=0,
    column=0,
    columnspan=3,
    pady=15
)


location_label = tk.Label(
    window,
    text="Location :",
    font=("Arial", 11, "bold"),
    bg=BG,
    fg="#0F172A"
)

location_label.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)



city_entry = tk.Entry(
    window,
    width=22,
    font=("Arial", 12),
    bg=ENTRY_COLOR,
    relief="solid"
)

city_entry.grid(
    row=1,
    column=1,
    padx=5,
    pady=10
)



search_button = tk.Button(
    window,
    text="Search",
    command=get_weather,
    bg=BUTTON_COLOR,
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    width=10,
    relief="flat"
)

search_button.grid(
    row=1,
    column=2,
    padx=10,
    pady=10
)


temperature_label = tk.Label(
    window,
    text="Temperature : --",
    font=("Arial", 11),
    bg=BG
)

temperature_label.grid(
    row=2,
    column=0,
    columnspan=3,
    sticky="w",
    padx=30,
    pady=5
)



humidity_label = tk.Label(
    window,
    text="Humidity : --",
    font=("Arial", 11),
    bg=BG
)

humidity_label.grid(
    row=3,
    column=0,
    columnspan=3,
    sticky="w",
    padx=30,
    pady=5
)



wind_label = tk.Label(
    window,
    text="Wind Speed : --",
    font=("Arial", 11),
    bg=BG
)

wind_label.grid(
    row=4,
    column=0,
    columnspan=3,
    sticky="w",
    padx=30,
    pady=5
)



pressure_label = tk.Label(
    window,
    text="Pressure : --",
    font=("Arial", 11),
    bg=BG
)

pressure_label.grid(
    row=5,
    column=0,
    columnspan=3,
    sticky="w",
    padx=30,
    pady=5
)



precipitation_label = tk.Label(
    window,
    text="Precipitation : --",
    font=("Arial", 11),
    bg=BG
)

precipitation_label.grid(
    row=6,
    column=0,
    columnspan=3,
    sticky="w",
    padx=30,
    pady=5
)

window.mainloop()