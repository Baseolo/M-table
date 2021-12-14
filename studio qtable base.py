from env_tallo_nv_1_00 import *
import keyboard
from time import *

mtable_pilota = []
mtable_memoria = []

LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 25000
SHOW_EVERY = 3000
xcasual = 1

casuali = scelte = vuote = 0
crea_mondo(100,50,30)
tallo = [random.randrange(1, at_mondo_colonne-1), random.randrange(1, at_mondo_righe-1)]
griglia = '0'*(at_vista+at_vista+1)**2
for studio in range(1, 10):
    cicli = studio * 1000000
    inizio = time()
    for x in range(0,cicli):
        if  mtable_pilota.count(griglia) == 0:
            mtable_pilota.append(griglia)
            t = []
            for i in range(0,9):
                t.append(random.randrange(-2,0))
            mtable_memoria.append(t)
        puntatore = mtable_pilota.index(griglia)
        azione = mtable_memoria[puntatore].index(max(mtable_memoria[puntatore]))
        if random.randint(1,xcasual) < 100:
            xcasual += 1
            azione = random.randint(0, 8)
            casuali += 1
        else:
            scelte += 1

        memoria = mtable_memoria[puntatore]
        punteggio, griglia = azione_tallo(tallo, azione)
        if  mtable_pilota.count(griglia) == 0:
            mtable_pilota.append(griglia)
            t = []
            for i in range(0,9):
                t.append(random.randrange(-2,0))
            mtable_memoria.append(t)
        if punteggio <= 0:
            nuovo_puntatore = mtable_pilota.index(griglia)
            max_future_q = max(mtable_memoria[nuovo_puntatore])
            current_q = mtable_memoria[puntatore][azione]
            reward = punteggio
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            mtable_memoria[puntatore][azione] = new_q
        else:
            mtable_memoria[puntatore][azione] = 0
    urti,cibo = dammi_valori()
    print(str(int(time()-inizio))+' '+str(cicli)+' '+str(urti)+' '+str(cibo))
print('fine')

