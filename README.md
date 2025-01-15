# Weather Viewer App 🌤️

A simple Streamlit app that allows you to view the current weather conditions of any city. The app fetches data from the OpenWeather API and displays information like temperature, humidity, and weather description.

## Features
- Check weather conditions by entering the city name.
- Displays temperature in both Celsius and Fahrenheit.
- Displays humidity and weather description.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/bigyan22/Weather-App.git
cd Weather-App
```

### 2. Create a ```.env``` file

Create a *.env* file in the root directory of the project and add your OpenWeather API key:
```bash
API_KEY = your_api_key
```


### 3. Install the dependencies
You have to install the required dependencies by using the following command.
<br>
```bash
pip install -r requirements.txt
```

### 4. Run the app
To run the app locally, use the following command:
```bash
streamlit run app.py
```