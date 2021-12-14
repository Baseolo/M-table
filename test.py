from env_tallo_1_00 import *
import keyboard
import time

mtable_pilota = []
mtable_memoria = []

casuali = scelte = vuote = 0
crea_mondo(100,50,30)
#stampa_mondo()
disegna_mondo()
tallo = [50,25]

while True:
    if keyboard.is_pressed("q"):
        break
    azione = 0
    if keyboard.is_pressed("1"):
        azione = 1
    if keyboard.is_pressed("2"):
        azione = 2
    if keyboard.is_pressed("3"):
        azione = 3
    if keyboard.is_pressed("4"):
        azione = 4
    if keyboard.is_pressed("5"):
        azione = 5
    if keyboard.is_pressed("6"):
        azione = 6
    if keyboard.is_pressed("7"):
        azione = 7
    if keyboard.is_pressed("8"):
        azione = 8
    if keyboard.is_pressed("9"):
        azione = 9
    if azione > 0:
        punteggio, griglia = azione_tallo(tallo,azione)
    time.sleep(0.1)


