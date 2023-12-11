#import winsound


# Dizionari per tenere traccia delle partite vinte da ciascun giocatore
part_vinte = {'X': 0, 'O': 0}
pedine = {'X': '\033[31mX\033[0m', 'O': '\033[93mO\033[0m'} #Pedine colorate con codici ASCII



# Funzione per avviare il gioco del Tris
def gioca_tictactoe():
    print('\033[31;1m'+'''
__________________TIC-TAC-TOE___________________\033[0m
          
        Benvenuti al gioco del tic-tac-toe.
            Si gioca in due, X e O.
          A turno bisogna posizionare
      la propria pedina in una griglia 3X3.
 Vince il primo che metterà in fila 3 sue pedine.
          Chi gioca per primo? X o O?''')
    inizializza_part()
    while True:
        primo_giocatore = input().upper()
        if primo_giocatore == 'X' or primo_giocatore == 'O':
            return assegna_posizione(primo_giocatore)
        print('Giocatore non valido!')



#Funzione per azzerare posizioni del gioco e numero turni
def inizializza_part():
    global posizioni 
    posizioni = {'A1': ' ', 'B1': ' ', 'C1': ' ',
                    'A2': ' ', 'B2': ' ', 'C2': ' ',
                    'A3': ' ', 'B3': ' ', 'C3': ' ',}
    global n_turno
    n_turno = 1



#Funzione per stampare la griglia di gioco e punteggio partite
def stampa_griglia(): 
    print(f'''
     A   B   C                PARTITE VINTE
    
1    {posizioni["A1"]} | {posizioni["B1"]} | {posizioni["C1"]}                    X | O
    -----------                   -----
2    {posizioni["A2"]} | {posizioni["B2"]} | {posizioni["C2"]}                    {part_vinte['X']} | {part_vinte['O']}
    -----------
3    {posizioni["A3"]} | {posizioni["B3"]} | {posizioni["C3"]}
    
    ''')



#Funzione per aggiornare posizione cursore per sovrascrivere alla griglia precedente
def aggiorna_cursore():
    print('\033[1A'+'  ', end = '\r')   #Codici ASCII per spostare cursore, da migliorare
    print('\033[12A')



#Funzione per assegnare la posizione alla pedina
def assegna_posizione(pedina):
    stampa_griglia()
    posizione = input(f'Giocatore {pedina} inserisci posizione in cui giocare {pedina}: (es. B2)\n').upper()
    aggiorna_cursore()
    #Controllo che la posizione esista e che non sia già occupata
    try:
        if posizioni[posizione] == ' ':
            posizioni[posizione] = pedine[pedina]
            global n_turno
            n_turno += 1
            return controlla_vittoria(pedina)
        else:
            #print('POSIZIONE NON VALIDA!')
            assegna_posizione(pedina)
    except:
        #print('POSIZIONE NON VALIDA!')
        assegna_posizione(pedina)



#Funzione che aggiorna condizioni vittoria
def aggiorna_cond_vittoria(pedina):
    cond1 = posizioni["A1"] == posizioni["B1"] == posizioni["C1"] == pedine[pedina]
    cond2 = posizioni["A2"] == posizioni["B2"] == posizioni["C2"] == pedine[pedina]
    cond3 = posizioni["A3"] == posizioni["B3"] == posizioni["C3"] == pedine[pedina]
    cond4 = posizioni["A1"] == posizioni["A2"] == posizioni["A3"] == pedine[pedina]
    cond5 = posizioni["B1"] == posizioni["B2"] == posizioni["B3"] == pedine[pedina]
    cond6 = posizioni["C1"] == posizioni["C2"] == posizioni["C3"] == pedine[pedina]
    cond7 = posizioni["A1"] == posizioni["B2"] == posizioni["C3"] == pedine[pedina]
    cond8 = posizioni["A3"] == posizioni["B2"] == posizioni["C1"] == pedine[pedina]
    COND_GEN = cond1 + cond2 + cond3 + cond4 + cond5 + cond6 + cond7 + cond8
    return COND_GEN



#Funzione che controlla eventuale vittoria o pareggio altrimenti cambia turno      
def controlla_vittoria(pedina):
    controllo = aggiorna_cond_vittoria(pedina)
    if controllo:
        part_vinte[pedina] += 1
        stampa_griglia()
        #winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print(f'Ha vinto il Giocatore {pedina}!'+' '*50+'\n'+' '*20)
        return inizia_nuova_partita(pedina)
    if n_turno == 10:
        stampa_griglia()
        print('Pareggio!'+ ' '*50)
        return inizia_nuova_partita(pedina)
    else:
        return cambia_turno(pedina)



#Funzione per cambiare turno       
def cambia_turno(pedina):
    if pedina == 'X':
        return assegna_posizione('O')
    else:
        return assegna_posizione('X')



#Funzione per iniziare una nuova partita    
def inizia_nuova_partita(pedina):
    print('Iniziare una nuova partita? Y/N')
    if input().upper() == 'Y':
        print('\n'+'-'*30+'\nQuesta volta inizierà il perdente!')
        inizializza_part()
        return cambia_turno(pedina)
    else:
        print(f'Il gioco finisce con un punteggio di X:{part_vinte["X"]} a O:{part_vinte["O"]}')
        return



#Chiamata del gioco
gioca_tictactoe()
