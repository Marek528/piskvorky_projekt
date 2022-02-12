import pygame, sys
import numpy as np

pygame.init()

SIRKA = 750
VYSKA = 750
SIRKA_CIARY = 15
SIRKA_VYHERNEJ_CIARY = 20

RIADKY_PLOCHY = 3
STLPCE_PLOCHY = 3

POLOMER_KRUHU = 70
SIRKA_KRUHU = 20

SIRKA_KRIZIKA = 25

FARBA_OBRAZOVKY = (255,255,255)
FARBA_CIARY = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

obrazovka = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption('Piskovrky')
obrazovka.fill(FARBA_OBRAZOVKY)

konzolova_plocha = np.zeros((RIADKY_PLOCHY, STLPCE_PLOCHY))

def nakresli_ciary():
    #horizontalne ciary
    pygame.draw.line(obrazovka, FARBA_CIARY, (0, 250), (750, 250), SIRKA_CIARY)
    pygame.draw.line(obrazovka, FARBA_CIARY, (0, 500), (750, 500), SIRKA_CIARY)

    #vertikalne ciary
    pygame.draw.line(obrazovka, FARBA_CIARY, (250, 0), (250, 750), SIRKA_CIARY)
    pygame.draw.line(obrazovka, FARBA_CIARY, (500, 0), (500, 750), SIRKA_CIARY)

def nakresli_objekty():
    for riadok in range(RIADKY_PLOCHY):
        for stlpec in range(STLPCE_PLOCHY):
            if konzolova_plocha[riadok][stlpec] == 1:
                pygame.draw.circle(obrazovka, RED, (int(stlpec * 250 + 125), int(riadok * 250 + 125)), POLOMER_KRUHU, SIRKA_KRUHU)
            elif konzolova_plocha[riadok][stlpec] == 2:
                pygame.draw.line(obrazovka, BLUE, (stlpec * 250 + 55, riadok * 250 + 250 - 55), (stlpec * 250 + 250 - 55, riadok * 250 + 55), SIRKA_KRIZIKA)
                pygame.draw.line(obrazovka, BLUE, (stlpec * 250 + 55, riadok * 250 + 55), (stlpec * 250 + 250 - 55, riadok * 250 + 250 - 55), SIRKA_KRIZIKA)

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
        if konzolova_plocha[0][stlpec] == hrac and konzolova_plocha[1][stlpec] == hrac and konzolova_plocha[2][stlpec] == hrac:
            nakresli_vertikalnu_ciaru(stlpec, hrac)
            return True

    #horizontalne
    for riadok in range(RIADKY_PLOCHY):
        if konzolova_plocha[riadok][0] == hrac and konzolova_plocha[riadok][1] == hrac and konzolova_plocha[riadok][2] == hrac:
            nakresli_horizontalnu_ciaru(riadok, hrac)
            return True
    
    #diagonalne zprava 
    if konzolova_plocha[0][0] == hrac and konzolova_plocha[1][1] == hrac and konzolova_plocha[2][2] == hrac:
        nakresli_diagonalnu_ciaru_zprava(hrac)
        return True
    
    #diagonalne zlava
    if konzolova_plocha[2][0] == hrac and konzolova_plocha[1][1] == hrac and konzolova_plocha[0][2] == hrac:
        nakresli_diagonalnu_ciaru_zlava(hrac)
        return True
    
    return False

def nakresli_vertikalnu_ciaru(stlpec, hrac):
    pozicia_x = stlpec * 250 + 125

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (pozicia_x, 15), (pozicia_x, VYSKA - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_horizontalnu_ciaru(riadok, hrac):
    pozicia_y = riadok * 250 + 125

    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, pozicia_y), (VYSKA - 15, pozicia_y), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zprava(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, 15), (SIRKA - 15, VYSKA - 15), SIRKA_VYHERNEJ_CIARY)

def nakresli_diagonalnu_ciaru_zlava(hrac):
    if hrac == 1:
        farba = RED
    elif hrac == 2:
        farba = BLUE

    pygame.draw.line(obrazovka, farba, (15, VYSKA - 15), (SIRKA - 15, 15), SIRKA_VYHERNEJ_CIARY)

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
            
            klikol_riadok = int(Y // 250)
            klikol_stlpec = int(X // 250)

            if volny_stvorec(klikol_riadok, klikol_stlpec):
                if hrac == 1:
                    oznac_stovrec(klikol_riadok, klikol_stlpec, 1)
                    if kontrola_vyhry(hrac):
                        koniec_hry = True
                        # vypisanie textu vyhral hrac
                    hrac = 2

                elif hrac == 2:
                    oznac_stovrec(klikol_riadok, klikol_stlpec, 2)
                    if kontrola_vyhry(hrac):
                        koniec_hry = True
                        # vypisanie textu vyhral hrac
                    hrac = 1

                nakresli_objekty()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or pygame.K_RETURN:
                restart()
                

    pygame.display.update()