import random
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
            break
    return

def dammi_griglia(xx, yy):
    griglia = ''
    for y in range(yy-at_vista, yy+at_vista+1):
        for x in range(xx - at_vista, xx + at_vista + 1):
            if x < 0 or y < 0 or x >= at_mondo_righe or y >= at_mondo_colonne:
                griglia += '3'
            else:
                griglia += str(at_mondo[x][y])
    return griglia

def azione_tallo(tallo, azione=9):  # azione 1 su, 2 destra, 3 giu, 4 sinistra, 5 su destra, 6 giu destra, 7 giu sinistra, 8 su sinistra, 9 fermo
    global  at_ciclo,at_urti, at_cibo
    at_ciclo += 1
    esito = random.randint(at_esito_niente_a, at_esito_niente_b) * -1
    if azione == 1:
        tallo[1] = tallo[1] - 1
    if azione == 2:
        tallo[0] = tallo[0] + 1
    if azione == 3:
        tallo[1] = tallo[1] + 1
    if azione == 4:
        tallo[0] = tallo[0] - 1
    if azione == 5:
        tallo[0] = tallo[0] + 1
        tallo[1] = tallo[1] - 1
    if azione == 6:
        tallo[0] = tallo[0] + 1
        tallo[1] = tallo[1] + 1
    if azione == 7:
        tallo[0] = tallo[0] - 1
        tallo[1] = tallo[1] + 1
    if azione == 8:
        tallo[0] = tallo[0] - 1
        tallo[1] = tallo[1] - 1
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
    if at_mondo[tallo[0]][tallo[1]] == 1:
        at_mondo[tallo[0]][tallo[1]] = 0
        crea_cibo()
        esito = random.randint(at_esito_cibo_a, at_esito_cibo_b)
        at_cibo+=1
    griglia = dammi_griglia(tallo[0],tallo[1])
    return esito, griglia

def dammi_valori():
    return at_urti, at_cibo
