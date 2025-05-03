import streamlit as st

st.title("AI Medical Image Analyzer (POC)")
st.write("Upload a medical image to get started:")

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.success("Image uploaded successfully!")

