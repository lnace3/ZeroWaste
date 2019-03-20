import cv2

i = 0
local_path = 'images/cans/'
image_type = 'can'

cap = cv2.VideoCapture('rtsp://10.106.19.211:8900/live')
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
