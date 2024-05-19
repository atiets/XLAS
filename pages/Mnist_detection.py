import streamlit as st
import tensorflow as tf
from tensorflow.keras import datasets
from tensorflow.keras.models import model_from_json
import numpy as np
import random

def tao_anh_ngau_nhien():
    image = np.zeros((10*28, 10*28), np.uint8)
    data = np.zeros((100, 28, 28, 1), np.uint8)

    for i in range(0, 100):
        n = random.randint(0, 9999)
        sample = st.session_state.X_test[n]
        data[i] = st.session_state.X_test[n]
        x = i // 10
        y = i % 10
        image[x*28:(x+1)*28, y*28:(y+1)*28] = sample[:, :, 0]
    return image, data

if 'is_load' not in st.session_state:
    # load model
    model_architecture = './train/model/Mnistdetection/digit_config.json'
    model_weights = './train/model/Mnistdetection/digit_weight.h5'
    model = model_from_json(open(model_architecture).read())
    model.load_weights(model_weights)

    OPTIMIZER = tf.keras.optimizers.Adam()
    model.compile(loss="categorical_crossentropy", optimizer=OPTIMIZER,
                  metrics=["accuracy"])
    st.session_state.model = model

    # load data
    (_, _), (X_test, y_test) = datasets.mnist.load_data()
    X_test = X_test.reshape((10000, 28, 28, 1))
    st.session_state.X_test = X_test

    st.session_state.is_load = True
    print('Lần đầu load model và data')
else:
    print('Đã load model và data rồi')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./pages/css/style.css")

# Hiển thị nút "Tạo ảnh" và hình ảnh tạo, cùng như nút "Nhận dạng" và kết quả, trong cùng một khung
col1, col2 = st.columns(2)

# Nút "Nhận dạng" và kết quả bên phải
if col1.button('Xác định số trên ảnh'):
    col1.markdown("### Phân thích chữ số trên ảnh:")
    data = st.session_state.data
    data = data/255.0
    data = data.astype('float32')
    ket_qua = st.session_state.model.predict(data)
    dem = 0
    s = ''
    for x in ket_qua:
        s = s + '%d ' % (np.argmax(x))
        dem = dem + 1
        if (dem % 10 == 0) and (dem < 100):
            s = s + '\n'
    col1.text(s)

# Nút "Tạo ảnh" và hình ảnh tạo bên trái
if col2.button('Tạo ảnh ngẫu nhiên'):
    st.session_state.image, st.session_state.data = tao_anh_ngau_nhien()

# Hiển thị ảnh tạo bên trái
if 'image' in st.session_state:
    col2.image(st.session_state.image, caption="Ảnh ngẫu nhiên", use_column_width=True)