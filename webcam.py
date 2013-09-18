# -*- coding: cp1252 -*-
#module to takepictures, setting their names and save a picture for its position
import cv2

class WebCam():
    
    """"constructor
        recieve the camera ID, picture default size, path and filename

    """
    def __init__(self, cameraId = 0, size = 500, path = "", filename = "img-%03d-%03d.jpg"):
        self.setPath(path)
        self.setFileName(filename)
        self.setCameraId(cameraId)
        self.size = size
        

    """set the image path"""
    def setPath(self, path):
        if not (path  == ""):
            contrabarra= "\\"
            if not (path[len-1]== contrabarra):
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
        

        cv2.imwrite("teste.jpg", picture)
        
        picture = self.setSize(picture)
        
        
        if (type(i)==int) and (type(j)==int):
            caminho = self.path + (self.filename % (i,j))
        else:
            caminho = i + j
        
        cv2.imwrite(caminho, picture)
        

    """set the cam id"""
    def setCameraId(self, cameraId):
        self.cameraId = cameraId   

    """set the picture size to the default value"""                    
    def setSize(self, picture):
        size = self.size
        shape = picture.shape

        while (shape[0]< size) or (shape[1]< size):
            size  = size - 100
        
        dy = shape[0] - size
        dx = shape[1] - size
        iy1 = dy/2
        iy2 = shape[0] - dy/2

        ix1 = dx/2
        ix2 = shape[1] - dx/2
           
            
        pc1 = picture[iy1:iy2]
        pc2 = picture.copy()
        pc2.resize((size,size,3), refcheck = True)

        for i in range(size):
            pc2[i] = pc1[i][ix1:ix2]
        

        return pc2    

    
        
        
                
