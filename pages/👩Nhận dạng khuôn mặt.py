import streamlit as st
import numpy as np
import cv2 as cv
import joblib

st.title("👩🧑‍🦰 Nhận dạng khuôn mặt 👩🧑‍🦰")

if "frame_stop" not in st.session_state:
    st.session_state.frame_stop = cv.imread('./data/image/stop.jpg')
    print('Đã load stop.jpg')

def show_video(frame):
    FRAME_WINDOW.image(frame, channels='BGR')

def visualize(input_frame, faces, results, fps, thickness=4, font_scale=1.2):
    if faces[1] is not None:
        for idx, face in enumerate(faces[1]):
            coords = face[:-1].astype(np.int32)
            cv.rectangle(input_frame, 
                         (coords[0], coords[1]), 
                         (coords[0] + coords[2], coords[1] + coords[3]), 
                         (0, 255, 0), thickness)
              
            landmarks = coords[4:].reshape(-1, 2)
            colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 255), (0, 255, 255)]
            for i, (x, y) in enumerate(landmarks):
                cv.circle(input_frame, (x, y), 2, colors[i], thickness)
            
            result = results[idx] if idx < len(results) else "Unknown"
            cv.putText(input_frame, result, (coords[0], coords[1] - 10), 
                       cv.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), thickness)
    
    cv.putText(input_frame, f'FPS: {fps:.2f}', (1, 16), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

start_stop_container = st.container()
start_stop_button = start_stop_container.button("Stop")

if 'stop' not in st.session_state:
    st.session_state.stop = False

if start_stop_button:
    st.session_state.stop = not st.session_state.stop

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./pages/css/style.css")

FRAME_WINDOW = st.image([])

if not st.session_state.stop:
    svc = joblib.load('./train/model/Facedetection/svc.pkl')
    labels = ['AnhTuyet', 'DiepY', 'LyNa', 'NgocHa', 'TuongVy']

    detector = cv.FaceDetectorYN.create(
        './train/model/Facedetection/face_detection_yunet_2023mar.onnx',
        "",
        (320, 320),
        0.9,
        0.3,
        5000)

    recognizer = cv.FaceRecognizerSF.create(
        './train/model/Facedetection/face_recognition_sface_2021dec.onnx', "")

    tm = cv.TickMeter()

    frame_width = 1280
    frame_height = 720

    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, frame_height)
    detector.setInputSize([frame_width, frame_height])

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Không thể lấy khung hình!')
            break

        tm.start()
        faces = detector.detect(frame)
        tm.stop()

        results = []
        if faces[1] is not None:
            for face in faces[1]:
                face_aligned = recognizer.alignCrop(frame, face)
                face_feature = recognizer.feature(face_aligned)
                prediction = svc.predict(face_feature)
                results.append(labels[prediction[0]])

        visualize(frame, faces, results, tm.getFPS())
        show_video(frame)