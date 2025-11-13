import sys
import requests
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton,
                             QLineEdit, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: "Arial";
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                    font-size: 40px;
            }
            QPushButton#get_weather_button{
                    font-size: 30px;
                    font-weight: bold;
            }
            QLabel#temperature_label{
                    font-size: 75px;
            }
            QLabel#emoji_label{
                    font-size: 100px;
                    font-family: "Segoe UI Emoji";
            }
            QLabel#description_label{
                    font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "d5343c257c801750f69bf6e605ae58a0"
        city = self.city_input.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request.\nPlease check the city name.")
                case 401:
                    self.display_error("Unauthorized.\nPlease check your API key.")
                case 403:
                    self.display_error("Forbidden.\nYou don't have access to this resource.")
                case 404:
                    self.display_error("City not found.\nPlease check the city name.")
                case 500:
                    self.display_error("Internal server error.\nPlease try again later.")
                case 502:
                    self.display_error("Bad gateway.\nPlease try again later.")
                case 503:
                    self.display_error("Service unavailable.\nPlease try again later.")
                case 504:
                    self.display_error("Gateway timeout.\nPlease try again later.")
                case _:
                    self.display_error(f"Http error occurred.\n{http_error}")

        except requests.exceptions.ConnectionError:
            print("Connection error.\nCheck your internet connection.")
        except requests.exceptions.Timeout:
            print("Timeout error.\nPlease try again later.")
        except requests.exceptions.TooManyRedirects:
            print("Too many redirects.\nCheck the URL.")
        except requests.exceptions.RequestException as req_error:
            print(f"An error occurred.\n{req_error}")



    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()


    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = round(temperature_c * 1.8 + 32, 2)
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"Temperature: {temperature_c:.0f} °C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(f"Description: {weather_description}")

    @staticmethod
    def get_weather_emoji(weather_id):

        if 200 <= weather_id < 232:
            return "⛈️"
        elif 300 <= weather_id < 321:
            return "🌦️"
        elif 500 <= weather_id < 531:
            return "🌧️"
        elif 600 <= weather_id < 622:
            return "❄️"
        elif 700 <= weather_id < 781:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id < 804:
            return "⛅"
        elif weather_id == 804:
            return "️"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
