import tkinter as tk
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x400')
        self.root.title("Login/Register App")
        self.root.configure(bg='#333333')
        # burlywood2

        # Add label above buttons
        self.btn_label = tk.Label(root, text="Choose an option:", font=('Arial', 19), bg='#333333', fg='white')
        self.btn_label.pack(pady=40)

        # Login button
        self.btn_login = tk.Button(root, text="Login", command=self.login, font=('Arial', 15), bg='darkslateblue', fg='white', bd=0, padx=8, pady=4)
        self.btn_login.pack(pady=40)

        # Register button
        self.btn_register = tk.Button(root, text="Register", command=self.open_register_window, font=('Arial', 15), bg='darkslateblue', fg='white', bd=0, padx=8, pady=4)
        self.btn_register.pack()

    def login(self):
        # Implement your login functionality here
        
        path = 'imagesAttendance'
        images = []
        classNames = []
        myList = os.listdir(path)
        print(myList)

        for cl in myList:
            curImg = cv2.imread(os.path.join(path, cl))
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])

        print(classNames)

        def findEncodings(images):
            encodingList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encodeImg = face_recognition.face_encodings(img)[0]
                encodingList.append(encodeImg)
            return encodingList


        def markAttendance(name):
            with open('Attendance.csv', 'r+') as f:
                myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                
                if name not in nameList:
                    now = datetime.now()
                    dateString = now.strftime('%Y-%m-%d %H:%M:%S')
                    f.writelines(f'\n{name},{dateString}')



        encodeListKnown = findEncodings(images)
        print('Encoding Complete')

        cap = cv2.VideoCapture(0)

        wait_time = 1000

        while True:

            keyCode = cv2.waitKey(wait_time)
            if (keyCode & 0xFF) == ord("q"):
                cv2.destroyAllWindows()
                break

            success, img = cap.read()
            imgSmall = cv2.resize(img, (0,0), None, 0.25, 0.25)
            imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

            facesCurrFrame = face_recognition.face_locations(imgSmall)
            encodeCurrFrame = face_recognition.face_encodings(imgSmall, facesCurrFrame)

            for encodeFace, faceLoc in zip(encodeCurrFrame, facesCurrFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
                    cv2.rectangle(img, (x1,y2-35), (x2, y2), (0,255,0), cv2.FILLED)
                    cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
                    markAttendance(name)


            cv2.imshow('Webcam', img)
            cv2.waitKey(1)


    def open_register_window(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register")
        register_window.geometry('450x350')
        register_window.configure(bg='burlywood2')

        # Name input field
        self.name_entry_label = tk.Label(register_window, text="Name:", font=('Arial', 14), bg='burlywood2')
        self.name_entry_label.pack(pady=30)

        self.name_entry = tk.Entry(register_window, bd=0, font=('Arial', 10))
        self.name_entry.pack(pady=10)

        # Capture button
        self.btn_capture = tk.Button(register_window, text="Capture", command=self.capture_name, font=('Arial', 10) , bd=0, padx=8, pady=4, bg='ghostwhite')
        self.btn_capture.pack(pady=20)

    def capture_name(self):
        # Implement your functionality for capturing the name here
        name = self.name_entry.get()
        print(f"Captured Name: {name}")

        cam_port = 0
        cam = cv2.VideoCapture(cam_port)

        result, image = cam.read()

        if result:
            cv2.imshow("Capture", image)

            path = 'imagesAttendance'
            if not os.path.exists(path):
                os.makedirs(path)

            cv2.imwrite(os.path.join(path, f'{name}.jpg'), image)

            # src_path = r"C:\Mr.Robot\PythonProjects\face-recognition"
            # src_path += f"{name}.jpg"
            # dst_path = r"C:\Mr.Robot\PythonProjects\face-recognition\imagesAttendance"

            # shutil.move(src_path, dst_path)

            cv2.waitKey(3000)
            cv2.destroyWindow("Capture")
        else:
            print("No Image detected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
