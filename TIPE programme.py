import random
from math import inf
import copy

"""M = [[0 for lig in range(7)]for col in range(6)]"""

def graph(M):
    Mgr = [[0 for p in range(7)]for q in range(6)]
    for lig in range(len(M)):
        for col in range(len(M[lig])):
            if M[lig][col] == 0:
                Mgr[lig][col] = '_'
            if M[lig][col] == 1 :
                Mgr[lig][col] = 'O'
            if M[lig][col] == -1 :
                Mgr[lig][col] = 'X'
    return Mgr

def aff(M):
    for lig in M:
        print (lig)
    print ('\n  0    1    2    3    4    5    6\n')
     


'''def jeu():
    M = [[0 for lig in range(7)]for col in range(6)]      
    """Mgr = graph(M)
    aff(Mgr)"""
    print(M)
    for t in range(21):    

        coupj1 = int(input('\nJoueur 1,\nDans quelle colonne placer le pion ? : \n'))
        M1 = placer(coupj1, M, 1)
        while M1 == False :  
            print(M)
            """Mgr = graph(M)
            aff(Mgr)"""
            print('ERREUR, LA COLONNE EST REMPLIE')
            coupj1 = int(input('\nJoueur 1,\nDans quelle colonne placer le pion ? : \n'))
            M1 = placer(coupj1, M, 1)
        
        Mgr = graph(M)
        aff(Mgr)
        print(M)
        if test(M, coupj1):
            print('LE JOUEUR 1 EST VAINQUEUR')
            return (1)
            break
        
        coupj2 = int(input('\nJoueur 1,\nDans quelle colonne placer le pion ? : \n'))
        M2 = placer(coupj2, M, -1)
        while M2 == False :  
            print(M)
            """Mgr = graph(M)
            aff(Mgr)"""
            print('ERREUR, LA COLONNE EST REMPLIE')
            coupj2 = int(input('\nJoueur 1,\nDans quelle colonne placer le pion ? : \n'))
            M2 = placer(coupj2, M, -1)
            
        Mgr = graph(M)
        aff(Mgr)
        print(M)
        if test(M, coupj2):
            print('LE JOUEUR 2 EST VAINQUEUR')
            return (-1)
            break
    return(0)'''

def jeu():
    M = [[0 for lig in range(7)]for col in range(6)]      
    Mgr = graph(M)
    aff(Mgr)
    for tour in range(21):
        
        coup1 = joueur(M, 1)
        poser(coup1, M, 1)
        print(M)
        if test(M, coup1):
            print('LE JOUEUR 1 EST VAINQUEUR')
            return (1)
            break
        
        coup2 = joueur(M, -1)
        poser(coup2, M, -1)
        print(M)
        if test(M, coup2):
            print('LE JOUEUR 2 EST VAINQUEUR')
            return (-1)
            break
    return 0

def creer():
    M = [[0 for lig in range(7)]for col in range(6)]      
    print(M)
    for tour in range(21):
        
        coup1 = joueur(M, 1)
        poser(coup1, M, 1)
        print(M)
        if test(M, coup1):
            print('LE JOUEUR 1 EST VAINQUEUR')
            return (1)
            break
        
        coup2 = joueur(M, -1)
        poser(coup2, M, -1)
        print(M)
        if test(M, coup2):
            print('LE JOUEUR 2 EST VAINQUEUR')
            return (-1)
            break
    return 0

def j(prof):
    M = [[0 for lig in range(7)]for col in range(6)]      
    Mgr = graph(M)
    aff(Mgr)
    for tour in range(21):
        
        coup1 = joueur(M, 1)
        poser(coup1, M, 1)
        Mgr = graph(M)
        aff(Mgr)
        if test(M, coup1):
            print('LE JOUEUR 1 EST VAINQUEUR')
            return (1)
            break
        
        coup2 = algo(M, prof, True, -1)
        poser(coup2, M, -1)
        Mgr = graph(M)
        aff(Mgr)
        if test(M, coup2):
            print('LE JOUEUR 2 EST VAINQUEUR')
            return (-1)
            break
    return 0


def joueur(M, pion):
    coups_possibles = pos_possibles(M)
    coupj = int(input('\nJoueur 1,\nDans quelle colonne placer le pion ? : \n'))
    while not(coupj in coups_possibles):  
        Mgr = graph(M)
        aff(Mgr)
        print('ERREUR, LA COLONNE EST REMPLIE')
        coupj = int(input('\nJoueur 1,\nDans quelle colonne placer le pion ? : \n'))
    return coupj
        
def algo(M, prof, maxj, pion):
    coupj, _ = minimax(M, prof, maxj, pion)
    return coupj
    
def aleatoire(M, pion):
    coups_possibles = pos_possibles(M)
    pos = random.randint(0, len(coups_possibles)-1)
    coupj = coups_possibles[pos]
    return coupj  


def minimax(noeud, prof, maxj, pion):
    liste_pos = pos_possibles(noeud)
    
    if prof == 0 or est_noeud_term(noeud) :
        if est_noeud_term(noeud) :
            if poids(noeud, pion) == inf:
                return (None, inf)
            elif poids(noeud, -pion) == inf:
                return (None, -inf)
            else:  
                return (None, 0)
        else :
            return(None , poids(noeud, pion))
    
    
    if maxj :
        valeur = -inf
        pos = liste_pos[random.randint(0, len(liste_pos)-1)]
        for col in liste_pos:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, pion)
            _, nv_valeur = minimax(noeud_c, prof-1, False, pion)
            if nv_valeur > valeur :
                valeur = nv_valeur
                pos = col
        return (pos, valeur)

    else :
        valeur = inf
        pos = liste_pos[random.randint(0, len(liste_pos)-1)]
        for col in liste_pos:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, -pion)
            _, nv_valeur = minimax(noeud_c, prof-1, True, pion)
            if nv_valeur < valeur :
                valeur = nv_valeur
                pos = col
        return (pos, valeur)
    
   
def alphabeta(noeud, prof, alpha, beta, maxj, pion):
    liste_pos = pos_possibles(noeud)
    
    if prof == 0 or est_noeud_term(noeud) :
        if est_noeud_term(noeud) :
            if poids(noeud, pion) == inf:
                return (None, inf)
            elif poids(noeud, -pion) == inf:
                return (None, -inf)
            else:  
                return (None, 0)
        else :
            return(None , poids(noeud, pion))
    
    
    if maxj :
        valeur = -inf
        pos = liste_pos[random.randint(0, len(liste_pos)-1)]
        for col in liste_pos:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, pion)
            _, nv_valeur = alphabeta(noeud_c, prof-1, alpha, beta, False, pion)
            if nv_valeur > valeur :
                valeur = nv_valeur
                pos = col
            alpha = max(alpha, valeur)
            if alpha >= beta:
                break
        return (pos, valeur)

    else :
        valeur = inf
        pos = liste_pos[random.randint(0, len(liste_pos)-1)]
        for col in liste_pos:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, -pion)
            _, nv_valeur = alphabeta(noeud_c, prof-1, alpha, beta, True, pion)
            if nv_valeur < valeur :
                valeur = nv_valeur
                pos = col
            beta = min(beta, valeur)
            if alpha >= beta:
                break
        return (pos, valeur)    
   
def est_fini(M):
    return poids(M, 1) == inf or poids(M,-1) == inf
        
            
def est_noeud_term(M):   
    return est_fini(M) or pos_possibles(M) == []

def pos_possibles(M):
    liste_pos = []
    for col in range(7):
        if legal(col, M) >= 0 :
            liste_pos.append(col)
    return liste_pos



def placer(col, M, pion):
    haut = 0
    for lig in range(6):
        haut += abs(M[lig][col])
    if haut <= 5:
        return True
    return False

def poser(col, M, pion):
    haut = 0
    for lig in range(6):
        haut += abs(M[lig][col])
    M[5-haut][col] = pion



def test(M, col):
    if col == -1 :
        return False
    else:
        haut = 0
        for li in range(6):
            haut += abs(M[li][col])
        lig = 6 - haut
        if test_ver(M, lig, col) or test_hor(M,lig) or test_diagmont(M) or test_diagdesc(M):
            return True
        return False

def test_ver(M,lig,col):
    if lig <= 2 :
        return (M[lig][col] == M[lig+1][col] == M[lig+2][col] == M[lig+3][col] != 0)
    return False
    
def test_hor(M,lig):
    for col in range(4):
        if M[lig][col] == M[lig][col+1] == M[lig][col+2] == M[lig][col+3] != 0:
            return True
    return False
    
def test_diagmont(M):
    for lig in range(3, 6):
        for col in range(4):
            if M[lig][col] == M[lig-1][col+1] == M[lig-2][col+2] == M[lig-3][col+3] != 0 :
                return True
    return False

def test_diagdesc(M):
    for lig in range(3):
        for col in range(4):
            if M[lig][col] == M[lig+1][col+1] == M[lig+2][col+2] == M[lig+3][col+3] != 0 :
                return True
    return False
        


    
    
######################



    
#Video




"""def poids(col, M, pion):
    v = 0
    lig = legal(col, M)
    if lig >= 0:
        M[lig][col] = pion
    lig = 6
    for li in range(6):
        lig -= abs(M[li][col])
    

    if test(M, col):
        return inf
    M_c = copy.deepcopy(M)
    M_c[lig][col] = -M_c[lig][col] 
    if test(M_c, col):
        return inf
    if col == 3:
        v += 7
    if col == 2 or col == 4:
        v += 4
    if col == 1 or col == 5:
        v += 2
    if col == 0 or col == 6:
        v -= 1
    if hor3(M, lig, col, pion):
        v += 13
    elif hor2(M, lig, col, pion):
        v += 6
    if ver3(M, lig, col, pion) or ver3(M, lig, col, -pion):
        v += 13
    elif ver2(M, lig, col, pion) or ver2(M, lig, col, -pion):
        v += 6
    if diag3(M, lig, col, pion) or diag3(M, lig, col, -pion):
        v += 18
    elif diag2(M, lig,col, pion) or diag2(M, lig, col, -pion):
        v += 9
    return v"""

def poids(M, pion):
    score = 0


    for lig in range(6): # pions au milieu de la grille
        if M[lig][2] == pion:
            score += 2
        if M[lig][3] == pion:
            score += 3
        if M[lig][4] == pion:
            score += 2
        if M[lig][1] == pion:
            score += 1
        if M[lig][5] == pion:
            score += 1
        
    
    for lig in range(6): # horizontalement
        for col in range(4):
            L_pions = [M[lig][col+i] for i in range(4)]
            score += score_case(L_pions, pion)

       
    for lig in range(3): # verticalement
        for col in range(7):
            L_pions = [M[lig+i][col] for i in range(4)]
            score += score_case(L_pions, pion)
        

    for lig in range(3): # diagonalement desc
        for col in range(4):
            L_pions = [M[lig+i][col+i] for i in range(4)]
            score += score_case(L_pions, pion)

    for lig in range(3): # diagonalement mont
        for col in range(4):
            L_pions = [M[lig+3-i][col+i] for i in range(4)]
            score += score_case(L_pions, pion)
            
    """for lig in range(6):
    row_array = [int(i) for i in list(M[lig,:])]
    for col in range(4):
        L_pions = row_array[col:col+4]
        score += score_case(L_pions, pion)
        
    for col in range(7):  # 
        col_array = [int(i) for i in list(M[:,col])]
        for lig in range(3):
            L_pions = col_array[lig:lig+4]
            score += score_case(L_pions, pion)"""
        
    return score


def score_case(L_pions, pion):
    score = 0
    
    
    if L_pions.count(pion) == 4:
        return inf
    elif L_pions.count(pion) == 3 and L_pions.count(0) == 1:
        score += 12
    elif L_pions.count(pion) == 2 and L_pions.count(0) == 2:
        score += 7
    
    if  L_pions.count(-pion) == 3 and L_pions.count(0) == 1:
        score -= 12
    if L_pions.count(-pion) == 4:
        return -inf
        
        
    return score
    
    

    
"""
def hor3(M, lig, col, pion):
    for k in range(5):
        if (col == k or col == k+1 or col == k+2) and (M[lig][k] == M[lig][k+1] == M[lig][k+2] == pion):
            return True
    return False


def hor2(M, lig, col, pion):
    for k in range(6):
        if (col == k or col == k+1) and (M[lig][k] == M[lig][k+1] == pion):
            return True
    return False


def ver3(M, lig, col, pion):
    if lig <= 3:
        if M[lig][col] == M[lig+1][col] == M[lig+2][col] == pion:
            return True
    return False


def ver2(M, lig, col, pion):
    if lig <= 4:
        if M[lig][col] == M[lig+1][col] == pion:
            return True
    return False


def diag3(M, lig, col, pion):
    if lig > 0 and lig < 5 and col > 0 and col < 6:
        if M[lig-1][col-1] == M[lig][col] == M[lig+1][col+1] == pion:
            return True
        if M[lig-1][col+1] == M[lig][col] == M[lig+1][col-1] == pion:
            return True
    if lig == 0:
        if col < 5:
            if M[lig][col] == M[lig+1][col+1] == M[lig+2][col+2] == pion:
                return True
        if col > 1:
            if M[lig][col] == M[lig+1][col-1] == M[lig+2][col-2] == pion:
                return True
    if lig == 5:
        if col < 5:
            if M[lig][col] == M[lig-1][col+1] == M[lig-2][col+2] == pion:
                return True
        if col > 1:
            if M[lig][col] == M[lig-1][col-1] == M[lig-2][col-2] == pion:
                return True
    return False
        
    

def diag2(M, lig, col, pion):
    if lig < 5:
        if col < 6 and (M[lig][col] == M[lig+1][col+1] == pion) :
            return True
        if col > 0 and (M[lig][col] == M[lig+1][col-1] == pion) :
            return True
    if lig > 0:
        if col < 6 and (M[lig][col] == M[lig-1][col+1] == pion) :
            return True
        if col > 0 and (M[lig][col] == M[lig-1][col-1] == pion) :
            return True
    return False
        
    


#graphe = [[[0,1,2,3,4,5,6],]]
"""

def legal(col, M):
    haut = 0
    for lig in range(6):
        haut += abs(M[lig][col])
    if haut <= 5:
        return (5-haut) #lig
    else:
        return (-1)   #coup impossible

"""

    
#fonction poids qui analyse le joueur qui a l'avantage dans la grille en évaluant cet écart


#def p(M):
    
    
#6 = 6
#7 = 7
PLAYER = 0
AI = 1

#0 = 0
PLAYER_PIECE = 1
AI_PIECE = 2

#4 = 4
    
    
def evaluate_window(window, piece):
	score = 0
	opp_piece = PLAYER_PIECE
	if piece == PLAYER_PIECE:
		opp_piece = AI_PIECE

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(0) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(0) == 2:
		score += 2

	if window.count(opp_piece) == 3 and window.count(0) == 1:
		score -= 4

	return score


def score_position(board, piece):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, 7//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(6):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(7-3):
			window = row_array[c:c+4]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(7):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(6-3):
			window = col_array[r:r+4]
			score += evaluate_window(window, piece)

	## Score positive sloped diagonal
	for r in range(6-3):
		for c in range(7-3):
			window = [board[r+i][c+i] for i in range(4)]
			score += evaluate_window(window, piece)

	for r in range(6-3):
		for c in range(7-3):
			window = [board[r+3-i][c+i] for i in range(4)]
			score += evaluate_window(window, piece)

	return score
    
 """   
    
    
