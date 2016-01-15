# This code gets the frames from the Pi camera for streaming.
# It was partially taken from  http://www.chioka.in/python-live-video-streaming-example/
# and from www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
#
# ARW 1/4/2016

import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        # self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
        # --------------- ARW -------------
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))
        # Get a generator object that serves up the frames
        self.frame_gen = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)
         
    def __del__(self):
#        self.video.release()
        pass

    def get_frame(self):
        #success, image = self.video.read()
        #   We are using Motion JPEG, but OpenCV defaults to capture raw images,
        #   so we must encode it into JPEG in order to correctly display the
        #   video stream.
        #ret, jpeg = cv2.imencode('.jpg', image)
        #return jpeg.tobytes()
        # --------------- ARW -------------
        frame = self.frame_gen.next()                   # get next frame
        image = frame.array
        ret, jpeg = cv2.imencode('.jpeg', image )       # jpeg to buffer
        self.rawCapture.truncate(0)                     # clear stream in prep for next frame
        return jpeg.tobytes()
    
         
