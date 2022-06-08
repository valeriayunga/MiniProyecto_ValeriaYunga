
from datetime import datetime,timezone

class Cita:
    __fechaHoraInicio = datetime.now(timezone.utc)
    __fechaHoraFin=datetime
    __contador=int
    __contador+=1 #Variable de clase Estática
    __dia = int

    def __init__(self, fechaHoraInicio, fechaHoraFin, dia):
        self.__fechaHoraInicio=fechaHoraInicio
        self.__fechaHoraFin=fechaHoraFin
        self.__dia=dia

    """print("Local time   {}".format(__fechaHoraInicio.astimezone().isoformat()))
"""