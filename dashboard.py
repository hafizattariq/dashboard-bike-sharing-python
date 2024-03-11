import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def data_load():
  data = pd.read_csv("hour.csv")
  return data

data = data_load()


st.set_page_config(
    page_title="Dashboard Bike Sharing",
    page_icon="🚲",
)

st.sidebar.markdown("<h1 style='color: green;'>Tentang Dashboard Ini</h1>", unsafe_allow_html=True)
st.sidebar.success(
    """
    Dashboard ini berisi visualisasi informasi dari data frame bicycle sharing.
    Informasi yang ditampilkan berupa jumlah penyewaan sepeda berdasarkan beberapa 
    feature yang disediakan pada dataset seperti musim (season), cuaca (weather),
    kelembapan (humidity), dan lain-lain. 🌧 ☁ 🌩
    """
    )

st.sidebar.subheader(" Dataset Info ")
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

if st.sidebar.checkbox("Kesimpulan Statistik Dataset"):
    st.subheader("Kesimpulan Statistik")
    st.write(data.describe())

st.sidebar.title("Author Information")
st.sidebar.markdown("Nama: M. Hafiz Attariq")
st.sidebar.markdown("Email: mhafizattariq29@gmail.com")
st.sidebar.markdown("id Dicoding: hafizattariq")

st.subheader("# Dashboard Bike Sharing 🚲")

year_desc = {0: "2011", 1: "2012"}
data["yr"] = data["yr"].map(year_desc)
year_cnt = data.groupby("yr")["cnt"].sum().reset_index()
fig_year_chart = px.bar(
    year_cnt, x="yr", y="cnt", title="Bike Sharing Count by Year")
st.plotly_chart(fig_year_chart, use_container_width=True,
                height=250, width=500)

hour_cnt = data.groupby("hr")["cnt"].sum().reset_index()
fig_hour_cnt = px.line(
    hour_cnt, x="hr", y="cnt", title="Bike Sharing Count by Hour")
st.plotly_chart(fig_hour_cnt, use_container_width=True,
                height=250, width=500)

season_desc = {1: "springer", 2: "summer", 3: "fall", 4: "winter"}
data["season"] = data["season"].map(season_desc)
season_cnt = data.groupby("season")["cnt"].sum().reset_index()
fig_season_cnt = px.bar(season_cnt, x="season",
                          y="cnt", title="Bike Sharing Count by Seasons")
st.plotly_chart(fig_season_cnt, use_container_width=True,
                height=250, width=500)

col1, col2 = st.columns([2, 1])

with col1:
    weather_cnt = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_cnt = px.bar(weather_cnt, x="weathersit",
                             y="cnt", title="Bike Sharing Count by Weather")
    st.plotly_chart(fig_weather_cnt, use_container_width=True,
                    height=250, width=500)

with col2:
    st.title(" ")
    st.write("Weather Index Information: ")
    st.write(" 1: Clear, Few clouds, Partly cloudy, Partly cloudy ")
    st.write(" 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ")
    st.write(" 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds ")
    st.write(" 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog ")

data['temp'] = data['temp'].apply(lambda x: x * 41)
temp_cnt = data.groupby("temp")["cnt"].sum().reset_index()
fig_temp_cnt = px.bar(
    temp_cnt, x="temp", y="cnt", color="temp",
                      color_continuous_scale='Bluered', title="Bike Sharing Count by Temperature")
st.plotly_chart(fig_temp_cnt, use_container_width=True,
                height=250, width=500)

data['hum'] = data['hum'].apply(lambda x: x * 100)
hum_cnt = data.groupby("hum")["cnt"].sum().reset_index()
fig_hum_cnt = px.bar(
    hum_cnt, x="hum", y="cnt", color="hum",
                      color_continuous_scale='Rdbu', title="Bike Sharing Count by Humidity")
st.plotly_chart(fig_hum_cnt, use_container_width=True,
                height=250, width=500)

windspd_cnt = data.groupby("windspeed")["cnt"].sum().reset_index()
fig_windspd_cnt = px.line(
    windspd_cnt, x="windspeed", y="cnt", title="Bike Sharing Count by Windspeed")
st.plotly_chart(fig_windspd_cnt, use_container_width=True,
                height=400, width=600)