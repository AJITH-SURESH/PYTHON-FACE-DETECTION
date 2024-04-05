import cv2
import face_recognition
import os
import datetime

# Define the directory where your known faces are stored
known_faces_dir = "/Users/ajith_04/Documents/AJ/Cs/projects/students"

# Create a list to store known face encodings and corresponding names
known_face_encodings = []
known_face_names = []

# Load known faces and their names from the directory
for filename in os.listdir(known_faces_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        name = os.path.splitext(filename)[0]
        image_path = os.path.join(known_faces_dir, filename)
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            known_face_encodings.append(face_encodings[0])
            known_face_names.append(name)

# Create or open the attendance file
attendance_file = "attendance.txt"
try:
    with open(attendance_file, "a") as file:
        pass
except Exception as e:
    print("Error creating or opening attendance file:", str(e))

# Create a set to keep track of recognized faces
recognized_faces = set()

# Capture video from the default camera (you may need to specify a different source)
video_capture = cv2.VideoCapture(0)

# Define the number of students you want to recognize and mark attendance for
num_students = 4
students_detected = [False] * num_students  # Keeps track of whether each student has been detected

while True:
    # Capture a frame
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through the face encodings found in the current frame
    for face_encoding in face_encodings:
        # Compare the face encoding to known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)

        # Initialize the name as "Unknown" by default
        name = "Unknown"

        # Check if any known face is found in the current frame
        if any(matches):
            # Get the first recognized name
            name = known_face_names[matches.index(True)]

            # Check if the face has not been recognized before
            if name not in recognized_faces:
                # Write attendance record to the file
                try:
                    with open(attendance_file, "a") as file:
                        now = datetime.datetime.now()
                        date_string = now.strftime("%Y-%m-%d %H:%M:%S")
                        attendance_record = f"{name}, {date_string}\n"
                        file.write(attendance_record)
                        print("Attendance Recorded(present):", attendance_record)
                        recognized_faces.add(name)  # Add to recognized faces set
                        
                        # Mark the student as detected
                        if name == "student1":
                            students_detected[0] = True
                        elif name == "student2":
                            students_detected[1] = True
                        elif name == "student3":
                            students_detected[2] = True
                        elif name == "student4":
                            students_detected[3] = True
                except Exception as e:
                    print("Error writing attendance record:", str(e))

    # Display the frame with recognized names
    for (top, right, bottom, left), name in zip(face_locations, [name] * len(face_locations)):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Check if all students have been detected and mark attendance
    if all(students_detected):
        print("All students have been detected and attendance marked.")
        break

    # If 'q' is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV window
video_capture.release()
cv2.destroyAllWindows()
