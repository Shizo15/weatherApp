# Weather App - Python GUI Project

This repository contains a Python-based GUI application that displays weather information for a user-specified city. Built using the **Tkinter** library, this app leverages the **OpenWeatherMap API** to fetch real-time weather data, including temperature, humidity, wind speed, and more. The application also updates dynamically with weather-specific icons for better user experience.

## Features
- Input a city name to get current weather details.
- Displays:
  - Temperature
  - Feels-like temperature
  - Humidity
  - Wind speed
  - Pressure
  - Weather description
- Updates dynamically with relevant weather icons.
- User-friendly graphical interface built with Tkinter.
- API integration with OpenWeatherMap for accurate weather data.

## Tools & Libraries
- **Tkinter**: For GUI design.
- **Requests**: To interact with the weather API.
- **Pillow**: For image handling.
- **dotenv**: To securely manage the API key.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your API key:
   - Create a file named `.env` in the project directory.
   - Add your OpenWeatherMap API key in the following format:
     ```plaintext
     API_KEY=your_api_key_here
     ```
4. Run the application:
   ```bash
   python main.py
   ```

## Screenshots

<img src="https://github.com/user-attachments/assets/c1886e1d-1780-483e-85d0-a6b0b0b4f1aa" alt="weatherapp1" width="450">

<img src="https://github.com/user-attachments/assets/90a3430b-d2d2-42fb-930e-aa776bc47805" alt="weatherapp2" width="450">


---
This project was developed as part of a semester project for a Python programming course. It demonstrates the integration of APIs with GUI applications and basic handling of real-time data.

