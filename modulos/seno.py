from math import pi, sin

def modelo(A:float,frecuencia:float,fase:float,tiempo:float)->float:
    return A*sin(2*pi*frecuencia*tiempo+fase)