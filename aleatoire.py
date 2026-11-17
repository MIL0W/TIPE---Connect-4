import random
import timeit


def jeu_aleat():
    M = [[0 for i in range(7)]for j in range(6)]
    for t in range(21):
        M1 = False
        while M1 == False:
            coupj1 = random.randint(0,6)
            M1 = placer(coupj1, M, 1)
        if test(coupj1, M):
            return (1)
        
        M2 = False
        while M2 == False:
            coupj2 = random.randint(0,6)
            M2 = placer(coupj2, M, -1)
        if test(coupj2, M):
            return (-1)
    return(0)


def placer(col, M, pion):
    haut = 0
    for i in range(6):
        haut += abs(M[i][col])
    if haut <= 5:
        M[5-haut][col] = pion
        return True
    return False


def test(j,M):
    haut = 0
    for i in range(6):
        haut += abs(M[i][j])
    i = 6 - haut
    if test_ver(M,i,j) or test_hor(M,i) or test_diagmont(M) or test_diagdesc(M):
        return True


def test_ver(M,i,j):
    if i > 2 :
        return False
    return (M[i][j] == M[i+1][j] == M[i+2][j] == M[i+3][j])
    
def test_hor(M,i):
    for k in range(4):
        if M[i][k] == M[i][k+1] == M[i][k+2] == M[i][k+3] != 0:
            return True
    return False
    
def test_diagmont(M):
    for i in range(3, 6):
        for j in range(4):
            if M[i][j] == M[i-1][j+1] == M[i-2][j+2] == M[i-3][j+3] != 0 :
                return True
    return False

def test_diagdesc(M):
    for i in range(3):
        for j in range(4):
            if M[i][j] == M[i+1][j+1] == M[i+2][j+2] == M[i+3][j+3] != 0 :
                return True
    return False



def aleat(N):
    j1, j2, nul = 0, 0, 0
    for i in range(N):
        res = jeu_aleat()
        if res == 1:
            j1 += 1
        if res == -1:
            j2 += 1
        if res == 0:
            nul += 1         
    return(j1, j2, nul)
