# EL MsgFactory esta para crear mensajes para retornar a los usuarios
# Español
class MsgFactory:

    def _init_(self, room):
        self.idRoom = room
    
    # Mensaje cuando se une un nuevo Jugador a la sala
    def addPlayer():
        return "Se agrego con exito a la sala"+self.idRoom
    
    # Mensaje cuando se intenta de unir un nuevo Jugador a la Sala y esta llena
    def fullRoom():
        return "La sala: "+self.idRoom+" esta llena."
    
    # Mensaje de salida a un jugador por reporte
    def leave(username):
        return "El jugador: "+username+" abandono la sala."
    
    # Mensaje del jugador ganador
    # Status: [(Juan,10),(Pepe,8)]
    def status(status):
        out = "El estado de la partida es: "
        for entry in status:
            out = out + "\n * "+entry[0]+": "+entry[1]
        return out
    
    # Mensaje de advertencia
    def warning():
        return "Por favor enviar una jugada o comando valido. En caso de reiterados casos se considera SPAM y abandono de la sala."

    # Mensaje de ganador
    def winner(username):
        return "El jugador: "+username+" es el ganador de la partida."



