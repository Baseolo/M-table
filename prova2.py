from env_tallo_1_00 import *
import keyboard

mtable_pilota = []
mtable_memoria = []

casuali = scelte = vuote = 0
crea_mondo(100,50,30)
#stampa_mondo()
disegna_mondo()
tallo = [3,3]
azione = 9
old_puntatore = -1

while True:
    punteggio, griglia = azione_tallo(tallo,azione)
    disegna_griglia(dammi_griglia(tallo[0],tallo[1]))
    if keyboard.is_pressed("q"):
        break
    if punteggio != 0 and old_puntatore != -1:
        mtable_memoria[old_puntatore][azione] += punteggio
    azione = random.randrange(1, 9)
    if griglia != '0'*(et_vista*2+1)**2:
        if mtable_pilota.count(griglia) == 0:
            mtable_pilota.append(griglia)
            mtable_memoria.append([0,0,0,0,0,0,0,0,0])
        puntatore = mtable_pilota.index(griglia)
        azione = mtable_memoria[puntatore].index(max(mtable_memoria[puntatore]))
        if mtable_memoria[puntatore][azione] == 0:
            casuali += 1
        else:
            scelte += 1
    else:
        vuote += 1
        azione = random.randrange(1, 9)
        puntatore = -1
    old_puntatore=puntatore
