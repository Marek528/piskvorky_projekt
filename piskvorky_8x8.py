import pygame, sys
import numpy as np

pygame.init()

SIRKA = 1000
VYSKA = SIRKA
SIRKA_CIARY = 15
SIRKA_VYHERNEJ_CIARY = 20

RIADKY_PLOCHY = 8
STLPCE_PLOCHY = 8

VELKOST_POLICOK = SIRKA // STLPCE_PLOCHY

POLOMER_KRUHU = VELKOST_POLICOK // 3
SIRKA_KRUHU = 20

SIRKA_KRIZIKA = 25
MEDZERA = VELKOST_POLICOK // 4
#farby
FARBA_OBRAZOVKY = (255,255,255)
FARBA_CIARY = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
DARK_BLUE = (0,0,128)

obrazovka = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption('Piskovrky')
obrazovka.fill(FARBA_OBRAZOVKY)

konzolova_plocha = np.zeros((RIADKY_PLOCHY, STLPCE_PLOCHY))

font = pygame.font.Font('freesansbold.ttf', MEDZERA + 50)

def nakresli_ciary():
    #horizontalne ciary
    pygame.draw.line(obrazovka, FARBA_CIARY, (0, VELKOST_POLICOK), (SIRKA, VELKOST_POLICOK), SIRKA_CIARY)
    for i in range(2,RIADKY_PLOCHY):
        pygame.draw.line(obrazovka, FARBA_CIARY, (0, VELKOST_POLICOK * i), (SIRKA, VELKOST_POLICOK * i), SIRKA_CIARY)

    #vertikalne ciary
    pygame.draw.line(obrazovka, FARBA_CIARY, (VELKOST_POLICOK, 0), (VELKOST_POLICOK, VYSKA), SIRKA_CIARY)
    for i in range(2,STLPCE_PLOCHY):
        pygame.draw.line(obrazovka, FARBA_CIARY, (VELKOST_POLICOK * i, 0), (VELKOST_POLICOK * i, VYSKA), SIRKA_CIARY)

def nakresli_objekty():
    for riadok in range(RIADKY_PLOCHY):
        for stlpec in range(STLPCE_PLOCHY):
            if konzolova_plocha[riadok][stlpec] == 1:
                pygame.draw.circle(obrazovka, RED, (int(stlpec * VELKOST_POLICOK + VELKOST_POLICOK // 2), int(riadok * VELKOST_POLICOK + VELKOST_POLICOK // 2)), POLOMER_KRUHU, SIRKA_KRUHU)
            elif konzolova_plocha[riadok][stlpec] == 2:
                pygame.draw.line(obrazovka, BLUE, (stlpec * VELKOST_POLICOK + MEDZERA, riadok * VELKOST_POLICOK + VELKOST_POLICOK - MEDZERA), (stlpec * VELKOST_POLICOK + VELKOST_POLICOK - MEDZERA, riadok * VELKOST_POLICOK + MEDZERA), SIRKA_KRIZIKA)
                pygame.draw.line(obrazovka, BLUE, (stlpec * VELKOST_POLICOK + MEDZERA, riadok * VELKOST_POLICOK + MEDZERA), (stlpec * VELKOST_POLICOK + VELKOST_POLICOK - MEDZERA, riadok * VELKOST_POLICOK + VELKOST_POLICOK - MEDZERA), SIRKA_KRIZIKA)

def oznac_stovrec(riadok, stlpec, hrac):
    konzolova_plocha[riadok][stlpec] = hrac

def volny_stvorec(riadok, stlpec):
    if konzolova_plocha[riadok][stlpec] == 0:
        return True
    else:
        return False

def kontrola_plochy():
    for riadok in range(RIADKY_PLOCHY):
        for stlpec in range(STLPCE_PLOCHY):
            if konzolova_plocha[riadok][stlpec] == 0:
                return False
    
    return True

def kontrola_vyhry(hrac):
    #kontrola vyhry
    #vertikalne
    for stlpec in range(STLPCE_PLOCHY):
        if konzolova_plocha[0][stlpec] == hrac and konzolova_plocha[1][stlpec] == hrac and konzolova_plocha[2][stlpec] == hrac and konzolova_plocha[3][stlpec] == hrac:
            nakresli_vertikalnu_ciaru_0(stlpec, hrac)
            return True
        elif konzolova_plocha[1][stlpec] == hrac and konzolova_plocha[2][stlpec] == hrac and konzolova_plocha[3][stlpec] == hrac and konzolova_plocha[4][stlpec] == hrac:
            nakresli_vertikalnu_ciaru_1(stlpec, hrac)
            return True
        elif konzolova_plocha[2][stlpec] == hrac and konzolova_plocha[3][stlpec] == hrac and konzolova_plocha[4][stlpec] == hrac and konzolova_plocha[5][stlpec] == hrac:
            nakresli_vertikalnu_ciaru_2(stlpec, hrac)
            return True
        elif konzolova_plocha[3][stlpec] == hrac and konzolova_plocha[4][stlpec] == hrac and konzolova_plocha[5][stlpec] == hrac and konzolova_plocha[6][stlpec] == hrac:
            nakresli_vertikalnu_ciaru_3(stlpec, hrac)
            return True
        elif konzolova_plocha[4][stlpec] == hrac and konzolova_plocha[5][stlpec] == hrac and konzolova_plocha[6][stlpec] == hrac and konzolova_plocha[7][stlpec] == hrac:
            nakresli_vertikalnu_ciaru_4(stlpec, hrac)
            return True

    #horizontalne
    for riadok in range(RIADKY_PLOCHY):
        if konzolova_plocha[riadok][0] == hrac and konzolova_plocha[riadok][1] == hrac and konzolova_plocha[riadok][2] == hrac and konzolova_plocha[riadok][3] == hrac:
            nakresli_horizontalnu_ciaru_0(riadok, hrac)
            return True
        elif konzolova_plocha[riadok][1] == hrac and konzolova_plocha[riadok][2] == hrac and konzolova_plocha[riadok][3] == hrac and konzolova_plocha[riadok][4] == hrac:
            nakresli_horizontalnu_ciaru_1(riadok, hrac)
            return True
        elif konzolova_plocha[riadok][2] == hrac and konzolova_plocha[riadok][3] == hrac and konzolova_plocha[riadok][4] == hrac and konzolova_plocha[riadok][5] == hrac:
            nakresli_horizontalnu_ciaru_2(riadok, hrac)
            return True
        elif konzolova_plocha[riadok][3] == hrac and konzolova_plocha[riadok][4] == hrac and konzolova_plocha[riadok][5] == hrac and konzolova_plocha[riadok][6] == hrac:
            nakresli_horizontalnu_ciaru_3(riadok, hrac)
            return True
        elif konzolova_plocha[riadok][4] == hrac and konzolova_plocha[riadok][5] == hrac and konzolova_plocha[riadok][6] == hrac and konzolova_plocha[riadok][7] == hrac:
            nakresli_horizontalnu_ciaru_4(riadok, hrac)
            return True

    #diagonalne zlava \
    # main
    for i in range(5):
        if konzolova_plocha[i][i] == hrac and konzolova_plocha[i + 1][i + 1] == hrac and konzolova_plocha[i + 2][i + 2] == hrac and konzolova_plocha[i + 3][i + 3] == hrac:
            if i == 0:
                nakresli_diagonalnu_ciaru_zlava_0(hrac)
                return True
            elif i == 1:
                nakresli_diagonalnu_ciaru_zlava_1(hrac)
                return True
            elif i == 2:
                nakresli_diagonalnu_ciaru_zlava_2(hrac)
                return True
            elif i == 3:
                nakresli_diagonalnu_ciaru_zlava_3(hrac)
                return True
            elif i == 4:
                nakresli_diagonalnu_ciaru_zlava_4(hrac)
                return True

    # lava cast \ --- 1
    if konzolova_plocha[1][0] == hrac and konzolova_plocha[2][1] == hrac and konzolova_plocha[3][2] == hrac and konzolova_plocha[4][3] == hrac:
        nakresli_diagonalnu_ciaru_zlava_5_1(hrac)
        return True
    if konzolova_plocha[2][1] == hrac and konzolova_plocha[3][2] == hrac and konzolova_plocha[4][3] == hrac and konzolova_plocha[5][4] == hrac:
        nakresli_diagonalnu_ciaru_zlava_5_2(hrac)
        return True
    if konzolova_plocha[3][2] == hrac and konzolova_plocha[4][3] == hrac and konzolova_plocha[5][4] == hrac and konzolova_plocha[6][5] == hrac:
        nakresli_diagonalnu_ciaru_zlava_5_3(hrac)
        return True
    if konzolova_plocha[4][3] == hrac and konzolova_plocha[5][4] == hrac and konzolova_plocha[6][5] == hrac and konzolova_plocha[7][6] == hrac:
        nakresli_diagonalnu_ciaru_zlava_5_4(hrac)
        return True

    # lava cast \ --- 2
    if konzolova_plocha[2][0] == hrac and konzolova_plocha[3][1] == hrac and konzolova_plocha[4][2] == hrac and konzolova_plocha[5][3] == hrac:
        nakresli_diagonalnu_ciaru_zlava_6_1(hrac)
        return True
    if konzolova_plocha[3][1] == hrac and konzolova_plocha[4][2] == hrac and konzolova_plocha[5][3] == hrac and konzolova_plocha[6][4] == hrac:
        nakresli_diagonalnu_ciaru_zlava_6_2(hrac)
        return True
    if konzolova_plocha[4][2] == hrac and konzolova_plocha[5][3] == hrac and konzolova_plocha[6][4] == hrac and konzolova_plocha[7][5] == hrac:
        nakresli_diagonalnu_ciaru_zlava_6_3(hrac)
        return True

    # lava cast \ --- 3
    if konzolova_plocha[3][0] == hrac and konzolova_plocha[4][1] == hrac and konzolova_plocha[5][2] == hrac and konzolova_plocha[6][3] == hrac:
        nakresli_diagonalnu_ciaru_zlava_7_1(hrac)
        return True
    if konzolova_plocha[4][1] == hrac and konzolova_plocha[5][2] == hrac and konzolova_plocha[6][3] == hrac and konzolova_plocha[7][4] == hrac:
        nakresli_diagonalnu_ciaru_zlava_7_2(hrac)
        return True
    
    # lava cast \ --- 4
    if konzolova_plocha[4][0] == hrac and konzolova_plocha[5][1] == hrac and konzolova_plocha[6][2] == hrac and konzolova_plocha[7][3] == hrac:
        nakresli_diagonalnu_ciaru_zlava_8_1(hrac)
        return True
    
    # prava cast \ --- 5
    if konzolova_plocha[0][1] == hrac and konzolova_plocha[1][2] == hrac and konzolova_plocha[2][3] == hrac and konzolova_plocha[3][4] == hrac:
        nakresli_diagonalnu_ciaru_zlava_9_1(hrac)
        return True
    if konzolova_plocha[1][2] == hrac and konzolova_plocha[2][3] == hrac and konzolova_plocha[3][4] == hrac and konzolova_plocha[4][5] == hrac:
        nakresli_diagonalnu_ciaru_zlava_9_2(hrac)
        return True
    if konzolova_plocha[2][3] == hrac and konzolova_plocha[3][4] == hrac and konzolova_plocha[4][5] == hrac and konzolova_plocha[5][6] == hrac:
        nakresli_diagonalnu_ciaru_zlava_9_3(hrac)
        return True
    if konzolova_plocha[3][4] == hrac and konzolova_plocha[4][5] == hrac and konzolova_plocha[5][6] == hrac and konzolova_plocha[6][7] == hrac:
        nakresli_diagonalnu_ciaru_zlava_9_4(hrac)
        return True

    # prava cast \ --- 6
    if konzolova_plocha[0][2] == hrac and konzolova_plocha[1][3] == hrac and konzolova_plocha[2][4] == hrac and konzolova_plocha[3][5] == hrac:
        nakresli_diagonalnu_ciaru_zlava_10_1(hrac)
        return True
    if konzolova_plocha[1][3] == hrac and konzolova_plocha[2][4] == hrac and konzolova_plocha[3][5] == hrac and konzolova_plocha[4][6] == hrac:
        nakresli_diagonalnu_ciaru_zlava_10_2(hrac)
        return True
    if konzolova_plocha[2][4] == hrac and konzolova_plocha[3][5] == hrac and konzolova_plocha[4][6] == hrac and konzolova_plocha[5][7] == hrac:
        nakresli_diagonalnu_ciaru_zlava_10_3(hrac)
        return True

    # prava cast \ --- 7
    if konzolova_plocha[0][3] == hrac and konzolova_plocha[1][4] == hrac and konzolova_plocha[2][5] == hrac and konzolova_plocha[3][6] == hrac:
        nakresli_diagonalnu_ciaru_zlava_11_1(hrac)
        return True
    if konzolova_plocha[1][4] == hrac and konzolova_plocha[2][5] == hrac and konzolova_plocha[3][6] == hrac and konzolova_plocha[4][7] == hrac:
        nakresli_diagonalnu_ciaru_zlava_11_2(hrac)
        return True

    # prava cast \ --- 8
    if konzolova_plocha[0][4] == hrac and konzolova_plocha[1][5] == hrac and konzolova_plocha[2][6] == hrac and konzolova_plocha[3][7] == hrac:
        nakresli_diagonalnu_ciaru_zlava_12_1(hrac)
        return True

    #diagonalne zprava /
    # main
    if konzolova_plocha[0][7] == hrac and konzolova_plocha[1][6] == hrac and konzolova_plocha[2][5] == hrac and konzolova_plocha[3][4] == hrac:
        nakresli_diagonalnu_ciaru_zprava_0(hrac)
        return True
    if konzolova_plocha[1][6] == hrac and konzolova_plocha[2][5] == hrac and konzolova_plocha[3][4] == hrac and konzolova_plocha[4][3] == hrac:
        nakresli_diagonalnu_ciaru_zprava_1(hrac)
        return True
    if konzolova_plocha[2][5] == hrac and konzolova_plocha[3][4] == hrac and konzolova_plocha[4][3] == hrac and konzolova_plocha[5][2] == hrac:
        nakresli_diagonalnu_ciaru_zprava_2(hrac)
        return True
    if konzolova_plocha[3][4] == hrac and konzolova_plocha[4][3] == hrac and konzolova_plocha[5][2] == hrac and konzolova_plocha[6][1] == hrac:
        nakresli_diagonalnu_ciaru_zprava_3(hrac)
        return True
    if konzolova_plocha[4][3] == hrac and konzolova_plocha[5][2] == hrac and konzolova_plocha[6][1] == hrac and konzolova_plocha[7][0] == hrac:
        nakresli_diagonalnu_ciaru_zprava_4(hrac)
        return True

    # lava cast / --- 1
    if konzolova_plocha[0][6] == hrac and konzolova_plocha[1][5] == hrac and konzolova_plocha[2][4] == hrac and konzolova_plocha[3][3] == hrac:
        nakresli_diagonalnu_ciaru_zprava_5_1(hrac)
        return True
    if konzolova_plocha[1][5] == hrac and konzolova_plocha[2][4] == hrac and konzolova_plocha[3][3] == hrac and konzolova_plocha[4][2] == hrac:
        nakresli_diagonalnu_ciaru_zprava_5_2(hrac)
        return True
    if konzolova_plocha[2][4] == hrac and konzolova_plocha[3][3] == hrac and konzolova_plocha[4][2] == hrac and konzolova_plocha[5][1] == hrac:
        nakresli_diagonalnu_ciaru_zprava_5_3(hrac)
        return True
    if konzolova_plocha[3][3] == hrac and konzolova_plocha[4][2] == hrac and konzolova_plocha[5][1] == hrac and konzolova_plocha[6][0] == hrac:
        nakresli_diagonalnu_ciaru_zprava_5_4(hrac)
        return True
    
    # lava cast / --- 2
    if konzolova_plocha[0][5] == hrac and konzolova_plocha[1][4] == hrac and konzolova_plocha[2][3] == hrac and konzolova_plocha[3][2] == hrac:
        nakresli_diagonalnu_ciaru_zprava_6_1(hrac)
        return True
    if konzolova_plocha[1][4] == hrac and konzolova_plocha[2][3] == hrac and konzolova_plocha[3][2] == hrac and konzolova_plocha[4][1] == hrac:
        nakresli_diagonalnu_ciaru_zprava_6_2(hrac)
        return True
    if konzolova_plocha[2][3] == hrac and konzolova_plocha[3][2] == hrac and konzolova_plocha[4][1] == hrac and konzolova_plocha[5][0] == hrac:
        nakresli_diagonalnu_ciaru_zprava_6_3(hrac)
        return True

    # lava cast / --- 3
    if konzolova_plocha[0][4] == hrac and konzolova_plocha[1][3] == hrac and konzolova_plocha[2][2] == hrac and konzolova_plocha[3][1] == hrac:
        nakresli_diagonalnu_ciaru_zprava_7_1(hrac)
        return True
    if konzolova_plocha[1][3] == hrac and konzolova_plocha[2][2] == hrac and konzolova_plocha[3][1] == hrac and konzolova_plocha[4][0] == hrac:
        nakresli_diagonalnu_ciaru_zprava_7_2(hrac)
        return True

    # lava cast / --- 4
    if konzolova_plocha[0][3] == hrac and konzolova_plocha[1][2] == hrac and konzolova_plocha[2][1] == hrac and konzolova_plocha[3][0] == hrac:
        nakresli_diagonalnu_ciaru_zprava_8_1(hrac)
        return True

    # prava cast / --- 5
    if konzolova_plocha[1][7] == hrac and konzolova_plocha[2][6] == hrac and konzolova_plocha[3][5] == hrac and konzolova_plocha[4][4] == hrac:
        nakresli_diagonalnu_ciaru_zprava_9_1(hrac)
        return True
    if konzolova_plocha[2][6] == hrac and konzolova_plocha[3][5] == hrac and konzolova_plocha[4][4] == hrac and konzolova_plocha[5][3] == hrac:
        nakresli_diagonalnu_ciaru_zprava_9_2(hrac)
        return True
    if konzolova_plocha[3][5] == hrac and konzolova_plocha[4][4] == hrac and konzolova_plocha[5][3] == hrac and konzolova_plocha[6][2] == hrac:
        nakresli_diagonalnu_ciaru_zprava_9_3(hrac)
        return True
    if konzolova_plocha[4][4] == hrac and konzolova_plocha[5][3] == hrac and konzolova_plocha[6][2] == hrac and konzolova_plocha[7][1] == hrac:
        nakresli_diagonalnu_ciaru_zprava_9_4(hrac)
        return True

    # prava cast / --- 6
    if konzolova_plocha[2][7] == hrac and konzolova_plocha[3][6] == hrac and konzolova_plocha[4][5] == hrac and konzolova_plocha[5][4] == hrac:
        nakresli_diagonalnu_ciaru_zlava_10_1(hrac)
        return True
    if konzolova_plocha[3][6] == hrac and konzolova_plocha[4][5] == hrac and konzolova_plocha[5][4] == hrac and konzolova_plocha[6][3] == hrac:
        nakresli_diagonalnu_ciaru_zlava_10_2(hrac)
        return True
    if konzolova_plocha[4][5] == hrac and konzolova_plocha[5][4] == hrac and konzolova_plocha[6][3] == hrac and konzolova_plocha[7][2] == hrac:
        nakresli_diagonalnu_ciaru_zlava_10_3(hrac)
        return True

    # prava cast / --- 7
    if konzolova_plocha[3][7] == hrac and konzolova_plocha[4][6] == hrac and konzolova_plocha[5][5] == hrac and konzolova_plocha[6][4] == hrac:
        nakresli_diagonalnu_ciaru_zprava_11_1(hrac)
        return True
    if konzolova_plocha[4][6] == hrac and konzolova_plocha[5][5] == hrac and konzolova_plocha[6][4] == hrac and konzolova_plocha[7][3] == hrac:
        nakresli_diagonalnu_ciaru_zprava_11_2(hrac)
        return True

    # prava cast / --- 8
    if konzolova_plocha[4][7] == hrac and konzolova_plocha[5][6] == hrac and konzolova_plocha[6][5] == hrac and konzolova_plocha[7][4] == hrac:
        nakresli_diagonalnu_ciaru_zprava_12_1(hrac)
        return True

    return False

#vertikalne
def nakresli_vertikalnu_ciaru_0(stlpec, hrac):
    pozicia_x = stlpec * VELKOST_POLICOK + VELKOST_POLICOK // 2

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (pozicia_x, 15), (pozicia_x, VELKOST_POLICOK * 4 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_vertikalnu_ciaru_1(stlpec, hrac):
    pozicia_x = stlpec * VELKOST_POLICOK + VELKOST_POLICOK // 2

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (pozicia_x, VELKOST_POLICOK + 15), (pozicia_x, VELKOST_POLICOK * 5 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_vertikalnu_ciaru_2(stlpec, hrac):
    pozicia_x = stlpec * VELKOST_POLICOK + VELKOST_POLICOK // 2

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (pozicia_x, VELKOST_POLICOK * 2 + 15), (pozicia_x, VELKOST_POLICOK * 6 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_vertikalnu_ciaru_3(stlpec, hrac):
    pozicia_x = stlpec * VELKOST_POLICOK + VELKOST_POLICOK // 2

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (pozicia_x, VELKOST_POLICOK * 3 + 15), (pozicia_x, VELKOST_POLICOK * 7 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_vertikalnu_ciaru_4(stlpec, hrac):
    pozicia_x = stlpec * VELKOST_POLICOK + VELKOST_POLICOK // 2

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (pozicia_x, VELKOST_POLICOK * 4 + 15), (pozicia_x, VELKOST_POLICOK * 8 - 15), SIRKA_VYHERNEJ_CIARY)

#horizontalne
def nakresli_horizontalnu_ciaru_0(riadok, hrac):
    pozicia_y = riadok * VELKOST_POLICOK + VELKOST_POLICOK // 2

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, pozicia_y), (VELKOST_POLICOK * 4 - 15, pozicia_y), SIRKA_VYHERNEJ_CIARY)

def nakresli_horizontalnu_ciaru_1(riadok, hrac):
    pozicia_y = riadok * VELKOST_POLICOK + VELKOST_POLICOK // 2

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, pozicia_y), (VELKOST_POLICOK * 5 - 15, pozicia_y), SIRKA_VYHERNEJ_CIARY)

def nakresli_horizontalnu_ciaru_2(riadok, hrac):
    pozicia_y = riadok * VELKOST_POLICOK + VELKOST_POLICOK // 2

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, pozicia_y), (VELKOST_POLICOK * 6 - 15, pozicia_y), SIRKA_VYHERNEJ_CIARY)

def nakresli_horizontalnu_ciaru_3(riadok, hrac):
    pozicia_y = riadok * VELKOST_POLICOK + VELKOST_POLICOK // 2

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, pozicia_y), (VELKOST_POLICOK * 7 - 15, pozicia_y), SIRKA_VYHERNEJ_CIARY)

def nakresli_horizontalnu_ciaru_4(riadok, hrac):
    pozicia_y = riadok * VELKOST_POLICOK + VELKOST_POLICOK // 2

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, pozicia_y), (VELKOST_POLICOK * 8 - 15, pozicia_y), SIRKA_VYHERNEJ_CIARY)

#diagonalne \
# main
def nakresli_diagonalnu_ciaru_zlava_0(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, 15), (VELKOST_POLICOK * 4 - 15, VELKOST_POLICOK * 4 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, VELKOST_POLICOK + 15), (VELKOST_POLICOK * 5 - 15, VELKOST_POLICOK * 5 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, VELKOST_POLICOK * 2 + 15), (VELKOST_POLICOK * 6 - 15, VELKOST_POLICOK * 6 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_3(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, VELKOST_POLICOK * 3 + 15), (VELKOST_POLICOK * 7 - 15, VELKOST_POLICOK * 7 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_4(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, VELKOST_POLICOK * 4 + 15), (VELKOST_POLICOK * 8 - 15, VELKOST_POLICOK * 8 - 15), SIRKA_VYHERNEJ_CIARY)

# lava cast \ --- 1
def nakresli_diagonalnu_ciaru_zlava_5_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, VELKOST_POLICOK + 15), (VELKOST_POLICOK * 4 - 15, VELKOST_POLICOK * 5 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_5_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, VELKOST_POLICOK * 2 + 15), (VELKOST_POLICOK * 5 - 15, VELKOST_POLICOK * 6 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_5_3(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, VELKOST_POLICOK * 3 + 15), (VELKOST_POLICOK * 6 - 15, VELKOST_POLICOK * 7 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_5_4(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, VELKOST_POLICOK * 4 + 15), (VELKOST_POLICOK * 7 - 15, VELKOST_POLICOK * 8 - 15), SIRKA_VYHERNEJ_CIARY)

# lava cast \ --- 2
def nakresli_diagonalnu_ciaru_zlava_6_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, VELKOST_POLICOK * 2 + 15), (VELKOST_POLICOK * 4 - 15, VELKOST_POLICOK * 6 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_6_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, VELKOST_POLICOK * 3 + 15), (VELKOST_POLICOK * 5 - 15, VELKOST_POLICOK * 7 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_6_3(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, VELKOST_POLICOK * 4 + 15), (VELKOST_POLICOK * 6 - 15, VELKOST_POLICOK * 8 - 15), SIRKA_VYHERNEJ_CIARY)

# lava cast \ --- 3
def nakresli_diagonalnu_ciaru_zlava_7_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, VELKOST_POLICOK * 3 + 15), (VELKOST_POLICOK * 4 - 15, VELKOST_POLICOK * 7 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_7_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, VELKOST_POLICOK * 4 + 15), (VELKOST_POLICOK * 5 - 15, VELKOST_POLICOK * 8 - 15), SIRKA_VYHERNEJ_CIARY)

# lava cast \ --- 4
def nakresli_diagonalnu_ciaru_zlava_8_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, VELKOST_POLICOK * 4 + 15), (VELKOST_POLICOK * 4 - 15, VELKOST_POLICOK * 8 - 15), SIRKA_VYHERNEJ_CIARY)

# prava cast \ --- 5
def nakresli_diagonalnu_ciaru_zlava_9_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, 15), (VELKOST_POLICOK * 5 - 15, VELKOST_POLICOK * 4 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_9_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, VELKOST_POLICOK + 15), (VELKOST_POLICOK * 6 - 15, VELKOST_POLICOK * 5 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_9_3(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, VELKOST_POLICOK * 2 + 15), (VELKOST_POLICOK * 7 - 15, VELKOST_POLICOK * 6 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_9_4(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, VELKOST_POLICOK * 3 + 15), (VELKOST_POLICOK * 8 - 15, VELKOST_POLICOK * 7 - 15), SIRKA_VYHERNEJ_CIARY)

# prava cast \ --- 6
def nakresli_diagonalnu_ciaru_zlava_10_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, 15), (VELKOST_POLICOK * 6 - 15, VELKOST_POLICOK * 4 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_10_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, VELKOST_POLICOK + 15), (VELKOST_POLICOK * 7 - 15, VELKOST_POLICOK * 5 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_10_3(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, VELKOST_POLICOK * 2 + 15), (VELKOST_POLICOK * 8 - 15, VELKOST_POLICOK * 6 - 15), SIRKA_VYHERNEJ_CIARY)

# prava cast \ --- 7
def nakresli_diagonalnu_ciaru_zlava_11_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, 15), (VELKOST_POLICOK * 7 - 15, VELKOST_POLICOK * 4 - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_11_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, VELKOST_POLICOK + 15), (VELKOST_POLICOK * 8 - 15, VELKOST_POLICOK * 5 - 15), SIRKA_VYHERNEJ_CIARY)

# prava cast \ --- 8
def nakresli_diagonalnu_ciaru_zlava_12_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, 15), (VELKOST_POLICOK * 8 - 15, VELKOST_POLICOK * 4 - 15), SIRKA_VYHERNEJ_CIARY)

#diagonalne /
# main
def nakresli_diagonalnu_ciaru_zprava_0(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, VELKOST_POLICOK * 4 - 15), (VYSKA - 15, 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, VELKOST_POLICOK * 5 - 15), (VELKOST_POLICOK * 7 - 15, VELKOST_POLICOK + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, VELKOST_POLICOK * 6 - 15), (VELKOST_POLICOK * 6 - 15, VELKOST_POLICOK * 2 + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_3(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, VELKOST_POLICOK * 7 - 15), (VELKOST_POLICOK * 5 - 15, VELKOST_POLICOK * 3 + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_4(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, VELKOST_POLICOK * 8 - 15), (VYSKA - VELKOST_POLICOK * 4 - 15, VELKOST_POLICOK * 4 + 15), SIRKA_VYHERNEJ_CIARY)

# lava cast / --- 1
def nakresli_diagonalnu_ciaru_zprava_5_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, VELKOST_POLICOK * 4 - 15), (VELKOST_POLICOK * 7 - 15, 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_5_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, VELKOST_POLICOK * 5 - 15), (VELKOST_POLICOK * 6 - 15, VELKOST_POLICOK + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_5_3(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, VELKOST_POLICOK * 6 - 15), (VELKOST_POLICOK * 5 - 15, VELKOST_POLICOK * 2 + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_5_4(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, VELKOST_POLICOK * 7 - 15), (VELKOST_POLICOK * 4 - 15, VELKOST_POLICOK * 3 + 15), SIRKA_VYHERNEJ_CIARY)

# lava cast / --- 2
def nakresli_diagonalnu_ciaru_zprava_6_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, VELKOST_POLICOK * 4 - 15), (VELKOST_POLICOK * 6 - 15, 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_6_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, VELKOST_POLICOK * 5 - 15), (VELKOST_POLICOK * 5 - 15, VELKOST_POLICOK + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_6_3(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, VELKOST_POLICOK * 6 - 15), (VELKOST_POLICOK * 4 - 15, VELKOST_POLICOK * 2 + 15), SIRKA_VYHERNEJ_CIARY)

# lava cast / --- 3
def nakresli_diagonalnu_ciaru_zprava_7_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, VELKOST_POLICOK * 4 - 15), (VELKOST_POLICOK * 5 - 15, 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_7_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, VELKOST_POLICOK * 5 - 15), (VELKOST_POLICOK * 4 - 15, VELKOST_POLICOK + 15), SIRKA_VYHERNEJ_CIARY)

# lava cast / --- 4
def nakresli_diagonalnu_ciaru_zprava_8_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, VELKOST_POLICOK * 4 - 15), (VELKOST_POLICOK * 4 - 15, 15), SIRKA_VYHERNEJ_CIARY)

# prava cast / --- 5
def nakresli_diagonalnu_ciaru_zprava_9_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, VELKOST_POLICOK * 5 - 15), (VELKOST_POLICOK * 8 - 15, VELKOST_POLICOK + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_9_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, VELKOST_POLICOK * 6 - 15), (VELKOST_POLICOK * 7 - 15, VELKOST_POLICOK * 2 + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_9_3(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, VELKOST_POLICOK * 7 - 15), (VELKOST_POLICOK * 6 - 15, VELKOST_POLICOK * 3 + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_9_4(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK + 15, VELKOST_POLICOK * 8 - 15), (VELKOST_POLICOK * 5 - 15, VELKOST_POLICOK * 4 + 15), SIRKA_VYHERNEJ_CIARY)

# prava cast / --- 6
def nakresli_diagonalnu_ciaru_zlava_10_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, VELKOST_POLICOK * 6 - 15), (VELKOST_POLICOK * 8 - 15, VELKOST_POLICOK * 2 + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_10_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, VELKOST_POLICOK * 7 - 15), (VELKOST_POLICOK * 7 - 15, VELKOST_POLICOK * 3 + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava_10_3(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 2 + 15, VELKOST_POLICOK * 8 - 15), (VELKOST_POLICOK * 6 - 15, VELKOST_POLICOK * 4 + 15), SIRKA_VYHERNEJ_CIARY)

# prava cast / --- 7
def nakresli_diagonalnu_ciaru_zprava_11_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, VELKOST_POLICOK * 7 - 15), (VELKOST_POLICOK * 8 - 15, VELKOST_POLICOK * 3 + 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava_11_2(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 3 + 15, VELKOST_POLICOK * 8 - 15), (VELKOST_POLICOK * 7 - 15, VELKOST_POLICOK * 4 + 15), SIRKA_VYHERNEJ_CIARY)

# prava cast / --- 8
def nakresli_diagonalnu_ciaru_zprava_12_1(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (VELKOST_POLICOK * 4 + 15, VELKOST_POLICOK * 8 - 15), (VELKOST_POLICOK * 8 - 15, VELKOST_POLICOK * 4 + 15), SIRKA_VYHERNEJ_CIARY)

def vypis_vyhry():
    vyhra_o = font.render('O vyhral!', True, RED, DARK_BLUE)
    vyhra_x = font.render('X vyhral!', True, BLUE, DARK_BLUE)
    if hrac == 1:
        textRect = vyhra_o.get_rect(center=(VYSKA // 2, SIRKA // 2))
        obrazovka.blit(vyhra_o, textRect)
    elif hrac == 2:
        textRect = vyhra_x.get_rect(center=(VYSKA // 2, SIRKA // 2))
        obrazovka.blit(vyhra_x, textRect)
        
def restart():
    obrazovka.fill(FARBA_OBRAZOVKY)
    nakresli_ciary()
    hrac = 1
    for riadok in range(RIADKY_PLOCHY):
        for stlpec in range(STLPCE_PLOCHY):
            konzolova_plocha[riadok][stlpec] = 0

nakresli_ciary()

hrac = 1
koniec_hry = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not koniec_hry:
            
            X = event.pos[0]
            Y = event.pos[1]
            
            klikol_riadok = int(Y // VELKOST_POLICOK)
            klikol_stlpec = int(X // VELKOST_POLICOK)

            if volny_stvorec(klikol_riadok, klikol_stlpec):
                if hrac == 1:
                    oznac_stovrec(klikol_riadok, klikol_stlpec, 1)
                    nakresli_objekty()
                    if kontrola_vyhry(hrac):
                        koniec_hry = True
                        #vypis_vyhry()
                    elif kontrola_plochy():
                        remiza = font.render('REMIZA!', True, FARBA_OBRAZOVKY, DARK_BLUE)
                        textRect = remiza.get_rect(center=(VYSKA // 2, SIRKA // 2))
                        obrazovka.blit(remiza, textRect)
                    hrac = 2

                elif hrac == 2:
                    oznac_stovrec(klikol_riadok, klikol_stlpec, 2)
                    nakresli_objekty()
                    if kontrola_vyhry(hrac):
                        koniec_hry = True
                        vypis_vyhry()
                    elif kontrola_plochy():
                        remiza = font.render('REMIZA!', True, FARBA_OBRAZOVKY, DARK_BLUE)
                        textRect = remiza.get_rect(center=(VYSKA // 2, SIRKA // 2))
                        obrazovka.blit(remiza, textRect)
                    hrac = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or pygame.K_RETURN:
                restart()
                koniec_hry = False
                

    pygame.display.update()