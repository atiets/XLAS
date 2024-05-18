import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

# -------------- SETTINGS --------------
page_title = "Trang chủ"
page_icon = ":tada"  # emoji mô tả trang web của bạn
layout = "wide"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
# st.title(page_title + " " + page_icon)
# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./pages/css/style.css")
local_css("./pages/css/clone.css")

# ---- LOAD ASSETS ----
img_contact_form = Image.open("./data/images/calculate.png")
img_chuso = Image.open("./data/images/chuso.png")
img_human = Image.open("./data/images/human.png")
img_object = Image.open("./data/images/object.png")
img_fruit = Image.open("./data/images/fruit.png")
img_number = Image.open("./data/images/sign.png")
img_process = Image.open("./data/images/img_process.png")
img_hand=Image.open("./data/images/okay-JPG-5442-1380073443-2910-1380077076.jpg")
img_count_hand=Image.open("./data/images/0dea366122b1b4ef91a372d9381666d3.jpg")


# ---- HEADER SECTION ----
with st.container():
    st.markdown(
        f'<h1 style="text-align: center"> ĐỒ ÁN CUỐI KỲ MÔN XỬ LÝ ẢNH SỐ </h1>',
        unsafe_allow_html=True
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column = st.columns([1])[0]
    with open("./pages/html/card.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    with left_column:
        st.markdown(html_content, unsafe_allow_html=True)

st.write("<h1 style='text-align:center'>My Projects</h1>", unsafe_allow_html=True)
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form, width=150)
    with text_column:
        st.subheader("GIẢI PHƯƠNG TRÌNH BẬC HAI")
        st.write(
            """
            ✨ Giải phương trình bậc 2: ax2+bx+c=0 (a≠0) \n
            ✨ Phương trình: Có nghiệm - Vô nghiệm - Vô số nghiệm 
            """
        )
        st.markdown('<a href="GiaiPhuongTrinhBac2" target="_self">Phương trình bậc 2🧮</a>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_human, width=150)
    with text_column:
        st.subheader("NHẬN DẠNG GƯƠNG MẶT")
        st.write(
            """
            ✨ NHẬN DẠNG GƯƠNG MẶT -  NHẬN DIỆN 5 Người trong 1 khuôn hình
            """
        )
        st.markdown('<a href="Face_Recognition" target="_self">Nhận diện khuôn mặt 🧑</a>', unsafe_allow_html=True)


with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_object, width=150)
    with text_column:
        st.subheader("NHẬN DẠNG ĐỐI TƯỢNG")
        st.write(
            """
            ✨ Phát hiện theo từng loại đối tượng khác nhau\n
            ✨ person - bicycle - car - motorbike - aeroplane - bus - train - truck - boat
            """
        )
        st.markdown('<a href="Object_detection" target="_self">Nhận diện đối tượng 👨‍👩‍👧‍👦</a>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_number, width=150)
    with text_column:
        st.subheader("NHẬN DẠNG CHỮ SỐ VIẾT TAY")
        st.write(
            """
            ✨ Nhận dạng chữ - số viết tay Mnist 
            """
        )
        st.markdown('<a href="Mnist_detection" target="_self">Nhận diện chữ số viết tay</a>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_fruit, width=150)
    with text_column:
        st.subheader("NHẬN DIỆN TRÁI CÂY")
        st.write(
            "✨ Nhận diện được 15 loại trái cây như: Dualeo - Tao - Kiwi - Chuoi - Cam - Dua - Dao - Chery - Le - Luu - Thom - Thom - Duahau - Dualuoi - Nho - Dau"
        )
        st.markdown('<a href="Fruit_detection" target="_self">Nhận diện các loại trái cây</a>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_process, width=150)
    with text_column:
        st.subheader("XỬ LÝ ẢNH")
        st.write(
            """
            ✨ Bao gồm 4 Chapter 3, 4, 5, 9\n
            
            """
        )
        st.markdown('<a href="Image_processing" target="_self">Xử lý ảnh 📷</a>', unsafe_allow_html=True)
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_hand, width=150)
    with text_column:
        st.subheader("NHẬN DIỆN KÍ HIỆU TAY")
        st.write(
            """
            ✨ Chỉ nhận dạng được 3 kí hiệu   A ,B ,C
            
            """
        )
        st.markdown('<a href="Hand_Detection" target="_self">Nhận dạng kí hiệu tay ✌️</a>', unsafe_allow_html=True)
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_count_hand, width=150)
    with text_column:
        st.subheader("Đếm SỐ NGÓN TAY")
        st.write(
            """
            ✨ Đếm số ngón tay  1 , 2 , 3, 4 , 5
            
            """
        )
        st.markdown('<a href="Count_Finger_Detection" target="_self">Đếm số ngón tay 🫷</a>', unsafe_allow_html=True)