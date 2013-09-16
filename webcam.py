#module to takepictures, setting their names and save a picture for its position
import cv

##é preciso definir ainda que camera se usará....
##a especificacao da camera nao é dificil mas fica como duvida
#o modulo esta praticamente pronto faltando tirar apenas algumas duvidas
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

        capture = cv.CaptureFromCAM(self.cameraId)

        cv.QueryFrame(capture)
        picture = cv.QueryFrame(capture)
        
        
        
        if (type(i)==int) and (type(j)==int):
            caminho = self.path + (self.filename % (i,j))
        else:
            caminho = i + j
        
        cv.SaveImage(caminho, picture)
        print "aqui"

    """set the cam id"""
    def setCameraId(self, cameraId):

        self.cameraId = cameraId           
            
