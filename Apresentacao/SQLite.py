import sqlite3

class DataBase:
	#Metodo responsavel por inicializar o banco de dados.
	def __init__(self):
		self.filename = 'C:\\Users\\THYAGO\\Desktop\\Apresentacao\\databasePI.db'
		#A linha de codigo acima carrega um arquivo no disco chamado mydatabase.db. Esse sera o arquivo que armazenara os dados do programa.
		#Caso o arquivo nao exista no diretorio, o programa criara-lo.
		
		#cria uma conexao com o banco de dados
		self.conn = sqlite3.connect(self.filename) # ou use :memory: para bota-lo na memoria RAM
		
		# next line avoids the 
        # OperationalError: Could not decode to UTF-8 column 'right_threshold_result' with text...
		#self.conn.text_factory = str
		
		#cria o objeto cursor que vai interagir com o banco de dados, possibilitando adicionar registros, deletar, atualizar, entre outras coisas.
		self.cursor = self.conn.cursor()
		
		
	#O metodo run eh responsavel por receber um comando SQL e executa-lo no banco de dados carregado no __init__
	def run(self, command): 
		print self.filename
		self.cursor.close() #destroi objetos cursores que ainda estejam abertos  
		self.cursor = self.conn.cursor() #cria o objeto cursor
		print "Database.run" + command #imprime o comando SQL solicitado pelo usuario atraves da string command
		result = self.cursor.execute(command) #executa o comando SQL
		
		#O camando commit salva os registros no banco de dados
		self.conn.commit()
		print 'Returning result.....\n\n\n'
		return self.cursor.fetchall() #retorna o resultado da operacao
		
	def consultarBanco(self):
		resultado = self.run("""SELECT * FROM arquivos""")
		return resultado
	
	#O metodo consultarColuna recebe o diretorio (que identifica a linha) e o numero da coluna, e retorna o valor armazenado na coluna
	def consultarColuna(self,dir,num): 
		self.cursor.close() #destroi objetos cursores que ainda estejam abertos  
		self.cursor = self.conn.cursor() #cria o objeto cursor
		if num == 1:
			sql = """SELECT (stepi) FROM arquivos WHERE diretorio = ?"""
			self.cursor.execute(sql, [(dir)])
		if num == 2:
			sql = """SELECT (stepj) FROM arquivos WHERE diretorio = ?"""
			self.cursor.execute(sql, [(dir)])
		if num == 3:
			sql = """SELECT (picturei) FROM arquivos WHERE diretorio = ?"""
			self.cursor.execute(sql, [(dir)])
		if num == 4:
			sql = """SELECT (picturej) FROM arquivos WHERE diretorio = ?"""
			self.cursor.execute(sql, [(dir)])
		if num == 5:
			sql = """SELECT (diretorio) FROM arquivos WHERE diretorio = ?"""
			self.cursor.execute(sql, [(dir)])
		if num == 6:
			sql = """SELECT (nomeimg) FROM arquivos WHERE diretorio = ?"""
			self.cursor.execute(sql, [(dir)])
			
		self.conn.commit()
		return self.cursor.fetchall() #retorna o resultado da operacao
		
	def deletarValor(self,valor):
		self.cursor.close() #destroi objetos cursores que ainda estejam abertos  
		self.cursor = self.conn.cursor() #cria o objeto cursor
		sql = """DELETE FROM arquivos WHERE diretorio = ?"""
		self.cursor.execute(sql, [(valor)])
		self.conn.commit()
		
	def inserir(self,stepi,stepj,picturei,picturej,diretorio,nomeimg):
		self.cursor.close() #destroi objetos cursores que ainda estejam abertos  
		self.cursor = self.conn.cursor() #cria o objeto cursor
		result = self.consultarColuna(diretorio,5) #validar insercao, retornara uma lista com uma tupla (ou seja, tamanho 1) se existir um diretorio de mesmo nome salvo
		if len(result) == 0: #verifica se ja existe um diretorio com esse nome
			sql = """INSERT INTO arquivos VALUES (?,?,?,?,?,?)"""
			self.cursor.execute(sql, [(stepi),(stepj),(picturei),(picturej),(diretorio),(nomeimg)])
			self.conn.commit()
			return 1
		else:  
			return 0
			
	def novoProjetoPadrao(self): #retorna o diretorio e as ibagens
		self.cursor.close() #destroi objetos cursores que ainda estejam abertos
		self.cursor = self.conn.cursor() #cria o objeto cursor]
		numeroDeRegistrosPadrao = len(self.run("""SELECT * FROM arquivos WHERE diretorio LIKE 'images\project%' """))
		if numeroDeRegistrosPadrao != 0:
			sql = """SELECT MAX(diretorio) FROM arquivos WHERE diretorio LIKE ? """
			self.cursor.execute(sql, [("images\project%")])
			self.conn.commit()
			resultado = self.cursor.fetchall()[0][0] #retorna o resultado da operacao
			numeroString = resultado[14:len(resultado)]
			numero = int(numeroString)
			numero = numero + 1
			numeroString = str(numero)
			resultadoFinal = "images\project" + numeroString
			return [resultadoFinal,"img-%03d-%03d.jpg"]
		else: 
			return ["images\project1","img-%03d-%03d.jpg"]
			

banco = DataBase()
#banco.deletarValor("images/project1")
#print banco.novoProjetoPadrao()
#banco.run("""CREATE TABLE arquivos (stepi int, stepj int, picturei int, picturej int, diretorio text, nomeimg text)""")
