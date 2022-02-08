# --{       Face Tracker V1       }--
# --{       Coded Tinkernut       }--
# --{ Updated by Parker Cranfield }--
# --{        Jan. 18, 2020        }--

# IMPORTS
import cv2
from time import sleep

# VARIABLES
cascPath = "haarcascade.xml" # Points to the haar cascade file
faceCascade = cv2.CascadeClassifier(cascPath) # Sets cascade file so openCV knows what it is
video_capture = cv2.VideoCapture(0) # start the camera

# SETUP FUNCTIONS
def set_res_720p():
	video_capture.set(3, 1280)
	video_capture.set(4, 720)

# SETUP VARIABLES
set_res_720p()

# MAIN VIDEO
def Video():
	sleep(0.1)  # Gives camera time to warm up
	while True: # start video frame capture loop

		# Take the frame, convert it to black and white, and look for facial features
		ret, frame = video_capture.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Use appropriate flag based on version of OpenCV
		if int(cv2.__version__.split('.')[0]) >= 3:
			cv_flag = cv2.CASCADE_SCALE_IMAGE
		else:
			cv_flag = cv2.cv.CV_HAAR_SCALE_IMAGE

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30),
			flags=cv_flag
		)

		# Draw green rectangle around each face
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		# Display the resulting image
		cv2.imshow('Video', frame)

		# Set "q" as the key to exit the program when pressed
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# STARTUP
if __name__ == "__main__":
	Video()

# Clear the stream capture
video_capture.release()
cv2.destroyAllWindows()