import streamlit as st
#import lib.common as tools

st.set_page_config(
    page_title="Đồ án cuối kỳ",
    page_icon="🍀",
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvdjU0NmJhdGNoMy1teW50LTM0LWJhZGdld2F0ZXJjb2xvcl8xLmpwZw.jpg");
    background-size: 100% 100%;
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right:2rem;
}
[data-testid="stSidebar"] > div:first-child {
    background-image: url("");
    background-position: center;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


# logo_path = "./VCT.png"
# st.sidebar.image(logo_path, width=200)
st.title ("TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT TP.HCM")
st.title ("KHOA CÔNG NGHỆ THÔNG TIN")
st.title ("Môn học: Xử lý ảnh số")
st.title ("Báo cáo đồ án cuối kỳ")
st.title (" ")
st.header ("GVHD: ThS. Trần Tiến Đức")
st.header (" Mã lớp : DIPR430685_23_2_03")
st.header ("Học kỳ: 2")
st.header ("Năm học: 2023 - 2024")
st.markdown(
    """
    ## Sản phẩm
    Project cuối kỳ cho môn học xử lý ảnh số DIPR430685 dùng framework Streamlit.

    ### 6 chức năng có trong bài
    - 📙Nhận dạng chữ viết tay
    - 📔Nhận dạng trái cây
    - 📒Nhận dạng khuôn mặt
    - 📕Xử lý ảnh
    - 📗Nhận dạng đếm ngón tay
    - 📘Nhận dạng biển số xe

    ## Thông tin sinh viên thực hiện
    - 👱Họ tên: Nguyễn Ánh Tuyết
    - 🔎MSSV: 21110717
    - 👦Họ tên: Trần Thị Tường Vy
    - 🔎MSSV: 21110735
    """
)


