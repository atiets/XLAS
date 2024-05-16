import streamlit as st
import numpy as np
from PIL import Image
import train.model.ImageProcessing.Chapter03 as c3
import train.model.ImageProcessing.Chapter04 as c4
import train.model.ImageProcessing.Chapter05 as c5
import train.model.ImageProcessing.Chapter09 as c9

# Set page title and icon

st.set_page_config(
    page_title="Digital Image Processing",
    page_icon=":camera_flash:",
    layout="wide"
)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./pages/css/style.css")

# Title
st.title("Digital Image Processing")

# Sidebar layout
st.sidebar.title("Select Chapter and Operation")

# Chapter selection
selected_chapter = st.sidebar.radio("Select Chapter", ["Chapter3", "Chapter4", "Chapter5", "Chapter9"])

# Operation selection
if selected_chapter == "Chapter3":
    selected_operation = st.sidebar.selectbox("Select Operation", [
        "Negative", "Logarithm","Exponentiate", "Piecewise Linear",
        "Histogram", "Histogram Equalization",
        "Color Histogram Equalization", "Local Histogram",
        "Histogram Statistics", "Box Filter", "Lowpass Gaussian",
        "Threshold", "Median Filter", "Sharpen", "Gradient"
    ])
elif selected_chapter == "Chapter4":
    selected_operation = st.sidebar.selectbox("Select Operation", [
        "Spectrum", "Frequency Filter",
        "Draw Notch Reject Filter", "Remove Moire"
    ])
elif selected_chapter == "Chapter5":
    selected_operation = st.sidebar.selectbox("Select Operation", [
        "Create Motion Noise", "Denoise Motion", "Denoisest Motion"
    ])
else:
    selected_operation = st.sidebar.selectbox("Select Operation", [
        "Connected Component", "Count Rice"
    ])

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "tif"])

if uploaded_file is not None:
    original_image = Image.open(uploaded_file)
    if st.button(f"Apply {selected_operation}", key="apply_button"):
        processed_image = None
        if selected_chapter == "Chapter3":
            operation_functions = {
                "Negative": c3.Negative,
                "Logarithm": c3.Logarit,
                "Exponentiate":c3.Exponentiate,
                "Piecewise Linear": c3.PiecewiseLinear,
                "Histogram": c3.Histogram,
                "Histogram Equalization": c3.HistEqual,
                "Color Histogram Equalization": c3.HistEqualColor,
                "Local Histogram": c3.LocalHist,
                "Histogram Statistics": c3.HistStat,
                "Box Filter": c3.onBoxFilter,
                "Lowpass Gaussian": c3.onLowpassGauss,
                "Threshold": c3.Threshold,
                "Median Filter": c3.onMedianFilter,
                "Sharpen": c3.Sharpen,
                "Gradient": c3.Gradient
            }
            selected_function = operation_functions.get(selected_operation)
            if selected_function:
                processed_image = selected_function(np.array(original_image))

        elif selected_chapter == "Chapter4":
            operation_functions = {
                "Spectrum": c4.Spectrum,
                "Frequency Filter": c4.FrequencyFilter,
                "Draw Notch Reject Filter": c4.DrawNotchRejectFilter,
                "Remove Moire": c4.RemoveMoire
            }
            selected_function = operation_functions.get(selected_operation)
            if selected_operation == "Draw Notch Reject Filter":
                processed_image = selected_function()
            else:
                processed_image = selected_function(np.array(original_image))

        elif selected_chapter == "Chapter5":
            operation_functions = {
                "Create Motion Noise": c5.CreateMotionNoise,
                "Denoise Motion": c5.DenoiseMotion,
                "Denoisest Motion": c5.onDenoisestMotion,
            }
            selected_function = operation_functions.get(selected_operation)
            if selected_function:
                processed_image = selected_function(np.array(original_image))

        elif selected_chapter == "Chapter9":
            operation_functions = {
                "Connected Component": c9.ConnectedComponent,
                "Count Rice": c9.CountRice,
            }
            selected_function = operation_functions.get(selected_operation)
            if selected_function:
                processed_image = selected_function(np.array(original_image))

        # Display processed image side by side with the original image
        if processed_image is not None:
            col1, col2 = st.columns(2)
            if selected_operation != "Draw Notch Reject Filter":
                col1.image(original_image, caption="Original Image", use_column_width=True)
            col2.image(processed_image, caption=f"{selected_operation} Image", use_column_width=True)
