import cv2

faceCascade = cv2.CascadeClassifier("include/xml/face.xml")
eyeCascade = cv2.CascadeClassifier("include/xml/eye.xml")
noseCascade = cv2.CascadeClassifier("include/xml/nose.xml")


def generate_dataset(img, id, img_id):
    cv2.imwrite("data/user."+str(id)+"."+str(img_id)+".jpg", img)


def detect(img, faceCascade, img_id):
    coords = draw_boundary(img, faceCascade)
    if len(coords) == 4:
        roi_img = img[coords[1]:coords[1] +
                      coords[3], coords[0]:coords[0]+coords[2]]
        user_id = 1
        generate_dataset(roi_img, user_id, img_id)

    return img


def draw_boundary(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.11)
    coords = []
    for (x, y, w, h,) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(roi_gray, 1.3)
        nose = noseCascade.detectMultiScale(roi_gray, 1.9)
        if len(eyes) == 2 and len(nose) == 1:
            coords = [x, y, w, h]
            face_ = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_color = face_[y:y+h, x:x+w]
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex+ew, ey+eh), (0, 255, 0), 2)
            for (ex, ey, ew, eh) in nose:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex+ew, ey+eh), (255, 255, 0), 2)
    return coords


def detect(img, img_id):
    coords = draw_boundary(img)
    if len(coords) == 4:
        roi_img = img[coords[1]:coords[1] +
                      coords[3], coords[0]:coords[0]+coords[2]]
        user_id = 1
        generate_dataset(roi_img, user_id, img_id)

    return img


video_capture = cv2.VideoCapture(-1)

# Initialize img_id with 0
img_id = 0

while True:
    if img_id % 50 == 0:
        print("Collected ", img_id, " images")
    _, img = video_capture.read()
    img = detect(img, img_id)
    cv2.imshow("train-session", img)
    img_id += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
