import cv2
import socket

def getWlanIp():
    #if(os.name == "nt") :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        if("172" in IP):
            print("Ip address detected is :: " + IP )
            IP = '127.0.0.1'
            print("Ip address changed to :: " + IP + "to avoid docker interface")
        print("Ip address detected is :: " + IP )
        
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

#capture_url = "rtsp://" + getWlanIp() + ":8900/live"
capture_url = 'rtsp://10.106.19.211:8900/live'

i = 0
local_path = 'images/cans/'
image_type = 'can'

cap = cv2.VideoCapture(capture_url)
while True:
    _, frame = cap.read()
    cv2.imshow('my webcam', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break  # press q to quit
    # "c" key
    elif k == ord('c'):
        local_file_name = image_type + str(i) + '.jpg'
        full_file_path = (local_path+ local_file_name)
        print("image printed", full_file_path)
        cv2.imwrite(full_file_path, frame)
        
        # upload created file
        print("\n Uploading to Blob Storage as blob:", local_file_name)
        
        i+=1
# clean up
cap.release()
cv2.destroyAllWindows()
