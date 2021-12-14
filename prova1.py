import random
from time import sleep
import keyboard
from datetime import datetime
import time
import pygame
import cv2

colore_mondo = '#FFFFCC'
colore_vis = '#FFCCFF'
colore_tes = '#DDDDDD'
colore_nvis = '#FFAAFF'
colore_cibo = '#00FFDD'
colore_tallo = '#00CCDD'
dimensione = 10 #numero pari
mondox = 100
mondoy = 50
vista = 2
qtable1 = []
qtable2 = []
scelte = 0
casuali = 0
cibo = 0
vuote = 0
nulle = 0
urti = 0


def creamondo(x=100, y=100, c=30):
    mondo = [[0] * y for i in range(x)]
    for n in range(c):
        mondo[random.randrange(0, x)][random.randrange(0, y)] = 1
    return mondo

def aggiusta_coord(x, y, tipo):
    xx = x * dimensione
    yy = y * dimensione
    if tipo == 'c':
        xx += int(dimensione + dimensione/2)
        yy += int(dimensione + dimensione/2)
    return xx,yy


def stampamondo(mondo):
    for row in mondotallo:
        for col in row:
            print(col, end=" ")
        print()


def disegnamondo():
    for x in range(1, mondox):
        for y in range(1, mondoy):
            xd,yd = aggiusta_coord(x,y,'q')
            pygame.draw.rect(sfondo, colore_vis, (xd, yd, dimensione, dimensione), 1)
            if mondotallo[x][y] == 1:
                pygame.draw.rect(sfondo, colore_cibo, (xd+1, yd+1, dimensione-2, dimensione-2))

def disegna(oggetto, tipo='T',azione=9):  # oggetto = [x,y,energia] , tipo = 'T' tallo 'C' cibo, azione 1 su, 2 destra, 3 giu, 4 sinistra, 5 su destra, 6 giu destra, 7 giu sinistra, 8 su sinistra, 9 fermo
    esito = -1
    xd, yd = aggiusta_coord(oggetto[0], oggetto[1], 'c')
    pygame.draw.circle(sfondo, colore_vis, (xd, yd), dimensione/2, 0)
    if azione == 1:
        oggetto[1] = oggetto[1] - 1
    if azione == 2:
        oggetto[0] = oggetto[0] + 1
    if azione == 3:
        oggetto[1] = oggetto[1] + 1
    if azione == 4:
        oggetto[0] = oggetto[0] - 1
    if azione == 5:
        oggetto[0] = oggetto[0] + 1
        oggetto[1] = oggetto[1] - 1
    if azione == 6:
        oggetto[0] = oggetto[0] + 1
        oggetto[1] = oggetto[1] + 1
    if azione == 7:
        oggetto[0] = oggetto[0] - 1
        oggetto[1] = oggetto[1] + 1
    if azione == 8:
        oggetto[0] = oggetto[0] - 1
        oggetto[1] = oggetto[1] - 1
    if oggetto[0] < 0:
        esito = -10
        oggetto[0] = 0
    if oggetto[0] > mondox -2:
        esito = -10
        oggetto[0] = mondox-2
    if oggetto[1] < 0:
        esito = -10
        oggetto[1] = 0
    if oggetto[1] > mondoy-2:
        esito = -10
        oggetto[1] = mondoy-2
    xd, yd = aggiusta_coord(oggetto[0], oggetto[1], 'c')
    pygame.draw.circle(sfondo, colore_tallo, (xd, yd), dimensione / 2, 0)
    if mondotallo[oggetto[0]][oggetto[1]] == 1:
        mondotallo[oggetto[0]][oggetto[1]] = 0
        mondotallo[random.randrange(0, mondox)][random.randrange(0, mondoy)] = 1
        esito = 100
    griglia = ''
    for y in range(oggetto[1]-vista, oggetto[1]+vista+1):
        for x in range(oggetto[0] - vista, oggetto[0] + vista + 1):
            if x < 0 or y < 0 or x >= mondox or y >= mondoy:
                griglia += '3'
            else:
                griglia += str(mondotallo[x][y])

#    if griglia != '0000000000000000000000000000000000000000000000000':
#        print('x', griglia[0:7], 'x')
#        print('x', griglia[7:14], 'x')
#        print('x', griglia[14:21], 'x')
#        print('x', griglia[21:28], 'x')
#        print('x', griglia[28:35], 'x')
#        print('x', griglia[35:42], 'x')
#        print('x', griglia[42:49], 'x')
#        print('--------------------')
#        input('invio per continuare')

    return esito, griglia

#-------------------------------------------------------------------------------

pygame.init()
sfondo=pygame.display.set_mode((1200,800))
pygame.display.set_caption('Tallo 1')
pygame.font.init()
miofont = pygame.font.SysFont('None', 24)
sfondo.fill(colore_mondo)
mondotallo = creamondo(mondox, mondoy,200)
tallo = [random.randrange(1, mondox-2), random.randrange(1, mondoy-2)]
#tallo = [0,0]
#mondotallo[tallo[0]][tallo[1]] = 2
# stampamondo(mondotallo)
datix = mondox * dimensione + dimensione
disegnamondo()
azione = 9
old_puntatore = -1
pygame.display.flip()

x = 0
while True:
    x+= 1
#for x in range(0,10000):
    #sleep(0.2)
    tempo = time.time()
    esito, griglia = disegna(tallo, 'T', azione)
    if esito == 100:
        cibo += 1
    if esito == -10:
        urti += 1
    if esito == -1:
        nulle += 1

    if keyboard.is_pressed("q"):
        break
    if esito != 0 and old_puntatore != -1:
        qtable2[old_puntatore][azione] += esito
    oo ='0'*(vista+vista+1)**2
    if griglia != '0'*(vista+vista+1)**2:
        if qtable1.count(griglia) == 0:
            qtable1.append(griglia)
            qtable2.append([0,0,0,0,0,0,0,0,0])
        puntatore = qtable1.index(griglia)
        azione = qtable2[puntatore].index(max(qtable2[puntatore]))
        if qtable2[puntatore][azione] == 0:
            azione = random.randrange(1, 9)
            casuali += 1
        else:
            scelte += 1
    else:
        vuote += 1
        azione = random.randrange(1, 9)
        puntatore = -1
    old_puntatore=puntatore
    pygame.draw.rect(sfondo, colore_tes, (datix, dimensione, datix +200,200))
    sfondo.blit(miofont.render('Cicli   '+format(x, ',d'), True, colore_tallo), (datix, dimensione))
    areatesto = miofont.render('Casuali '+str(casuali), True, colore_tallo)
    sfondo.blit(areatesto, (datix, dimensione+20))
    areatesto = miofont.render('Scelte  '+str(scelte), True, colore_tallo)
    sfondo.blit(areatesto, (datix, dimensione+40))
    sfondo.blit(miofont.render('Cibo    '+str(cibo), True, colore_tallo), (datix, dimensione+60))
    sfondo.blit(miofont.render('Qtable  '+str(len(qtable1)), True, colore_tallo), (datix, dimensione+80))
    sfondo.blit(miofont.render('Tempo   '+str(tempo - time.time()), True, colore_tallo), (datix, dimensione+100))
    sfondo.blit(miofont.render('Nulle   '+str(nulle), True, colore_tallo), (datix, dimensione+120))
    sfondo.blit(miofont.render('Urti    '+str(urti), True, colore_tallo), (datix, dimensione+140))
    sfondo.blit(miofont.render('Vuote   '+str(vuote), True, colore_tallo), (datix, dimensione+160))
    pygame.display.flip()
print ('fine')





