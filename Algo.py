from math import inf

"""def minmax(noeud, prof, maxj):
    if prof = 0 or noeud est un noeud terminal:  # pareil ?
        return la valeur heuristique du noeud (poids)
    if maxj:
        valeur = - inf
        for enfant de noeud:
            valeur = max(valeur, minmax(fils, prof - 1, False))
    else:  #minimiser le joueur
        valeur = + inf
        for enfant de noeud:
            valeur = min(valeur, minmax(fils, prof - 1, True))
    return valeur"""

"""attribuer des valeurs aux différents coups possibles
faire une fonction qui créer des graphes -> faire une copie de la grille et joueur des coups avec des points
video complete"""

"""mettre 'legal' dans heuristique/graphe"""




"""def creer_grille(M, pion):
    L = []
    for col in range(7):
        lig = legal(col,M)
        if lig >= 0:
            Mp = [lig[:] for lig in M]
            Mp[lig][col] = pion
            L.append(Mp)
    return L"""
            

"""def minmax(noeud, prof, maxj, pion, col):
    if prof == 0: # or noeud est un noeud terminal:
        return None, poids(col, noeud, pion)
    if maxj:
        valeur = - inf
        meilleur_coup = None
        nouvgrille = creer_grille(noeud, pion)
        for col in range(len(nouvgrille)):
            _, valeur_coup = minmax(nouvgrille[col], prof-1, False, -pion, col)
            if valeur_coup > valeur:
                valeur = valeur_coup
                meilleur_coup = nouvgrille[col]
        return meilleur_coup, col, valeur
    else:
        valeur = inf
        meilleur_coup = None
        nouvgrille = creer_grille(noeud, pion)
        for col in range(len(nouvgrille)):
            _, valeur_coup = minmax(nouvgrille[col], prof-1, True, -pion, col)
            if valeur_coup < valeur:
                valeur = valeur_coup
                meilleur_coup = nouvgrille[col]
        return meilleur_coup, col, valeur"""
    
    
#Video
def minimax(noeud, prof, maxj, pion, col_prec):
    liste_pos = pos_possibles(noeud)
    if prof == 0 or est_noeud_term(noeud) :
        if est_noeud_term :
            return "Le jeu est fini"
        else:
            return (col_prec, poids(col_prec, noeud, pion))
    if maxj :
        valeur = -inf
        for col in liste_pos:
            lig = legal(col, noeud)
            noeud_c = noeud.copy()
            noeud_c[lig][col] = pion
            _, nv_valeur = minimax(noeud_c, prof-1, False, -pion, col)
            if nv_valeur > valeur :
                valeur = nv_valeur
                pos = col
        return pos, valeur

    else :
        valeur = inf
        for col in liste_pos:
            lig = legal(col, noeud)
            noeud_c = noeud.copy()
            noeud_c[lig][col] = pion
            _, nv_valeur = minimax(noeud_c, prof-1, True, -pion, col)
            if nv_valeur < valeur:
                valeur = nv_valeur
                pos = col
        return pos, valeur
        
            
def est_noeud_term(M, col):   
    return (test(M, col) or pos_possibles == [])

def pos_possibles(M):
    liste_pos = []
    for col in range(7):
        if legal(col, M) >= 0 :
            liste_pos.append(col)
    return liste_pos



"""def generer_arbre_de_jeu(grille, profondeur, joueur_maximisant=True):
    
    #Génère le graphe des dispositions de grilles possibles jusqu'à une certaine profondeur.
    
    if profondeur == 0 or est_fin_jeu(grille):
        return None, evaluer_grille(grille)

    if joueur_maximisant:
        valeur = float('-inf')
        meilleur_coup = None
        for coup in generer_coups_possibles(grille):
            _, valeur_coup = generer_arbre_de_jeu(coup, profondeur - 1, False)
            if valeur_coup > valeur:
                valeur = valeur_coup
                meilleur_coup = coup
        return meilleur_coup, valeur
    else:
        valeur = float('inf')
        meilleur_coup = None
        for coup in generer_coups_possibles(grille):
            _, valeur_coup = generer_arbre_de_jeu(coup, profondeur - 1, True)
            if valeur_coup < valeur:
                valeur = valeur_coup
                meilleur_coup = coup
        return meilleur_coup, valeur"""
            
            
        
        
        


def poids(col, M, pion):
    v = 0
    lig = legal(col, M)
    if lig >= 0:
        M[lig][col] = pion

    if test(col, M):
        return inf
    if col == 3:
        v += 5
    if col == 2 or col == 4:
        v += 3
    if col == 1 or col == 5:
        v += 1
    if hor3(M, lig, col, pion):
        v += 10
    elif hor2(M, lig, col, pion):
        v += 4
    if ver3(M, lig, col, pion) or ver3(M, lig, col, -pion):
        v += 10
    elif ver2(M, lig, col, pion) or ver2(M, lig, col, -pion):
        v += 4
    if diag3(M, lig, col, pion) or diag3(M, lig, col, -pion):
        v += 12
    elif diag2(M, lig,col, pion) or diag2(M, lig, col, -pion):
        v += 5
    return v


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
        if M[lig][col] == M[lig-1][col] == M[lig-2][col] == pion:
            return True
    return False


def ver2(M, lig, col, pion):
    if lig <= 4:
        if M[lig][col] == M[lig-1][col] == pion:
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


def legal(col, M):
    haut = 0
    for lig in range(6):
        haut += abs(M[lig][col])
    if haut <= 5:
        return (5-haut) #lig
    else:
        return (-1)   #coup impossible


def test(col, M):
    haut = 0
    for li in range(6):
        haut += abs(M[li][col])
    lig = 6 - haut
    if test_ver(M, col, lig) or test_hor(M, lig) or test_diagmont(M) or test_diagdesc(M):
        return True


def test_ver(M, lig, col):
    if lig <= 2:
        return (M[lig][col] == M[lig+1][col] == M[lig+2][col] == M[lig+3][col])
    return False


def test_hor(M, lig):
    for col in range(4):
        if M[lig][col] == M[lig][col+1] == M[lig][col+2] == M[lig][col+3] != 0:
            return True
    return False


def test_diagmont(M):
    for lig in range(3, 6):
        for col in range(4):
            if M[lig][col] == M[lig-1][col+1] == M[lig-2][col+2] == M[lig-3][col+3] != 0:
                return True
    return False


def test_diagdesc(M):
    for lig in range(3):
        for col in range(4):
            if M[lig][col] == M[lig+1][col+1] == M[lig+2][col+2] == M[lig+3][col+3] != 0:
                return True
    return False
