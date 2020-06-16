# Player mantiene la logica de un jugador de un juego puntual. Mantendra toda la información necesaria de un jugador
# de un juego. Otra de las cosas que debera chequear es al momento de hacer una jugada, que el comando que llega
# sea valido con su informacion (ej: que tenga la carta que se esta pidiendo tirar)
# Player Truco

class Player:

    def _init_(self, user, room):
        self.username = user
        self.idRoom = room
        self.belongings = [] #['3E':1, '12O':1]
        self.penalties = 0
    
    # Este metodo se encarga de controlar que el Jugador cuente con la pertenencia
    # que desea tirar.
    # Card: String Ej: 3E (3 de espada), 12C (12 de copa), 1E (1 de espada)
    def playCard(card):
        try:
            cant = self.belongings[card]
            if (cant <= 0):
                return False
            else:
                self.belongings[card] = cant - 1
            return True
        except:
            return False
    
    # Este metodo es para agregar una carta a las pertenencias del Jugador
    def addCard(card):
        if card in self.belongings():
            cant = self.belongings[card]
            self.belongings[card] = cant + 1
        else:
            self.belongings[card] = 1
    
    # Aumenta la cantidad de penalidades y retorna la cantidad de penalidalidades del Jugador
    def penalty():
        cant = self.penalties
        self.penalties = cant + 1
        return self.penalties
