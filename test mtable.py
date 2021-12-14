from env_tallo_1_00 import *
import keyboard
import time

mtable_pilota = []
mtable_memoria = []

automatico = False

casuali = scelte = vuote = 0
crea_mondo(100,50,30)
disegna_mondo()
tallo = [random.randrange(1, at_mondo_colonne-1), random.randrange(1, at_mondo_righe-1)]
griglia = '0'*(at_vista+at_vista+1)**2
while True:
    pygame.draw.rect(at_sfondo, at_col_visitato, (1, 505, 1500 ,700))
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
    at_sfondo.blit(at_font.render('q:esci m:manuale a:automatico  -  azione 1:su 2:destra 3:giu 4:sinistra 5:su destra 6:giu destra 7:giu sinistra 8:su sinistra 0:fermo  ', True, at_col_ostacolo), (10, 510))
    at_sfondo.blit(at_font.render('Casuali   '+format(casuali, ',d'), True, at_col_ostacolo), (10, 530))
    at_sfondo.blit(at_font.render('Scelte   '+format(scelte, ',d'), True, at_col_ostacolo), (10, 550))
    at_sfondo.blit(at_font.render('M-table  '+format(len(mtable_pilota), ',d'), True, at_col_ostacolo), (10, 570))
    at_sfondo.blit(at_font.render('prima di eseguire azione: azione e puntatore e griglia  '+format(azione, ',d')+' '+format(puntatore, ',d')+' '+griglia, True, at_col_ostacolo), (10, 600))
    at_sfondo.blit(at_font.render('Memoria   ' + ' '.join(str(e) for e in memoria), True, at_col_ostacolo), (10, 620))
    pygame.display.flip()
    if not automatico:
        azione = -1
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
        if keyboard.is_pressed("0"):
            azione = 0
        time.sleep(0.1)
    if azione >= 0:
        punteggio, griglia = azione_tallo(tallo, azione)
        mtable_memoria[puntatore][azione] += punteggio
        at_sfondo.blit(at_font.render('dopo esecuzione: azione e puntatore e griglia  '+format(azione, ',d')+' '+format(puntatore, ',d')+' '+griglia, True, at_col_ostacolo), (10, 650))
        at_sfondo.blit(at_font.render('Memoria   ' + ' '.join(str(e) for e in memoria), True, at_col_ostacolo), (10, 670))
        at_sfondo.blit(at_font.render('Punteggio   ' + format(punteggio, ',d'), True, at_col_ostacolo), (10, 690))
        pygame.display.flip()
        #time.sleep(5)
    if keyboard.is_pressed("q"):
        break
    if keyboard.is_pressed("a"):
        automatico = True
    if keyboard.is_pressed("m"):
        automatico = False


