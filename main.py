import pygame
import pygame_gui
import os
import pickle
import random
from ülesandedF import *

class Player:
    def __init__(self):
        self.xp = 0
        self.level = 1
        self.items = []
        self.exhaustion = 0
    
    def addSleep(self, amount):
        self.exhaustion+=amount
    
    def addItem(self, item):
        self.items.append(item)
    
    def addXP(self, amount):
        self.xp+=amount

class Item:
    def __init__(self, name, image, cost=9999999):
        self.name = name
        self.image = pygame.image.load(os.path.join("Assets", image))
        self.cost = cost
    
if os.path.exists("playerData.pickle"):
    loadFile = open("playerData.pickle", "rb")
    player=pickle.load(loadFile)
    kasutatudÜlesanded=pickle.load(loadFile)
    loadFile.close()
else:
    player = Player()

class xpbar:
    def __init__(self, x, y, w, h, max_xp):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.exp = player.xp
        self.max_xp= max_xp*player.level
    def draw(self, surface):
        ratio = self.exp / self.max_xp
        pygame.draw.rect(surface, "white", (self.x,self.y,self.w,self.h))
        pygame.draw.rect(surface, "green", (self.x,self.y,self.w* ratio, self.h))
    def add_EXP(self, amount):
        self.exp += amount
        player.xp += amount
        if self.exp == self.max_xp:
            player.xp = player.xp - self.max_xp
            self.exp = self.exp - self.max_xp
            player.level += 1
            self.max_xp += 10
            if player.level == 10:
                pass

xp_bar=xpbar(650,600,300,40,10)


# pygame.image.load(os.path.join('Assets', 'pilt.png'))
TAUSTPILT = pygame.image.load(os.path.join("Assets", "taust.png"))
RAAMATPILT = pygame.image.load(os.path.join("Assets", "raamat.png"))
TUBAPILT = pygame.image.load(os.path.join("Assets", "tuba.png"))

MUSIC = [os.path.join("Assets", "C418Mice.mp3"),
         os.path.join("Assets", "C418Minecraft.mp3"),
         os.path.join("Assets", "C418Subwoofer.mp3"),
         os.path.join("Assets", "C418Sweden.mp3")]
pygame.mixer.init()

pygame.init()
pygame.font.init()


WIND = (1000, 700)
FPS = 60
WIN = pygame.display.set_mode(WIND)
pygame.display.set_caption('Revenge of the mathizens')
GManager = pygame_gui.UIManager(WIND)

GManager.add_font_paths("PressStart2P", os.path.join("Assets", "PressStart2P.ttf"))
GManager.get_theme().load_theme("theme.json")
# UI elements
UIElements = {
    "PlayButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500-100, 250), (200,100)),
                                          text="PLAY",
                                          manager=GManager,
                                          visible=False),
    "ShopButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500-100, 350), (200,100)),
                                          text="SHOP",
                                          manager=GManager,
                                          visible=False),
    "OptionsButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500-100, 450), (200,100)),
                                          text="OPTIONS",
                                          manager=GManager,
                                          visible=False),
    "QuitButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500-100, 550), (200,100)),
                                          text="QUIT",
                                          manager=GManager,
                                          visible=False),
    "BackMainMenuButton2": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500-100, 550), (200,100)),
                                          text="BACK",
                                          manager=GManager,
                                          visible=False),
    "BackMainMenuButton1": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 10), (75,75)),
                                          text="[=]",
                                          manager=GManager,
                                          visible=False,
                                          object_id="#BackMainMenuButton1"),
    "UksButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((105, 0), (210,50)),
                                          text="Kool",
                                          manager=GManager,
                                          visible=False),
    "MagaButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 525), (210,100)),
                                          text="Maga",
                                          manager=GManager,
                                          visible=False,
                                          allow_double_clicks=False),
    "LaudButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((780, 30), (160,70)),
                                          text="Harjuta",
                                          manager=GManager,
                                          visible=False,
                                          object_id="#LaudButton"),
    "tuletisedButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 125), (300,100)),
                                          text="Tuletise arvutamine",
                                          manager=GManager,
                                          visible=False,
                                          object_id=pygame_gui.core.ObjectID(class_id="@ülesanneNupp")),
    "piirväärtusButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 125), (300,100)),
                                          text="Piirväärtus",
                                          manager=GManager,
                                          visible=False,
                                          object_id=pygame_gui.core.ObjectID(class_id="@ülesanneNupp")),
    "integraalButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 250), (300,100)),
                                          text="Integraal",
                                          manager=GManager,
                                          visible=False,
                                          object_id=pygame_gui.core.ObjectID(class_id="@ülesanneNupp")),
    "maatriksButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 250), (300,100)),
                                          text="Maatriks",
                                          manager=GManager,
                                          visible=False,
                                          object_id=pygame_gui.core.ObjectID(class_id="@ülesanneNupp")),
    "vastusTextNupp": pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((500-150, 450), (250,75)),
                                                      manager=GManager,
                                                      visible=False,
                                                      placeholder_text="Vastus"),
    "vastusEnterNupp": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700-100, 450), (100, 75)),
                                                    manager=GManager,
                                                    visible=False,
                                                    text="Esita"),
    "volumeSlider": pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((WIND[0]/2-125, 250), (250, 75)),
                                                           manager=GManager,
                                                           visible=False,
                                                           start_value=1,
                                                           value_range=(0.0, 1.0),
                                                           click_increment=0.1),
    "ülesanneValikBackButton": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500-100, 550), (200,100)),
                                          text="BACK",
                                          manager=GManager,
                                          visible=False),
    "continueButton1": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500,400),(200,100)),
                                                    manager=GManager,
                                                    text="Edasi",
                                                    visible=False),
    "vastusEnterNuppTimed": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700-100, 450), (100, 75)),
                                                    manager=GManager,
                                                    visible=False,
                                                    text="Esita"),
    "continueButton2": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500,400),(200,100)),
                                                    manager=GManager,
                                                    text="Edasi",
                                                    visible=False),
    "bossBattleButtonActivate": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500-150,430), (300,100)),
                                                    manager=GManager,
                                                    text="Zolk Battle",
                                                    visible=False)
}

def get_font(SIZE):
    FONT = pygame.font.Font(os.path.join("Assets", "PressStart2P.ttf"), SIZE)
    return FONT

def renderText(text, size, color, pos, screen):
    writeText = get_font(size).render(text, True, color)
    screen.blit(writeText, writeText.get_rect(center=pos))

def invisElements():
    global UIElements
    for element in UIElements:
        UIElements[element].visible = False

def visElements(elementList):
    global UIElements
    for element in elementList:
        UIElements[element].visible = True

def randomÜlesanne(type):
    if len(kasutatudÜlesanded[type]) == 0:
        kasutatudÜlesanded[type] = [i for i in range(0, len(ülesanded[type]))]
    ülesanneNr = random.choice(kasutatudÜlesanded[type])
    kasutatudÜlesanded[type].remove(ülesanneNr)
    return ülesanded[type][ülesanneNr]

isSleeping = False

def sleep():
    fade = pygame.Surface((WIND[0], WIND[1]))
    fade.fill((125, 125, 125))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        WIN.fill((0, 0, 0))
        WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(20)
    UIElements["MagaButton"].enable()
    UIElements["MagaButton"].visible = True
    
class Zolk:
    def __init__(self, x, y):
        self.run = True
        self.x = x
        self.y = y
        self.image = pygame.image.load(os.path.join("Assets", "Zolk.png"))
        self.bubble = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "speechBubble.png")), (500,300))
    
    def moveIn(self):
        startx = -100
        starty = 200
        difx = self.x-startx
        dify = self.y-starty
        loops = 300
        for i in range(0, loops):
            WIN.blit(self.image, (startx+i*difx/loops,starty+i*dify/loops))
            pygame.display.update()
            pygame.time.delay(5)
    
    def dialoog(self, tekst, size):
        WIN.blit(self.bubble, (self.x+200, self.y-90))
        writeText = get_font(size).render(tekst, True, "Black")
        WIN.blit(writeText, (self.x+300,self.y))
        #renderText(tekst, size, "Black", (self.x+350,self.y+80), WIN)

    def exist(self):
        WIN.blit(self.image, (self.x, self.y))


zolk = Zolk(150,200)

bossAttempt = 0

class GameState():
    def __init__(self):
        self.state = "mainMenu"

        random.shuffle(MUSIC)
        self.currentMusic = MUSIC[0]
        pygame.mixer_music.load(self.currentMusic)
        pygame.mixer_music.play()

        self.ülesanne = None

    def stateManager(self):
        match self.state:
            case "mainMenu":
                self.mainMenu()
            case "tuba":
                self.tuba()
            case "valiÜlesanded":
                self.valiÜlesanded()
            case "harjutamine":
                self.harjutamine()
            case "optionsMenu":
                self.optionsMenu()
            case "bossBattle1":
                self.bossBattle1()
            case "timedÜlesanne":
                self.timedÜlesanne()
            case "failScene":
                self.failScene()
            case "successScene":
                self.successScene()
            case "shop":
                self.shop()
            case "notrequiredlevel":
                self.notrequiredlevel()
    
    def mainMenu(self):
        WIN.blit(TAUSTPILT, (0,0))
        renderText("Revenge of the mathizens", 35, "Red", (WIND[0]/2, 150), WIN)
        visElements(["PlayButton", "ShopButton", "OptionsButton", "QuitButton"])
    
    def tuba(self):
        WIN.blit(TUBAPILT, (0,0))
        xp_bar.draw(WIN)
        lvl1 = "Level: " + str({player.level})
        XP_TEXT = get_font(20).render(lvl1, True, "green")
        XP_RECT = XP_TEXT.get_rect(center=(850,585))
        WIN.blit(XP_TEXT,XP_RECT)
        lvl2 = str(xp_bar.exp) + "/" + str(xp_bar.max_xp)
        XP1_TEXT = get_font(10).render(lvl2, True, "black")
        XP1_RECT = XP1_TEXT.get_rect(center=(800,620))
        WIN.blit(XP1_TEXT,XP1_RECT)
        visElements(["BackMainMenuButton1", "UksButton", "MagaButton", "LaudButton"])
    
    def valiÜlesanded(self):
        WIN.blit(TAUSTPILT, (0,0))
        visElements(["tuletisedButton", "ülesanneValikBackButton", "bossBattleButtonActivate", "integraalButton", "maatriksButton", "piirväärtusButton"])
    
    def harjutamine(self):
        WIN.blit(TAUSTPILT, (0,0))
        WIN.blit(self.ülesanne[0], (WIND[0]/2-250,150))
        visElements(["vastusTextNupp", "vastusEnterNupp"])
    
    def optionsMenu(self):
        WIN.blit(TAUSTPILT, (0,0))
        renderText("Options", 35, "Red", (WIND[0]/2, 150), WIN)
        renderText("Volume", 20, "Black", (WIND[0]/2, 225), WIN)
        visElements(["BackMainMenuButton2", "volumeSlider"])
        UIElements["volumeSlider"].show()
    
    def bossBattle1(self):
        WIN.blit(TAUSTPILT, (0,0))
        if zolk.run:
            zolk.moveIn()
            zolk.run = False
        zolk.exist()
        zolk.dialoog("""Arvad, et saad\nhakkama? Vaatame.""", 22)
        visElements(["continueButton1"])
    
    def failScene(self):
        WIN.blit(TAUSTPILT, (0,0))
        if zolk.run:
            zolk.moveIn()
            pygame.mixer.Sound("Assets/fail.mp3").play()
            zolk.run = False
        zolk.exist()
        zolk.dialoog("""Ei saanud hakkama.\nProovi uuesti.""", 21)
        visElements(["continueButton2"])

    def successScene(self):
        WIN.blit(TAUSTPILT, (0,0))
        if zolk.run:
            zolk.moveIn()
            pygame.mixer.Sound("Assets/victory.mp3").play()
            zolk.run = False
        zolk.exist()
        zolk.dialoog("""Tubli! Oled oman-\ndanud palju tead-\nmisi!""", 21)
        visElements(["continueButton2"])

    
    def timedÜlesanne(self):
        WIN.blit(TAUSTPILT, (0,0))
        WIN.blit(self.ülesanne[0], (WIND[0]/2-250,150))
        WIN.blit(get_font(24).render(f'{bossAttempt+1}/5', True, (85,214,194)), (650,120))
        visElements(["vastusTextNupp", "vastusEnterNuppTimed"])
    
    def shop(self):
        WIN.blit(TAUSTPILT, (0,0))
        renderText("You do not have the required DLC\n      to use this feature.", 24, "Black", (500,280), WIN)
        visElements(["BackMainMenuButton2"])
    def notrequiredlevel(self):
        WIN.blit(TAUSTPILT, (0,0))
        renderText(f"You need to be level {bossFightLvlRequirement}\n   to fight Mr. Zolk.", 24, "Black", (500,280), WIN)
        visElements(["BackMainMenuButton2"])

bossFightLvlRequirement = 1

gameState = GameState()
clock = pygame.time.Clock()
run = True
tracker = "bossBattle1"
while run:
    delta = clock.tick(FPS)/1000
    gameState.stateManager()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == UIElements["volumeSlider"]:
                pygame.mixer_music.set_volume(UIElements["volumeSlider"].get_current_value())

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == UIElements["PlayButton"]:
                gameState.state = "tuba"
            if event.ui_element == UIElements["bossBattleButtonActivate"]:
                if player.level >= bossFightLvlRequirement:
                    gameState.state = "bossBattle1"
                else:
                    gameState.state = "notrequiredlevel"
            if event.ui_element == UIElements["BackMainMenuButton1"]:
                gameState.state = "mainMenu"
            if event.ui_element == UIElements["ShopButton"] or event.ui_element == UIElements["UksButton"]:
                gameState.state = "shop"
            if event.ui_element == UIElements["tuletisedButton"]:
                gameState.state = "harjutamine"
                gameState.ülesanne = randomÜlesanne("tuletised")
            if event.ui_element == UIElements["integraalButton"]:
                gameState.state = "harjutamine"
                gameState.ülesanne = randomÜlesanne("integraal")
            if event.ui_element == UIElements["piirväärtusButton"]:
                gameState.state = "harjutamine"
                gameState.ülesanne = randomÜlesanne("piirväärtus")
            if event.ui_element == UIElements["maatriksButton"]:
                gameState.state = "harjutamine"
                gameState.ülesanne = randomÜlesanne("maatriks")
            if event.ui_element == UIElements["continueButton1"]:
                zolk.run = True
                gameState.ülesanne = randomÜlesanne(random.choice(list(ülesanded.keys())))
                gameState.state = "timedÜlesanne"
            if event.ui_element == UIElements["continueButton2"]:
                zolk.run = True
                gameState.state = "valiÜlesanded"
            if event.ui_element == UIElements["vastusEnterNuppTimed"]:
                if UIElements["vastusTextNupp"].get_text() == gameState.ülesanne[1]:
                    bossAttempt+=1
                    xp_bar.add_EXP(5)
                    if bossAttempt != 5:
                        gameState.ülesanne = randomÜlesanne(random.choice(list(ülesanded.keys())))
                        gameState.state = "timedÜlesanne"
                    else:
                        bossAttempt=0
                        gameState.state = "successScene"
                else:
                    bossAttempt=0
                    gameState.state = "failScene"
                UIElements["vastusTextNupp"].set_text("")
            if event.ui_element == UIElements["vastusEnterNupp"]:
                gameState.state = "tuba"
                if UIElements["vastusTextNupp"].get_text() == gameState.ülesanne[1]:
                    pygame.mixer.Sound("Assets/victory.mp3").play()
                    xp_bar.add_EXP(5)
                else:
                    pygame.mixer.Sound("Assets/fail.mp3").play()
                UIElements["vastusTextNupp"].set_text("")
            if event.ui_element == UIElements["LaudButton"]:
                gameState.state = "valiÜlesanded"
            if event.ui_element == UIElements["BackMainMenuButton2"]:
                UIElements["volumeSlider"].hide()
                gameState.state = "mainMenu"
            if event.ui_element == UIElements["OptionsButton"]:
                gameState.state = "optionsMenu"
            if event.ui_element == UIElements["MagaButton"]:
                UIElements["MagaButton"].disable()
                UIElements["MagaButton"].visible = False
                sleep()
            if event.ui_element == UIElements["ülesanneValikBackButton"]:
                gameState.state = "tuba"
            if event.ui_element == UIElements["QuitButton"]:
                run = False
        GManager.process_events(event)
    if tracker != gameState.state:
        invisElements()
        tracker = gameState.state
    GManager.update(delta)
    GManager.draw_ui(WIN)
    pygame.display.update()
    if not pygame.mixer_music.get_busy():
        random.shuffle(MUSIC)
        pygame.mixer_music.load(MUSIC[0])
        pygame.mixer_music.play()

dumpFile = open("playerData.pickle", "wb")
pickle.dump(player, dumpFile)
pickle.dump(kasutatudÜlesanded, dumpFile)
dumpFile.close()
pygame.quit()