from time import strftime
from tkinter import *
import datetime
import requests
import json
from PIL import ImageTk, Image
from dotenv import load_dotenv
import os


window = Tk()
window.geometry('500x700')
window.title('Weather App')
window.iconphoto(True, PhotoImage(file='Icons/appIcon.png'))
window.configure(background='#e0f6fb')
window.resizable(False, False)

# API key
load_dotenv()
api_key = os.getenv('API_KEY') #instead of this enter your api key here if needed

# Global image reference
current_weather_image = None
weather_label = Label(window, background='#e0f6fb')
weather_label.place(x=230, y=240)


# Change weather image function
def weather_image(image_path="Images/weather.png"):
    global current_weather_image
    img = Image.open(image_path)
    resized = img.resize((250, 250))
    current_weather_image = ImageTk.PhotoImage(resized)
    weather_label.config(image=current_weather_image)


weather_image("Images/weather.png")

# Downloading weather data and displaying
def load_weather_data():
    try:
        update_time()

        # API request
        api_request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_entry.get()}&appid={api_key}&units=metric"
        )

        if api_request.status_code != 200:
            city_entry.delete(0, END)
            city_entry.insert(0, "Error: city not found")
            return

        api = json.loads(api_request.content)

        # Extracting weather data from json
        current_temperature = api['main']['temp']
        feels_like = api['main']['feels_like']
        temp_max = api['main']['temp_max']
        temp_min = api['main']['temp_min']
        humidity = api['main']['humidity']
        pressure = api['main']['pressure']
        wind_speed = api['wind']['speed']
        weather = api['weather'][0]['id']
        description = api['weather'][0]['description']
        city = api['name']

        # Updating labels with data
        city_label.config(text=city)
        temperature_label.config(text=f"{round(current_temperature)}°")
        feels_like_label.config(text=f"Feels like: {round(feels_like)}°C")
        mintemp_label.config(text=f"Min temp: {int(temp_min)}°C")
        maxtemp_label.config(text=f"Max temp: {int(temp_max)}°C")
        hum_data.config(text=f"{int(humidity)}%")
        wind_data.config(text=f"{int(wind_speed)} km/h")
        pressure_data.config(text=f"{int(pressure)} hPa")
        desc_label.config(text=description)

        # Changing weather images
        if 200 <= weather <= 321:
            image_path = "Images/rain.png"
        elif 600 <= weather <= 622:
            image_path = "Images/snowy.png"
        elif 701 <= weather <= 781:
            image_path = "Images/mist.png"
        elif weather == 800:
            if 8 <= int(dt.strftime('%H')) <= 18:
                image_path = "Images/sunny.png"
            else:
                image_path = "Images/clear_night.png"
        elif weather == 801:
            image_path = "Images/littleCloudy.png"
        elif 802 <= weather <= 804:
            image_path = "Images/cloudy.png"
        else:
            image_path = "Images/weather.png"

        weather_image(image_path)

    except requests.exceptions.RequestException as e:
        city_entry.delete(0, END)
        city_entry.insert(0, "Connection error")
        print(f"Error: {e}")

    except KeyError as e:
        city_entry.delete(0, END)
        city_entry.insert(0, "Data error")
        print(f"API response error: {e}")


# Time update function
def update_time():
    current_time = strftime("%H:%M")
    hour.config(text=current_time)


# City name entry
city_name = StringVar()
city_entry = Entry(window,
                   font=('Arial', 14),
                   borderwidth=2,
                   textvariable=city_name)
city_entry.grid(row=0, column=0, columnspan=2, padx=25, pady=30, sticky=W, ipady=6, ipadx=70)

# Search button
searchIcon = PhotoImage(file='Icons/search.png')
search_button = Button(window,
                       image=searchIcon,
                       borderwidth=0,
                       bg='#e0f6fb',
                       command=load_weather_data)
search_button.grid(row=0, column=2, padx=0, pady=10, sticky=W)

# Date and hour
dt = datetime.datetime.now()
date_num = Label(window, text=dt.strftime('%d-%m-%Y'), font=('Arial', 18), bg='#e0f6fb')
date_day = Label(window, text=dt.strftime('%A'), font=('Arial', 18), bg='#e0f6fb')
hour = Label(window, text=dt.strftime('%H:%M'), font=('Arial', 18), bg='#e0f6fb')
date_num.place(x=360, y=100)
date_day.place(x=380, y=130)
hour.place(x=390, y=160)

# City name label
city_label = Label(window,
                   text="City",
                   font=('Arial', 32, 'bold'),
                   bg='#e0f6fb')
city_label.grid(row=2, column=0, columnspan=2, padx=20, pady=15, sticky=W)

# Temperature
temperature_label = Label(window, text="...°", font=('Arial', 76), bg='#e0f6fb')
temperature_label.grid(row=3, column=0, columnspan=2, padx=70, pady=5, sticky=W)

# Weather description
desc_label = Label(window, text="...", font=('Arial', 16, 'italic'), bg='#e0f6fb')
desc_label.grid(row=4, column=0, columnspan=2, padx=20, pady=15, sticky=W)

# Feels like temperature
feels_like_label = Label(window, text="Feels like: ", font=('Arial', 14, 'bold'), bg='#e0f6fb')
feels_like_label.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky=W)

# Min temperature
mintemp_label = Label(window, text="Min. temp: ", font=('Arial', 14, 'bold'), bg='#e0f6fb')
mintemp_label.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky=W)

# Max temperature
maxtemp_label = Label(window, text="Max. temp: ", font=('Arial', 14, 'bold'), bg='#e0f6fb')
maxtemp_label.grid(row=7, column=0, columnspan=2, padx=20, pady=10, sticky=W)

# Other weather data icons
humidity_img = Image.open('Icons/humidity.png').resize((60, 60))
new_hum = ImageTk.PhotoImage(humidity_img)
humidity_label = Label(window, image=new_hum, background='#e0f6fb')
humidity_label.place(x=60, y=550)

wind_img = Image.open('Icons/windSpeed.png').resize((60, 60))
new_wind = ImageTk.PhotoImage(wind_img)
wind_label = Label(window, image=new_wind, background='#e0f6fb')
wind_label.place(x=220, y=550)

pressure_img = Image.open('Icons/pressure.png').resize((60, 60))
new_press = ImageTk.PhotoImage(pressure_img)
pressure_label = Label(window, image=new_press, background='#e0f6fb')
pressure_label.place(x=380, y=550)

# Other data labels
hum_data = Label(window, text="... %", font=('Arial', 20), bg='#e0f6fb')
hum_data.place(x=60, y=620)

wind_data = Label(window, text="... km/h", font=('Arial', 20), bg='#e0f6fb')
wind_data.place(x=200, y=620)

pressure_data = Label(window, text="... hPa", font=('Arial', 20), bg='#e0f6fb')
pressure_data.place(x=350, y=620)

window.mainloop()
