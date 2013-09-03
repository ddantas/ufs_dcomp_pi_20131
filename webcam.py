#module to takepictures, setting their names and save a picture for its position
import cv

##é preciso definir ainda que camera se usará....
##a especificacao da camera nao é dificil mas fica como duvida
#o modulo esta praticamente pronto faltando tirar apenas algumas duvidas
class WebCam():

    def __init__(self, path = "", filename = "img-%03d-%03d.jpg" ):
        self.path = path
        self.filename = filename
        


    def setPath(self, path):
        self.path = path
    
    def setFileName(self, filename):
        self.filename = filename

    def takePicture(self, i, j):
        capture = cv.CaptureFromCAM(0)
        picture = cv.QueryFrame(capture)
        if (type(i) == int):
            caminho = self.path + (self.filename % (i,j))
        else:
            caminho = i + j
        cv.SaveImage(caminho, picture)
        
