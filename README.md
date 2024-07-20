# Face Recognition Attendance App

## Description

This is an attendance application that uses OpenCV and face-recognition libraries. Users can register with their name and take a photo. Upon logging in, the camera will recognize their face and display their name if they have registered before. The application logs the name and time of login into an `Attendance.csv` file.

## Features

- **User Registration:** Capture a photo of the user and save it for future recognition.
- **User Login:** Recognize the user from the captured photo and log the login time.
- **Face Recognition:** Uses OpenCV and face-recognition libraries to detect and recognize faces.
- **Attendance Logging:** Records the user's name and login time in `Attendance.csv`.

## Technologies and Libraries Used

- **Python 3.x**
- **Tkinter:** For the graphical user interface.
- **OpenCV:** For image processing and video capture.
- **face-recognition:** For face detection and recognition.
- **NumPy:** For numerical operations.
- **OS:** For directory operations.
- **Datetime:** For timestamping the login times.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Libraries

Install the required libraries using pip:

```sh
pip install tkinter opencv-python numpy face-recognition
```

## Usage

### Running the Application
1. Clone the repository:

```sh
git clone "https://github.com/YoussefMoustafaa/face_reco_attendance_app.git"
```

2. Run the application:

```sh
python app.py
```

### Using the Application

1. Register a User:

. Click the "Register" button.

. Enter the user's name in the provided field.

. Click the "Capture" button to take a photo.

2. Login:

. Click the "Login" button.

. The application will use the webcam to detect and recognize the user's face.

. If the user is recognized, their name will be displayed on the screen, and their login time will be logged in Attendance.csv.
