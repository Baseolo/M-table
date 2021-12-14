from env_tallo_1_00 import *
import keyboard
import time

mtable_pilota = []
mtable_memoria = []

LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 25000
SHOW_EVERY = 3000
xcasual = 1

casuali = scelte = vuote = 0
crea_mondo(100,50,30)
disegna_mondo()
tallo = [random.randrange(1, at_mondo_colonne-1), random.randrange(1, at_mondo_righe-1)]
griglia = '0'*(at_vista+at_vista+1)**2
for x in range(0,500000):
    pygame.draw.rect(at_sfondo, at_col_visitato, (1, 505, 1500 ,700))
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
    #print(str(puntatore)+' '+str(azione)+ ' '.join(str(e) for e in memoria))
    at_sfondo.blit(at_font.render('Casuali   '+format(casuali, ',d'), True, at_col_ostacolo), (10, 530))
    at_sfondo.blit(at_font.render('Scelte   '+format(scelte, ',d'), True, at_col_ostacolo), (10, 550))
    at_sfondo.blit(at_font.render('M-table  '+format(len(mtable_pilota), ',d'), True, at_col_ostacolo), (10, 570))
    pygame.display.flip()
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
    #time.sleep(0.4)
    if keyboard.is_pressed("q"):
        break
input('premi invio')

