# WeatherApp

A basic Python command-line app that fetches current weather data for a city using the OpenWeatherMap API.

## What It Does
- Prompts for a city name.
- Uses OpenWeatherMap Geocoding API to get latitude and longitude.
- Uses OpenWeatherMap Current Weather API to fetch weather data for those coordinates.
- Prints raw JSON response (formatted) and a readable weather summary.

## Tech Stack
- Python 3
- `requests`
- `python-dotenv`

## Project Structure
- `app.py` - main script
- `.env` - environment variables (you provide this locally)

## Setup
1. Clone the project and enter the folder.
2. Create and activate a virtual environment (recommended):
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows (PowerShell): `python -m venv .venv; .venv\\Scripts\\Activate.ps1`
3. Install dependencies:
   - `pip install requests python-dotenv`
4. Create a `.env` file with your API key:
   - `WEATHER_API=your_openweathermap_api_key`

## Run
```bash
python app.py
```

Then enter a city when prompted.

## Notes
- Temperature is converted from Kelvin to Celsius in the output.
- The current script assumes API calls succeed and returned data is not empty.

## Possible Improvements
- Add robust error handling for:
  - Invalid city names
  - Empty geocoding results
  - Missing API key
  - Network timeouts and request failures
- Use HTTPS for all API endpoints (including geocoding).
- Add unit selection (`metric`, `imperial`, `standard`) via input or CLI flags.
- Improve output formatting and remove debug prints (`print(len(data))`).
- Add retries and timeout values to API requests.
- Support state/country disambiguation for city search.
- Add forecast support (hourly/daily) in addition to current weather.
- Split logic into functions/modules for better testability.
- Add automated tests and a `requirements.txt` file.
