# Este modulo tiene la función de mantener la logica del juego del juego, el control de los msj de los jugadores en el juego
# y estado de la partida. Ademas de la comunicacion con el servidor, con los mensajes a retornar.
# Esta clase será la base de los Rooms 

from Auxiliar import MsgFactory

class Room:

    def _init_(self, idR, cant, server):
        self.idRoom = idR
        self.state = "Free"
        self.cantPlayers = cant
        self.players = [self.cantPlayers]
        self.currentPlayers = 0
        self.maxPenalties = 5
        self.srv = server
        self.managerMsg = MsgFactory(idR)
        self.turn = 0 # Al igual que en LOR el turn aumenta cada vez que se tira una carta
        self.historyPlayer = []
        self.historyPlay = []
        # Instanciar los Comandos
        c1 = "/play"
        c2 = "/help"
        c3 = "/status"
        c4 = "/history"
        self.commands = [c1: playCommand(card),c2: helpCommand(),c3: statusCommand(),c4: historyCommand()]

    # Este metodo se encarga de agregar un nuevo jugador al Room
    def addPlayer(username):
        message = ""
        if(self.state != "Full"):
            player = Player(username,self.idRoom)
            self.players[self.currentPlayers] = player
            self.currentPlayers = self.currentPlayers + 1
            
            if (self.currentPlayers == self.cantPlayers):
                self.state = "Full"
            message = managerMsg.addPlayer()
        else:
            message = managerMsg.fullRoom()
        srv.sendMsg(username,message)

    # Este metodo es el cual recibe los mensajes del servidor
    def reciveMsg(Msg):
        valid = self.validMsg(Msg)
        if not(valid):
            self.penaltyPlayer(player)

    # El ojetivo de esta funcion es la de validar el mensaje Msg y en caso de ser un Comando lo ejecuta
    # Return: True (si todo funciono) - False (si algo fallo)
    def validMsg(Msg):
        sender = Msg.username
        text = Msg.text
        end = False
        player
        i = 0
        # Chequeo que el mensaje proviene de un usuario que esta en la sala
        existPlayer = self.searchPlayer(sender)
        if (existPlayer == NULL)
            return False
        else:
            # ACA DEBE IR LA LOGICA DE EVALUAR SI ES O NO UN COMANDO
            comando = self.searchCommand(text)
            if(comando == NULL):
                return False
            else:
                return comando

    # Busca a partir de un username(String) el Player
    def searchPlayer(sender):
        i = 0
        end = False
        player = ""
        while ((i != self.cantPlayers) and (not end)):
            player = self.players[i]
            if(player.name == sender):
                end = True
            i = i + 1
        if end:
            return player
        else:
            return NULL

    # Busca a partir del texto(String) el Comando al que corresponde
    # Return: True (si todo funciono) - False (si algo fallo)
    def searchCommand(text):
        i = 0
        size = len(self.commands)
        end = False
        command = ""
        args = text.split()
        arg0 = args[0]
        try:
            if (args == "/play"):
                arg1 = args[1]
                return self.commands[arg0](arg1)
            else:
                return self.commands[arg0]
        except:
            return False
    
    # Este metodo se encarga de aplicar la penalizacion a un jugador y el status final al irse
    def penaltyPlayer(player):
        cantPenalty = player.penalty()
        if (cantPenalty == self.maxPenalties):
            msgLeave = managerMsg.leave(player.username)
            status = self.game.status()
            msgStatus = managerMsg.status(status)
            # Notificar a todos demas jugadores
            for p in self.players:
                srv.sendMsg(p.username,msgLeave)
                srv.sendMsg(p.username,msgStatus)
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
                status = self.game.status()
                msgStatus = self.managerMsg.status(status)
                msgWinner = self.managerMsg.winner(player.username) # Crea un mensaje con el ganador del juego
                for p in self.players:
                    srv.sendMsg(p.username,msgStatus)
                    srv.sendMsg(p.username,msgWinner)
                srv.cleanRoom(idRoom)
            else:
                self.turn = self.turn + 1
        else:
            self.penaltyPlayer(player)
    
# ------------------------ METODOS DE COMANDOS ------------------------










