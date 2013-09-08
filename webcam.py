#module to takepictures, setting their names and save a picture for its position
import cv

class WebCam():
    
    
    def __init__(self, cameraId = 0, path = "", filename = "img-%03d-%03d.jpg"):
        self.setPath(path)
        self.setFileName(filename)
        self.setCameraId(cameraId)
        

    """set the image path"""
    def setPath(self, path):
        self.path = path
        
    """set the image filename"""
    def setFileName(self, filename):
        self.filename = filename
    """take picures and save it on a file, the file name and path,
        could be the deault or the chose"""
    def takePicture(self, i, j):
        
        picture = self.picture(self.cameraId)
        
        if (type(i)==int) and (type(j)==int):
            caminho = self.path + (self.filename % (i,j))
        else:
            caminho = i + j
        cv.SaveImage(caminho, picture)
        

    """set the cam id"""
    def setCameraId(self, cameraId):
        withoutCams = -1
        # ajustando 0 como camera padrao
        self.cameraId = 0
        if self.getNumCams() == withoutCams:
            print "Without enable cams. Connect a camera please"
        elif (self.getNumCams() <= cameraId):
            print "without cams to the selected ID!"
        else:
            self.cameraId = cameraId
            
        
            
            

    """this function take a picture from a cam id, if there is no enable cam
        it return None"""
    def picture(self, cameraId):
        capture = cv.CaptureFromCAM(cameraId)

        picture = cv.QueryFrame(capture)
        picture = cv.QueryFrame(capture)
        
        return picture
        
    """enable cams number
        -1 -> indicates no enable cams"""
    def getNumCams(self):

        i = -1
        while self.picture(i+1):
            i = i + 1
            
        return i - 1
        
