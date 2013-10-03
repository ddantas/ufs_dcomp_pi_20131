import cv2
import numpy

'''	Calcula parAmetros intrInsecos e extrInsecos de uma camera 
a partir de uma imagem com resoluCAo arbitrAria de um tabuleiro de xadrez 
com 10X7 quadrados de largura e altura, respectivamente, obtida a partir da mesma camera. '''

''' VariAveis Globais '''
camera_matrix = []
dist_coefs = []
rvecs = [] 
tvec = []
calibrated = False


''' Realiza a correCAo da distorCAo radial e tangencial e retorna um tuple 
indicando o sucesso ou nAo da calibraCAo da camera assim 
como a imagem do tabuleiro de chadrez corrigida '''
def calibrate(src_image_name): 
	
	global camera_matrix
	global dist_coefs
	global rvecs 
	global tvec 
	global calibrated
	
	''' Inicializa algumas variAveis necessArias para obtenCAo das cordenadas dos
	pontos dos objetos '''
	pattern_size = (9,6)
	square_size = 1.0
	object_points = []
	image_points = []
	width = 0
	height = 0 
	
	''' LE a imagem de entrada '''
	src_image = cv2.imread(src_image_name)
	
	''' ObtEm a resoluCAo da imagem '''
	height, width = src_image.shape[:2]
	''' Gera as cordenadas dos pontos dos objetos '''
	pattern_points = numpy.zeros( ( numpy.prod(pattern_size) , 3) , numpy.float32 ) 
	pattern_points [:,:2] = numpy.indices(pattern_size).T.reshape(-1,2)
	pattern_points *= square_size
	''' Realiza a converSAo da imagem de entrada para Escala de cinza com profundidade de 8 bits '''
	gray_image = cv2.cvtColor(src_image, cv2.COLOR_RGB2GRAY)
	
	''' Encontra as cordenadas dos cantos dos quadrados internos do tabuleiro de xadrez '''
	val,corners = cv2.findChessboardCorners(gray_image , pattern_size) 
	
	''' Refina as cordenadas dos cantos dos quadrados internos do tabuleiro de xadrez '''
	term = ( cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1 )
	cv2.cornerSubPix(gray_image, corners, (5, 5), (-1, -1), term)
	
	''' Testa se foi possIvel encontrar as cordenadas dos cantos dos quadrados internos	
	do tabuleiro de xadrez. Se foi possIvel, prossegue com a calibraCAo. SenAo, 
	interrompe a execuCAo e exibe mensagem de erro'''
	if val:
		
		''' Inclui as cordenadas dos pontos dos objetos e as da imagem depois de remoldadas, em listas individuais '''
		image_points.append(corners.reshape(-1,2))
		object_points.append(pattern_points)
		''' Calcula parAmetros intrInseco e extrInsecos da camera alEm dos vetores de rotaCAo e translaCAo '''
		rms, camera_matrix, dist_coefs, rvecs, tvec = cv2.calibrateCamera( object_points, image_points,(width, height) )
		''' Reliza a correCAo da distorCAo da imagem fornecida. Gerando dois mapas a partir dos parAmetros dados e 
		remapeando cada pixel da imagem de entrada para a sua verdadeira posiCAo na imagem de saIda atravEs desses mesmos mapas '''
		dst_image = cv2.undistort(src_image, camera_matrix, dist_coefs)
		'''Muda o status da camera para calibrada'''
		calibrated = True
		''' Exibe mensagem de erro caso nAo tenha sido possIvel encontrar as cordenadas dos cantos dos quadrados internos	
		do tabuleiro de xadrez '''
	else:
		
		print "The Program can not correct the image"
	
		''' Retorna a imagem corrigida e o status da operaCAo '''
	return val, dst_image
	
	
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