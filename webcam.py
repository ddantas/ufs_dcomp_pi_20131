# -*- coding: cp1252 -*-
#module to takepictures, setting their names and save a picture for its position
#para modificar o path é preciso toma cuidado com o contraba'\'
#em python ele é usado quando se quer por caracter especial, como "'" ou " " ", ou 
## o proprio contrabarra. para especificar o caminho vc usa o contrabarra duas vezes:
####para caminho relativo:
# path = "E:\\pasta1\\pasta2" 
##para caminho absoluto
##path = "E:\\pasta1\\pasta2\\" 



import cv2

class WebCam():
    
    """"construtor da cl
        recebe como parâmetros o ID da camera, o tamanho padrão das fotos, o path e o filename

    """
    def __init__(self, cameraId = 0, path = "", filename = "img-%03d-%03d.jpg"):
        self.setPath(path)
        self.setFileName(filename)
        self.setCameraId(cameraId)
            

    """set the image path"""
    
    def setPath(self, path):
        if not (path  == ""):
            contrabarra= "\\"
            if not (path[len(path)-1]== contrabarra):
                path = path + contrabarra
        self.path = path
        
    """set the image filename"""
    def setFileName(self, filename):
        self.filename = filename
                
    """take picures and save it on a file, the file name and path,
        could be the deault or the chose"""
    def takePicture(self, i, j):
        camera = cv2.VideoCapture(self.cameraId)
        realease, picture = camera.read()
        realease, picture = camera.read()
        
        
        if (type(i)==int) and (type(j)==int):
            caminho = self.path + (self.filename % (i,j))
        else:
            caminho = i + j
        
        cv2.imwrite(caminho, picture)
        

    """set the cam id"""
    def setCameraId(self, cameraId):
        self.cameraId = cameraId

    """returns the filename"""
    def getFileName(self):
        return self.filename

    """"retrurn the actual path"""
    def getPath(self):
        return self.path

    """give the camera ID"""
    def getCameraId(self):
        return self.cameraId
