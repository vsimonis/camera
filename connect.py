import cv2
import time 

capSource = 1
capWindow = 'window'
capMirrored = False
capResolution = ()
framesElapsed = 0
start = 0 

#Capture and release
def run( self ):
    cap = cv2.VideoCapture(capSource, 
                           capWindow, 
                           capMirrored, 
                           capResolution)

    window = cv2.namedWindow('window')

    while True:
        #ret, frame = cap.read()      
        ret = cap.grab()
        if ret: 
            ret1, frame = cap.retrieve()
   
        window.show(frame)
        if framesElapsed == 0:
            start = time.time()
        else: 
            timeElapsed = time.time() - start
      self._cap.exitFrame()
            self._rawWindow.processEvents()
            logt.info('processing: %0.6f' % (time.time() - t1))
