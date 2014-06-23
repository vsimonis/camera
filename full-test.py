import cv2
import time 
import logging
import prop as p
#Basic logging set up 


logging.basicConfig(
        level = logging.INFO, 
        format='%(asctime)s\t%(levelname)s\t%(name)s\t\t%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

log = logging.getLogger('')


#Capture and release
def run():
    cap = cv2.VideoCapture(2)

    #Check properties
    p.getExposure(cap)
    p.getBrightness(cap)
    p.getContrast(cap)
    p.getSaturation(cap)
    p.getFPS(cap)
    p.getResolution(cap)

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
            if int(timeElapsed) % 10 == 0:
                log.info('fps estimate = %d' % fpsEstimate)
        framesElapsed += 1
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
