from comics import GetComics
from brightness import setBrightness
from bacha import getage
from getOUT import showAlert
import face_recognition
import cv2
from apscheduler.schedulers.background import BackgroundScheduler
import ctypes
from datetime import datetime
from PIL import Image, ImageStat
import wmi
value = 0

def brightness():
    setBrightness(value)

def whatage():
    try:
        if getage() < 15:
            print("BACHA SPOTTED: ")
            startTime = 0
            ctypes.windll.user32.LockWorkStation()
    except:
        print("Bag image caught")

# def dostuff():
def capture_video():
    video_capture = cv2.VideoCapture(0)
    user_image = face_recognition.load_image_file("training/ashish1.jpg")
    bachaImage = face_recognition.load_image_file("training/pp.jpg")
    user_face_encoding = face_recognition.face_encodings(user_image)[0]
    bacha_face_encoding = face_recognition.face_encodings(bachaImage)[0]
    known_faces = [
        user_face_encoding,
        bacha_face_encoding
    ]
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    flag = False
    startTime = 0
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im)
        stat = ImageStat.Stat(pil_im)
        value = int(stat.mean[0])
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(small_frame)
            # print(face_locations)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                match = face_recognition.compare_faces(known_faces, face_encoding)
                name = "Unknown"

                if match[0]:
                    name = "Ashish"
                    flag = False
                    startTime = datetime.now()
                elif match[1]:
                    print("BACHA DETECTED BYE BYE")
                    # LOCK Computer
                else:
                    flag = True
                    cv2.imwrite("bacha.jpg", frame)
                    whatage()
                    # p.daemon = True
                face_names.append(name)

        process_this_frame = not process_this_frame
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)
        if flag and type(startTime) != 0:
            timenow = datetime.now()
            seconds = (timenow - startTime).total_seconds()
            if seconds > 30:
                flag = False
                ctypes.windll.user32.LockWorkStation()

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
