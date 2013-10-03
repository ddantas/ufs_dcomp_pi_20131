########################################################################################################################
#                                                                                                                      #
# VERSÃO 2.0 = TIRANDO FOTOS A PARTIR DOS PICS I E PICS J, FALTA CHAMAR O CÓDIGO DO MOTOR DE PASSOS                    #
#                                                                                                                      #
########################################################################################################################

from Tkinter import *
import Image, ImageTk
import tkMessageBox 
import ttk 
import SQLite 
import os
import webcam
import cv2
import numpy
import unicodedata
import shutil


#Instanciando as Classes Tkinter e Webcam
root = Tk()
cam = webcam.WebCam(0,"","img-%03d-%03d.jpg")


################################################# FUNCOES DO BANCO DE DADOS ######################################################

banco = SQLite.DataBase()

def iniciarbd(): #ok
	#c['values']= ['1','2']
	#banco.deletarValor("Dinho")
	
	global master
	master = Tk()
	global c
	c = ttk.Combobox(master,width=100) 
	c.pack() 
	atualizarComboList()
	#c['values'] = ['1','2','3']

	botaoDeletar = Button(master, text='Deletar', command=deletarDoBanco) 
	botaoDeletar.pack()

	botaoCarregar = Button(master, text='Carregar', command=carregarDoBanco) 
	botaoCarregar.pack() 

	#botaoInserir = Button(root, text='Inserir', command=inserirNoBanco('10','10','10','10','C:/Users','Fotos6')) 
	#botaoInserir.pack() 

	master.mainloop()
	
def atualizarComboList(): #serve tanto para inicializar a comobo list como para atualiza-la depois de uma exclusao no banco de dados #ok
	registros = banco.consultarBanco()
	cont = 0
	list = []
	registrosString = str(registros[0][0]) + ", "		+ str(registros[0][1]) + ", " + str(registros[0][2])+ ", " + str(registros[0][3])+ ", '" + str(registros[0][4])+ "', " + str(registros[0][5])
	print registrosString
	for i in registros:
		registrosString = str(registros[cont][0]) + ", "		+ str(registros[cont][1]) + ", " + str(registros[cont][2])+ ", " + str(registros[cont][3])+ ", '" + str(registros[cont][4])+ "', " + str(registros[cont][5])
		list.append(registrosString)
		cont = cont + 1
	print list
	c['values'] = list
	
	#registros = banco.consultarBanco()
	#print registros
	#for i in registros:
	#	c['values'] = registros

def carregarDoBanco(): #carrega uma tupla em uma lista para os textboxs da tela principal #ok
        global listaBD 
        listaBD = []
        try: 
                tupla = c.get()#pega a tupla selecionada no comobox em forma de vetor de caracteres

                # tupla.find('\'') pega a primeira ocorrencia de aspa na tupla
                # tupla.rfind('\'') pega a ultima ocorrencia de aspa na tupla
                diretorio = getDiretorio(tupla)

                listaBD.append(banco.consultarColuna(diretorio,1)[0][0]) #pega o valor da primeira coluna da tupla
                listaBD.append(banco.consultarColuna(diretorio,2)[0][0]) #pega o valor da segunda coluna da tupla
                listaBD.append(banco.consultarColuna(diretorio,3)[0][0]) #pega o valor da terceira coluna da tupla
                listaBD.append(banco.consultarColuna(diretorio,4)[0][0]) #pega o valor da quarta coluna da tupla
                listaBD.append(banco.consultarColuna(diretorio,5)[0][0]) #pega o valor da quinta coluna da tupla
                listaBD.append(banco.consultarColuna(diretorio,6)[0][0]) #pega o valor da sexta coluna da tupla
                preencherTextos()
                path = diretorio+"\\"+listaBD[5]

                path = unicodedata.normalize('NFKD', path).encode('ascii','ignore')
                print path % (0,0)
                a = "images\project1\img-000-000.jpg"
                carregaImagens(listaBD[2],listaBD[3],path)
                master.destroy()
                #print c.get()
        except:
                tkMessageBox.showerror("Error3", "Selecione uma opcao valida!")
		

def deletarDoBanco(): #deleta a tupla selecionada tanto da combolist como do banco de dados 
	#c.event_generate('<Button-1>') 
	#c.set('null')
	tupla = c.get()#pega a tupla selecionada no comobox em forma de vetor de caracteres
	diretorio = getDiretorio(tupla)
	# tupla.find('\'') pega a primeira ocorrencia de aspa na tupla
	# tupla.rfind('\'') pega a ultima ocorrencia de aspa na tupla
	print "----------" + diretorio + "-------------"
	shutil.rmtree(diretorio)
	banco.deletarValor(diretorio)
	atualizarComboList()

def inserirNoBanco(stepi,stepj,picturei,picturej,diretorio,nomeimg): #recebe 4 valores do textbox (devem ser valores inteiros), o diretorio, o nome do projeto 
	banco = SQLite.DataBase()
	resultado = banco.inserir(int(stepi),int(stepj),int(picturei),int(picturej),diretorio,nomeimg)
	if resultado == 1:
		tkMessageBox.showinfo("Salvo", "Projeto salvo com sucesso!")
	else:
		tkMessageBox.showerror("Erro", "Projeto ja existe. Salve o projeto com outro nome!")

def getDiretorio(tupla):#ok
	inicio = tupla.find('\'')+1
	cont = 0
	char = tupla[inicio]
	while char != '\'': #DESSA FORMA O DIRETORIO NAO PODE TER NENHUMA ASPA
		cont = cont + 1
		char = tupla[inicio+cont]
	fim = inicio + cont
	diretorio = tupla[inicio:fim]
	return diretorio

def novoProjetoPadrao():
	banco = SQLite.DataBase()
	list = []
	list = banco.novoProjetoPadrao()
	return list
	
##################################FIM BANCO DE DADOS##################################################################### 	

################################# FUNÇÕES DA INTERFACE GRÁFICA ##########################################################

#Funcao para Abrir a Tela do Banco de Dados
def newProject():
	list = []
	list = novoProjetoPadrao()
	v.set("")
	w.set("")
	y.set("")
	z.set("")
	f7.set(list[0])
	f8.set(list[1])
	print list

	frame = Frame(root, bd=2, width=400,height=400,background="Red")
	frame.place(x=10,y=10)

	frame.grid_rowconfigure(0, weight=1)
	frame.grid_columnconfigure(0, weight=1)

	xscrollbar = Scrollbar(frame,orient=HORIZONTAL)
	xscrollbar.grid(row=1, column=0, sticky=E+W)


	yscrollbar = Scrollbar(frame)
	yscrollbar.grid(row=0, column=1, sticky=N+S)

	canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
	canvas.grid(row=0, column=0, sticky=N+S+E+W)

	img = ImageTk.PhotoImage(Image.open("branco.jpg"))
	label = Label(image=img)
	label.image = img # keep a reference!
        
	canvas.create_image(0,0,image=img, anchor="nw")
        
	canvas.config(scrollregion=canvas.bbox(ALL),width=750,height=430)

	xscrollbar.config(command=canvas.xview)
	yscrollbar.config(command=canvas.yview)
        

#Funcao para salvar os valores no Banco de Dados
def saveProject():
	list = []
	list = getCampos()
	print list
	inserirNoBanco(list[0],list[1],list[2],list[3],list[4],list[5])

#Funcao para verificar se os valores de entrada sao validos
def validarCampos():
	
	textStepsi = v.get()
	textStepsj = w.get()
	textPicsi = y.get()
	textPicsj = z.get()
	diretorio = f7.get()
	imagens = f8.get()

	if textStepsi.isdigit() and textStepsj.isdigit() and textPicsi.isdigit() and textPicsj.isdigit(): #and diretorio.isdigit() and imagens.isdigit():
		text1 = int(textStepsi)
		text2 = int(textStepsj)
		text3 = int(textPicsi)
		text4 = int(textPicsj)
		if text1>255 or text1<0 or text2>255 or text2<0 :
			print text1
			tkMessageBox.showerror("Error2", "Please enter a value between 0-255")
			clicked_wbbalance()
		elif text1<255 and text1>0 and text1<255 and text1>0:
				
			tkMessageBox.showinfo("Validacaoo","Valores validados com sucesso!")
			os.mkdir(diretorio)
			testarWeb()
			getCampos()
			saveProject()
			pass
	
	else:
		tkMessageBox.showerror("Error1", "A entrada nao eh um numero inteiro!")
						
        
#Funcao para pegar os valores dos TextBoxes
def getCampos():
	textStepsi = v.get()
	textStepsj = w.get()
	textPicsi = y.get()
	textPicsj = z.get()
	diretorio = f7.get()
	imagens = f8.get()

	list = []
	list.append(textStepsi)
	list.append(textStepsj)
	list.append(textPicsi)
	list.append(textPicsj)
	list.append(diretorio)
	list.append(imagens)

	#tkMessageBox.showinfo("Validacao","Valores: " +list[0])
	print list
   

	return list

#Funcao para preencher os TextBoxes	
def preencherTextos():
        v.set(listaBD[0]) # TextBox Steps i
        w.set(listaBD[1]) # TextBox Steps j
        y.set(listaBD[2]) # TextBox Pictures i
        z.set(listaBD[3]) # TextBox Pictures j
        f7.set(listaBD[4])
        f8.set(listaBD[5])

#Funcao para carregar as imagens desejadas na tela
def carregaImagens(pici,picj,caminho):
        frame = Frame(root, bd=2, width=400,height=400,background="Red")
        frame.place(x=10,y=10)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)

        yscrollbar = Scrollbar(frame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)

        canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        canvas.grid(row=0, column=0, sticky=N+S+E+W)
        
        tot = 0;
        i =0;
        k= 0;
        w = int(pici);
        j =0;
        z=0;
        total_pics = int(pici)* int(picj);
        print pici;
        print picj;
        print caminho;
        list = []
        while (tot < total_pics):
                img1 = ImageTk.PhotoImage(Image.open(caminho % (z,j))) # abre essa imagem usando essa função
                label = Label(image=img1)
                label.image = img1 # keep a reference!

                image_file = caminho % (z,j) # recebe o caminho da imagem
                img = Image.open(caminho % (z,j)) # abre a imagem novamente usando outra função

                largura, altura = img.size # detecta o tamanho da foto em pixels (largura e altura)

                #inicio_pixel_x = inicio_pixel_x + (largura+10); # contador para arrumar a foto na tela em espaço de 10 pixeis entre as fotos
                i = i + (largura+10);

                list.append(img1) # adicionar as fotos tiradas em uma lista

                canvas.create_image(i,k,image=list[tot], anchor="nw")
        
        
                j = j+1;

                tot= tot+1;        
        
                if (tot==w): # verificar o fim de uma linha na matriz
                        #inicio_pixel_y = inicio_pixel_y + (altura+10)
                        k = k+ (altura+10);
                        i=0;
                        z= z+1;
                        j = 0;
                        w = w + pici;

        canvas.config(scrollregion=canvas.bbox(ALL),width=750,height=430)

        xscrollbar.config(command=canvas.xview)
        yscrollbar.config(command=canvas.yview)
        
# Função para tirar as fotos e salva-las no diretorio em questão
def testarWeb():
        tkMessageBox.showinfo("Aviso","Vai começar a sessão de Fotos!!!")
        list = []
        list = getCampos()
        a = list[0]
        b = list[1]
        c = list[2]
        d = list[3]
        e = list[4]
        f = list[5]

        #AQUI CHAMA OS MÉTODOS DE ALICE
        #StepXY(a,b,arduino)

        frame = Frame(root, bd=2, width=400,height=400,background="Red")
        frame.place(x=10,y=10)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)

        yscrollbar = Scrollbar(frame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)

        canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        canvas.grid(row=0, column=0, sticky=N+S+E+W)

        tot = 0; #contador de quantidade de fotos
        # Aqui são os índices da matriz de imagens (X,Y)
        z = 0; # índice da matriz eixo X
        j = 0; # índice da matriz eixo Y
        
        i = 0; #contador para posicionar as fotos nos pixels corretos da tela eixo x
        k = 0; #contador para posicionar as fotos nos pixels corretos da tela eixo x
        
        pici = int(c); #Transformar para inteiro os valores do TextBox Pictures i
        picj = int(d); #Transformar para inteiro os valores do TextBox Pictures j
        w = pici; # determina a quebra de linha da matriz
        total_pics = pici * picj;
        
        list = [] #criação de uma lista para as imagens
        
        while (tot < total_pics):
                cam.setPath(e) #funcao para setar o caminho das fotos
                cam.setFileName(f) #funcao par setar o nome das fotos
                cam.takePicture(z,j) #Tira uma foto da webcam na posição desejada
                caminho = cam.path + cam.filename % (z,j) # pega o diretorio e o nome da foto tirada anteriormente
                
                img1 = ImageTk.PhotoImage(Image.open(caminho)) # abre essa imagem usando essa função
                label = Label(image=img1)
                label.image = img1 # keep a reference!

                image_file = caminho # recebe o caminho da imagem
                img = Image.open(caminho) # abre a imagem novamente usando outra função

                largura, altura = img.size # detecta o tamanho da foto em pixels (largura e altura)

                i = i + (largura+10);

                list.append(img1) # adicionar as fotos tiradas em uma lista

                canvas.create_image(i,k,image=list[tot], anchor="nw") #criar a imagem usando o widget canvas
                canvas.config(scrollregion=canvas.bbox(ALL),width=750,height=430) #Aparecer a imagem na tela

                xscrollbar.config(command=canvas.xview)
                yscrollbar.config(command=canvas.yview)
        
                j = j+1; #incrementar o índice da matriz

                tot= tot+1;        
        
                if (tot==w): # verificar o fim de uma linha na matriz
                        k = k+ (altura+10);
                        i=0;
                        z= z+1;
                        j = 0;
                        w = w + pici;


        
        
                
#Funcao para tirar uma unica foto pela webcam
def tiraFoto():
        frame = Frame(root, bd=2, width=400,height=400,background="Red")
        frame.place(x=10,y=10)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)

        yscrollbar = Scrollbar(frame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)

        canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        canvas.grid(row=0, column=0, sticky=N+S+E+W)

        cam.takePicture(1,1) #Tira uma foto da webcam na posição desejada
        caminho = cam.path + cam.filename % (1,1) # pega o diretorio e o nome da foto tirada anteriormente
        img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\THYAGO\\Desktop\\Apresentacao\\img-001-001.jpg"))
        label = Label(image=img1)
        label.image = img1 # keep a reference!
        #label.pack()
        canvas.create_image(0,0,image=img1, anchor="nw")
        canvas.config(scrollregion=canvas.bbox(ALL),width=750,height=430)

        xscrollbar.config(command=canvas.xview)
        yscrollbar.config(command=canvas.yview)

################################################################################################################

###################################FUNÇÕES DE ASAPHE ###########################################################
# cria o event handler promeiro

def getValor():
        resultado = qtd.get()
        print resultado
        return resultado
        
def criaTela():
        #eHello.delete(0,END)
        # cria a janela/frame de alto nivel
        global top
        global resultado
        top = Tk()
        top.geometry("200x200+100+100")
        F = Frame(top)
        F.pack(expand="true")
        

        # agora a frame com a caixa de texto
        global qtd
        qtd = StringVar()
        #fEntry = Frame(F,textvariable=qtd)
        eHello = Entry(F,textvariable=qtd)
        #fEntry.pack(side="top", expand="true")
        eHello.pack(side=LEFT)

        # e finalmente uma frame com os botões.
        # vamos usar o sunken neste só para dar um gosto diferente
        bClear = Button(F, text="OK",command=getValor)
        bClear.pack(side="left")
        
        
        
        top.mainloop()

# agora cria o loop que vai fazer correr o programa

import cv2
import numpy

def show_video_capture():

	capture = cv2.VideoCapture(1)
	cv2.namedWindow('window',1)
	
	while True:
	
		ok, img = capture.read()
		cv2.imshow('window',img)
		val = cv2.waitKey(10)
		if val == 99:
			cv2.imwrite('calibracao/img_calibrate.jpg',img)
			tkMessageBox.showinfo("Validacaoo","Foto tirada com sucesso! :)")
			
		if val == 27:
			break
	cv2.destroyWindow('window')

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def correcao():
        correct_image("img-000-000.jpg","img-000-000_c.jpg")


def calibracao():
        tkMessageBox.showinfo("Validacaoo","Aperte C para tirar Foto, ESC para fechar com a janela selecionada! :)")
        show_video_capture()
        res1,res2 = calibrate("calibracao/img_calibrate.jpg")
        if (res1 == True):
                tkMessageBox.showinfo("Validacaoo","Foto Calibrada com sucesso!!")
                cv2.imwrite('calibracao/img_calibrate_correct.jpg',res2)
                cv2.namedWindow('window Calibrate Result',1)
                cv2.imshow('window Calibrate Result',res2)

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

	try:
	   ''' Encontra as cordenadas dos cantos dos quadrados internos do tabuleiro de xadrez '''
	   val,corners = cv2.findChessboardCorners(gray_image , pattern_size) 
	   
	   ''' Refina as cordenadas dos cantos dos quadrados internos do tabuleiro de xadrez '''
	   term = ( cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1 )
	   cv2.cornerSubPix(gray_image, corners, (5, 5), (-1, -1), term)
	   global dst_image
	   dst_image = None
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
	   ''' Retorna a imagem corrigida e o status da operaCAo '''
	   return val, dst_image    
	except:
	   #print "The Program can not correct the image"
	   tkMessageBox.showerror("ERRO","Foto não calibrada!! Imagem de entrada não válida, favor entrar com tabuleiro de Xadrez!")
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

###################################### FIM FUNÇÕES DE ASAPHE ###################################################        

################################################################################################################
#                                      CRIAÇÃO DA INTERFACE GRÁFICA                                            #
################################################################################################################

#Comando para definir o tamanho e titulo da tela princial
root.geometry("800x600+100+100")
root.title("Projeto Final Processamento de Imagens 2013.1")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Calibrate",command=calibracao)
filemenu.add_command(label="Correct",command=correcao)
menubar.add_cascade(label="File", menu=filemenu)

#Frame dos Botoes
frame2=Frame(root)

def disableButton():
    save.config(state="disabled")
    save.update()

#Criando os Botoes
go       = Button(frame2,width=15,text='Go!',command=validarCampos).pack(side=LEFT)
new      = Button(frame2,width=15,text='New',command=newProject).pack(side=LEFT,padx=10)
database = Button(frame2,width=15,text='Database',command=iniciarbd).pack(side=LEFT,padx=10)

frame2.place(width=530,height=40,x=10,y=540)
#save.configure(state=disabled)

#Frame para Steps i
frame3=Frame(root)
frame3.place(x=550,y=480)
Label (frame3,text='Steps i:').pack(side=LEFT)
v = StringVar()
Entry(frame3,width=10,textvariable=v).pack(side=LEFT)

#Frame para Steps j
frame4=Frame(root)
frame4.place(x=550,y=510)
Label (frame4,text='Steps j:').pack(side=LEFT)
w = StringVar()
Entry(frame4,width=10,textvariable=w).pack(side=LEFT)

#Frame para Pictures i
frame5=Frame(root)
frame5.place(x=650,y=480)
Label (frame5,text='Pictures i:').pack(side=LEFT)
y = StringVar()
Entry(frame5,width=10,textvariable=y).pack(side=LEFT)

#Frame para Pictures j
frame6=Frame(root)
frame6.place(x=650,y=510)
Label (frame6,text='Pictures j:').pack(side=LEFT)
z = StringVar()
Entry(frame6,width=10,textvariable=z).pack(side=LEFT)

#Frame para Diretorio
frame7=Frame(root)
frame7.place(x=10,y=480)
Label (frame7,text='Diretorio:').pack(side=LEFT)
f7 = StringVar()
Entry(frame7,width=60,textvariable=f7).pack(side=LEFT)

#Frame para Diretorio
frame8=Frame(root)
frame8.place(x=10,y=510)
Label (frame8,text='Nome das Imagens:').pack(side=LEFT)
f8 = StringVar()
Entry(frame8,width=20,textvariable=f8).pack(side=LEFT)

#Frame para Botão Mostrar Web
frame10=Frame(root)
frame10.place(x=610,y=545)
webcam = Button(frame10,width=15,text='Mostrar WebCam!',command=show_video_capture).pack(side=LEFT)


root.config(menu=menubar)
root.mainloop()
