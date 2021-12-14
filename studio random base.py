from env_tallo_nv_1_00 import *
from time import *




casuali = scelte = vuote = 0
crea_mondo(100,50,30)
tallo = [random.randrange(1, at_mondo_colonne-1), random.randrange(1, at_mondo_righe-1)]
for studio in range(1, 10):
    cicli = studio * 1000000
    inizio = time()
    for x in range(0,cicli ):
        azione = random.randint(0, 8)
        casuali += 1
        punteggio, griglia = azione_tallo(tallo, azione)
    urti,cibo = dammi_valori()
    print(str(int(time()-inizio))+' '+str(cicli)+' '+str(urti)+' '+str(cibo))
print('fine')

