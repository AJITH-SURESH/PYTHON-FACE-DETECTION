# PYTHON-FACE-DETECTION
 "Real-time face recognition attendance system in Python, utilizing OpenCV and face_recognition library to log attendance by detecting known faces and recording their names and timestamps in individual text files."
Face Recognition Attendance System

Overview:
This Python script utilizes the face recognition library to implement a real-time attendance system. The system captures video from the default camera and detects faces in the video stream. When a known face is recognized, the script records the attendance by appending the person's name and timestamp to a text file. Each recognized face has its own attendance file, making it convenient for tracking attendance of multiple individuals.

Features:
Face Detection: Utilizes the face_recognition library to detect faces in real-time video frames.
Attendance Logging: Records attendance by appending names and timestamps to individual text files for each recognized face.
Dynamic File Creation: Creates separate attendance files for each recognized face based on their name.
Customizable: Easily adaptable for different environments and use cases by adjusting parameters such as known faces directory and recognition tolerance.


Requirements:
Python 3.x;
OpenCV (cv2) library;
face_recognition library;


Usage:
Ensure Python and the required libraries are installed.
Place images of known faces in the specified directory (known_faces_dir).
Run the script.
The system will start capturing video from the default camera and recognize known faces.
Attendance records will be logged in individual text files named after recognized faces.
Additional Notes:
Adjust the known_faces_dir variable to point to the directory containing images of known faces.
Customize the tolerance parameter in face recognition to control recognition sensitivity.
Press 'q' to exit the video stream.


Credits:
Face recognition functionality is provided by the face_recognition library.
Video capture and display are facilitated by the OpenCV (cv2) library.
