# Este modulo tiene la función de mantener la logica del juego del juego, el control de los msj de los jugadores en el juego
# y estado de la partida. Ademas de la comunicacion con el servidor, con los mensajes a retornar.
# Esta clase será la base de los Rooms 

import MsgFactory

class Room:

    def _init_(self, id, cant, server):
        self.idRoom = id
        self.state = "Free"
        self.cantPlayers = cant
        self.players = [self.cantPlayers]
        self.currentPlayers = 0
        self.maxPenalties = 5
        self.srv = server
        self.managerMsg = MsgFactory()
        self.turn = 0 # Al igual que en LOR el turn aumenta cada vez que se tira una carta
        self.historyPlayer = []
        self.historyPlay = []

    # Este metodo se encarga de agregar un nuevo jugador al Room
    def addPlayer(username):
        player = Player(username,self.idRoom)
        self.players[self.currentPlayers] = player
        self.currentPlayers = self.currentPlayers + 1
        
        if (self.currentPlayers == self.cantPlayers):
            self.state = "Full"

    # Este metodo es el cual recibe los mensajes del servidor
    def reciveMsg(Msg):
        sender = Msg.username
        player = self.searchPlayer(sender)
        play = Msg.text
        itsValidPlay = self.validMsg(Msg)
        if not(itsValidPlay):
            self.penaltyPlayer(player)
        else:
            self.playCard(player,play)

    # Busca a partir de un username(String) el Player
    def searchPlayer(sender):
        i = 0
        end = False
        player = ""
        while ((i != self.cantPlayers) and (not end)):
            player = self.players[i]
            if(player.name == sender):
                end = True
            i++
        if end:
            return player
        else:
            return NULL

    # El ojetivo de esta funcion es la de validar el mensaje Msg
    def validMsg(Msg):
        sender = Msg.username
        play = Msg.text
        end = False
        player
        i = 0
        # Chequeo que el mensaje proviene de un usuario que esta en la sala
        existPlayer = self.searchPlayer(sender)
        if (existPlayer == NULL)
            return False
        else:
            # ACA DEBE IR LA LOGICA DE EVALUAR SI ES O NO UN COMANDO
            return True
    
    # Este metodo se encarga de aplicar la penalizacion a un jugador
    def penaltyPlayer(player):
        cantPenalty = player.penalty()
        if (cantPenalty == self.maxPenalties):
            message = managerMsg.leave()
            srv.sendMsg(player.username,message)
            srv.cleanRoom(idRoom)
        else:
            message = managerMsg.warning()
            srv.sendMsg(player.username,message)

    # Realiza la jugada actualizando los historiales, y aplicando la jugada al jugador y al juego
    def playCard(player,play):
        validPlay = player.playCard(play)
        
        if (validPlay):
            h = self.historyPlayer
            self.historyPlayer.insert(len(h),player)
            h = self.historyPlay
            self.historyPlay.insert(len(h),play)
            
            gameOver = self.game.playCard(player,play)
            if (gameOver):
                # El juego termino y notifico a cada jugador que gano y limpio el Room
                i = 0
                size = len(self.players)
                message = self.managerMsg.endGame(player.username) # Crea un mensaje con el ganador del juego
                while (i != size):
                    p = self.players[i]
                    srv.sendMsg(p.username,message)
                    i++
                srv.cleanRoom(idRoom)
                
            else:
                self.turn++
        else:
            self.penaltyPlayer(player)











