from math import inf

def etat_initial():
    return (1, ((0,0,0,0,0,0,0),(0,0,0,0,0,0,0),(0,0,0,0,0,0,0),(0,0,0,0,0,0,0),(0,0,0,0,0,0,0),(0,0,0,0,0,0,0)))


def coups_possibles(etat):
    M = etat[1]
    liste_pos = []
    for col in range(7):
        lig = legal(col, M)
        if lig >= 0 :
            liste_pos.append((lig, col))
    return liste_pos

def legal(col, M):
    haut = 0
    for lig in range(6):
        haut += abs(M[lig][col])
    if haut <= 5:
        return (5-haut) #lig
    else:
        return (-1)   #coup impossible
    
def est_gagnant(etat):
    M = etat[1]

            
    for lig in range(6): # horizontalement
        for col in range(4):
            L_pions = [M[lig][col+i] for i in range(4)]
            if score_case(L_pions, 1):
                return 1
            if score_case(L_pions, -1):
                return -1
       
    for lig in range(3): # verticalement
        for col in range(7):
            L_pions = [M[lig+i][col] for i in range(4)]
            if score_case(L_pions, 1):
                return 1
            if score_case(L_pions, -1):
                return -1
        
    for lig in range(3): # diagonalement desc
        for col in range(4):
            L_pions = [M[lig+i][col+i] for i in range(4)]
            if score_case(L_pions, 1):
                return 1
            if score_case(L_pions, -1):
                return -1

    for lig in range(3): # diagonalement mont
        for col in range(4):
            L_pions = [M[lig+3-i][col+i] for i in range(4)]
            if score_case(L_pions, 1):
                return 1
            if score_case(L_pions, -1):
                return -1
                        
    return 0


def score_case(L_pions, pion):
        
    if L_pions.count(pion) == 4:
        return True
    
    
def jouer_coup(etat, coup):
    l, c = coup
    joueur = etat[0]
    M = etat[1]
    nv_joueur = - joueur
    nv_M = tuple(
        (
            tuple((joueur if i == l and j == c else M[i][j] for j in range(7)))
            for i in range(6)
            )
        )
    return(nv_joueur, nv_M)
    
def premier_parcours():
    dico = dict()
    pile = [etat_initial()] # on commence à l'état initial
    while len(pile) > 0:
        etat = pile.pop()
        if etat not in dico:
            dico[etat] = None     
            if est_gagnant(etat) == 0 :
                coups = coups_possibles(etat)
                if coups != [] :
                    for i in coups :
                        pile.append(jouer_coup(etat, i))
    return dico

    
    
    
    
    