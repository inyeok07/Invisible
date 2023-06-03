from keras_cv_attention_models import yolor
import cv2 as cv
from pandas import read_table

model = yolor.YOLOR_CSP(pretrained="coco")  #필요한 확장자 설치

df = read_table('coco-labels-paper.txt',index_col=False)
col = str(df.columns[0])

COCO_LABELS = df.to_numpy().reshape(-1,).tolist()
COCO_LABELS.insert(0,col)

webcam = cv.VideoCapture(0)
while webcam.isOpened():
    ret, img = webcam.read()
    if not ret:
        print("Can't read camera")
        break
    cv.imshow("PC_camera", img)
    status, frame = webcam.read()
    frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB) #화면을 인식할 프레임 생성
    preds = model(model.preprocess_input(frame)) #생성한 프레임으로 모델생성
    bboxs, labels, confidences = model.decode_predictions(preds)[0]
    if status:
        print([COCO_LABELS[i] for i in labels.numpy().tolist()])

    if cv.waitKey(1) & 0xFF == ord('q'): #q를 누를시 작동 종료
        print('off')
        break