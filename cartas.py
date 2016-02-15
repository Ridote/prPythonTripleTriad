##################################################################################################################################
# IMPORTS ########################################################################################################################
##################################################################################################################################
from random import randint

##################################################################################################################################
# ENUMS ##########################################################################################################################
##################################################################################################################################

class Regla:
	Suma = 0
	Igual = 1
	Elemental = 2
	def __init__(self, Type):
		self.value = Type
	def __str__(self):
		if self.value == Regla.Suma:
			return 'Suma'
		if self.value == Regla.Igual:
			return 'Igual'
		if self.value == Regla.Elemental:
			return 'Elemental'
	def __eq__(self,y):
		return self.value==y.value

class Elemento:
	NoElemental = 0
	Fuego = 1
	Agua = 2
	Rayo = 3
	Tierra = 4
	def __init__(self, Type):
		self.value = Type
	def __str__(self):
		if self.value == Regla.NoElemental:
			return 'No Elemental'
		if self.value == Regla.Fuego:
			return 'Fuego'
		if self.value == Regla.Agua:
			return 'Agua'
		if self.value == Regla.Rayo:
			return 'Rayo'
		if self.value == Regla.Tierra:
			return 'Tierra'
	def __eq__(self,y):
		return self.value==y.value

##################################################################################################################################
# CLASS CARTA ####################################################################################################################
##################################################################################################################################

class Carta:
	def __init__(self,top,bottom,right,left,player=0):
		self.top = top
		self.bottom = bottom
		self.right = right
		self.left = left
		self.player = player
	def getTop(self):
		return self.top
	def getBottom(self):
		return bottom
	def getRight(self):
		return self.right
	def getLeft(self):
		return self.left
	def getPlayer(self):
		return self.player
	def setPlayer(self,player):
		self.player = player
	def __str__(self):
		return "("+str(self.top)+","+str(self.bottom)+","+str(self.right)+","+str(self.left)+","+str(self.player)+")"

##################################################################################################################################
# CLASS MANO #####################################################################################################################
##################################################################################################################################

class Mano:
	def __init__(self, player = 0, cantidadCartas = 5):
		self.cartas = []
		self.jugadas = []
		for x in range(0,cantidadCartas):
			self.anadirCarta(randomCarta(player))
	def anadirCarta(self, carta):
		self.cartas = self.cartas + [carta]
		self.jugadas = self.jugadas + [False]
	def getCarta(self, pos):
		if(pos >= len(self.jugadas)):
			return None
		return self.cartas[pos]
	def playCarta(self, pos):
		if(pos >= len(self.jugadas)):
			return False
		self.jugadas[pos] = True
		return True
	def retrieveCarta(self, pos):
		if(pos >= self.jugadas[pos]):
			return False
		self.cartas[pos] = None
		self.jugadas[pos] = False
		return True
	def deepShow(self):
		salida = ""
		for x in range(0,len(self.cartas)):
			salida += str(self.cartas[x]) + str(self.jugadas[x]) +  " / "
		return salida.rsplit("/", 1)[0]
	def __str__(self):
		salida = ""
		for x in range(0,len(self.cartas)):
			if(self.jugadas[x] == False and self.cartas[x] != None):
				salida += str(self.cartas[x]) + " / "
		return salida.rsplit("/", 1)[0]

##################################################################################################################################
# CLASS JUGADOR ##################################################################################################################
##################################################################################################################################

class Jugador:
	def __init__(self, identificador = 0):
		self.identificador = identificador
		self.mano = Mano()
	def getMano(self):
		return mano
	def anadirCarta(self, carta):
		mano.anadirCarta(carta)
	def getCarta(self, pos):
		return self.mano.getCarta(pos)
	def playCarta(self, pos):
		return self.mano.playCarta(pos)
	def __str__(self):
		return "Jugador " + str(self.identificador) + ": " + str(self.mano)

##################################################################################################################################
# CLASS TABLERO ##################################################################################################################
##################################################################################################################################

class Tablero:
	def __init__(self, tamanoTablero = 3):
		self.tamanoTablero = tamanoTablero
		self.celdas = []
		for x in range(0, tamanoTablero):
			fila = []
			for y in range(0, tamanoTablero):
				fila =  fila + [Carta(0,0,0,0,-1)]
			self.celdas = self.celdas+[fila]

	def setCarta(self, carta, x, y):
		print("\n")
		for x2 in range(0,3):
			for y2 in range(0,3):
				print(str(self.celdas[x2][y2]))
			print()
		print(str(self.tamanoTablero) + "\n")
		print("(" + str(x) + ", " + str(y) + ") - Carta: " + str(carta))
		print("\n")
		if(x < self.tamanoTablero and x > 0 and y < self.tamanoTablero and y > 0):
			if(self.celdas[x][y].getPlayer() != -1):
				return False
			self.celdas[x][y] = carta
			return True
		return False

	def libre(self, x, y):
			return self.celdas[x][y].getPlayer() == -1
	def jugar(self, carta, x, y):
		if(self.libre(x, y) != True):
			return False
		linea[x][y] = carta
		return True
	def __str__(self):
		salida = ""
		for x in range(0, self.tamanoTablero):
			for y in range(0, self.tamanoTablero):
				salida += str(self.celdas[x][y]) + ",\t"
			salida = salida.rsplit(",\t",1)[0] + "\n"
		return salida

##################################################################################################################################
# CLASS JUEGO ####################################################################################################################
##################################################################################################################################

class Juego:
	#turno <- turno del jugador que viene ahora
	#turnos <- numero de turnos hasta el momento
	def __init__(self, jugadores = 2, tamanoTablero = 3):
		self.tamanoTablero = tamanoTablero
		self.jugadores = []
		self.tablero = Tablero(3)
		self.turnos = 0
		self.turno = 0
		for x in range(0,jugadores):
			self.jugadores += [Jugador(x)]

	def getTurno(self):
		return self.turno

	def iteracion(self, posCarta, posicionX, posicionY):
		carta = self.jugadores[self.turno].getCarta(posCarta)
		if(self.jugadores[self.turno].playCarta(posCarta)):
			if(self.tablero.setCarta(carta,posicionX,posicionY)):
				self.turno += 1
				if(self.turno >= len(self.jugadores)):
					self.turno = 0
			else:
				return "\n*********************************************************************************\nNo se puede colocar una carta en (" + str(posicionX) + "," + str(posicionY) + "). Compruebe que no se haya salido\ndel tablero o que no este intentando colocar una carta sobre otra ya colocada\n*********************************************************************************\n"
		else:
			return "Indice de carta invalido"
	def finalizado(self):
		return False#self.turnos == self.tamanoTablero**2

	def __str__(self):
		salida = ""
		for x in self.jugadores:
			salida += str(x) + "\n\n"
		salida += str(self.tablero)
		salida += "Turno del jugador: " + str(self.turno)
		return salida

##################################################################################################################################
# AUXILIAR FUNCTIONS AND METHODS #################################################################################################
##################################################################################################################################

def menu(tablero):
	print("Introducir carta. Formato: TOP,BOTTOM,RIGHT,LEFT,PLAYER")
	lectura = raw_input()
	datos = lectura.split(',')
	carta = Carta(datos[0],datos[1],datos[2],datos[3],datos[4])
	print("introducir posicion")
	lectura = raw_input()
	posicion = lectura.split(',')
	posicionX = int(posicion[0])
	posicionY = int(posicion[1])
	if(tablero.jugar(carta, posicionX, posicionY) == False):
		print("POSICION INVALIDA")
	print("\n")
	print(tablero)
	print("\n")

def randomCarta(player,minimo=1,maximo=9):
	return Carta(randint(minimo,maximo),randint(minimo,maximo),randint(minimo,maximo),randint(minimo,maximo),player)

##################################################################################################################################
# MAIN ###########################################################################################################################
##################################################################################################################################

juego = Juego(2,3)

while(juego.finalizado() == False):
	print(str(juego))
	print("Introduzca la carta que va a utilizar")
	numCarta = raw_input()
	if(numCarta.isdigit()):
		print("Introduzca la posicion. Ej: 1,2")
		posicion = raw_input()
		try:
			coordenadas = posicion.split(',')
			posicionX = int(coordenadas[0])
			posicionY = int(coordenadas[1])
			resultado = juego.iteracion(int(numCarta), posicionX, posicionY)
			if(resultado != None):
				print("\n" + resultado + "\n")
		except ValueError as excepcion:
			print "\nFormato de posicion incorrecta, por favor introduzca dos numeros separados por una coma. + " + excepcion + "\n"
	else:
		print("\nCarta incorrecta...\n")
	






