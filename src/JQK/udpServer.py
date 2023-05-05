import numpy as np
import cv2
from socket import *


s = socket(AF_INET, SOCK_DGRAM) # 创建UDP套接字
addr = ('0.0.0.0', 8081)  # 0.0.0.0表示本机
s.bind(addr)

s.setblocking(0) # 设置为非阻塞模式

while True:
    data = None
    try:
        data, _ = s.recvfrom(921600)
        receive_data = np.frombuffer(data, dtype='uint8')
        r_img = cv2.imdecode(receive_data, 1)

        cv2.putText(r_img, "server", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('server', r_img)
    except BlockingIOError as e:
        pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
