import cv2

vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened()==False):
    print("Não conseguimos achar sua câmera")

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(width)
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(height)
#fps = int(vid.get(cv2.CAP_PROP_FPS))
#print(fps)

vidSalvar = cv2.VideoWriter("Tio câmera lenta.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))

while(True):
    ret, frame = vid.read()
    cv2.imshow("Video", frame)
    vidSalvar.write(frame)
    if cv2.waitKey(25) == 32:
        break
vid.release()
vidSalvar.release()
vid.destroyAllWindows()