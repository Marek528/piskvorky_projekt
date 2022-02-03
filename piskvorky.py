import pygame, sys

pygame.init()

SIRKA = 750
VYSKA = 750
DLZKA_CIARY = 15

RED = (255,0,0)
FARBA_OBRAZOVKY = (255,255,255)
FARBA_CIARY = (0,0,0)


obrazovka = pygame.display.set_mode((SIRKA, VYSKA))
obrazovka.fill(FARBA_OBRAZOVKY)



def nakresli_ciary():
    #horizontalne
    pygame.draw.line(obrazovka, FARBA_CIARY, (0, 250), (750, 250), DLZKA_CIARY)
    pygame.draw.line(obrazovka, FARBA_CIARY, (0, 500), (750, 500), DLZKA_CIARY)

    #vertikalne
    pygame.draw.line(obrazovka, FARBA_CIARY, (250, 0), (250, 750), DLZKA_CIARY)
    pygame.draw.line(obrazovka, FARBA_CIARY, (500, 0), (500, 750), DLZKA_CIARY)

nakresli_ciary()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()