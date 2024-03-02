import pygame
import os

#Kirjas kasutatudÜlesanded, kuid pigem kasutamataülesanded on sobiv
kasutatudÜlesanded = dict()

imageSize = (500, 200)

ülesanded = {
    "tuletised": [
        [pygame.image.load(os.path.join("Assets", "tuletis", "ül1.png")), "-6"],
        [pygame.image.load(os.path.join("Assets", "tuletis", "ül2.png")), "0"],
        [pygame.image.load(os.path.join("Assets", "tuletis", "pilt07.png")), "0"],
        [pygame.image.load(os.path.join("Assets", "tuletis", "pilt08.png")), "900"],

    ],
    "maatriks": [
        [pygame.image.load(os.path.join("Assets", "maatriks", "pilt01.png")), "0"],
        [pygame.image.load(os.path.join("Assets", "maatriks", "pilt03.png")), "900"],
        [pygame.image.load(os.path.join("Assets", "maatriks", "pilt05.png")), "-76"],
        [pygame.image.load(os.path.join("Assets", "maatriks", "pilt07.png")), "0"]
    ],
    "integraal": [
        [pygame.image.load(os.path.join("Assets", "integraal", "pilt01.png")), "3250"],
        [pygame.image.load(os.path.join("Assets", "integraal", "pilt03.png")), "3"],
        [pygame.image.load(os.path.join("Assets", "integraal", "pilt05.png")), "5"],
        [pygame.image.load(os.path.join("Assets", "integraal", "pilt07.png")), "-664"]
    ],
    "piirväärtus": [
        [pygame.image.load(os.path.join("Assets", "piirväärtus", "pilt03.png")), "1"],
        [pygame.image.load(os.path.join("Assets", "piirväärtus", "pilt04.png")), "-6"],
        [pygame.image.load(os.path.join("Assets", "piirväärtus", "pilt05.png")), "0"],
        [pygame.image.load(os.path.join("Assets", "piirväärtus", "pilt06.png")), "4"]
    ]
}
for type in ülesanded:
    kasutatudÜlesanded[type] = [i for i in range(0, len(ülesanded[type]))]
    #for i in range(0, len(ülesanded[type])):
    #    ülesanded[type][i] = [pygame.transform.scale_by(ülesanded[type][i][0], 0.25), ülesanded[type][i][1]]