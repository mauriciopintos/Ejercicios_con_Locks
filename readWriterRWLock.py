import threading
from rwlock import RWLock
import time
import random

marker = RWLock()

DIAS = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
hoy = 0

def calendar_reader(id_number):