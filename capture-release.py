import cv2
import time 
import logging

#Basic logging set up 


logging.basicConfig(
        level = logging.INFO, 
        format='%(asctime)s\t%(levelname)s\t%(name)s\t\t%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
log = logging.getLogger('')

def getBrightness( capture ):
    try:
        brightness = capture.get( cv2.cv.CV_CAP_PROP_BRIGHTNESS )
        log.info('Received brightness %s' % str(brightness) )
    except Exception as e:
        log.exception(str(e))
        pass
        
def setBrightness( capture, setting):
    try:     
        capture.set( cv2.cv.CV_CAP_PROP_BRIGHTNESS, float(setting) )
        log.info('Tried to set brightness %s' % str(setting) ) 
    except Exception as e:
        log.exception(str(e))
        pass
        
        
def setExposure( capture, setting ):
    try:
        capture.set( cv2.cv.CV_CAP_PROP_EXPOSURE, setting )
        log.info('Tried to set exposure %s' % str(setting) ) 
    except Exception as e:
        log.exception(str(e))
        pass
            
def getExposure( capture ):
    try:
        exp = capture.get( cv2.cv.CV_CAP_PROP_EXPOSURE )
        log.info('Received exposure %s' % str(exp) )
    except Exception as e:
        log.exception(str(e))
        pass

#Capture and release
def run():
    cap = cv2.VideoCapture(2)

    #Check properties
    getExposure(cap)
    getBrightness(cap)


    framesElapsed = 0

    while True:
        ret = cap.grab()
        if ret: 
            ret1, frame = cap.retrieve()
            cv2.imshow('frame', frame)
   

        if framesElapsed == 0:
            start = time.time()
        else: 
            timeElapsed = time.time() - start
            fpsEstimate = framesElapsed / timeElapsed
            log.debug('fps estimate = %d' % fpsEstimate)
        framesElapsed += 1
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()















    




if __name__ == "__main__":
    run()
