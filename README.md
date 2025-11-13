# Python Weather App

A small, beginner-friendly desktop weather application built with Python and PyQt5. Enter a city name and the app fetches the current weather from OpenWeatherMap, displays the temperature, a short description, and an emoji representing the weather.

This README explains how to configure, run, and extend the project.

---

## Features

- Query current weather by city name using OpenWeatherMap API
- Displays temperature in °C and a short description
- Shows a simple emoji representing the weather condition
- Minimal, easy-to-read PyQt5 GUI (single window)

## Security note

This repo previously included an API key in files. Do NOT commit your real API key to version control. Use an environment variable or a local configuration file that is excluded from Git.

## Requirements

- Python 3.8+
- The Python packages listed in `requirements.txt` (PyQt5, requests)

You can install dependencies with:

```sh
python -m pip install -r requirements.txt
```

## Get an OpenWeatherMap API key

1. Sign up at https://openweathermap.org/ and get a free API key (AppID).
2. Store it in an environment variable that the app will read, for example on macOS / Linux:

```sh
export OPENWEATHER_API_KEY="your_api_key_here"
```

On Windows (PowerShell):

```powershell
$env:OPENWEATHER_API_KEY = "your_api_key_here"
```

Note: The sample code currently contains a hard-coded key — remove it from the code and use the environment variable for security.

## Run the app

From the project root (where `main.py` is located):

```sh
python main.py
```

Type a city name (for example "London") and click "Get Weather".

## How it works (high level)

- `main.py` builds a PyQt5 window with a `QLineEdit` for the city, a button, and labels for temperature, emoji, and description.
- When the button is clicked the app calls the OpenWeatherMap API and parses the JSON response.
- The app maps the weather condition ID to a small emoji string and updates the UI.

## Troubleshooting

- Emoji not rendering or showing as a blank square:
  - Rendering is controlled by your system's emoji fonts. On macOS, the app prefers "Apple Color Emoji". On Windows it prefers "Segoe UI Emoji" and on Linux `Noto Color Emoji`.
  - If an emoji doesn't display, install a compatible emoji font on your system or use a small image (PNG/SVG) instead.

- PyQt5 import errors or GUI fails to open:
  - Make sure you installed PyQt5 in the same Python environment you use to run the app.
  - On macOS you may have to use the system Python or the virtualenv interpreter configured in PyCharm.

- API errors (bad request, 401 Unauthorized, 404 not found, etc.):
  - Double-check the city name and the `OPENWEATHER_API_KEY` value.
  - The app contains basic handling for HTTP response codes and displays user-friendly messages.

## Development notes

- The UI is purposely simple so beginners can read and extend it.
- If you want to improve the emoji display consistency across platforms, consider shipping small PNG/SVG icons and setting the `emoji_label` pixmap instead of relying on system emoji fonts.
- Consider adding unit tests around the weather-parsing logic (e.g., `get_weather_emoji`) and use a small mocking library to simulate API responses.

## Next improvements (ideas)

- Add unit tests for parsing & mapping logic
- Add settings to toggle °C/°F
- Cache recent queries and show history
- Improve error UI (popup dialogs instead of text-only)

## License

This project is provided under the MIT License. See `LICENSE` for details.

---

If you'd like, I can also:

- remove the hard-coded API key from `main.py` and make the app read `OPENWEATHER_API_KEY` from the environment; or
- implement a small settings dialog to set and persist the API key locally (and add `.gitignore` for the settings file).

Tell me which option you want and I will implement it.
