import streamlit as st
import folium
import geocoder
from streamlit_folium import st_folium

g = geocoder.ip('me')

m = folium.Map(location=(g.lat, g.lng))

st_folium(m, use_container_width=True)