from keras_cv_attention_models import yolor
import cv2
model = yolor.YOLOR_CSP(pretrained="coco")  #필요한 확장자 설치

webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    status, frame = webcam.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #화면을 인식할 프레임 생성

    preds = model(model.preprocess_input(frame)) #생성한 프레임으로 모델생성
    bboxs, lables, confidences = model.decode_predictions(preds)[0]

    if status:
        print(lables) #인식된 물체 출력
    if cv2.waitKey(1) & 0xFF == ord('q'): #q를 누를시 작동 종료
        break
