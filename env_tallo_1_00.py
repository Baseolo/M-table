import random
import pygame
import math


at_mondo_righe = 50
at_mondo_colonne = 100
at_mondo_cibo = 30
at_dimensione = 10
at_vista = 3
at_mondo = []
at_ciclo = 0
at_urti = 0
at_cibo = 0

at_esito_urto_a = 70
at_esito_urto_b = 100
at_esito_niente_a = 0
at_esito_niente_b = 2
at_esito_cibo_a = 800
at_esito_cibo_b = 1200

at_col_at_sfondo = '#8fbc8f'
at_col_cibo = '#2f4f4f'
at_col_cella = '#1e90ff'
at_col_ostacolo = '#8b0000'
at_col_tallo = '#000000'
at_col_visitato = '#98FF98'

pygame.init()
at_sfondo=pygame.display.set_mode((1200,800))
pygame.display.set_caption('Ambiente Tallo 1.0')
#pygame.font.init()
at_font = pygame.font.SysFont('None', 24)
at_sfondo.fill(at_col_at_sfondo)


def crea_mondo(righe=100, colonne=100, cibo=30):
    global at_mondo_righe, at_mondo_colonne, at_mondo_cibo, at_mondo
    at_mondo_righe = righe
    at_mondo_colonne = colonne
    at_mondo_cibo = cibo
    at_mondo = [[0] * at_mondo_colonne for i in range(at_mondo_righe)]
    for i in range(cibo):
        crea_cibo()
    return

def crea_cibo():
    global at_mondo
    while True:
        cibox = random.randrange(0, at_mondo_righe-1)
        ciboy = random.randrange(0, at_mondo_colonne-1)
        if at_mondo[cibox][ciboy] == 0:
            at_mondo[cibox][ciboy] = 1
            xd, yd = aggiusta_coord(cibox, ciboy, 'q')
            pygame.draw.rect(at_sfondo, at_col_cibo, (xd + 1, yd + 1, at_dimensione - 2, at_dimensione - 2))
            break
    return

def stampa_mondo():
    for riga in at_mondo:
        for cella in riga:
            print(cella,end=' ')
        print()


def disegna_mondo():
    for x in range(0, at_mondo_righe):
        for y in range(0, at_mondo_colonne):
            xd,yd = aggiusta_coord(x,y,'q')
            pygame.draw.rect(at_sfondo, at_col_cella, (xd, yd, at_dimensione, at_dimensione), 1)
            if at_mondo[x][y] == 1:
                pygame.draw.rect(at_sfondo, at_col_cibo, (xd+1, yd+1, at_dimensione-2, at_dimensione-2))
    pygame.display.flip()
    return

def aggiusta_coord(x, y, tipo):
    xx = x * at_dimensione
    yy = y * at_dimensione
    if tipo == 'c':
        xx += int(at_dimensione/2)
        yy += int(at_dimensione/2)
    return xx,yy

def dammi_griglia(xx, yy):
    griglia = ''
    for y in range(yy-at_vista, yy+at_vista+1):
        for x in range(xx - at_vista, xx + at_vista + 1):
            if x < 0 or y < 0 or x >= at_mondo_righe or y >= at_mondo_colonne:
                griglia += '3'
            else:
                griglia += str(at_mondo[x][y])
    return griglia

def disegna_griglia(griglia):
    base = int(math.sqrt(len(griglia)))
    pos_tallo = int((base -1) / 2)
    for x in range(0, base):
        for y in range(0, base):
            posizione = int(x*base+y)
            valore = griglia [posizione:posizione+1]
            if x == pos_tallo and y == pos_tallo:
                valore = '2'
            xx,yy = aggiusta_coord(y,x,'q')
            xx += 1000 + at_dimensione
            yy += at_dimensione
            pygame.draw.rect(at_sfondo, at_col_at_sfondo, (xx, yy, at_dimensione, at_dimensione), 0)
            if valore == '0':
                pygame.draw.rect(at_sfondo, at_col_cella, (xx, yy, at_dimensione, at_dimensione), 0)
                pygame.draw.rect(at_sfondo, '#293133', (xx, yy, at_dimensione, at_dimensione), 1)
            if valore == '1':
                pygame.draw.rect(at_sfondo, at_col_cella, (xx, yy, at_dimensione, at_dimensione), 1)
                pygame.draw.rect(at_sfondo, at_col_cibo, (xx + 1, yy + 1, at_dimensione - 2, at_dimensione - 2))
            if valore == '2':
                pygame.draw.rect(at_sfondo, at_col_cella, (xx, yy, at_dimensione, at_dimensione), 1)
                xx,yy = aggiusta_coord(y,x,'c')
                xx += 1000 + at_dimensione
                yy += at_dimensione
                pygame.draw.circle(at_sfondo, at_col_tallo, (xx, yy), at_dimensione / 2, 0)
            if valore == '3':
                pygame.draw.rect(at_sfondo, at_col_ostacolo, (xx, yy, at_dimensione, at_dimensione), 0)
                pygame.draw.rect(at_sfondo, '#293133', (xx, yy, at_dimensione, at_dimensione), 1)
    return

def azione_tallo(tallo, azione=9):  # azione 1 su, 2 destra, 3 giu, 4 sinistra, 5 su destra, 6 giu destra, 7 giu sinistra, 8 su sinistra, 9 fermo
    global  at_ciclo,at_urti, at_cibo
    at_ciclo += 1
    esito = random.randint(at_esito_niente_a, at_esito_niente_b) * -1
    xd, yd = aggiusta_coord(tallo[0], tallo[1], 'q')
    pygame.draw.rect(at_sfondo, at_col_cella, (xd, yd, at_dimensione, at_dimensione), 1)
    xd, yd = aggiusta_coord(tallo[0], tallo[1], 'c')
    pygame.draw.circle(at_sfondo, at_col_visitato, (xd, yd), at_dimensione/2-1, 0)
    pygame.draw.rect(at_sfondo, at_col_tallo, (1098, 18, 44, 44), 0)
    if azione == 1:
        tallo[1] = tallo[1] - 1
        disegna_freccia((1120,60),(1120,25))
    if azione == 2:
        tallo[0] = tallo[0] + 1
        disegna_freccia((1100,40),(1133,40))
    if azione == 3:
        tallo[1] = tallo[1] + 1
        disegna_freccia((1120,20),(1120,55))
    if azione == 4:
        tallo[0] = tallo[0] - 1
        disegna_freccia((1130,40),(1105,40))
    if azione == 5:
        tallo[0] = tallo[0] + 1
        tallo[1] = tallo[1] - 1
        disegna_freccia((1100,60),(1133,25))
    if azione == 6:
        tallo[0] = tallo[0] + 1
        tallo[1] = tallo[1] + 1
        disegna_freccia((1100,20),(1133,55))
    if azione == 7:
        tallo[0] = tallo[0] - 1
        tallo[1] = tallo[1] + 1
        disegna_freccia((1140,20),(1105,55))
    if azione == 8:
        tallo[0] = tallo[0] - 1
        tallo[1] = tallo[1] - 1
        disegna_freccia((1140,60),(1105,25))
    if tallo[0] < 0:
        esito = random.randint(at_esito_urto_a, at_esito_urto_b) * -1
        tallo[0] = 0
        at_urti += 1
    if tallo[0] > at_mondo_righe -1:
        esito = random.randint(at_esito_urto_a, at_esito_urto_b) * -1
        tallo[0] = at_mondo_righe-1
        at_urti += 1
    if tallo[1] < 0:
        esito = random.randint(at_esito_urto_a, at_esito_urto_b) * -1
        tallo[1] = 0
        at_urti += 1
    if tallo[1] > at_mondo_colonne-1:
        esito = random.randint(at_esito_urto_a, at_esito_urto_b) * -1
        tallo[1] = at_mondo_colonne-1
        at_urti += 1
    xd, yd = aggiusta_coord(tallo[0], tallo[1], 'c')
    pygame.draw.circle(at_sfondo, at_col_tallo, (xd, yd), at_dimensione / 2, 0)
    if at_mondo[tallo[0]][tallo[1]] == 1:
        at_mondo[tallo[0]][tallo[1]] = 0
        crea_cibo()
        esito = random.randint(at_esito_cibo_a, at_esito_cibo_b)
        at_cibo+=1
    griglia = dammi_griglia(tallo[0],tallo[1])
    disegna_griglia(griglia)
    pygame.draw.rect(at_sfondo, at_col_visitato, (1002, 100, 1250 +200,300))
    at_sfondo.blit(at_font.render('Cicli   '+format(at_ciclo, ',d'), True, at_col_ostacolo), (1005, 105))
    at_sfondo.blit(at_font.render('Urti    ' + format(at_urti, ',d'), True, at_col_ostacolo), (1005, 125))
    at_sfondo.blit(at_font.render('Cibo    ' + format(at_cibo, ',d'), True, at_col_ostacolo), (1005, 145))
    pygame.display.flip()
    return esito, griglia

def disegna_freccia( start, end):
    pygame.draw.line(at_sfondo,'#FF6600',start,end,2)
    rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
    pygame.draw.polygon(at_sfondo, '#FF6600', ((end[0]+7*math.sin(math.radians(rotation)), end[1]+7*math.cos(math.radians(rotation))), (end[0]+7*math.sin(math.radians(rotation-120)), end[1]+7*math.cos(math.radians(rotation-120))), (end[0]+7*math.sin(math.radians(rotation+120)), end[1]+7*math.cos(math.radians(rotation+120)))))