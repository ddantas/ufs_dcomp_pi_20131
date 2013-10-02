import cv2
import numpy

'''	Calcula parAmetros intrInsecos e extrInsecos de uma camera 
a partir de imagens com resoluCAo arbitrAria de um padrAo de calibraCAo 
com 8X9 cIrculos de largura e altura, respectivamente, obtida a partir da mesma camera.
E realiza a remoCAo das distorCOes radial e tangencial de imagens obtidas com essa camera '''

''' VariAveis Globais '''
camera_matrix = []
dist_coefs = []
rvecs = [] 
tvec = []
calibrated = False
num_patterns = None
img_patterns = []
pattern_size = (8,9)
cauht_patterns = False
image_points = []
width = 0
height = 0 


''' Calcula parAmetros intrInsecos e extrInsecos da camera '''
def calibrate(): 

	global camera_matrix
	global dist_coefs
	global rvecs 
	global tvec 
	global calibrated
	global pattern_size
	global cauht_patterns 
	global image_points
	global width
	global height
	global num_patterns
	
	if not cauht_patterns:
		print 'The parameters are not yet caught.'
		return 0
	''' Inicializa uma variAvel necessAria para obtenCAo das cordenadas dos
	pontos dos objeto '''
	object_points = []	
	''' Gera as cordenadas dos pontos dos objeto '''
	pattern_points = numpy.zeros( ( numpy.prod(pattern_size) , 3) , numpy.float32 ) 
	pattern_points [:,:2] = numpy.indices(pattern_size).T.reshape(-1,2)
	''' Inclui as cordenadas dos pontos dos objeto em uma lista individual '''
	counter0 = num_patterns 
	while(counter0):
		object_points.append(pattern_points)
		counter0 = counter0 -1
	''' Calcula parAmetros intrInsecos e extrInsecos da camera alEm dos vetores de rotaCAo e translaCAo '''
	rms, camera_matrix, dist_coefs, rvecs, tvec = cv2.calibrateCamera( object_points, image_points,(width, height) )
	'''Muda o status da camera para calibrada'''
	calibrated = True
	

''' Corrige as distorCOes radial e tangencial da imagem de entrada e grava o resultado em um arquivo de saIda cujo diretOrio E dado '''
def correct_image(src_name,dst_name):

	global camera_matrix
	global dist_coefs
	global calibrated

	''' Verifica se a camera jA foi calibrada '''
	if not calibrated:
		print 'Camera has not been calibrated'
		return False
	''' LE a imagem de entrada '''
	in_image = cv2.imread(src_name)

	''' Corrige as distorCOes da imgem '''
	out_image = cv2.undistort(in_image, camera_matrix, dist_coefs)

	''' Grava a imagem resultante '''
	ok = cv2.imwrite(dst_name,out_image)

	return ok		

''' Retorna parAmetros intrInsecos e extrInsecos de uma camera '''	
def get_cam_parameters():

	''' Verifica se a camera jA foi calibrada '''
	if not calibrated:
		print 'Camera has not been calibrated'

	return camera_matrix, dist_coefs, rvecs, tvec

def get_patterns(cam_id, number_patterns):

	global pattern_size
	global num_patterns
	global image_points
	global height
	global width
	global cauht_patterns
	
	capture = cv2.VideoCapture(cam_id)
		
	cv2.namedWindow('Cam',1)
	capture.set(3,1280) 
	capture.set(4,960)
	counter = 0
		
	while (number_patterns > counter):
		
		ok, img = capture.read()
		im = img
		''' ObtEm a resoluCAo das imagens '''
		height, width = img.shape[:2]
		''' Encontra as cordenadas dos centros dos circulos da grade '''
		pattern_found, centers = cv2.findCirclesGrid(img,pattern_size,flags = cv2.CALIB_CB_SYMMETRIC_GRID)
		cv2.drawChessboardCorners(img, pattern_size, centers, pattern_found)
		cv2.imshow('Cam',img)
		val = cv2.waitKey(1)
		if (val == 27):
			print'Capture Process Aborted'
			break
		if ( (val == 99) and ( pattern_found )):
			img_patterns.append(im)
			image_points.append(centers.reshape(-1,2))
			print'%snd Image Captured.' % (counter + 1)
			counter = counter + 1	
	num_patterns = number_patterns
	cauht_patterns = True
	cv2.destroyWindow('Cam')

def print_cam_parameters():	

	global camera_matrix 
	global dist_coefs
	
	print'\n'
	print'Camera Matrix: \t', camera_matrix 
	print'\n'
	print'Distortion Coeficients: \t', dist_coefs
	
def show_res_calib():

	global calibrated
	global img_paterns
	global camera_matrix
	global dist_coefs
	
	if not calibrated:
		print 'Camera has not been calibrated'
		return 0
	cv2.namedWindow('1nd Image',1)
	dst_image = cv2.undistort(img_patterns[0], camera_matrix, dist_coefs)
	
	cv2.imshow('1nd Image', dst_image)
	cv2.waitKey(0)
		
	
'''if __name__ == '__main__':
	
	get_patterns(0,20)
	calibrate()
	correct_image('d:/d/grade_o.jpg','d:/d/grade_c.jpg')
	print_cam_parameters()	
	show_res_calib()'''
	
