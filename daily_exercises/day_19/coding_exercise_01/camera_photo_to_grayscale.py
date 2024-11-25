import streamlit as st
from PIL import Image


def set_upload():
    st.session_state["image"] = "upload"


def set_camera():
    st.session_state["image"] = "camera"


st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image", on_change=set_upload)

with st.expander("Start Camera"):
    camera_image = st.camera_input(
        "Web Camera", label_visibility="collapsed", on_change=set_camera
    )

if "image" in st.session_state:
    if st.session_state["image"] == "upload" and uploaded_image:
        img = Image.open(uploaded_image)
    elif st.session_state["image"] == "camera" and camera_image:
        img = Image.open(camera_image)
    else:
        img = None

    if img:
        gray_camera_img = img.convert('L')
        st.image(gray_camera_img)
