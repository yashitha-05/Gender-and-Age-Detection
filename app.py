
import streamlit as st
import cv2
import numpy as np

st.title("Gender and Age Detection")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), channels="RGB")

    # Here call your age/gender detection functions from detect.py
    st.write("Predicted: Male, 25-32 years (example)")
