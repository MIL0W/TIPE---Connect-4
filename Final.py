import random
from math import inf, log
import copy
import timeit
import matplotlib.pyplot as plt


def graph(M):
    Mgr = [[0 for j in range(7)] for i in range(6)]
    for lig in range(len(M)):
        for col in range(len(M[lig])):
            if M[lig][col] == 0:
                Mgr[lig][col] = "_"
            if M[lig][col] == 1:
                Mgr[lig][col] = "O"
            if M[lig][col] == -1:
                Mgr[lig][col] = "X"
    return Mgr


def aff(M):
    for lig in M:
        print(lig)
    print("\n  0    1    2    3    4    5    6\n")


# -- Placer un pion dans une colonne de la grile --#


def poser(col, M, pion):
    haut = 0
    for lig in range(6):
        haut += abs(M[lig][col])
    M[5 - haut][col] = pion


# -- Création d'une grille --#


def creer():
    M = [[0 for lig in range(7)] for col in range(6)]
    print(M)
    for tour in range(21):

        coup1 = joueur(M, 0, 1)
        poser(coup1, M, 1)
        print(M)
        if test(M, coup1):
            print("LE JOUEUR 1 EST VAINQUEUR")
            return 1
            break

        coup2 = joueur(M, 0, -1)
        poser(coup2, M, -1)
        print(M)
        if test(M, coup2):
            print("LE JOUEUR 2 EST VAINQUEUR")
            return -1
            break
    return 0


# -- Jeu entre deux vrais joueurs --#


def jeu(prof):
    M = [[0 for lig in range(7)] for col in range(6)]
    Mgr = graph(M)
    aff(Mgr)
    for tour in range(21):

        coup1 = joueur(M, prof, 1)
        poser(coup1, M, 1)
        Mgr = graph(M)
        aff(Mgr)
        if test(M, coup1):
            print("LE JOUEUR 1 EST VAINQUEUR")
            return 1
            break

        coup2 = joueur(M, prof, -1)
        poser(coup2, M, -1)
        Mgr = graph(M)
        aff(Mgr)
        if test(M, coup2):
            print("LE JOUEUR 2 EST VAINQUEUR")
            return -1
            break
    return 0


# -- Jeu avec algorithmes --#


def j(prof):
    M = [[0 for lig in range(7)] for col in range(6)]
    Mgr = graph(M)
    aff(Mgr)
    for tour in range(21):

        coup1 = joueur(M, prof, 1)
        poser(coup1, M, 1)
        Mgr = graph(M)
        aff(Mgr)
        if test(M, coup1):
            print("LE JOUEUR 1 EST VAINQUEUR")
            return 1
            break

        coup2 = algo_alphabeta_t(M, prof, -1)
        poser(coup2, M, -1)
        Mgr = graph(M)
        aff(Mgr)
        if test(M, coup2):
            print("LE JOUEUR 2 EST VAINQUEUR")
            return -1
            break
    return 0


# -- Fonctions des joueurs --#


def joueur(M, prof, pion):
    coups_possibles = pos_possibles(M)
    p = 2
    if pion == 1:
        p = 1
    coupj = int(
        input("\nJoueur " + str(p) + ",\nDans quelle colonne placer le pion ? : \n")
    )
    while not (coupj in coups_possibles):
        Mgr = graph(M)
        aff(Mgr)
        print("ERREUR, LA COLONNE EST REMPLIE")
        coupj = int(input("\nJoueur 1,\nDans quelle colonne placer le pion ? : \n"))
    return coupj


def aleatoire(M, prof, pion):
    coups_possibles = pos_possibles(M)
    pos = random.randint(0, len(coups_possibles) - 1)
    coupj = coups_possibles[pos]
    return coupj


def algo_minimax(M, prof, pion):
    coupj, _ = minimax(M, prof, True, pion)
    return coupj


def algo_alphabeta(M, prof, pion):
    coupj, _ = alphabeta(M, prof, -inf, +inf, True, pion)
    return coupj


def algo_alphabeta_r(M, prof, pion):
    coupj, _ = alphabeta_r(M, prof, -inf, +inf, True, pion)
    return coupj


def algo_alphabeta_t(M, prof, pion):
    coupj, _ = alphabeta_t(M, prof, -inf, +inf, True, pion)
    return coupj


# -- Test de fin de récurrence --#


def est_fini(M):
    return heuristique(M, 1) == inf or heuristique(M, -1) == inf


def est_noeud_term(M):
    return est_fini(M) or pos_possibles(M) == []


# -- Liste des positions possibles --#


def pos_possibles(M):
    liste_pos = []
    for col in range(7):
        if legal(col, M) >= 0:
            liste_pos.append(col)
    return liste_pos


def legal(col, M):
    haut = 0
    for lig in range(6):
        haut += abs(M[lig][col])
    if haut <= 5:
        return 5 - haut  # lig
    else:
        return -1  # coup impossible


# -- Test si la grille est gagnante pour un coup --#


def test(M, col):
    if col == -1:
        return False
    else:
        haut = 0
        for li in range(6):
            haut += abs(M[li][col])
        lig = 6 - haut
        if (
            test_ver(M, lig, col)
            or test_hor(M, lig)
            or test_diagmont(M)
            or test_diagdesc(M)
        ):
            return True
        return False


def test_ver(M, lig, col):
    if lig <= 2:
        return M[lig][col] == M[lig + 1][col] == M[lig + 2][col] == M[lig + 3][col] != 0
    return False


def test_hor(M, lig):
    for col in range(4):
        if M[lig][col] == M[lig][col + 1] == M[lig][col + 2] == M[lig][col + 3] != 0:
            return True
    return False


def test_diagmont(M):
    for lig in range(3, 6):
        for col in range(4):
            if (
                M[lig][col]
                == M[lig - 1][col + 1]
                == M[lig - 2][col + 2]
                == M[lig - 3][col + 3]
                != 0
            ):
                return True
    return False


def test_diagdesc(M):
    for lig in range(3):
        for col in range(4):
            if (
                M[lig][col]
                == M[lig + 1][col + 1]
                == M[lig + 2][col + 2]
                == M[lig + 3][col + 3]
                != 0
            ):
                return True
    return False


# -- Algorithme minimax --#


def minimax(noeud, prof, maxj, pion):
    liste_pos = pos_possibles(noeud)

    if prof == 0 or est_noeud_term(noeud):
        if est_noeud_term(noeud):
            if heuristique(noeud, pion) == inf:
                return (None, inf)
            elif heuristique(noeud, -pion) == inf:
                return (None, -inf)
            else:
                return (None, 0)
        else:
            return (None, heuristique(noeud, pion))

    if maxj:
        valeur = -inf
        pos = liste_pos[random.randint(0, len(liste_pos) - 1)]
        for col in liste_pos:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, pion)
            _, nv_valeur = minimax(noeud_c, prof - 1, False, pion)
            if nv_valeur > valeur:
                valeur = nv_valeur
                pos = col
        return (pos, valeur)

    else:
        valeur = inf
        pos = liste_pos[random.randint(0, len(liste_pos) - 1)]
        for col in liste_pos:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, -pion)
            _, nv_valeur = minimax(noeud_c, prof - 1, True, pion)
            if nv_valeur < valeur:
                valeur = nv_valeur
                pos = col
        return (pos, valeur)


# -- Avec l'élagage alpha-beta --#


def alphabeta(noeud, prof, alpha, beta, maxj, pion):
    liste_pos = pos_possibles(noeud)

    if prof == 0 or est_noeud_term(noeud):
        if est_noeud_term(noeud):
            if heuristique(noeud, pion) == inf:
                return (None, inf)
            elif heuristique(noeud, -pion) == inf:
                return (None, -inf)
            else:
                return (None, 0)
        else:
            return (None, heuristique(noeud, pion))

    if maxj:
        valeur = -inf
        pos = liste_pos[random.randint(0, len(liste_pos) - 1)]
        for col in liste_pos:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, pion)
            _, nv_valeur = alphabeta(noeud_c, prof - 1, alpha, beta, False, pion)
            if nv_valeur > valeur:
                valeur = nv_valeur
                pos = col
            alpha = max(alpha, valeur)
            if alpha >= beta:
                break
        return (pos, valeur)

    else:
        valeur = inf
        pos = liste_pos[random.randint(0, len(liste_pos) - 1)]
        for col in liste_pos:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, -pion)
            _, nv_valeur = alphabeta(noeud_c, prof - 1, alpha, beta, True, pion)
            if nv_valeur < valeur:
                valeur = nv_valeur
                pos = col
            beta = min(beta, valeur)
            if alpha >= beta:
                break
        return (pos, valeur)


# -- En choisissant aléatoirement l'ordre des noeuds --#


def alphabeta_r(noeud, prof, alpha, beta, maxj, pion):
    liste_pos = pos_possibles(noeud)

    if prof == 0 or est_noeud_term(noeud):
        if est_noeud_term(noeud):
            if heuristique(noeud, pion) == inf:
                return (None, inf)
            elif heuristique(noeud, -pion) == inf:
                return (None, -inf)
            else:
                return (None, 0)
        else:
            return (None, heuristique(noeud, pion))

    if maxj:
        valeur = -inf
        pos = liste_pos[random.randint(0, len(liste_pos) - 1)]
        random.shuffle(liste_pos)
        for col in liste_pos:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, pion)
            _, nv_valeur = alphabeta_r(noeud_c, prof - 1, alpha, beta, False, pion)
            if nv_valeur > valeur:
                valeur = nv_valeur
                pos = col
            alpha = max(alpha, valeur)
            if alpha >= beta:
                break
        return (pos, valeur)

    else:
        valeur = inf
        pos = liste_pos[random.randint(0, len(liste_pos) - 1)]
        random.shuffle(liste_pos)
        for col in liste_pos:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, -pion)
            _, nv_valeur = alphabeta_r(noeud_c, prof - 1, alpha, beta, True, pion)
            if nv_valeur < valeur:
                valeur = nv_valeur
                pos = col
            beta = min(beta, valeur)
            if alpha >= beta:
                break
        return (pos, valeur)


# -- En choisissant l'ordre des noeuds en commançant par les colonnes centrales --#


def alphabeta_t(noeud, prof, alpha, beta, maxj, pion):
    liste_pos = pos_possibles(noeud)

    if prof == 0 or est_noeud_term(noeud):
        if est_noeud_term(noeud):
            if heuristique(noeud, pion) == inf:
                return (None, inf)
            elif heuristique(noeud, -pion) == inf:
                return (None, -inf)
            else:
                return (None, 0)
        else:
            return (None, heuristique(noeud, pion))

    if maxj:
        valeur = -inf
        pos = liste_pos[random.randint(0, len(liste_pos) - 1)]
        liste_pos_t = choix(liste_pos)
        for col in liste_pos_t:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, pion)
            _, nv_valeur = alphabeta_r(noeud_c, prof - 1, alpha, beta, False, pion)
            if nv_valeur > valeur:
                valeur = nv_valeur
                pos = col
            alpha = max(alpha, valeur)
            if alpha >= beta:
                break
        return (pos, valeur)

    else:
        valeur = inf
        pos = liste_pos[random.randint(0, len(liste_pos) - 1)]
        liste_pos_t = choix(liste_pos)
        for col in liste_pos_t:
            noeud_c = copy.deepcopy(noeud)
            poser(col, noeud_c, -pion)
            _, nv_valeur = alphabeta_r(noeud_c, prof - 1, alpha, beta, True, pion)
            if nv_valeur < valeur:
                valeur = nv_valeur
                pos = col
            beta = min(beta, valeur)
            if alpha >= beta:
                break
        return (pos, valeur)


def choix(L):
    ordre = [3, 2, 4, 1, 5, 0, 6]
    T = [c for c in ordre if c in L]
    return T


# -- Score d'un joeuur pour une grille --#


def heuristique(M, pion):
    score = 0

    for lig in range(6):  # pions au milieu de la grille
        if M[lig][3] == pion:
            score += 18
        if M[lig][2] == pion:
            score += 2
        if M[lig][4] == pion:
            score += 2
        if M[lig][1] == pion:
            score += 1
        if M[lig][5] == pion:
            score += 1

    for lig in range(6):  # horizontalement
        for col in range(4):
            L_pions = [M[lig][col + i] for i in range(4)]
            score += score_case(L_pions, pion)

    for lig in range(3):  # verticalement
        for col in range(7):
            L_pions = [M[lig + i][col] for i in range(4)]
            score += score_case(L_pions, pion)

    for lig in range(3):  # diagonalement desc
        for col in range(4):
            L_pions = [M[lig + i][col + i] for i in range(4)]
            score += score_case(L_pions, pion)

    for lig in range(3):  # diagonalement mont
        for col in range(4):
            L_pions = [M[lig + 3 - i][col + i] for i in range(4)]
            score += score_case(L_pions, pion)

    return score


# -- Compte le score d'un joeur pour une portion de grille --#


def score_case(L_pions, pion):
    score = 0

    if L_pions.count(pion) == 4:
        return inf
    if L_pions.count(-pion) == 4:
        return -inf

    if L_pions.count(pion) == 3 and L_pions.count(0) == 1:
        score += 30
    elif L_pions.count(pion) == 2 and L_pions.count(0) == 2:
        score += 12

    elif L_pions.count(-pion) == 3 and L_pions.count(0) == 1:
        score -= 24
    elif L_pions.count(-pion) == 2 and L_pions.count(0) == 2:
        score -= 10

    elif L_pions.count(pion) == 3 and L_pions.count(-pion) == 1:
        score += 4
    elif L_pions.count(-pion) == 3 and L_pions.count(pion) == 1:
        score -= 2

    return score


# -- Compte des résultats --#


def compte(fct1, fct2, N, prof):
    j1, j2, nul = 0, 0, 0
    for i in range(N):
        res = partie(fct1, fct2, prof)
        if res == 1:
            j1 += 1
        if res == -1:
            j2 += 1
        if res == 0:
            nul += 1
    return (j1, j2, nul)


def partie(fct1, fct2, prof):
    M = [[0 for lig in range(7)] for col in range(6)]
    L = [0, 1, 2, 3, 4, 5, 6]
    n = len(L) - 1
    for t in range(21):

        if fct1 == aleatoire:
            pos = random.randint(0, n)
            coup1 = L[pos]
            M1 = placer(coup1, M, 1)
            if not (M1):
                L.pop(pos)
                n -= 1
                pos = random.randint(0, n)
                coup1 = L[pos]
                M1 = placer(coup1, M, 1)
        else:
            coup1 = fct1(M, prof, 1)
            poser(coup1, M, 1)
        if test(M, coup1):
            return 1

        if fct2 == aleatoire:
            pos = random.randint(0, n)
            coup2 = L[pos]
            M2 = placer(coup2, M, -1)
            if not (M2):
                L.pop(pos)
                n -= 1
                pos = random.randint(0, n)
                coup2 = L[pos]
                M2 = placer(coup2, M, -1)
        else:
            coup2 = fct2(M, prof, -1)
            poser(coup2, M, -1)
        if test(M, coup2):
            return -1

    return 0


def placer(col, M, pion):
    haut = 0
    for i in range(6):
        haut += abs(M[i][col])
    if haut <= 5:
        M[5 - haut][col] = pion
        return True
    return False


"""
execution_time = timeit.timeit('compte(aleatoire, aleatoire, 10000, 3)', globals=globals(), number=1)
print(f"Le temps d'exécution est : {execution_time} secondes")
"""


def comparaison(N):
    mini = []
    albe = []
    alber = []
    albet = []
    prof = []
    for i in range(1, N + 1):
        mini.append(
            timeit.timeit(
                lambda: compte(algo_minimax, aleatoire, 1, i),
                globals=globals(),
                number=1,
            )
        )
        albe.append(
            timeit.timeit(
                lambda: compte(algo_alphabeta, aleatoire, 1, i),
                globals=globals(),
                number=1,
            )
        )
        alber.append(
            timeit.timeit(
                lambda: compte(algo_alphabeta_r, aleatoire, 1, i),
                globals=globals(),
                number=1,
            )
        )
        albet.append(
            timeit.timeit(
                lambda: compte(algo_alphabeta_t, aleatoire, 1, i),
                globals=globals(),
                number=1,
            )
        )
        prof.append(i)
    return (albe, alber, albet, prof)


"""mini, albe, alber, albet, prof = comparaison(7)"""

"""mini prof = ([0.012873500003479421,
  0.12876110000070184,
  0.8332669000374153,
  5.493653699988499,
  53.576833999948576,
  156.80710590002127,
  1114.435542399995],
 [1, 2, 3, 4, 5, 6, 7])"""

albe, alber, albet, prof = (
    [
        0.01257470017299056,
        0.05968530010432005,
        0.4132680001202971,
        1.1638197000138462,
        6.772554200142622,
        14.374894100008532,
        61.99796380009502,
        258.7563416000921,
        754.2332723001018,
    ],
    [
        0.009079999988898635,
        0.07573630008846521,
        0.2827386998105794,
        0.7134771998971701,
        2.2866003999952227,
        9.436307600000873,
        44.63105609989725,
        97.62404730007984,
        654.22109919996,
    ],
    [
        0.015954599948599935,
        0.040820199996232986,
        0.21575850015506148,
        0.4163550999946892,
        2.19830820010975,
        5.263464800082147,
        33.50402750005014,
        62.22340909997001,
        250.00832720007747,
    ],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
)


def lo(L):
    T = []
    for i in L:
        T.append(log(i))
    return T


lalbe, lalber, lalbet = lo(albe), lo(alber), lo(albet)
"""
plt.scatter([1,2,3,4,5,6,7],mini, label = 'Minimax')

plt.scatter(prof,albe, label = 'Alpha-beta')
plt.scatter(prof,alber, label = 'Alpha-beta et parcours aléatoire')
plt.scatter(prof,albet, label = 'Alpha-beta et parcours optimisé')
plt.title("Comparaison du temps d'exécution des algorithmes pour une partie")
plt.xlabel('profondeur')
plt.ylabel('temps en secondes')
plt.legend()
plt.show()"""
