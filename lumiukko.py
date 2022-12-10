import pygame


def alusta():
    """ Alustaa pygame ikkunan ja palauttaa näyttöolion """
    pygame.init()
    naytto = pygame.display.set_mode((700, 700))
    return naytto


def piirra_pallo_1(naytto, x: int, y: int):
    """ Piirtää ruudulle pallon annettuihin koordinaatteihin """
    # Parametrit: näyttöolio, väri (r,g,b), x- ja y-koordinaatit
    # tuplena, koko x-suunnassa, koko y-suunnassa
    pygame.draw.circle(naytto, (255, 255, 255), (x, y), 40, 40)


def piirra_pallo_2(naytto, x: int, y: int):
    """ Piirtää ruudulle pallon annettuihin koordinaatteihin """
    # Parametrit: näyttöolio, väri (r,g,b), x- ja y-koordinaatit
    # tuplena, koko x-suunnassa, koko y-suunnassa
    pygame.draw.circle(naytto, (255, 255, 255), (x, y), 60, 60)


def piirra_pallo_3(naytto, x: int, y: int):
    """ Piirtää ruudulle pallon annettuihin koordinaatteihin """
    # Parametrit: näyttöolio, väri (r,g,b), x- ja y-koordinaatit
    # tuplena, koko x-suunnassa, koko y-suunnassa
    pygame.draw.circle(naytto, (255, 255, 255), (x, y), 80, 80)


def piirra_musta_nappi(naytto, x: int, y: int):
    """ Piirtää ruudulle pallon annettuihin koordinaatteihin """
    # Parametrit: näyttöolio, väri (r,g,b), x- ja y-koordinaatit
    # tuplena, koko x-suunnassa, koko y-suunnassa
    pygame.draw.circle(naytto, (0, 0, 0), (x, y), 7, 7)


def piirra_nena(naytto, x: int, y: int):
    """ Piirtää ruudulle pallon annettuihin koordinaatteihin """
    # Parametrit: näyttöolio, väri (r,g,b), x- ja y-koordinaatit
    # tuplena, koko x-suunnassa, koko y-suunnassa
    pygame.draw.circle(naytto, (255, 69, 0), (x, y), 7, 7)


naytto = alusta()


# Lumiukon aloituskoordinaatit
lumiukko_x = 350
lumiukko_y = 600

# Reunojen koordinaatit
YLAREUNA = 280
VASEN_REUNA = 80
OIKEA_REUNA = 620
ALAREUNA = 620

# Liikkeen nopeus
NOPEUS = 20

# Lumiukko
# Sisältää 8 elementtia, jotka liikkuvat samaan aikaan


def piirretty_lumiukko():
    piirra_pallo_1(naytto, lumiukko_x, lumiukko_y-210),
    piirra_pallo_2(naytto, lumiukko_x, lumiukko_y-120),
    piirra_pallo_3(naytto, lumiukko_x, lumiukko_y),
    piirra_nena(naytto, lumiukko_x, lumiukko_y-200),
    piirra_musta_nappi(naytto, lumiukko_x, lumiukko_y-100),
    piirra_musta_nappi(naytto, lumiukko_x, lumiukko_y-140),
    piirra_musta_nappi(naytto, lumiukko_x, lumiukko_y+10),
    piirra_musta_nappi(naytto, lumiukko_x, lumiukko_y-40)


# alustetaan ajastin
ajastin = pygame.time.Clock()


# Pygamen pääsilmukka, jossa odotetaan ikkunan sulkeutumista
while True:

    # Odotetaan  hetki
    ajastin.tick(100)

    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((25, 25, 112))
    piirretty_lumiukko()

    # mitä nappuloita on nyt pohjassa?
    painetut_nappulat = pygame.key.get_pressed()
    if painetut_nappulat[pygame.K_LEFT]:
        lumiukko_x -= NOPEUS
    if painetut_nappulat[pygame.K_RIGHT]:
        lumiukko_x += NOPEUS
    if painetut_nappulat[pygame.K_DOWN]:
        lumiukko_y += NOPEUS
    if painetut_nappulat[pygame.K_UP]:
        lumiukko_y -= NOPEUS

    # Tarkistetaan, ettei mennyt reunasta yli
    if lumiukko_x < VASEN_REUNA:
        lumiukko_x = VASEN_REUNA
    if lumiukko_x > OIKEA_REUNA:
        lumiukko_x = OIKEA_REUNA
    if lumiukko_y < YLAREUNA:
        lumiukko_y = YLAREUNA
    if lumiukko_y > ALAREUNA:
        lumiukko_y = ALAREUNA


# tämä piirtää ruuduun uudestaan muu
# tosten jälkeen
    pygame.display.flip()
