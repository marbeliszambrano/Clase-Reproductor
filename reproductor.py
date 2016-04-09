# Clase-Reproductor
# UNEFA Mérida
# Integrantes: marbeliszambrano, yasmeliguerrero, GepsyO, Euduar, william14maldonado
# Profesor: javierri
# Clificación: 

tipo = ["RADIO","CD","USB"]
def detectar_cambio (B):
	cont = 0
		
	for i in tipo:
		if(i == B.upper()):
			return cont
		cont = cont+1
	return -1

class Reproductor:
	
	Encendido = False
	Modo = tipo[0]
	Volumen_maximo = 100
	Num_cancion = 0
	Bandeja = False
	Puerto_USB = False
	Volumen = 50
	Cancion = []
	Emisora = "FM"
 	
	def Encender(self):
		if(self.Encendido == False):
			self.Encendido = True
			print "BIENVENIDO"

	def Apagar(self):
		if(self.Encendido == True):
			self.Encendido = False
			print "HASTA LUEGO"
	
	def Abrir_bandeja(self):
		if((self.Encendido == True) and (self.Bandeja==False)):
			self.Bandeja = True
			print "ABRIR BANDEJA"

	def Cerrar_bandeja(self):
		if((self.Encendido == True) and (self.Bandeja == True)):
			self.Bandeja = False
			print "CERRAR BANDEJA"
	
	def Cambiar_modo(self,B,C =[]):
		if(self.Encendido == True):
			num = detectar_cambio(B)
			if(num != -1):
				self.Modo = tipo[num]
				if(self.Modo == tipo[0]):
					self.reproducir(C)
				if(self.Modo == tipo[1]):
					self.insertar_CD()
					self.reproducir(C)
				if(self.Modo == tipo[2]):
					self.insertar_USB()
					self.reproducir(C)
	
	def subir_volumen(self):
		if((self.Encendido == True) and (self.Volumen < self.Volumen_maximo)):
			self.Volumen = self.Volumen+1
			print "Vol: ",self.Volumen

	def bajar_volumen(self):
		if((self.Encendido) and (self.Volumen > 0)):
			self.Volumen = self.Volumen-1
			print "Vol: ",self.Volumen

	def cambiar_sig(self):
		if((self.Encendido==True) and (len(self.Cancion) != 0)):
			self.Num_cancion=self.Num_cancion+1
			if(self.Num_cancion==len(Cancion)):
				self.Num_cancion = 0
			print "SIGUIENTE CANCION",self.Cancion[self.Num_cancion]

	def cambiar_ant(self):

		if((self.Encendido == True) and (len(self.Cancion) != 0)):
			self.Num_cancion = self.Num_cancion-1
			if(self.Num_cancion == -1):
				self.Num_cancion == len(self.Cancion)-1
			print "ANTERIOR CANCION", self.Cancion[self.Num_cancion]

	def insertar_CD(self,a = []):
		self.Abrir_bandeja()
		self.Cerrar_bandeja()
		print "LEYENDO CD..."
		self.Cancion = a

	def reproducir(self,a = []):
		if(self.Encendido == True):
			self.Cancion = a
			if (len(self.Cancion) != 0):	
				if (self.Modo == tipo[0]):
					print "Sintonizando ",self.Cancion[self.Num_cancion]				
				else:			
					print "REPRODUCIENDO ",self.Cancion[self.Num_cancion]
			else:
				if (self.Modo == tipo[0]):
					print "No se puede sintonizar con alguna emisora..."
				else:
					print "No tiene canciones"
	def expulsar_CD(self):
		self.Abrir_bandeja()
		print "RETIRAR EL CD"
		self.Cerrar_bandeja()
		if (self.Modo == tipo[1]):
			self.Cancion = []

	def expulsar_USB(self):
		print "RETIRAR USB"
		Puerto_USB = False
		if (self.Modo == tipo[2]):
			self.Cancion = []
	
	def cambiar_emisora(self,a = []):
		if((self.Encendido == True) and (self.Modo == tipo[0]) and (self.Emisora == "FM")):
			print "AM"
			self.Emisora = "AM"
			self.Cancion = a	
		elif((self.Encendido == True) and (self.Modo == tipo[0]) and (self.Emisora == "AM")):
			self.Emisora = "FM"
			print "FM"
			self.Cancion = a
	def insertar_USB (self,a = []):
		self.Puerto_USB = True
		print "LEYENDO UNIDAD..."
		self.Cancion = a
	def mute (self):
		self.Volumen = 0
		print "Vol: ",self.Volumen
#PRINCIPAL

re = Reproductor()
re.Encender()

while True:
	val = raw_input()
	
	if val.upper() == "V":
		re.Apagar()
		break
	if val.upper() == "D":
		re.cambiar_sig()
	if val.upper() == "A":
		re.cambiar_ant()
	if val.upper() == "W":
		re.subir_volumen()
	if val.upper() == "S":
		re.bajar_volumen()
	if val.upper() == "O":
		re.reproducir()
	if val.upper() == "Z":
		re.Cambiar_modo("radio")
	if val.upper() == "X":
		re.Cambiar_modo("cd")
	if val.upper() == "C":
		re.Cambiar_modo("usb")
	if val.upper() == "J":
		re.expulsar_CD()
	if val.upper() == "K":
		re.expulsar_USB()
	if val.upper() == "L":
		re.cambiar_emisora()
