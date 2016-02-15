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

class Color:
    COLORS = ['\033[96m','\033[95m', '\033[94m', '\033[92m', '\033[93m', '\033[91m', '\033[97m']
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def __ini__(self):
    	pass
    def colorear(self, cadena, color):
    	return self.COLORS[color] + cadena + self.ENDC
    def mensajeError(self, cadena):
    	return self.COLORS[5] + cadena + self.ENDC

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
		return Color().colorear("("+str(self.top)+","+str(self.bottom)+","+str(self.right)+","+str(self.left)+")", self.player)

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
	def getCarta(self, pos):
		if(pos >= len(self.cartas)):
			return None
		return self.cartas[pos]
	def playCarta(self, pos):
		if(pos >= len(self.cartas)):
			return False
		self.jugadas += [self.cartas[pos]]
		del self.cartas[pos]
		return True
	def __str__(self):
		salida = "\tEn Mano:"
		for x in range(0,len(self.cartas)):
			salida += "\t" + str(self.cartas[x])
			if(x % 5 == 4):
				salida += "\n\t\t"
		salida += "\n\tJugadas: "
		for x in range(0,len(self.jugadas)):
			salida += "\t" + str(self.jugadas[x])
			if(x % 5 == 4):
				salida += "\n\t\t"
		return salida[:-2]

##################################################################################################################################
# CLASS JUGADOR ##################################################################################################################
##################################################################################################################################

class Jugador:
	def __init__(self, identificador = 0, numCartas = 5):
		self.identificador = identificador
		self.mano = Mano(identificador, numCartas)
	def getMano(self):
		return mano
	def anadirCarta(self, carta):
		mano.anadirCarta(carta)
	def getCarta(self, pos):
		return self.mano.getCarta(pos)
	def playCarta(self, pos):
		return self.mano.playCarta(pos)
	def __str__(self):
		return "Jugador " + str(self.identificador) + ":\n" + str(self.mano)

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
	def libre(self, x, y):
			return self.celdas[x][y].getPlayer() == -1
	def posicionValida(self, x, y):
		return (x < self.tamanoTablero and x >= 0 and y < self.tamanoTablero and y >= 0)
	def setCarta(self, jugador, posCarta, x, y):
		if(self.libre(x,y)):
			carta = jugador.getCarta(posCarta)
			if(jugador.playCarta(posCarta)):
				self.celdas[x][y] = carta
				return True
		return False
	def __str__(self):
		salida = "\t0"
		for y in range(1, self.tamanoTablero):
			salida += "\t\t" + str(y)
		salida += "\n"
		for x in range(0, self.tamanoTablero):
			salida += str(x) + "\t"
			for y in range(0, self.tamanoTablero):
				salida += str(self.celdas[x][y]) + ",\t"
			salida = salida[:-2] + "\n"
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
		self.tablero = Tablero(tamanoTablero)
		self.turnos = 0
		self.turno = 0
		numCartas = tamanoTablero**2 / jugadores
		if(numCartas*jugadores < tamanoTablero**2):
			numCartas += 1

		for x in range(0,jugadores):
			self.jugadores += [Jugador(x, numCartas)]
	def getTurno(self):
		return self.turno
	def iteracion(self, posCarta, posicionX, posicionY):
		posicionValida = self.tablero.posicionValida(posicionX, posicionY)
		if(posicionValida):
			if(self.tablero.setCarta(self.jugadores[self.turno], posCarta, posicionX,posicionY)):
				self.turno += 1
				self.turnos += 1
				if(self.turno >= len(self.jugadores)):
					self.turno = 0
			else:
				return Color().mensajeError("\n*********************************************************************************\nEl indice facilitado no coincide con ninguna carta del jugador " + str(self.turno) + "\n*********************************************************************************\n")
		else:
			return Color().mensajeError("\n*********************************************************************************\nHa habido un error debido a una posicion no valida en el tablero\n*********************************************************************************\n")
	def finalizado(self):
		return self.turnos == self.tamanoTablero**2

	def __str__(self):
		salida = "\n\n******************************************** Turno " + str(self.turnos) + " ********************************************\n"
		for x in self.jugadores:
			salida += str(x) + "'\033[0m'\n\n"
		salida += str(self.tablero)
		salida += "Turno del jugador: " + str(self.turno)
		return salida + "\n"

##################################################################################################################################
# AUXILIAR FUNCTIONS AND METHODS #################################################################################################
##################################################################################################################################

def randomCarta(player,minimo=1,maximo=9):
	return Carta(randint(minimo,maximo),randint(minimo,maximo),randint(minimo,maximo),randint(minimo,maximo),player)

##################################################################################################################################
# MAIN ###########################################################################################################################
##################################################################################################################################

print("Introduce el numero de jugadores (max. 6)")
numPlayers = raw_input()
while(not numPlayers.isdigit() or int(numPlayers) > 6 or int(numPlayers) < 2):
	print("Introduce el numero de jugadores (max. 6)")
	numPlayers = raw_input()

print("Introduce el ancho del tablero (max. 5, min. 3")
tablero = raw_input()
while(not tablero.isdigit() or int(tablero) > 5 or int(tablero) < 3):
	print("Introduce el ancho del tablero (max. 5, min. 3")
	tablero = raw_input()

juego = Juego(int(numPlayers),int(tablero))

while(juego.finalizado() == False):
	print(str(juego))
	print("Introduzca la carta que va a utilizar")
	numCarta = raw_input()
	if(numCarta.isdigit()):
		print("Introduzca la posicion. Ej: 1,2)")
		posicion = raw_input()
		try:
			coordenadas = posicion.split(',')
			posicionX = int(coordenadas[0])
			posicionY = int(coordenadas[1])
			resultado = juego.iteracion(int(numCarta), posicionX, posicionY)
			if(resultado != None):
				print("\n" + resultado + "\n")
		except ValueError as excepcion:
			print(Color().mensajeError("\n\n************************************************************************************************\nFormato de posicion incorrecta, por favor introduzca dos numeros separados por una coma.\n************************************************************************************************\n"))
	else:
		print(Color().mensajeError("\n\n***********************************************************\nFormato de carta incorrecta. Introduzca un digito\n***********************************************************\n"))
print("\n\n" + str(juego) + "\n\n")
print("\n\n JUEGO FINALIZADO \n\n")


