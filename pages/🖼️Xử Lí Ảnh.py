import cv2
import numpy as np
import Chapter03 as c3
import Chapter04 as c4
import Chapter05 as c5
import Chapter09 as c9
import streamlit as st

# Set Streamlit theme
st.set_page_config(layout="wide", page_title="Xử lí Ảnh", page_icon="👀🏞️")

# Custom CSS styling
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f5f7f9;
    }
    .sidebar .sidebar-content .block-container {
        margin-bottom: 1rem;
    }
    .stButton button {
        background-color: #4b8bbe;
        color: white;
    }
    .custom-text {
        font-size: 20px;
        color: #FF0000;
        font-weight: bold;
        text-align: center;
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
   f"""
    <style>
    [data-testid="stSidebar"] > div:first-child {{
        background-image: url(https://bizweb.dktcdn.net/100/438/408/files/hinh-nen-mau-hong-yody-vn30.jpg?v=1685068694111);
    }}
    </style>
    """,
    unsafe_allow_html=True
)


def save_image(img):
    # Implement the logic to save the image
    # For example, you can use OpenCV's imencode to convert the image to bytes
    success, buffer = cv2.imencode('.jpg', img)
    if success:
        return buffer.tobytes()
    else:
        return None

def main():
    st.title("👀🏞️ Xử lí Ảnh")
    imgin = None
    imgout = None
    color_mode = st.sidebar.radio("Chọn chế độ màu", ["Ảnh xám", "Ảnh màu"])

    file_menu = st.sidebar.file_uploader("Mở ảnh", type=["jpg", "jpeg", "png", "tif"])

    if file_menu is not None:
        imgin = cv2.imdecode(np.frombuffer(file_menu.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        if color_mode == "Ảnh xám":
                # Ảnh xám
                st.image(imgin, channels="GRAY", use_column_width=True)
        else:
            if len(imgin.shape) == 3:
                # Ảnh màu
                st.image(imgin, channels="BGR", use_column_width=True)
            else:
                st.sidebar.write("Lỗi khi tải ảnh. Định dạng ảnh không hợp lệ. Vui lòng tải lên ảnh màu.")
    else:
        st.sidebar.write("Vui lòng tải lên một ảnh")

    chapter = st.sidebar.selectbox("Chọn chương", ["Chapter 3", "Chapter 4", "Chapter 5", "Chapter 9"])

    st.sidebar.write("---")  # Thêm một đường phân cách

    if chapter == "Chapter 3":
        st.sidebar.markdown("### Thao tác")
        titlel ="Chapter 3"
        operation = st.sidebar.selectbox("Chọn thao tác",
                                ["Negative", "Logarithm",'Power' ,"Piecewise Linear", "Histogram",
                                 "Histogram Equalization", "Color Histogram Equalization",
                                 "Local Histogram Equalization", "Histogram Statistics",
                                 "Box Filter", "Lowpass Gaussian Filter", "Thresholding",
                                 "Median Filter", "Sharpening", "Gradient"])

        if operation == "Negative":
            st.subheader("Negative")
            if imgin is not None:
                imgout = c3.Negative(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)
        if operation == "Logarithm":
            st.subheader("Logarithm")
            if imgin is not None:
                imgout = c3.Logarit(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)
        if operation == "Power":
            st.subheader("Power")
            if imgin is not None:
                imgout = c3.Power(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)
        if operation == "Piecewise Linear":
            st.subheader("Piecewise Linear")
            if imgin is not None:
                imgout = c3.PiecewiseLinear(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)
        if operation == "Histogram":
            st.subheader("Histogram")
            if imgin is not None:
                imgout = c3.Histogram(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)
        if operation == "Histogram Equalization":
            st.subheader("Histogram Equalization")
            if imgin is not None:
                imgout = c3.HistEqual(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)

        if operation == "Color Histogram Equalization":
            st.subheader("Color Histogram Equalization")
            if imgin is not None:
                imgout = c3.HistEqualColor(imgin)
                st.image(imgout, channels="RBG", use_column_width=True)

        if operation == "Local Histogram Equalization":
            st.subheader("Local Histogram Equalization")
            if imgin is not None:
                imgout = c3.LocalHist(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)

        if operation == "Histogram Statistics":
            st.subheader("Histogram Statistics")
            if imgin is not None:
                imgout = c3.HistStat(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)

        if operation == "Box Filter":
            st.subheader("Box Filter")
            if imgin is not None:
                imgout = cv2.blur(imgin,(21,21))
                st.image(imgout, channels="GRAY", use_column_width=True)

        if operation == "Lowpass Gaussian Filter":
            st.subheader("Lowpass Gaussian Filter")
            if imgin is not None:
                imgout = cv2.GaussianBlur(imgin,(43,43),7.0)
                st.image(imgout, channels="GRAY", use_column_width=True)

        if operation == "Thresholding":
            st.subheader("Thresholding")
            if imgin is not None:
                imgout = c3.Threshold(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)
        if operation == "Median Filter":
            st.subheader("Median Filter")
            if imgin is not None:
                imgout = c3.MedianFilter(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)

        if operation == "Sharpening":
            st.subheader("Sharpening")
            if imgin is not None:
                imgout = c3.Sharpen(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)

        if operation == "Gradient":
            st.subheader("Gradient")
            if imgin is not None:
                imgout = c3.Gradient(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)
            
    elif chapter == "Chapter 4":
        titlel ="Chapter 4"
        st.sidebar.markdown("### Operations")
        chapter4Menu = st.sidebar.selectbox("Chapter 4", ["Spectrum", "FrequencyFilter", "DrawNotchRejectFilter", "RemoveMoire"])
        if chapter4Menu == "Spectrum":
            st.subheader("Perform Spectrum operation")
            if imgin is not None:
                imgout = c4.Spectrum(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)

        elif chapter4Menu == "FrequencyFilter":
            st.subheader("Perform FrequencyFilter operation")
            if imgin is not None:
                imgout = c4.FrequencyFilter(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)


        elif chapter4Menu == "DrawNotchRejectFilter":
            st.subheader("Perform DrawNotchRejectFilter operation")
            if imgin is not None:
                imgout = c4.DrawNotchRejectFilter()
                st.image(imgout, channels="GRAY", use_column_width=True)


        elif chapter4Menu == "RemoveMoire":
            st.subheader("Perform RemoveMoire operation")
            if imgin is not None:
                imgout = c4.RemoveMoire(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)

    elif chapter == "Chapter 5":
        titlel ="Chapter 5"
        st.sidebar.markdown("### Operations")
        chapter5Menu = st.sidebar.selectbox("Chapter 5", ["CreateMotionNoise", "DenoiseMotion", "DenoisestMotion"])
        if chapter5Menu == "CreateMotionNoise":
            st.subheader("Perform CreateMotionNoise operation")
            if imgin is not None:
                imgout = c5.CreateMotionNoise(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)

        elif chapter5Menu == "DenoiseMotion":
            st.subheader("Perform DenoiseMotion operation")
            if imgin is not None:
                imgout = c5.DenoiseMotion(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)

        elif chapter5Menu == "DenoisestMotion":
            st.subheader("Perform DenoisestMotion operation")
            if imgin is not None:
                temp = cv2.medianBlur(imgin, 7)
                imgout = c5.DenoiseMotion(temp)
                st.image(imgout, channels="GRAY", use_column_width=True)
    elif chapter == "Chapter 9":
        titlel ="Chapter 9"
        st.sidebar.markdown("### Operations")
        chapter9Menu = st.sidebar.selectbox("Chapter 9", ["ConnectedComponent", "CountRice"])
        if chapter9Menu == "ConnectedComponent":
            st.subheader("Perform ConnectedComponent operation")
            if imgin is not None:
                imgout = c9.ConnectedComponent(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)
        if chapter9Menu == "CountRice":
            st.subheader("Perform CountRice operation")
            if imgin is not None:
                imgout = c9.CountRice(imgin)
                st.image(imgout, channels="GRAY", use_column_width=True)
        # Call self.onDenoisestMotion function
    if imgout is not None:
        download_filename = "processed_image.jpg"  # Customize the file name here
        st.sidebar.download_button("Download Processed Image", save_image(imgout), file_name=download_filename)
    # Implement the remaining chapters and operations using Streamlit components

if __name__ == "__main__":
    main()