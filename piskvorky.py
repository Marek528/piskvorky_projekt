import pygame, sys
import numpy as np

pygame.init()

SIRKA = 750
VYSKA = 750
SIRKA_CIARY = 15

RIADKY_PLOCHY = 3
STLPCE_PLOCHY = 3

POLOMER_KRUHU = 70
SIRKA_KRUHU = 20

SIRKA_CIARY = 25

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
                pygame.draw.line(obrazovka, BLUE, (stlpec * 250 + 55, riadok * 250 + 250 - 55), (stlpec * 250 + 250 - 55, riadok * 250 + 55), SIRKA_CIARY)
                pygame.draw.line(obrazovka, BLUE, (stlpec * 250 + 55, riadok * 250 + 55), (stlpec * 250 + 250 - 55, riadok * 250 + 250 - 55), SIRKA_CIARY)

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

nakresli_ciary()

hrac = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            X = event.pos[0]
            Y = event.pos[1]
            
            klikol_riadok = int(Y // 250)
            klikol_stlpec = int(X // 250)

            if volny_stvorec(klikol_riadok, klikol_stlpec):
                if hrac == 1:
                    oznac_stovrec(klikol_riadok, klikol_stlpec, 1)
                    hrac = 2

                elif hrac == 2:
                    oznac_stovrec(klikol_riadok, klikol_stlpec, 2)
                    hrac = 1



                nakresli_objekty()
                

    pygame.display.update()