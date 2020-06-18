# Los Games contienne la logica de los juegos que se llevaran a cabo en las salas. 
# Los Games deben controlar que se cumplan las reglas del juego en cuestion, mantendran los puntajes, turnos,
# cartas, fichas, cuando un juego esta terminado y determinar el o los ganadores.
# Debera haber un Game diferente por cada uno de los juegos que se desee implementar
# EL Juego debera implementar las jugadas de cada Jugador. Penalizar en caso de ser necesario
# y notificar a la sala de toda comunicacion hacia los Jugadores.
# El juego no tiene acceso ni al Servidor, ni a la API que se comunica con Telegram
class Game:

    def _init_(self):
        self.maxPenalties = 5


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
    
    # Este metodo implementa el comando de /play card
    # Realiza la jugada actualizando los historiales, y aplicando la jugada al jugador y al juego
    # Play: String Ej: 3E (3 de espada), 12C (12 de copa), 1E (1 de espada)
    def playCommand(player,play):
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
