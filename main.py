import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
#getting api key
api_key = os.getenv("API_KEY")

st.set_page_config(page_title='Wather Viewer', page_icon="🌤️", layout='centered')
st.title("🌤️ Weather Viewer App")
st.divider()
st.write("Enter a city name below to check its current weather conditions.")

city = st.text_input("City Name:", placeholder="Enter city name").strip()

if st.button("Check Weather"):
    if city:
        try: # featching the weather data by using the api key
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
            )
            response.raise_for_status()  # Raise HTTP errors
            data = response.json()
            

            # Extract all the weather details
            weather = data['weather'][0]['description'].capitalize()
            temp_f = data['main']['temp']
            feels_like_f = data['main']['feels_like']
            humidity = data['main']['humidity']
            temp_c = (temp_f - 32) * 5 / 9
            feels_like_c = (feels_like_f - 32) * 5 / 9

            # Display weather information
            st.success(f"Weather in **{city.capitalize()}**")
            col1, col2 = st.columns(2)

            with col1:
                st.metric("🌡️ Temperature (°C)", f"{temp_c:.2f}°C")
                st.metric("🌡️ Feels Like (°C)", f"{feels_like_c:.2f}°C")

            with col2:
                st.metric("💧 Humidity", f"{humidity}%")
                st.metric("🌤️ Description", weather)

        except requests.exceptions.HTTPError as http_err: # if status_code in response is 400 or 500, the 'requests' library raise the error and this error is extracted from this line
            st.error(f"City not found! Please check the city name.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a city name!")
