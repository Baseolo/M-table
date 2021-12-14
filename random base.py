from env_tallo_1_00 import *
import keyboard
import time


casuali = scelte = vuote = 0
crea_mondo(100,50,30)
disegna_mondo()
griglia = ''
tallo = [random.randrange(1, at_mondo_colonne-1), random.randrange(1, at_mondo_righe-1)]
for x in range(0,500000):
    pygame.draw.rect(at_sfondo, at_col_visitato, (1, 505, 1500 ,700))
    azione = random.randint(0, 8)
    casuali += 1
    at_sfondo.blit(at_font.render('q:interrompi', True, at_col_ostacolo), (10, 510))
    at_sfondo.blit(at_font.render('Casuali   '+format(casuali, ',d'), True, at_col_ostacolo), (10, 530))
    pygame.display.flip()
    punteggio, griglia = azione_tallo(tallo, azione)
    if keyboard.is_pressed("q"):
        break
input('premi invio per chiudere ')

