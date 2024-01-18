import cv2  # pip install opencv-python
import cvzone  # pip install cvzone
from cvzone.PoseModule import PoseDetector

video = cv2.VideoCapture('vd01.mp4')  # Captura o vídeo
detector = PoseDetector()  # Instancia o detector de pose

while True:
    _, frame = video.read()  # Lê o frame
    img = cv2.resize(frame, (1280,720))  # Redimensiona o frame
    resultado = detector.findPose(img)  # Encontra a pose
    pontos,bbox = detector.findPosition(img, draw=False)  # Encontra os pontos e bounding box
    if len(pontos)>=1:  # Se houver pontos
        x, y, w, h = bbox['bbox']  # Pega as coordenadas da bounding box
        cabeca = pontos[0][1]  # Pega a posição da cabeça
        joelho = pontos[26][1]  # Pega a posição do joelho
        diferenca = joelho-cabeca  # Calcula a diferença entre a cabeça e o joelho

        if diferenca <=0:  # Se a diferença for menor ou igual a zero
            cvzone.putTextRect(img,'QUEDA DETECTADA',(x,y-80),scale=3,thickness=3,colorR=(0,0,255))


    cv2.imshow('Video', img)
    cv2.waitKey(1)