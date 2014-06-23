import logging
import cv2

logging.basicConfig(
        level = logging.INFO, 
        format='%(asctime)s\t%(levelname)s\t%(name)s\t\t%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

log = logging.getLogger('prop')

#### Properties to test

### Resolution 
def getResolution( capture ):
    try: 
        w = capture.get ( cv2.cv.CV_CAP_PROP_FRAME_WIDTH )
        h = capture.get ( cv2.cv.CV_CAP_PROP_FRAME_HEIGHT )
        log.info( 'Received resolution\t%s x %s' % (str(w), str(h)) )
    except Exception as e:
        log.exception(str(e))
        pass
    


### Frames per second
def getFPS( capture ):
    try:
        fps = capture.get( cv2.cv.CV_CAP_PROP_FPS )
        log.info('Received fps\t%s' % str(fps) )
    except Exception as e:
        log.exception(str(e))
        pass

### Contrast    
def getContrast( capture ):
    try:
        value = capture.get( cv2.cv.CV_CAP_PROP_CONTRAST )
        log.info('Received contrast\t%s' % str(value) )
    except Exception as e:
        log.exception(str(e))
        pass
        
def setContrast( capture, setting):
    try:     
        capture.set( cv2.cv.CV_CAP_PROP_CONTRAST, float(setting) )
        log.info('Tried to set contrast\t%s' % str(setting) ) 
    except Exception as e:
        log.exception(str(e))
        pass

###  Saturation
def getSaturation( capture ):
    try:
        value = capture.get( cv2.cv.CV_CAP_PROP_SATURATION )
        log.info('Received saturation\t%s' % str(value) )
    except Exception as e:
        log.exception(str(e))
        pass
        
def setSaturation( capture, setting):
    try:     
        capture.set( cv2.cv.CV_CAP_PROP_CONTRAST, float(setting) )
        log.info('Tried to set saturation\t%s' % str(setting) ) 
    except Exception as e:
        log.exception(str(e))
        pass


### Brightness    
def getBrightness( capture ):
    try:
        brightness = capture.get( cv2.cv.CV_CAP_PROP_BRIGHTNESS )
        log.info('Received brightness\t%s' % str(brightness) )
    except Exception as e:
        log.exception(str(e))
        pass
        
def setBrightness( capture, setting):
    try:     
        capture.set( cv2.cv.CV_CAP_PROP_BRIGHTNESS, float(setting) )
        log.info('Tried to set brightness\t%s' % str(setting) ) 
    except Exception as e:
        log.exception(str(e))
        pass
        
### Exposure        
def setExposure( capture, setting ):
    try:
        capture.set( cv2.cv.CV_CAP_PROP_EXPOSURE, setting )
        log.info('Tried to set exposure\t%s' % str(setting) ) 
    except Exception as e:
        log.exception(str(e))
        pass
            
def getExposure( capture ):
    try:
        exp = capture.get( cv2.cv.CV_CAP_PROP_EXPOSURE )
        log.info('Received exposure\t%s' % str(exp) )
    except Exception as e:
        log.exception(str(e))
        pass
