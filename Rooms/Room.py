# Este modulo tiene la función de mantener la logica del juego del juego, el control de los msj de los jugadores en el juego
# y estado de la partida. Ademas de la comunicacion con el servidor, con los mensajes a retornar.
# Esta clase será la base de los Rooms 

from Auxiliar import MsgFactory

class Room:

    def _init_(self, idR, cant, server):
        self.idRoom = idR
        self.state = "Free"
        self.cantUsers = cant # Cantidad maxima de USUARIOS != JUGADORES
        self.users = [self.cantUsers] # Arreglo de los USUARIOS en la sala
        self.currentUsers = 0 # Cantidad de USUARIOS actuales en la sala
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

    # Este metodo es el cual recibe los mensajes del servidor
    # y responde el resultado de ejecutar el mensaje al servidor
    # El ojetivo de esta funcion es la de validar el mensaje Msg y en caso de ser un Comando lo ejecuta
    def reciveMsg(Msg):
        mensaje = ""
        sender = self.users[Msg.username]
        text = Msg.text
        if (sender == NULL):
            mensaje = self.managerMsg.invalidUser()
        else:
            # ACA DEBE IR LA LOGICA DE EVALUAR SI ES O NO UN COMANDO
            command = self.searchCommand(sender,text)
            if(command == NULL):
                gameMessage = self.game.executeCommand(sender,text)
            else:
                mensaje = self.managerMsg.invalidInput()
        self.srv.sendMsg(Msg.username,mensaje)

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

    # ------------------------------------------------ METODOS USERS ------------------------------------------------

    # Este metodo se encarga de agregar un nuevo jugador al Room
    # Ademas de solicitar al Game agregar al nuevo jugador.
    def addPlayer(username):
        message = ""
        if(self.state != "Full"):
            operationOk = self.game.addPlayer(username)
            if(operationOk):
                self.users[self.currentUsers] = username
                self.currentUsers = self.currentUsers + 1
                # De momento se van a llevar la misma cantidad en ambas clases (Game-Room), pero en un futuro estaran para poder ver espectadores o suplenetes
                if (self.currentUsers == self.cantUsers):
                    self.state = "Full"
                message = managerMsg.addPlayer()
            else:
                message = managerMsg.fullRoom()
        else:
            message = managerMsg.fullRoom()
        self.srv.sendMsg(username,message)

    # Notifica a los Jugadores de una Pelanlizacion
    def penaltyPlayer(username):
        message = managerMsg.warning()
        self.srv.sendMsg(username,message)
    
    # Expulsa a un Jugador de la Sala y notifica a los demas el estado final de la partida
    def leavePlayer(username,status):
        msgLeave = managerMsg.leave(username)
        msgStatus = managerMsg.status(status)
        # Notificar a todos demas jugadores
        for user in self.users:
            self.srv.sendMsg(user,msgLeave)
            self.srv.sendMsg(user,msgStatus)
        self.srv.cleanRoom(idRoom)

    # ------------------------------------------------  METODOS DE COMANDOS ------------------------------------------------
    # Este metodo se encarga de registrar cuando un usuario esta listo para jugar
    # Estado: A TRABAJAR
    def readyCommand(username):
        pass
    
    # Este metodo implementa el comando de /help
    def helpCommand(username):
        message = self.game.help()
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










