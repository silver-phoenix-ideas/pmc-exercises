import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera", label_visibility="collapsed")

if camera_image:
    pillow_image = Image.open(camera_image)
    grayscale_image = pillow_image.convert("L")
    st.image(grayscale_image)
