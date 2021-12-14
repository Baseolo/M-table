from env_tallo_nv_1_00 import *
import keyboard
from time import *

mtable_pilota = []
mtable_memoria = []

casuali = scelte = vuote = 0
crea_mondo(100,50,30)
tallo = [random.randrange(1, at_mondo_colonne-1), random.randrange(1, at_mondo_righe-1)]
griglia = '0'*(at_vista+at_vista+1)**2
for studio in range(1, 10):
    cicli = studio * 1000000
    inizio = time()
    for x in range(0,500000):
        if  mtable_pilota.count(griglia) == 0:
            mtable_pilota.append(griglia)
            mtable_memoria.append([0,0,0,0,0,0,0,0,0])
        puntatore = mtable_pilota.index(griglia)
        azione = mtable_memoria[puntatore].index(max(mtable_memoria[puntatore]))
        memoria = mtable_memoria[puntatore]
        if mtable_memoria[puntatore][azione] == 0:
            azione = random.randint(0, 8)
            casuali += 1
        else:
            scelte += 1
        punteggio, griglia = azione_tallo(tallo, azione)
        mtable_memoria[puntatore][azione] += punteggio
    urti,cibo = dammi_valori()
    print(str(int(time()-inizio))+' '+str(cicli)+' '+str(urti)+' '+str(cibo))
print('fine')


