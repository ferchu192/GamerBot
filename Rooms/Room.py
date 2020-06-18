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
        self.srv = server
        self.game = Game()
        self.managerMsg = MsgFactory(idR)
        self.turn = 0 # Al igual que en LOR el turn aumenta cada vez que se tira una carta
        # Instanciar los Comandos
        c1 = "/ready"
        c2 = "/help"
        c3 = "/status"
        c4 = "/history"
        c5 = "/rules"
        self.commands = {c1: readyCommand(), c2: helpCommand(), c3: statusCommand(), c4: historyCommand(), c5: rulesCommand()}

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
        self.srv.sendMsg(username,message)

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
        i = 0
        # Chequeo que el mensaje proviene de un usuario que esta en la sala
        existPlayer = self.searchPlayer(sender)
        if (existPlayer == NULL)
            return False
        else:
            # ACA DEBE IR LA LOGICA DE EVALUAR SI ES O NO UN COMANDO
            command = self.searchCommand(sender,text)
            if(command == NULL):
                gameCommand = self.game.executeCommand(text)
                return gameCommand
            else:
                return command

    # Busca a partir de un username(String) el Player
    def searchPlayer(sender):
        i = 0
        end = False
        player = ""
        while ((i != self.cantPlayers) and (not end)):
            player = self.players[i]
            if(player.username == sender):
                end = True
            i = i + 1
        if end:
            return player
        else:
            return NULL

    # Busca a partir del texto(String) el Comando al que corresponde
    # Return: True (si todo funciono) - False (si algo fallo)
    def searchCommand(sender,text):
        i = 0
        size = len(self.commands)
        end = False
        command = ""
        args = text.split()
        arg0 = args[0]
        try:
            return self.commands[arg0](sender)
        except:
            return False

    # Notifica a los Jugadores de una Pelanlizacion
    def penaltyPlayer(player):
        message = managerMsg.warning()
        self.srv.sendMsg(player.username,message)
    
    # Expulsa a un Jugador de la Sala y notifica a los demas el estado final de la partida
    def leavePlayer(player,status):
        msgLeave = managerMsg.leave(player.username)
        msgStatus = managerMsg.status(status)
        # Notificar a todos demas jugadores
        for p in self.players:
            self.srv.sendMsg(p.username,msgLeave)
            self.srv.sendMsg(p.username,msgStatus)
        self.srv.cleanRoom(idRoom)

    # ------------------------------------------------  METODOS DE COMANDOS ------------------------------------------------
    # Este metodo se encarga de registrar cuando un usuario esta listo para jugar
    # Estado: A TRABAJAR
    def readyCommand(username):
        pass
    
    # Este metodo implementa el comando de /help
    def helpCommand(username):
        message = self.game.helpTruco()
        self.srv.sendMsg(username,message)
        return True

    # Este metodo implementa el comando /status
    def statusCommand(username):
        message = self.game.status()
        self.srv.sendMsg(username,message)
        return True
    
    # Este metodo implementa el comando /history
    def historyCommand(username):
        self.srv.sendMsg(username,self.history)
        return True
    
    # Este metodo implementa el comando /rules
    def rulesCommand(username):
        rules = self.game.rules()
        self.srv.sendMsg(username,rules)
        return True










