import random
import time
import math

try:
    import pygame
    pygame.mixer.init()
except:
    soundImportSuccesful = False
    print("Pygame wasn't succesfully initialized.# Audio has been disabled.")
    print()



def chapter_4(funcs):
    doDialogText = funcs['doDialogText']
    doDialogSlow = funcs['doDialogSlow']
    askChoice = funcs['askChoice']
    askNum = funcs['askNum']
    doDialogChoice = funcs['doDialogChoice']
    doTimedQuestion = funcs['doTimedQuestion']
    doTimedAttack = funcs['doTimedAttack']
    doTimedSpam = funcs['doTimedSpam']
    printGraphic = funcs['printGraphic']
    getPrompt = funcs['getPrompt']
    playSong = funcs['playSong']
    pauseSong = funcs['pauseSong']
    stopSong = funcs['stopSong']
    timeControl = funcs['timeControl']
    setTime = funcs['setTime']
    pgFilter = funcs['pgFilter']
    saveFile = funcs['saveFile']
    saveGame = funcs['saveGame']
    curSaveName = funcs['curSaveName']
    soundImportSuccesful = funcs['soundImportSuccesful']

    loadModule = funcs['loadModule']

    route4 = {
        "startIndex": 0,
        "DEATHS": 0,

        "inventory": [],
        "money": 0,
        "players": [],

        "on_weirdRoute": False,
        "battle_firstChoice": 0,
        "battle_noHit": True,
        "helped_annie": 0,
        "helped_everyone": 0,
        "played_conjuring": False,
        "peak_horseRiding": 0,
        "wordle": 0,
        "rajith_noHit": True,

        "guard_spared": 0,

        "COMPLETED": False
    }

    for i in saveFile['route4']:
        route4[i] = saveFile['route4'][i]

    finalSave = False
    
    doDialogText("CHAPTER 4:##  Light and Dark..", spd = 25, step = 3)
    print()

    nameChoice = saveFile['route1']['name_choice']

    money = 0
    inventory = []

    def getMaxHP(person):
        """GETS THE MAX HP FOR A PLAYER USING NUMBERED INDEX:\n
        1: YOU (THE PLAYER)\n
        2: ASHISH\n
        3: KNIGHT\n
        4: FLOWERY"""
        if person == 1: return 10 + player['lv']*5
        if person == 2: return 10 + ashish['lv']*5
        if person == 3: return 15 + knight['lv']*5
        if person == 4: return 15 + flowery['lv']*5
    
    def getDamageDealt(enemyATK, targetStruct, fResult):
        damage = math.ceil(max(1-fResult, 0.45)*(enemyATK/targetStruct["defense"]))
        return damage
    



    def doEpicIntro(music = True):
        if not music:
            printGraphic("""
█████████████████████▀▄▀▄▀     ▀         ▄▄
████████████████▀███▄▀▄▀▄▀  ▄        ▄▄▀▀  █▄
███▀▄▄▀██████▀▄▄█▄▄▀▄▀██▄▀  ▄       █       ▀█▄       ██▄▄
██ ██▀▀▄██████▄▄▀▄▄███▄▀▄▀▄  ▀       ▀█▄   ▄█▀      ▀█████▀
██ ██ ████████████████████▄▀▄▀▄        ▀█▄█▀          ██
██ ███▄▀▀███▀██████▀████▄█▄▀▄▀ ▀         ▀            ▀█▄
██▄▀▀████▄▄▄█ ████▄▀▄████▀██▄▀▄▀▄                 ▄█▄  ██
█████▄▄ ▀▀▀▄▄█████████████▄▀▄▀▄                  ▀▀█▀▀  █
██████████████████████████▄▀█▀▄▀▄▀▄
█████████████████████████▀██▄█▄▀▄▀
█████▀▄▀█████████▀██████▄▀▄██▀█▀▄▀▄        ▄
██████▄█████████▄▀▄█████████████▄▀▄▀      ▀█▀▀             ▄
███████████████████████████████▀▄▀▄▀▄                    ▄███▄
████████████████████████████████▄█▄▀▄▀             ▄      ▀█▀
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀▀████▀▄▀▄           ▄█▄
██████████████████████████▀█▀██▄▄▄██▄▀▄▀          ███
████████████████████████▀▄▀▄█▀▄▀███▀▄▀▄▀▄▀         █▀
█████████████████████▄▄▄▀▄█▄▄▀█▀▄████▀▄▀▄ ▄        █      ▄▄▄█
█████████████████████████▄▄▄▄▄▄███████▄▀▄▀                  ▀ ▀
█████████████████████████████████████▀▄▀▄▀▄

""")
            doDialogText("LONG AGO,# THE UNIVERSE WAS FILLED WITH LIGHT AND DARKNESS.")
            doDialogText("THE PERFECT BALANCE OF BRIGHT AND SHALLOW UNIFORMLY FILLED TILL EVERY CORNER.")
            doDialogText("WHEN,# People Started Dreaming.")
            printGraphic('''

███████████▄      ▄  █    ██▄      ▄    ▄               ▀
█████████████▄        ▀▄   ▀█▄    █ ▀▄           ▀           ▀
███████████████▄        ▀▄  ▀██▄  █  ▀▄   ▄▄         ▀
█████████████████▄     ▄ ▀▄   ▀█▄  ▀▄  ▀▀▀ █   ▀   ▄▀▄    ▄ ▀
███████████████████▄      ▀▄   ▀█▄   ▀▄▄▄▄▀   ▄     ▀          ▄
█████████████████████▄    ▄▀▄   ▀██          ▀▄▀         ▄
███████████████████████▄    ▀▄    ██▄     ▀     ▀   ▄▄
█████████████████████████▄   █    ████▄          █▄ ▀▀         ▄
███████████████████████████▄ █    ███████▄▄        ▀▀██▀▀   ▀
███████████████████████▀▀▀███▄  ▄████▀ ▀█████▄▄▄    ▄█ ▀▄▄     ▄
██████████████▀▀▀▀▀▀▀▀▄███▄▀████▀▀        ▀▀▀██████▄▄▄▄
███████████▀▄▄███████ ████ ██████▄                ▀▀▀▀██████▄▄▄▄▄
█████████▀▄█████████▀▄█▀▀▄█████████▄      ▄▄                  ▀▀▀
████████▀▄███████████▄▄██ ███████████▄   █  ▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄▄
████████ ███████████████▀▄█████████████▄ █                  ▀▀▀▄
████████ ███████████████ ████████████████▄        ▀             ▀
█████████ █████▀▀▄▄▄▄▄▄▄█▄ ▀▀▀█████████████▄
██████████▄▀█▀▄███▀█████▄▄████▄▀▀████████████▄         ▀
████████████ ▄██▄▄███████████████▄▀████████████▄           ▄
████████████ ██████████████████████▄▀████████████▄

''')
            doDialogText("AT NIGHT PEOPLE WOULD SLEEP,# HAVING THE WILDEST DREAMS.#.#.#")
            doDialogText("EACH ONE,# WHICH THEY WISHED WOULD COME TRUE.#.#.#")
            doDialogText("DREAMS WHICH PEOPLE CHASED,# TO EVERY CORNER OF THE UNIVERSE.")
            doDialogText("SOME DREAMS REACHABLE,# SOME DREAMS SEEMLINGLY UNATTAINABLE.#.#.#")
            doDialogText("HOWEVER,# ALL WERE TO EVENTUALLY COME TO TRUTH.### unless.#.#.#")
            printGraphic('''
                                    ▀▀▀▀▄▄▄▄▄
▀▀█▄▄▄▄▄▄▄▄▄                           ▄ █   ▀▀▄
           ▀▀▀▀▀▀▀█▄▄▄         ▄▄▀▀▀▄  ▀ ▄    ▄▀  ▄▄
                     ▀▀█▄    ▄▀      ▀▄▀   ▄▄▀     █▀▀▀▀▀▄
██▄▄▄▄                  ▀█▄  █        █  ▀▀▀▄▄▄▄▄▄▀       ▀▄
█████████▄▄▄              █   █       ▄█                    ▀▄▄
████████████████▄▄▄       █▄   ▀▄  ▄▄▀  ▀▀▄▄                   █
█████████████████████▄▄▄        ▄▀▀     ▄▄▄█▀▀▀▀▀▀▀█▄▄▄▄        █
██████████████████████████▄ ▄▄▄ ▀     █▀▀              ▀▀█▄▄▄▄
███████████████████████████ █████▀▀ ▄                        ▀▀█▄
████████████████████▀█▀████ ▀▀▀ ▄▄████████▄▄▄▄
██████▀ ▄▄▄▄ ████▀▄▀▄▀▄█ █▀▄▄████████████████████▄▄▄
██████ █████▄▀ ▄▄▀▄▀▄▀▀▄▀ ▄█████████████████████████████▄▄▄
██████ █████ ▄▀     █ █ █▀▀ ▀█▀▀▀█████████████████████████████▄▄▄
██▀▀▄▄█████▀ █            ▀█ ▄██▄▀███████████████████████████████
█ ▄█████████▄▀             █ █████▄▀█████████████████████████████
█▄▀██████████████▄▄▄▄▄▄▄▄▄▄▄ █████▀▄█████████████████████████████
██▄▄▀▀█████████▀████████████ █████ ▄▀▀███████████████████████████
█████▄▄ ▀▀█████▄▄ ▀▀▀▀▀▀▀▀▀▀ █████████▄▄▀████████████████████████
████████ ███████████████████████▀████████▄▀██████████████████████

''')
            doDialogText("DARKNESS STARTED SLEEPING INTO DREAMS,# TURNING ROT IN MINDS.#.#.#")
            doDialogText("REPLACING FAITH WITH HORROR,# UNLEASHING EVERYTHING WRONG POSSIBLE.#.#.#")
            doDialogText("ENCIRCLING NIGHTMARES.")
            doDialogText("TODAY,# WITH THE SHARP FORCE OF WILL,# ONE MUST BREAK INTO THE DARKNESS.#.#.#")
            doDialogText("AND FILL EVERYONE's DREAMS WITH ENLIGHTMENT.")
            doDialogText("BANISHING THE FORCE OF DARKNESS FROM PEOPLE'S LIFELINES.#.#.#")
            print()
            doDialogText("RESTORING BALANCE TO THE DARKNESS.")
            print()
            doDialogText("THE WORLD OF DREAMS.#.#.#")
            doDialogText("|#Lies in your hands.#|")

            printGraphic('''
                ▄▄▀    ▀█
                    █    ▀█
                    █▄
              ▄     ██
             █     ▄███
            ▀      █████▄        █
                 ▄█████████▄      ▀▀
▄▄█▀         ▄▄██████████████▄
      ▀█████████████████████████▄▄
          ▀▀███████████████████████▀▀██▄     ▀█▄▄
 ▀▄▄▄▄    ▄▄▄ ▀▀██████████████▀▀    ▄▄
      ▀▀▀    ▄▀   █████████▀▀         ▄█▀▀
       ██▄   ▀▄▄▄  ▀█████▀           ▀
      ▄              ███      █▄
      █     ▄ ▀▄      ▀   ▄█▀  █▄    █
      █▄▄▄▄ █  ▀▀     █    ▄    ██▄▄▄██
           █     ▀▀▀▀██▄▄▄▀▀█▀▀▀▄     █
           █          █     █   █      █
           █▄         █         █      █
            ▀▀▀▀▀▀    ▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀▀


▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀
█  ▀   ▄ █   █▄    ▄      ▄█    ▄█  ▄  ▄ █ ▄
█▄ █ ███ █▀█ █▄   ██ █▀▄ █▄█   █▄█ ██ █  █▀▄ ▄
      ▄█
▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀ 

''')
        elif music:
            endMusic = False
            startTime = time.time()

            playSong("assets/soundtrack/videogame.ogg")

            texts = 0
            while not endMusic:
                curTime = time.time() - startTime
                
                if texts == 0:
                    texts += 1
                    printGraphic("""
█████████████████████▀▄▀▄▀     ▀         ▄▄
████████████████▀███▄▀▄▀▄▀  ▄        ▄▄▀▀  █▄
███▀▄▄▀██████▀▄▄█▄▄▀▄▀██▄▀  ▄       █       ▀█▄       ██▄▄
██ ██▀▀▄██████▄▄▀▄▄███▄▀▄▀▄  ▀       ▀█▄   ▄█▀      ▀█████▀
██ ██ ████████████████████▄▀▄▀▄        ▀█▄█▀          ██
██ ███▄▀▀███▀██████▀████▄█▄▀▄▀ ▀         ▀            ▀█▄
██▄▀▀████▄▄▄█ ████▄▀▄████▀██▄▀▄▀▄                 ▄█▄  ██
█████▄▄ ▀▀▀▄▄█████████████▄▀▄▀▄                  ▀▀█▀▀  █
██████████████████████████▄▀█▀▄▀▄▀▄
█████████████████████████▀██▄█▄▀▄▀
█████▀▄▀█████████▀██████▄▀▄██▀█▀▄▀▄        ▄
██████▄█████████▄▀▄█████████████▄▀▄▀      ▀█▀▀             ▄
███████████████████████████████▀▄▀▄▀▄                    ▄███▄
████████████████████████████████▄█▄▀▄▀             ▄      ▀█▀
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀▀████▀▄▀▄           ▄█▄
██████████████████████████▀█▀██▄▄▄██▄▀▄▀          ███
████████████████████████▀▄▀▄█▀▄▀███▀▄▀▄▀▄▀         █▀
█████████████████████▄▄▄▀▄█▄▄▀█▀▄████▀▄▀▄ ▄        █      ▄▄▄█
█████████████████████████▄▄▄▄▄▄███████▄▀▄▀                  ▀ ▀
█████████████████████████████████████▀▄▀▄▀▄

""", step=75, afterdelay=0)
                    doDialogText(indep=True, spd=3, text="LONG AGO,# THE UNIVERSE WAS FILLED WITH LIGHT AND DARKNESS.")
                if texts == 1 and 4.3 < curTime:
                    texts += 1
                    doDialogText(indep=True, spd=3, text="THE PERFECT BALANCE OF BRIGHT AND SHALLOW UNIFORMLY FILLED TILL EVERY CORNER.")
                
                if texts == 2 and 9.3 < curTime:
                    texts += 1
                    doDialogText(indep=True, spd=3, text="WHEN,# People Started Dreaming.")
                    print()
                    printGraphic('''

███████████▄      ▄  █    ██▄      ▄    ▄               ▀
█████████████▄        ▀▄   ▀█▄    █ ▀▄           ▀           ▀
███████████████▄        ▀▄  ▀██▄  █  ▀▄   ▄▄         ▀
█████████████████▄     ▄ ▀▄   ▀█▄  ▀▄  ▀▀▀ █   ▀   ▄▀▄    ▄ ▀
███████████████████▄      ▀▄   ▀█▄   ▀▄▄▄▄▀   ▄     ▀          ▄
█████████████████████▄    ▄▀▄   ▀██          ▀▄▀         ▄
███████████████████████▄    ▀▄    ██▄     ▀     ▀   ▄▄
█████████████████████████▄   █    ████▄          █▄ ▀▀         ▄
███████████████████████████▄ █    ███████▄▄        ▀▀██▀▀   ▀
███████████████████████▀▀▀███▄  ▄████▀ ▀█████▄▄▄    ▄█ ▀▄▄     ▄
██████████████▀▀▀▀▀▀▀▀▄███▄▀████▀▀        ▀▀▀██████▄▄▄▄
███████████▀▄▄███████ ████ ██████▄                ▀▀▀▀██████▄▄▄▄▄
█████████▀▄█████████▀▄█▀▀▄█████████▄      ▄▄                  ▀▀▀
████████▀▄███████████▄▄██ ███████████▄   █  ▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄▄
████████ ███████████████▀▄█████████████▄ █                  ▀▀▀▄
████████ ███████████████ ████████████████▄        ▀             ▀
█████████ █████▀▀▄▄▄▄▄▄▄█▄ ▀▀▀█████████████▄
██████████▄▀█▀▄███▀█████▄▄████▄▀▀████████████▄         ▀
████████████ ▄██▄▄███████████████▄▀████████████▄           ▄
████████████ ██████████████████████▄▀████████████▄

''', step=75, afterdelay=0)
                    doDialogText(indep=True, spd=2, text="AT NIGHT PEOPLE WOULD SLEEP,# HAVING THE WILDEST DREAMS.#.#.#", afterdelay=0.3)
                    doDialogText(indep=True, spd=2, text="EACH ONE,# WHICH THEY WISHED WOULD COME TRUE.#.#.#", afterdelay=0.3)
                    doDialogText(indep=True, spd=2, text="DREAMS WHICH PEOPLE CHASED,# TO EVERY CORNER OF THE UNIVERSE.", afterdelay=0.3)
                    doDialogText(indep=True, spd=2, text="SOME DREAMS REACHABLE,# SOME DREAMS SEEMLINGLY UNATTAINABLE.#.#.#", afterdelay=0.3)
                    doDialogText(indep=True, spd=2, text="HOWEVER,# ALL WERE TO EVENTUALLY COME TO TRUTH.### unless.#.#.#", afterdelay=0.3)
                if texts == 3 and 24.0 < curTime:
                    texts += 1
                    print()
                    doDialogText(indep=True, spd=1.4, afterdelay=0.2, text="DARKNESS STARTED SLEEPING INTO DREAMS,# TURNING ROT IN MINDS.#.#.#")
                    printGraphic('''
                                    ▀▀▀▀▄▄▄▄▄
▀▀█▄▄▄▄▄▄▄▄▄                           ▄ █   ▀▀▄
           ▀▀▀▀▀▀▀█▄▄▄         ▄▄▀▀▀▄  ▀ ▄    ▄▀  ▄▄
                     ▀▀█▄    ▄▀      ▀▄▀   ▄▄▀     █▀▀▀▀▀▄
██▄▄▄▄                  ▀█▄  █        █  ▀▀▀▄▄▄▄▄▄▀       ▀▄
█████████▄▄▄              █   █       ▄█                    ▀▄▄
████████████████▄▄▄       █▄   ▀▄  ▄▄▀  ▀▀▄▄                   █
█████████████████████▄▄▄        ▄▀▀     ▄▄▄█▀▀▀▀▀▀▀█▄▄▄▄        █
██████████████████████████▄ ▄▄▄ ▀     █▀▀              ▀▀█▄▄▄▄
███████████████████████████ █████▀▀ ▄                        ▀▀█▄
████████████████████▀█▀████ ▀▀▀ ▄▄████████▄▄▄▄
██████▀ ▄▄▄▄ ████▀▄▀▄▀▄█ █▀▄▄████████████████████▄▄▄
██████ █████▄▀ ▄▄▀▄▀▄▀▀▄▀ ▄█████████████████████████████▄▄▄
██████ █████ ▄▀     █ █ █▀▀ ▀█▀▀▀█████████████████████████████▄▄▄
██▀▀▄▄█████▀ █            ▀█ ▄██▄▀███████████████████████████████
█ ▄█████████▄▀             █ █████▄▀█████████████████████████████
█▄▀██████████████▄▄▄▄▄▄▄▄▄▄▄ █████▀▄█████████████████████████████
██▄▄▀▀█████████▀████████████ █████ ▄▀▀███████████████████████████
█████▄▄ ▀▀█████▄▄ ▀▀▀▀▀▀▀▀▀▀ █████████▄▄▀████████████████████████
████████ ███████████████████████▀████████▄▀██████████████████████

''', step=75, afterdelay=0)
                    doDialogText(indep=True, spd=1.2, afterdelay=0.37, text="REPLACING FAITH WITH HORROR,# UNLEASHING EVERYTHING WRONG POSSIBLE.#.#.#")
                    doDialogText(indep=True, spd=1.2, afterdelay=0.37, text="ENCIRCLING NIGHTMARES.")
                    doDialogText(indep=True, spd=1.2, afterdelay=0.37, text="TODAY,# WITH THE SHARP FORCE OF WILL,# ONE MUST BREAK INTO THE DARKNESS.#.#.#")
                    doDialogText(indep=True, spd=1.2, afterdelay=0.37, text="AND FILL EVERYONE's DREAMS WITH ENLIGHTMENT.")
                    doDialogText(indep=True, spd=1.2, afterdelay=0.37, text="BANISHING THE FORCE OF DARKNESS FROM PEOPLE'S LIFELINES.#.#.#")
                
                if texts == 4 and 35 < curTime:
                    texts += 1
                    print()
                    doDialogText(indep=True, spd=3, text="RESTORING BALANCE TO THE DARKNESS.")
                
                if texts == 5 and 38.8 < curTime:
                    texts += 1
                    print()
                    doDialogText(indep=True, spd=3, text="THE WORLD OF DREAMS.#.#.#")
                    doDialogText(indep=True, spd=3, text="|#Lies in your hands.#|")
        
                    printGraphic('''
                ▄▄▀    ▀█
                    █    ▀█
                    █▄
              ▄     ██
             █     ▄███
            ▀      █████▄        █
                 ▄█████████▄      ▀▀
▄▄█▀         ▄▄██████████████▄
      ▀█████████████████████████▄▄
          ▀▀███████████████████████▀▀██▄     ▀█▄▄
 ▀▄▄▄▄    ▄▄▄ ▀▀██████████████▀▀    ▄▄
      ▀▀▀    ▄▀   █████████▀▀         ▄█▀▀
       ██▄   ▀▄▄▄  ▀█████▀           ▀
      ▄              ███      █▄
      █     ▄ ▀▄      ▀   ▄█▀  █▄    █
      █▄▄▄▄ █  ▀▀     █    ▄    ██▄▄▄██
           █     ▀▀▀▀██▄▄▄▀▀█▀▀▀▄     █
           █          █     █   █      █
           █▄         █         █      █
            ▀▀▀▀▀▀    ▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀▀


▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀
█  ▀   ▄ █   █▄    ▄      ▄█    ▄█  ▄  ▄ █ ▄
█▄ █ ███ █▀█ █▄   ██ █▀▄ █▄█   █▄█ ██ █  █▀▄ ▄
      ▄█
▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀   ▀▀▀▀▀▀ 

''', step=45)
                    break
    
    def doDarkIntro(music=True):
        if not music:
            printGraphic('''
            ████                       █▄█▀▀
            ████                       █
            ████        ▄█▄     ▄▄▄█▀▀▀   ▄
            ▀███         ▀   ▄▀▀▀      ▀███
             ████          ▄▄▀          ▀▀▀██
              ███          █                ▀▀
               ███         █▄▄               █
               ████           ▀▀▀▀▄▄▄▄▄▄▄▄     ▀▀
               ████                      ▀▀▀▀██▄▄        ▄▄▄▀▀█▄▄
              ▄███▀     ▄                      ██▄▄▄▄▄▄▀▀
              ███▀    ▀▀█▀                     ████
             ███▀                               ███▄
            ████           ▄▄██████▄            ▀███
           ▄███▀          ▄██████████            ███
           ███            ██▀▀▀▀▀▀▀██            ███
▄          ███     ▄█▄    █         █            ██▀
█          ███      ▀     █           ▄         ███
▄▄▄▄▄▄      ███            ▀▄▄▄▄▄▄█    █        ██▀▄▄▄▄▀▀
      ▀▀▀▄  ███▄          █   ▀        ▄       ███
         ▀▄▄▀▀██▄            ▄      █  ▀      ▄██▀
              ▀██▄▄       █  ▀                ███
                ███▄      ▀             ▄     ███
                ████    ▄       ▀   ▀   ▀ ▄   ███▄
▄         ▄▄▄▄ ▄████   ▀▄   █   ▀▄   █   ▄▀   ████▄
▀         ▀▀▀▀ ████      ▄▄            ▀      ▀███▀▄▄▄▄▄▄
         ▄▀▀▀▀▀████                            ███    ▄
        █       ███▄                            ▀     █
    ▄▄▀▀▀▄       ▀▀█▀                              ▄██▀
 ▄▀▀▀    ▀█▄                                      ▀▀
▀▀        ▀█▄▄
            ▀▀▀▀
''')
            doDialogText("A dark figure is seen within the FOUNTAIN.")
            if route4['on_weirdRoute']: doDialogText("YOUR SENSES HEIGHTEN DRAMATICALLY.###.", spd=5, step=2)
            else: doDialogText("YOUR SENSES ARE DULLED BY THE DARKNESS.", spd=5, step=2)
            printGraphic('''
                                                               ▄█
                                                               ██
                                                    ▄          ██
                                                    ▀         ███
               ▀                                    ▄        ████
                    ▀                                        ████
▄              ▀                                             ████
█                         ▄███████▄▄▄            ▀▀    ▀▀    ████
██▄                     ▄█▀▀▀▀▀▀▀▀▀▀████▄▄                   ████
███                   ▄█▀             ▀▀███                   ███
████▄                ▄█▀                 ▀██        ▄         ███
█████▄              ██▀                    ██       ▀          ██
██████             ██▀                     ██                  ██
███████            ██                      ██                   █
███████▄           ██                      █▀                   █
████████           ██               ▄      █                    ▀
████████           ██▄             ▀▄▀    ▄█
████████           ▀██                    ██
███████             ▀██                   █               ▄
██████▀              ▀██                  █
██████                 ▀█               ▄▀                   ▀▀
█████                   ▀█▄                                ▀
████▀                     █                ▀▀▀▄▄▄▄▄▄▄▄▄▄ ▄
████                    ▄▄▀                              █
██▀     █             ▄██▀                              █
▀       ▀          ▄▄█▀                                 █
                 ▄█▀▀                                  █
         ▄▄    ▄██        ▄                           ▄▀
  ▀▀          ███▀       ▄▀                           █
              ██▀       █▀                           ▄▀
       █      ██        █▄                           ▀▄
             ██▀                                      ▀█
             ▀▀                                        ▀▀


''')
            printGraphic('''  ██████▄ ▀▄▄        ▄ ▄▄▄  ▀
  ▀██████     ▄      ▀                                ▄  ▀  ▀
   ███████   ▄        ▄▀▄▄                             ▀
   ███████   ▀   ▄    ▀  ▀▀                 ▄▄▄▄▄       ▀▀▄
  ████████   ▄     █     ▄▄▄▄▄▄          ▄██████████▄▄    █
  ████████           ▄▄██▀▀▀▀▀▀█▄      ▄██████▀▀▀    ▀▄  ▀
 ▄███████▀          █▀          █     ▄███▀           ▀▄ ▄
 ████████          █▀           █    ▄██▀              █   ▀    ▀
█████████          █▄          ██    ██▀               █   ▄    ▄
█████████           █▄        ██▀    █                 █   ▄   ▀
████████             █▄       ██     █                ▄▀      ▄
████▀▀▀ ▄▄▄▄▄▄▄      ▀█▄      ██     █                █      ▀
█▀ ▄▄████▀▀▀▀▀▀████▄  ▀█▄      ▀█    ▀█▄             █▀
 ▄███▀             ▀▀▀███▄      █▄     ▀█           ▄█
████           ▀█        ▀       █  ▄██ ▀▀█▄        █
██▀       ▄      █               ▀▀▀   ▀▀██          ██▄▄
██      ▄███▀    █                ▄        ▀            ▀▀▀▀█
██        ▀      ▀                 █                       ▄█
███▄                 ▄█            █                       █
 ▀███▄             ▄▄█▀                                   █▀
█▄  ▀██▄▄▄██▀▀▀▀▀▀▀▀               ▄█                     █
██     ▀▀▀██                    ▄▄█▀   ▄                  █
██        ██            ▀      █▀      █                  █
███▄      ▀█▄       ▄▄   ▄    ▄█       █                ▄ █▄
███▀       ▀▀██▄▄▄█▀▀   ██  ▄▄█        ██               █  █
███          █         ▄█▀▀▀            █               █   █
███          ▀█▄▄▄▄█▀▀▀▀                █               █   █
███▄                                    █               ▀▄  █
████                    ▄               █                █  ▀▄▄
█████                  ██              ▄█                ▀▄   █
█████            ▄█▀  █▀ █  ▄▄▄       █▀                  █   █
█████▄             █         ▄        █          ▄        █▄▀▀▀
▀▀▀▀▀▀▀             ▀       ▀▀        ▀          ▀▀       ▀

''')
            printGraphic('''
                                                   ▄▄      ▄
                               ▄▄█████████████▄    ▀       ▀█
     █                    ▄▄██████▀▀▀▀▀▀▀▀██████▄           █▄
    ▄▀       ▀█        ▄▄███▀▀▀              ▀███▄     █
   ▀▀  ▄      ▀▄    ▄████▀▀                     ▀██    ▀
      █▀        ▀ ▄███▀▀                          ▀█▄      ▄▀
      ▀         ▄████▀                             ██▄     █
   █           ▄████                               ███     █
   █           ███▀                                 ██     ▀
  ▄▀          ███▀                                   █▄
  █          ▄██▀                      ▄             ██
             ███                       █             ██
            ▄██                        █              ██
            ██                         █              ██     █
            █▀                         █              ███     █
            █                      ▄▄▄ ▄ ▄▄▄          ███     █
    ▄      █                           ▄                ██     █
   █▀      █                           █               ██     █
   █       █                           █               ██     █
   █       ▀█                          ▀               ██     ▀
            █▄                                         ██
             █                                        ██▀
             ▀█                                       █▀   ▄
               █▄                                    █▀     █
                ▀▄                                  █▀      █
                  ▀▄                               █▀       ▀█
              ▄▄▄██▀                             ▄█▀
      ▄▄▄▄▄███▀▀▀            ▄▄▄▄         ▄  ▄    █▄▄▄▄▄
▄▄▄█████▀▀▀▀                        ▀                ▀▀▀▀███▄▄▄
████▀                                                     ▀▀███▄
▀                                                            ████
                                                              ▀▀▀

''')
        else:
            initTime = time.time()

            texts = 0
            playSong("assets/soundtrack/darkfight.ogg", looping=True)
            while True:
                curTime = time.time() - initTime

                if texts == 0:
                    printGraphic('''
            ████                       █▄█▀▀
            ████                       █
            ████        ▄█▄     ▄▄▄█▀▀▀   ▄
            ▀███         ▀   ▄▀▀▀      ▀███
             ████          ▄▄▀          ▀▀▀██
              ███          █                ▀▀
               ███         █▄▄               █
               ████           ▀▀▀▀▄▄▄▄▄▄▄▄     ▀▀
               ████                      ▀▀▀▀██▄▄        ▄▄▄▀▀█▄▄
              ▄███▀     ▄                      ██▄▄▄▄▄▄▀▀
              ███▀    ▀▀█▀                     ████
             ███▀                               ███▄
            ████           ▄▄██████▄            ▀███
           ▄███▀          ▄██████████            ███
           ███            ██▀▀▀▀▀▀▀██            ███
▄          ███     ▄█▄    █         █            ██▀
█          ███      ▀     █           ▄         ███
▄▄▄▄▄▄      ███            ▀▄▄▄▄▄▄█    █        ██▀▄▄▄▄▀▀
      ▀▀▀▄  ███▄          █   ▀        ▄       ███
         ▀▄▄▀▀██▄            ▄      █  ▀      ▄██▀
              ▀██▄▄       █  ▀                ███
                ███▄      ▀             ▄     ███
                ████    ▄       ▀   ▀   ▀ ▄   ███▄
▄         ▄▄▄▄ ▄████   ▀▄   █   ▀▄   █   ▄▀   ████▄
▀         ▀▀▀▀ ████      ▄▄            ▀      ▀███▀▄▄▄▄▄▄
         ▄▀▀▀▀▀████                            ███    ▄
        █       ███▄                            ▀     █
    ▄▄▀▀▀▄       ▀▀█▀                              ▄██▀
 ▄▀▀▀    ▀█▄                                      ▀▀
▀▀        ▀█▄▄
            ▀▀▀▀
''', afterdelay=0)
                    doDialogText("A dark figure is seen within the FOUNTAIN.", indep=True)
                    if route4['on_weirdRoute']: doDialogText("YOUR SENSES HEIGHTEN DRAMATICALLY.###.", spd=5, step=2, indep=True)
                    else: doDialogText("YOUR SENSES ARE DULLED BY THE DARKNESS.", spd=5, step=2, indep=True)
                    texts += 1
                
                if texts == 1 and 8.85 < curTime:
                    texts += 1
                    printGraphic('''

                                                               ▄█
                                                               ██
                                                    ▄          ██
                                                    ▀         ███
               ▀                                    ▄        ████
                    ▀                                        ████
▄              ▀                                             ████
█                         ▄███████▄▄▄            ▀▀    ▀▀    ████
██▄                     ▄█▀▀▀▀▀▀▀▀▀▀████▄▄                   ████
███                   ▄█▀             ▀▀███                   ███
████▄                ▄█▀                 ▀██        ▄         ███
█████▄              ██▀                    ██       ▀          ██
██████             ██▀                     ██                  ██
███████            ██                      ██                   █
███████▄           ██                      █▀                   █
████████           ██               ▄      █                    ▀
████████           ██▄             ▀▄▀    ▄█
████████           ▀██                    ██
███████             ▀██                   █               ▄
██████▀              ▀██                  █
██████                 ▀█               ▄▀                   ▀▀
█████                   ▀█▄                                ▀
████▀                     █                ▀▀▀▄▄▄▄▄▄▄▄▄▄ ▄
████                    ▄▄▀                              █
██▀     █             ▄██▀                              █
▀       ▀          ▄▄█▀                                 █
                 ▄█▀▀                                  █
         ▄▄    ▄██        ▄                           ▄▀
  ▀▀          ███▀       ▄▀                           █
              ██▀       █▀                           ▄▀
       █      ██        █▄                           ▀▄
             ██▀                                      ▀█
             ▀▀                                        ▀▀


''', afterdelay=0)
                    
                if texts == 2 and 13.3 < curTime:
                    texts += 1
                    printGraphic('''  ██████▄ ▀▄▄        ▄ ▄▄▄  ▀
  ▀██████     ▄      ▀                                ▄  ▀  ▀
   ███████   ▄        ▄▀▄▄                             ▀
   ███████   ▀   ▄    ▀  ▀▀                 ▄▄▄▄▄       ▀▀▄
  ████████   ▄     █     ▄▄▄▄▄▄          ▄██████████▄▄    █
  ████████           ▄▄██▀▀▀▀▀▀█▄      ▄██████▀▀▀    ▀▄  ▀
 ▄███████▀          █▀          █     ▄███▀           ▀▄ ▄
 ████████          █▀           █    ▄██▀              █   ▀    ▀
█████████          █▄          ██    ██▀               █   ▄    ▄
█████████           █▄        ██▀    █                 █   ▄   ▀
████████             █▄       ██     █                ▄▀      ▄
████▀▀▀ ▄▄▄▄▄▄▄      ▀█▄      ██     █                █      ▀
█▀ ▄▄████▀▀▀▀▀▀████▄  ▀█▄      ▀█    ▀█▄             █▀
 ▄███▀             ▀▀▀███▄      █▄     ▀█           ▄█
████           ▀█        ▀       █  ▄██ ▀▀█▄        █
██▀       ▄      █               ▀▀▀   ▀▀██          ██▄▄
██      ▄███▀    █                ▄        ▀            ▀▀▀▀█
██        ▀      ▀                 █                       ▄█
███▄                 ▄█            █                       █
 ▀███▄             ▄▄█▀                                   █▀
█▄  ▀██▄▄▄██▀▀▀▀▀▀▀▀               ▄█                     █
██     ▀▀▀██                    ▄▄█▀   ▄                  █
██        ██            ▀      █▀      █                  █
███▄      ▀█▄       ▄▄   ▄    ▄█       █                ▄ █▄
███▀       ▀▀██▄▄▄█▀▀   ██  ▄▄█        ██               █  █
███          █         ▄█▀▀▀            █               █   █
███          ▀█▄▄▄▄█▀▀▀▀                █               █   █
███▄                                    █               ▀▄  █
████                    ▄               █                █  ▀▄▄
█████                  ██              ▄█                ▀▄   █
█████            ▄█▀  █▀ █  ▄▄▄       █▀                  █   █
█████▄             █         ▄        █          ▄        █▄▀▀▀
▀▀▀▀▀▀▀             ▀       ▀▀        ▀          ▀▀       ▀

''', afterdelay=0)
                if texts == 3 and 15.5 < curTime:
                    texts += 1
                    printGraphic('''
                                                   ▄▄      ▄
                               ▄▄█████████████▄    ▀       ▀█
     █                    ▄▄██████▀▀▀▀▀▀▀▀██████▄           █▄
    ▄▀       ▀█        ▄▄███▀▀▀              ▀███▄     █
   ▀▀  ▄      ▀▄    ▄████▀▀                     ▀██    ▀
      █▀        ▀ ▄███▀▀                          ▀█▄      ▄▀
      ▀         ▄████▀                             ██▄     █
   █           ▄████                               ███     █
   █           ███▀                                 ██     ▀
  ▄▀          ███▀                                   █▄
  █          ▄██▀                      ▄             ██
             ███                       █             ██
            ▄██                        █              ██
            ██                         █              ██     █
            █▀                         █              ███     █
            █                      ▄▄▄ ▄ ▄▄▄          ███     █
    ▄      █                           ▄                ██     █
   █▀      █                           █               ██     █
   █       █                           █               ██     █
   █       ▀█                          ▀               ██     ▀
            █▄                                         ██
             █                                        ██▀
             ▀█                                       █▀   ▄
               █▄                                    █▀     █
                ▀▄                                  █▀      █
                  ▀▄                               █▀       ▀█
              ▄▄▄██▀                             ▄█▀
      ▄▄▄▄▄███▀▀▀            ▄▄▄▄         ▄  ▄    █▄▄▄▄▄
▄▄▄█████▀▀▀▀                        ▀                ▀▀▀▀███▄▄▄
████▀                                                     ▀▀███▄
▀                                                            ████
                                                              ▀▀▀

''', afterdelay=0, step=90)
                if texts == 4 and 17.1 < curTime:
                    break
    
    def doCreditsSequence(music=True):
        if not music:
            doDialogText("ADVIL:# yooo anyone wanna play deadshot?", step=99)
            doDialogText("SIBIN:# Bro its 2AM only I am here.", step=99)
            doDialogText("ADVIL:# you wanna play deadshot?", step=99)
            doDialogText("SIBIN:# sure, Im here anyways. What's the code?", step=99, afterdelay=3)
            doDialogText("ADVIL:# WBISKW.", spd=6,  step=2)
            print()
            printGraphic('''
 
     ▄▄
    ████▄                                              ██▄  ▄█▄
   ▄██ ██     ▄                            ▄     ▄▄    ████████
  ▄██▄▄▄██   ▄██   ▄███ █ █▄ ▀█▀ ▄███ █ █▄ ██ ▄█ ███   █████▀██
 ▄██▀▀▀▀███  ████  ██▄▄ ████  █  ██▄▄ ████ ████  ███   ██ ▀▀ ██
 ███    ███ ██  █▄ ▄▄▄█ █ ██ ▄██ ▄▄▄█ █ ██ ██ █▄ █ ▀█ ██▀    ██


''')
            doDialogText("A GAME BY SIDDHARTH A.")
            print()

            doDialogText("STARRING:# ASHISH and DEVAGIRI HIGH TEAM")
            print()

            doDialogText("SPECIAL THANKS TO:# Aravind M,# for assisting with supplementary coding.")
            print()

            doDialogText("HEAVY INSPIRATIONS FROM: DELTARUNE by TOBY FOX.")
            print()

            doDialogText("AASHISHKAM.")
            print()

            doDialogText("The BLUE MOON remains.")
            print()

            doDialogText("To be continued.#.#.#")
            print()
        else:
            doDialogText("ADVIL:# yooo anyone wanna play deadshot?", indep=True, afterdelay=1.5)
            doDialogText("SIBIN:# Bro its 2AM only I am here.", indep=True, afterdelay=1.5)
            doDialogText("ADVIL:# you wanna play deadshot?", indep=True, afterdelay=1.5)

            doDialogText("SIBIN:# sure, Im here anyways. What's the code?", afterdelay=1, indep=True)
            playSong("assets/soundtrack/lokahbanger.ogg")
            startTime = time.time()

            doDialogText("ADVIL:# ", indep=True, line=False, afterdelay=0)

            texts = 0
            while True:
                curTime = time.time() - startTime
                
                if texts == 0 and 2.4 < curTime:
                    doDialogText("WBISKW.", spd=8,  step=2, indep=True, afterdelay=0)
                    texts += 1

                if texts == 1 and 4.3 < curTime:
                    texts += 1
                    printGraphic('''
 
     ▄▄
    ████▄                                              ██▄  ▄█▄
   ▄██ ██     ▄                            ▄     ▄▄    ████████
  ▄██▄▄▄██   ▄██   ▄███ █ █▄ ▀█▀ ▄███ █ █▄ ██ ▄█ ███   █████▀██
 ▄██▀▀▀▀███  ████  ██▄▄ ████  █  ██▄▄ ████ ████  ███   ██ ▀▀ ██
 ███    ███ ██  █▄ ▄▄▄█ █ ██ ▄██ ▄▄▄█ █ ██ ██ █▄ █ ▀█ ██▀    ██


''', afterdelay=0, step=25)
                
                if texts == 2 and 5.8 < curTime:
                    print()
                    time.sleep(0.04)
                    print("A GAME BY: Siddharth A.")
                    texts += 1

                elif texts == 3 and 7.7 < curTime:
                    print()
                    time.sleep(0.04)
                    print("STARRING: ASHISH and DEVAGIRI HIGH TEAM.")
                    texts += 1
                
                elif texts == 4 and 10.4 < curTime:
                    print()
                    time.sleep(0.04)
                    print("SPECIAL THANKS TO: Aravind M, for assisting with supplementary coding.")
                    texts += 1

                elif texts == 5 and 13.0 < curTime:
                    print()
                    time.sleep(0.04)
                    print("HEAVY INSPIRATIONS FROM: DELTARUNE by TOBY FOX.")
                    texts += 1
                
                elif texts == 6 and 15.6 < curTime:
                    print()
                    time.sleep(0.04)
                    print("AASHISHKAM.")
                    texts += 1
                
                elif texts == 7 and 18.2 < curTime:
                    print()
                    time.sleep(0.04)
                    print("The BLUE MOON remains.")
                    texts += 1
                
                elif texts == 8 and 20.8 < curTime:
                    print()
                    time.sleep(0.04)
                    doDialogText("The mystery continues...", indep=True)
                    texts += 1
                
                elif texts == 9 and 26.6 < curTime:
                    print()
                    time.sleep(0.04)
                    doDialogText("Thanks for playing.", indep=True)
                    texts += 1
                
                elif curTime > 31.3: break

            



                


    player = {
        "attack": 10,
        "defense": 10,
        "hp": 15,
        "lv": 1,
        "weapon": "HARDCOVER AXE",
        "armor": "NIL"
    }
    ashish = {
        "attack": 6,
        "defense": 8,
        "hp": 15,
        "lv": 1,
        "weapon": "PAPYRUS SWORD",
        "armor": "HARDCOVER SHIELD",
        "spells": ["HEALING SONG"]
    }
    knight = {
        "attack": 12,
        "defense": 10,
        "hp": 20,
        "lv": 1,
        "weapon": "TWISTED SWORD",
        "armor": "ICE SHEATH",
    }
    flowery = {
        "attack": 12,
        "defense": 10,
        "hp": 20,
        "lv": 1,
        "spells": ["PHOTOSYNTHESIS"],
        "weapon": "VINE WHIP",
        "armor": "SAND BAG"
    }

    if "players" in saveFile['route4']:
        if saveFile['route4']['players'] != []:
            player = saveFile['route4']['players'][0]
            ashish = saveFile['route4']['players'][1]
            knight = saveFile['route4']['players'][2]
            flowery = saveFile['route4']['players'][3]
    


    startindex = 1


    # Some save files might not have this key, soo fixing that
    if "startIndex" in saveFile['route4']: startindex = saveFile['route4']['startIndex']

    if saveFile['route4']['COMPLETED'] == True:
        pass #startindex = doDialogChoice("Where would you like to start from?", choices=["The Beginning..", "After EDWIN's battle.", "After the Inn."]) - 1

    doDialogText("WARNING:# This is a rushed chapter.# Beware of bugs.")

    if startindex == 0:

        player = {
            "attack": 10,
            "defense": 10,
            "hp": 15,
            "lv": 1,
            "weapon": "HARDCOVER AXE",
            "armor": "NIL"
        }
        ashish = {
            "attack": 6,
            "defense": 8,
            "hp": 15,
            "lv": 1,
            "weapon": "PAPYRUS SWORD",
            "armor": "HARDCOVER SHIELD",
            "spells": ["HEALING SONG"]
        }
        knight = {
            "attack": 12,
            "defense": 10,
            "hp": 20,
            "lv": 1,
            "weapon": "TWISTED SWORD",
            "armor": "ICE SHEATH",
        }
        flowery = {
            "attack": 12,
            "defense": 10,
            "hp": 20,
            "lv": 1,
            "spells": ["PHOTOSYNTHESIS"],
            "weapon": "VINE WHIP",
            "armor": "SAND BAG"
        }

        money = 0
        inventory = []

        # DARK WORLD CREATED BY ASHISH'S SISTER:
        if saveFile['route3']['rude_stay'] != "UNFORGIVED":
            doDialogText(".#.#.#")
            doDialogText("You see a BLADE in the hands of the shadowy figure.")
            doDialogText("(Adithya.#.#.#?)")
            doDialogText("(No.# The figure is taller.)")
            doDialogText("The figure walks into the middle of the room.")
            doDialogText("It looks at the static screensaver on the computer.")
            doDialogText("It's logging into the computer?")
            doDialogText("(What is it doing on the computer.#.#.)")
            doDialogText("It opened something.#.#.")
            doDialogText("|| TURN ||", spd=1)
            doDialogText("(####It's looking at me.# Quick! Pretend to be asleep.)")
            doDialogText("You can hear it walking over to you.")
            doDialogText("In the shining moonlight,# you could see it's blade reflect.#.#.")
            doDialogText("It rises it's BLADE into the air.")
            doDialogText("(Is this.#.#.# the end for me?")
            doDialogText("The figure gets ready to stab-")
            doDialogText("But right now,# you feel nothing but a cold sensation slowly crossing your skin.")
            doDialogText("You feel.#.#.# sleepy.")
            doDialogText("You start to see the light.#.#.# but it fades away.")
            doDialogText(".#.#.##.##.###.", afterdelay=3)
            print()

            # ENTRY INTO DARK WORLD
            doDialogText("It's cold.")
            doDialogText("You open your eyes.# You're in a white snowing deserted area,# and the sky is dark.")
            doDialogText("It feels.#.#.# cold.")
            doDialogText("(Am I dreaming?)")
            doDialogText("!# You spot ASHISH lying beside you,# visibly asleep.")
            doDialogText("YOU:# Hey,# ASHISH!")

            if nameChoice == "NORMAL" or nameChoice == "RUDE":
                doDialogText("ASHISH:# .#.#.# hey.#.#.# what time is it?")
                doDialogText("YOU: Ashish,# look around us.# Where are we?")
                doDialogText("ASHISH:# .#.#.######## Wait.#.#.# this isn't home.")
                doDialogText("YOU:# What happened?# Am I dreaming?")
                doDialogText("ASHISH:# I don't know.# Maybe I'm also dreaming.")
                print("        ", end="")
                doDialogText("Pinch me!")
                doDialogText("YOU:# U-#huh?")
                doDialogText("ASHISH:# I-#I mean...# uhh...# FORGET IT!")
                doDialogText("Ashish pinches himself.")
                doDialogText("ASHISH:# OWOWOW okay this is not a dream.")
                doDialogText("YOU:# Then where are we,# how did we get here?")

            # KNIGHT ENTRY
            doDialogText("KNIGHT: Don't worry,# I may know a way back.")
            doDialogText("YOU:# Oh thanks!", afterdelay=5)
            print(end="     ")
            doDialogText("wait a minute who are you?", spd=2)
            doDialogText("A tall lady,# covered in metal,# with streaks of hair sneaking through her helmet stands before you.")
            doDialogText("KNIGHT:# Call me.#.#.# the KNIGHT.")
            doDialogText("ASHISH:# Uhm,# Mr or Ms Knight?# Do you know where we are?")
            doDialogText("KNIGHT:# You're on the outskirts of the this world.# Beyond the edge,# there is nothing but infinite snowy land.#.#.#")
            print(end="        ")
            doDialogText("Vast lands that are yet waiting to be conquered by a worthy leader.")
            doDialogText("YOU:# .#.#.# are we no longer on earth?")
            doDialogText("KNIGHT:# No,# this is still EARTH,# but,# you're in another world now.# a DARK world,# if I may add.")
            doDialogText("YOU:# A Dark world?")
            doDialogText("KNIGHT:# Yes.# A DARK world is a world created out of nothing but darkness,# created by anyone with a will or vision trapped in the darkness of their own thoughts,# imagining and imagining until the world around you starts to change,# and shift,# and eventually mold into your desires.")
            doDialogText("or when someone's having a really, really bad dream.")
            print(end="        ")
            doDialogText("This Dark world belongs to someone else,# who is suffering from,# perhaps,# severe disbelief,# and you've been trapped in it.")
            doDialogText("YOU:# Uh huh.#.#.#")
            doDialogText("KNIGHT:# Follow me.# I'll guide you through your journey.")
            print(end="        ")
            doDialogText("oh,# and by the way,# i'm a ms.knight")
            doDialogText("ASHISH: ok..")
            print()
            doDialogText("You and Ashish start following the knight into a direction that seemingly leads to nowhere.")
            doDialogText("The more you walk,# the more infinite the world seems.")
            doDialogText("Until.#.#.# you start to see buildings.#.#.# but,##")
            doDialogText("The buildings are shaped like bookshelves?")
            doDialogText("As you walk closer,# the buildings really do resemble bookshelves,# full of fat books.")
            doDialogText("YOU:# What's that?# Those buildings are shaped like.#.#.# bookshelves.")
            doDialogText("KNIGHT:# You're right,# these buildings are modeled after bookshelves.")
            print(end="        ")
            doDialogText("Keep following me.")
            doDialogText("You keep following the knight.")
            doDialogText("ASHISH:# Is that.#.#.#")

            # LIBRARY n CENGAGE
            doDialogText("KNIGHT:# Welcome,# to LIBRARY!# Despite it's name,# Library is actually a humble town modeled after an actual library.")
            doDialogText("ASHISH:# Is that my CENGAGE book?")
            doDialogText("KNIGHT:# Probably. Maybe this is your bedroom,# ASHISH.")
            doDialogText("ASHISH:# Woah.#.#.# Why is it so big tho?")
            doDialogText("KNIGHT:# Wanna head there?")
            doDialogText(f"ASHISH:# {saveFile['name']},# wanna go there?")
            doDialogText("YOU:# Sure,# but I think that's too big to be an actual book.")
            doDialogText("The team heads over to Ashish's really big CENGAGE book.# It's fixed on the top of a building.")
            doDialogText("KNIGHT:# Looks like we're gonna have to head to the top.# Come on in,# guys.")
            doDialogText("You head into the building to find what resembles a Lobby.# You enter an elevator,# and head to the 12th floor.") 
            doDialogText('The sign reads "FLOOR 12:# CENGAGE Materials: Exam Crack".')
            doDialogText("The elevator door finally opens,# and.#.#.#")
            doDialogText("ASHISH:# Is this my CENGAGE book?")
            doDialogText("JOHN CENGAGE:# Hello ASHISH!# Which problems would you like to solve today?")
            doDialogText("ASHISH:# Ooh lemme see.#.#.#")
            doDialogText("(Damn.# I could never touch a book as fat as that.)")
            doDialogText("ASHISH:# .#.#.# these questions are genius!")
            doDialogText("YOU:# Huh?# Lemme see")
            doDialogText("You look into the book.# Your head melts from how complex these questions are.")
            doDialogText("ASHISH:# But what are these questions about?# Something about light and dark.#.#.#")
            doDialogText("KNIGHT:# That's probably because we're in the dark world.# Hm,# maybe the Dark world also wanted to implement some questions into it?")
            print(end='        ')
            doDialogText("Though,# I wasn't expecting the CENGAGE to hold actual questions to appear in someone's dreams as well.#.#.#")
            doDialogText("ASHISH:# Wait,# if this is someone's dream,# then why is my room here?")
            doDialogText(f"KNIGHT:# This is also your dream as well,# Ashish and {saveFile['name']}.# Maybe it's conflicting with someone else.")
            doDialogText("YOU:# So this IS a dream?")
            doDialogText("KNIGHT:# Not quite.# Think of it as a temporary but real manifestation of your dream.# It's not exactly a dream,# but more like a seperate dimension.")
            doDialogText("ASHISH:# How do you know this?")
            doDialogText("KNIGHT:# Well,# I am a darkner.# Us Darkners are part of the Dark world itself.# Some objects in the dark world can turn into living creatures.# So we just.#.#.# know everything.")
            doDialogText("ASHISH:# Ohhh,# makes sense.")
            doDialogText("KNIGHT:# Well,# JOHN CENGAGE,# can you give these kids some weapons to defend themselves?")
            doDialogText("JOHN CENGAGE:# Depends on if you have money.")
            doDialogText("KNIGHT:# Here take this,# I'll have that.")
            doDialogText("ASHISH GOT PAPYRUS SWORD AND HARDCOVER SHIELD.", step=2, spd=4)
            doDialogText("YOU GOT AN HARDCOVER AXE AND ELECTRIC GLOVES.", step=2, spd=4)
            doDialogText("KNIGHT:# Sorry,# I didn't have enough to get you a shield.")

            # KEYCHAIN LOCKET
            if saveFile["route2"]["house_roomChoice"] == "CLEANED":
                doDialogText("YOU:# Oh,# that's alright,# I already got a cool axe and some gloves.# Thanks for buying these for us-", afterdelay=0.3)
                doDialogText("Something resonates within your pockets.#.#.#")
                doDialogText("Its your keychain!# It's now.#.#.# a locket?")
                doDialogText("KNIGHT:# Oh,# you brought something of your own?")
                doDialogText("YOU:# I-# What is my keychain doing here?")
                doDialogText("KNIGHT:# The dark world shifted your keychain into a locket.# Try it on!")
                doDialogText("YOU:# Okay.")
                doDialogText("You put on your keychain locket.# You feel tougher now.")
                doDialogText("YOUR DEFENSE RAISED FROM 10 TO 12.", step=2, spd=4)
                doDialogText("YOU:# Oh nice,# I feel tougher now.")
                inventory += ["KEYCHAIN LOCKET"]
                player["defense"] = 12
            else:
                doDialogText("YOU:# Oh,# that's alright,# I already got a cool axe and some gloves.# Thanks for buying these for us-", afterdelay=0.3)
            doDialogText("The team leaves the building.")
            doDialogText("KNIGHT:# This DARK WORLD has a fountain.")
            print(end="        ")
            doDialogText("And by sealing that fountain,# this dark world will cease to exist anymore.")
            print(end="        ")
            doDialogText("In this case,# the person who caused this dark world to exist will also feel relief and peace.")
            doDialogText("ASHISH:# So by sealing this fountain,# we can stop the person's nightmare?")
            doDialogText("KNIGHT:# Exactly.")
            doDialogText("YOU:# Do you know who this Dark World belongs to?")
            doDialogText("KNIGHT:# Not quite,# but I know that this person is nearby.")
            print(end="        ")
            doDialogText("The reason I bought you weapons is because the way to the fountain will be littered with enemies.")
            doDialogText("ASHISH:# Enemies?")
            doDialogText("KNIGHT:# Not every object that becomes a darkner will be friendly.")
            print(end='        ')
            doDialogText("""Whether a darkner is friend or for, depends on how they feel about you.#
            For example,# JOHN CENGAGE was nice to ASHISH because ASHISH took good care of him.""")

            # EDWIN JOLLY GEORGE FIGHT
            doDialogText("YOU:# Wait who's that guy?# Why is he walking towards us?")
            doDialogText("ASHISH:# No way...# Is that...### EDWIN DUAN PORSCHE MY RIVAL?!")
            doDialogText("YOU:# W-#Who?")
            doDialogText("""ASHISH:# This guy in my tuition who keeps snagging the top rank!###
            I always try to beat him,# but no matter what he always comes first!""")
            print(end="        ")
            doDialogText("I have a photo of him taped to the back of my pillow,# and I vent my anger out at him.")
            doDialogText("KNIGHT:# That's probably why he's coming to attack us.")
            doDialogText("ASHISH: wait what", spd=3, afterdelay=0.3)
            print()
            edwinHP = 25
            edwinMERCY = 5
            edwinATK = 24
            edwinDEF = 5
            doDialogText("YOUR SENSES HEIGHTEN IN RESPONSE TO BATTLE!#", spd=5, step=2, afterdelay=0)
            doDialogText("GET READY!", spd=5, step=2)
            doDialogText("ASHISH:# Huh whats going on?")
            doDialogText("""KNIGHT:# You're in battle!# I'll show you the way!
            You can FIGHT to attack the ENEMY.
            You can perform ACTIONS to distract the ENEMY or do something else.
            You can cast SPELLS to influence the ENEMY.
            You can also use some ITEMS you collected along the way.
            Or you could BEG FOR MERCY from the enemy if you're really hopeless.
            I think you get the hang of it!""")

            # BATTLE LOOP
            turn = 0
            hasAlly = False
            hasFight = False
            hasAction = False
            hasSpell = False
            hasItem = False
            hasBeenCalledHandsome = False
            while True:
                if player["hp"] <= 0:
                    route4["DEATHS"] += 1
                    player["hp"] = 1
                    doDialogText("Your HP was 0,# but you held on.")
                    doDialogText("HP Regenerated to 1!")

                if not hasAlly and turn > 2 and ashish["spells"] != []:
                    if not "SUMMON ALLY" in ashish['spells']:
                        doDialogText("ASHISH learnt a new SPELL:# SUMMON ALLY.")
                        ashish["spells"] += ["SUMMON ALLY"]

                if edwinMERCY <= 0:
                    doDialogText("KNIGHT:# EDWIN DUAN PORSCHE seems pleased with the course of the battle.# Now's your chance to use MERCY!")
                    edwinMERCY = 0
                if hasAlly:
                    doDialogText("With SHARATH's help in Actions,# ", afterdelay=0, line=False)
                btselect = doDialogChoice("What will you do?", choices=["Fight", "Action", "Spell", "Item", "Beg For Mercy"])
                if btselect == 1:
                    if not hasFight:
                        hasFight = True
                        doDialogText("KNIGHT:# Seems like you decided to fight.# Get ready to AIM!")

                    playingPlayers = ["You"]
                    if ashish['hp'] > 0: playingPlayers += ["Ashish"]
                    if knight['hp'] > 0: playingPlayers += ["The Knight"]
                    doDialogText(f"{', '.join(playingPlayers)} get ready to Attack EDWIN!")
                    fightResult = doTimedAttack(3, 3, 2)

                    if fightResult > 0.2:
                        dmg = math.ceil((player["attack"] + ashish["attack"])*fightResult/edwinDEF)
                        edwinHP -= dmg
                        doDialogText(f"Your party deals {dmg} damage to EDWIN! ({str(edwinHP)}/25)")
                    else:
                        doDialogText("Your party missed!")
                    route4["battle_firstChoice"] = "FIGHT"

                elif btselect == 2:
                    if not hasAction:
                        hasAction = True
                        doDialogText(f"""KNIGHT:# Actions are based on {saveFile['name']}'s judgement.# Your actions influence the enemy,# and you may even gain their mercy.
            Actions are different for each enemy.""")

                    acts = doDialogChoice("ACTS:", choices=["Check", "Physics", "Chemistry", "Maths", "Return."])
                    if acts == 1:
                        doDialogText(f""" 
EDWIN:#
ATTACK: {edwinATK},#
DEFENSE: {edwinDEF},#
Ashish's Rival.# He looks strong,# but we can defeat him!""")
                        if hasBeenCalledHandsome:
                            doDialogText("SHARATH:# Please don't challenge him in maths,# i don't like the tall lady calling me handsome", spd=2)

                    elif acts == 2:
                        if hasAlly:
                            doDialogText("SHARATH helps you with Physics!")
                            edwinMERCY -= 0.5

                        if saveFile['route2']['house_studyChoice'] == "STUDYING":
                            doDialogText("You tackle against Edwin with your Physics Skills.")
                            doDialogText("You get him on the cross-product question!")
                            edwinMERCY -= 1
                            doDialogText(f"You gained {(5- max(0, edwinMERCY))/5*100}% MERCY!")
                        else:
                            doDialogText("You and ASHISH try to compete against Edwin on Physics.")
                            edwinMERCY -= 2
                            doDialogText(f"You gained {(5- max(0, edwinMERCY))/5*100}% MERCY!")
                    elif acts == 3:
                        if hasAlly:
                            doDialogText("SHARATH helps ASHISH with Chemistry!")
                            edwinMERCY -= 0.5

                        doDialogText("Ashish tackles Edwin on Chemistry.")
                        edwinMERCY -= 1
                        doDialogText(f"You gained {(5- max(0, edwinMERCY))/5*100}% MERCY!")
                    elif acts == 4:
                        if hasAlly: 
                            doDialogText("SHARATH helps the KNIGHT with Maths!")
                            edwinMERCY -= 0.5
                            if not hasBeenCalledHandsome:
                                doDialogText("""KNIGHT:# Oh,# thanks young one!#
            you know you're really handsome...""")
                                doDialogText("SHARATH:# Uh,# thanks?# lady please don't flirt with me-", afterdelay=0.2)
                                hasBeenCalledHandsome = True
                            else:
                                doDialogText("KNIGHT:# Thank you,# handsome knight.")
                                doDialogText("SHARATH:# Lady we've talked about this...")

                        doDialogText("The Knight takes on Edwin with her Maths skills.")
                        edwinMERCY -= 1
                        doDialogText(f"You gained {(5- max(0, edwinMERCY))/5*100}% MERCY!")
                    elif acts == 5:
                        continue
                    
                elif btselect == 3:
                    if not hasSpell:
                       hasSpell = True
                       doDialogText("KNIGHT:# Spells are ASHISH's territory.# He can cast spells that can either influence the enemies or us.")
                       doDialogText("ASHISH:# B-#But I have no spells.#.#.#")
                       doDialogText("KNIGHT:# Oh crap,# let me teach you a spell right now!")
                       doDialogText("ASHISH LEARNT A SPELL: HEALING SONG!", spd=5, step=2)
                       doDialogText("HEALING SONG:# Heals a friend in battle.")
                       doDialogText("ASHISH:# HEALING SONG????# But I can barely sing!")
                       doDialogText("KNIGHT:# That's alright!# Quick,# get ready!")
                       doDialogText("ASHISH:# Uhh uhh uhh uh-",afterdelay=0)


                    spell = doDialogChoice("ASHISH's SPELLS:", choices=ashish['spells'] + ['Return.'])
                    if spell > len(ashish["spells"]):
                        continue
                    else:
                        selSpell = ashish['spells'][spell-1]

                        if selSpell == "HEALING SONG":
                            doDialogText("ASHISH sings a soothing melody.# Some notes are off.")
                            player["hp"] += 4
                            ashish["hp"] += 2
                            knight["hp"] += 3
                            if player['hp'] > getMaxHP(1): player['hp'] = getMaxHP(1)
                            if ashish['hp'] > getMaxHP(2): ashish['hp'] = getMaxHP(2)
                            if knight['hp'] > getMaxHP(3): knight['hp'] = getMaxHP(3)
                            doDialogText(f"{saveFile['name'].upper()} was HEALED. ({(player['hp'])}/{(getMaxHP(1))})")
                            doDialogText(f"ASHISH was HEALED. ({(ashish['hp'])}/{(getMaxHP(2))})")
                            doDialogText(f"KNIGHT was HEALED. ({(knight['hp'])}/{(getMaxHP(3))})")
                        elif selSpell == "SUMMON ALLY":
                            if not hasAlly:
                                doDialogText("ASHISH:# Since when did I have a new spell?")
                                doDialogText("KNIGHT:# Seems like this spell came naturally with you.# Try it!")
                                doDialogText("ASHISH:# B-#but I don't know how to cast this spell!# What if I mess it up?")
                                doDialogText("KNIGHT:# C'mon Ashish!# You can do it!")
                                doDialogText("ASHISH:# I-# FINE!# Watch what happens when I cast a spell that I DON'T KNOW!")
                                doDialogText("ASHISH casts SUMMON ALLY!# As the name suggested,# an ally was spawned.")
                                doDialogText("SHARATH:# Yo guys,# what's popping?")
                                doDialogText("ASHISH:# SHARATH?# OH IT'S SARBATH!# Are you my ally?")
                                doDialogText("SHARATH:# Yep,# I can help you in dealing with Edwin,# no problem!")
                                doDialogText("ASHISH:# OH yeah,# SARBATH is my tuition buddy.# We're friends in the tuition,# and both are competing for the top!")
                                doDialogText("YOU:# Well SARBATH let's get him!")
                                doDialogText("SHARATH:# Actually im just sharath,# the guy i'm probably based off is called sarbath.")
                            else:
                                doDialogText("ASHISH:# I-#I already have this ally!# No need to cast the spell again.")
                            hasAlly = True
                            continue
                        
                elif btselect == 4:
                    if not hasItem:
                        hasItem = True
                        doDialogText("KNIGHT:# From here,# you can use ITEMS you've found along the journey!# You may not have much now.")

                    if inventory == []:
                        doDialogText("Your inventory is empty.")
                        continue
                    else:
                        item = doDialogChoice("CHOOSE AN ITEM", choices=inventory + ["Return."])
                        if item > len(inventory):
                            continue
                        elif inventory[item-1] == "KEYCHAIN LOCKET":
                            doDialogText("You are already wearing the Keychain Locket.")
                            continue
                        else:
                            doDialogText("HOW DO YOU HAVE AN ITEM THIS EARLY IN THE GAME.", spd=6, step=2)
                            continue
                        
                elif btselect == 5:
                    if edwinMERCY <= 0:
                        doDialogText("You ask Edwin for forgiveness.")
                        doDialogText("Edwin forgives you!")
                        print()
                        doDialogText("YOU WIN!# YOU GOT 37 DARK DOLLARS!")
                        money += 37
                        doDialogText(f"You now have {str(money)} Dark Dollars.")
                        break
                    else:
                        doDialogText("You ask Edwin for forgiveness,# but he wouldn't budge!")

                if edwinHP <= 0:
                    doDialogText("EDWIN DUAN PORSCHE ran away!# he also left some money for you to not attack him again.")
                    doDialogText("YOU WIN!# YOU GOT 37 DARK DOLLARS!")
                    money += 37
                    doDialogText(f"You now have {str(money)} Dark Dollars.")

                    route4["on_weirdRoute"] = True
                    break
                
                # EDWIN'S TURN
                doDialogText("EDWIN DUAN PORSCHE GETS READY TO ATTACK!", spd=5, step=2)
                edwinAttack = random.randint(1,3)
                targetINDEX = random.randint(0,2)
                PLAYERNAMES = [saveFile['name'].upper(), "ASHISH", "The KNIGHT"]
                # Make sure Edwin's target isn't a downed ally
                while [player, ashish, knight][targetINDEX]['hp'] <= 0:
                    targetINDEX = random.randint(0,2)
                targetStruct = [player, ashish, knight][targetINDEX]
                if edwinAttack == 1:
                    doDialogText("Edwin shoots a chemical orb of Conc. Sulphuric Acid!")
                    fResult = doTimedAttack(3, 3, 2)
                    if 0.9 <= fResult <= 1:
                        doDialogText("Edwin missed his attack!")
                    else:
                        dmg = getDamageDealt(edwinATK, targetStruct, fResult)
                        targetStruct["hp"] -= dmg
                        doDialogText(f"{PLAYERNAMES[targetINDEX]} got hit by Edwin's Attack!")
                        doDialogText(f"{PLAYERNAMES[targetINDEX]} lost {dmg} HP!")
                        if targetStruct["hp"] <= 0: doDialogText(f"{PLAYERNAMES[targetINDEX]} WAS DOWNED!", spd=5, step=2)
                        route4["battle_noHit"] = False
                elif edwinAttack == 2:
                    doDialogText("Edwin readies a spring cannon loaded with a block of mass 5kg!")
                    fResult = doTimedAttack(3, 1, 2)
                    if 0.9 <= fResult <= 1:
                        doDialogText("You dodged Edwin's trajectory!")
                    else:
                        dmg = getDamageDealt(edwinATK, targetStruct, fResult)
                        targetStruct["hp"] -= dmg
                        doDialogText(f"{PLAYERNAMES[targetINDEX]} got struck by Edwin's 5kg block!")
                        doDialogText(f"{PLAYERNAMES[targetINDEX]} lost {dmg} HP!")
                        if targetStruct["hp"] <= 0: doDialogText(f"{PLAYERNAMES[targetINDEX]} WAS DOWNED!", spd=5, step=2)
                        route4["battle_noHit"] = False
                elif edwinAttack == 3:
                    doDialogText("Edwin challenges you with a Math Penalty based Question!")
                    ind = random.randint(0,2)
                    question = ["Use PEMDAS or BODMAS!# What is 12x3 + 5?",
                                "What's 5x8 + 1?",
                                "If a man takes 4 seconds to jump after a TIMER starts,# and hits the ground when the TIMER reaches 45 seconds,# how long was the man in the air?"][ind]

                    fResult = doTimedQuestion(question, 41, 5)
                    if fResult == 1:
                        doDialogText("You answered Edwin's question correctly!")
                    else:
                        dmg = getDamageDealt(edwinATK, targetStruct, fResult)
                        targetStruct["hp"] -= dmg
                        doDialogText(f"{PLAYERNAMES[targetINDEX]} miscalculated and got dealt a penalty!")
                        doDialogText(f"{PLAYERNAMES[targetINDEX]} lost {dmg} HP!")
                        if targetStruct["hp"] <= 0: doDialogText(f"{PLAYERNAMES[targetINDEX]} WAS DOWNED!", spd=5, step=2)
                        route4["battle_noHit"] = False

                    # TURN END
                    turn += 1

            doDialogText("ASHISH:# We.#.#.# we beat that guy...")
            doDialogText("KNIGHT:# Yes we did.# Good job,# both of you!")
            doDialogText("""ASHISH:# WOOOOOOOOOO WE FINALLY BEAT THAT GUY!
            a-#ahem.""")
            doDialogText("YOU:# .#.#.#")

            if player["hp"] <= 0:
                doDialogText(f"KNIGHT:# {saveFile['name']},# you seem to possess remarkable will and determination.# You refused to give up,# even when you were beaten and downed.")
                doDialogText("YOU:# Yeah...# Not gonna lie it kinda hurt.")
                doDialogText("KNIGHT:# We'll be counting on your power.# With your determination,# we could NEVER LOSE A FIGHT.")
                doDialogText("YOU:# Yeah.#.#.# you can count on me.")
            else:
                doDialogText(f"""KNIGHT:# {saveFile['name']},# you may not know it,# but you possess a remarkable ability to persist even when downed and keep fighting.
            We'll be counting on your power.# With your determination,# we could NEVER LOSE A FIGHT.""")
                doDialogText("YOU:# Alright.")


            if ashish["hp"] == player["hp"] == 15 and knight["hp"] == 20:
                route4["battle_noHit"] = True
                doDialogText("ASHISH:# Seems like we took no damage...")
                doDialogText("ASHISH LEVELED UP! (LV 2)")
            else:
                route4["battle_noHit"] = False
                doDialogText("ASHISH:# Seems like we took some damage.# lemme heal everyone!")
                doDialogText("Ashish concentrates and starts casting HEALING SONG.")
                doDialogText("This time,# the notes come out beautifully.")
                doDialogText("ASHISH LEVELED UP! (LV 2)")

                player['hp'] += 5
                ashish['hp'] += 4
                knight['hp'] += 7

                if player['hp'] > getMaxHP(1): player['hp'] = getMaxHP(1)
                if ashish['hp'] > getMaxHP(2): ashish['hp'] = getMaxHP(2)
                if knight['hp'] > getMaxHP(3): knight['hp'] = getMaxHP(3)
            ashish['lv'] = 2
            ashish['attack'] += 5
            ashish['defense'] += 5

            doDialogText("ASHISH:# Woah,# I feel stronger!")
            doDialogText("KNIGHT:# As you keep fighting,# you'll gain experience and grow stronger and tougher.", afterdelay=0)
            doDialogText("        Kinda like how you level up in videogames.")
            doDialogText("YOU:# This...## dream,# feels like a videogame already.")
            print()

            save1 = getPrompt("Save this chapter here?")

            if save1:
                route4["startIndex"] = 1
                route4['players'] = [player, ashish, knight, flowery]
                saveFile["route4"] = route4

                
                saveFile['route4']['inventory'] = inventory
                saveFile['route4']['money'] = money

                try:
                    saveGame(curSaveName, saveFile)
                    doDialogText("The game was saved.")
                except:
                    doDialogText("There was an error in saving the game.")
            
            continue1 = getPrompt("Continue your journey?")

            if continue1:
                startindex = 1
                doDialogText("Continuing from EDWIN DUAN PORSCHE's Fight.#.#.#", afterdelay=2)
        else:
            doDialogText(".#.#.#")
            doDialogText("You woke up to knocking on the door.")
            doDialogText("Someone's outside.")
            doDialogText("You look through the door's peephole.")
            doDialogText("(A tall figure.#.#.# holding a knife...)###")
            print()
            doDialogText("It's WAYDANT.", afterdelay=1.5)
            doDialogText("YOU:# Hey,# you're WAYDANT,# right?")
            doDialogText("WAYDANT:# Yes,# I'm here to help you.")
            doDialogText("YOU:# Help me?")
            doDialogText("WAYDANT:# Let me in.")
            doDialogText("YOU:# Not with that knife in the middle of the night.")
            doDialogText("WAYDANT:# NO WAIT-# It's not what it looks like,# I swear!")
            doDialogText("YOU:# Then why do you have a knife with you?")
            doDialogText("WAYDANT:# Look-# I'll put it on the ground and walk away,# so you can have it.# The Knife's for you!")
            doDialogText("YOU:# Why are you giving me the knife?")
            doDialogText("WAYDANT:# It's to protect you from ADITHYA and his FANTASY gang.# Ok I will keep the knife right here so you can have it.")
            doDialogText("Waydant rises the blade,# preparing to stab.")
            doDialogText("His body lights up as he stabs at the ground.")
            doDialogText("Suddenly-",afterdelay=0.3)
            printGraphic(''' 
█ ████████████████████████████████ █
 █ ████████████████████████████████ █
 █ ████████████████████████████████ █
 █ ████████████████████████████████ █
 █ ████████████████████████████████ █
 █ ████████████████████████████████ █
 █ ████████████████████████████████ █                 ▄▀▀▀▀▀▄
  ▀▄▀██████████████████████████████ █              ▄▄▀▄     ▀▄▀▀▀
▀▀ ▀▀▄▄▄▄▄▀███████████████████████ ▄█         ▄▀▀▄▀    █  ▄▄▄▀
 ▀█▄███████ ██████████████████████ █        ▄▀   ▀▄▄▀▀▀▄▀▀   ▀▄▄
▀▄█▄▄▀▀████▀▄▀████████████████████ █        ▀▄▄▄▄▀▄▄   ▄▀▄▄ ▄▀  ▀
▀▄▄▄▄▀▀▄▄▀▄▀█▀▄███████████████████ █      ▄▀▀▄   █  ▀▄▄█▄ ▄▀▄▀▀▀▀
▀▄▄▄▀▀█▀▀▄▀▀▄█████████████████████ █      ▀▄  ▀▄▄▄▀▄▀   ▄▀   █
▄▀▄▄  ███▀▄▀▄████      ███▀   ▀██ █▀        ▀█▄▄▄▄█  ▄▀ ▀▄▄     ▀
▀▄ ▄▀▀▄▄▄▀▄▀█████      ███     ▀█ █          █    ▀▀▀▀▀▀█▄▄█▄▄▄▀▀
▄▀▀▄▀▀▄▄▀▀ ██████▄    ▄███    ▄██ █          █                ▀▀▀
▄█▄▀▀▄▄▄██ ███████    ▀▀█    ▄███ █          █
   █ █████ ██████▀          ▄███▀ █          █
   █ █████ ██████          ▄████ █▀          █▄
   █▄▀████▄▀████▀          █████ █            █
    █ █████ █████▀▀▀▀█▄   ▄█████ █            █
    █ █████ ████      ▀█▄ █████▀ █            █
▀▀▀▀▄▀ ▄▄▄▄▄█▀▀█       █▀▀█████ █▀            █
    ▀█▄ ████   █▄     ▄█  ▀███▀ █             █▄▄▄▄▄▄
      █ ▀██   ████▄▄▄▄███  ██▀ █▀                   ▀▀▀▀▀█▄▄▄▄▄
▀▀▀▀▀▀ ▄██▄   ▀▀▀▀▀▀▀▀▀█▀ ▄█▀▄▀█▄                             ▀▀▀
        ▄█▄ ▀   ▀█  █▀    ▀ ██▄  ▀▀▀▀▀▀▀▀▀▀██▄▄▄▄▄▄▄▄▄▄▄▄
       █  ▀█▄  ▄██  █▄▄▄█▀▄▄        ▀▀▀  ▄▀             ▀▀▀▀▀▀▀▀▀
     ▄▀     ▀▄██ ▀   █▀      ▀▀▀▀▀▀     ▄▀
    ▄▀         ██▄▀▀▀██▀▀        ▄     ▄▀
   ▄▀        ▄ ▀▄ ██▀ ▄▀▀▀    ▄▄      █
  █          ▀▄ ▄▄▀▄▄▀ ▀▀█           █
 ▀      ▀▀     ▀     ▀▀▀            ▀
''')
            doDialogText("A Bright light flashes from the ground.")
            doDialogText("WAYDANT: WAIT WHATS HAPPENING-", spd=2, afterdelay=0.5)
            doDialogText("Waydant loses conciousness and is sucked into the light.")
            doDialogText("YOU:# WHAT THE HELL JUST HAPPENED,# WAYDANT ARE YOU OKAY?!")
            doDialogText("Waydant is sucked in by the light.")
            doDialogText("You quickly open the door.")
            printGraphic('''  ███  ███████████████████████████████████████████  ██████▄ █▄
  ██  ████████████████████████████████████████████  ███████ ▀█
  █  █████████████████████████████████████████████  ███████ █▄
  █  █████████████████████████████████████████████  ███████  █
     █████████████████████████████████████████████  ██████  ▄█
     ▀████████████████████████████████████████████  ████▀  ██
 █▄   ▀███████████████████████████████████████████  ██ ▄ ▄█▀
  █▄   ▀██████████████████████████████████████████▄▄     ▀
 ▀██     █████████████████████████████████████████▀█   ▄
   ██   ▄█████████████████████████████████████████  ▄   █▄▄
    ▀▄  ██████████████████████████████████████████  ▀▄   █▀
     ▀  █████████████████ ▄▀▀██████████████████████  █    █
        █████████████████ ███▄ ████████████████████  █
     ▄   ████████████████ ████ ████████████████████     █▄▄
     ██   ▀██████████████ ████ ████████████████████▄█  ███     ▄▄
      ▀     █████████████ ████ ██████████████████████   █▀
           █████████████ ▄▀▀██ ███████████████████▀██   █▀▄
      ▄▄   █████████████ ███▄▄▀▀█████████████████▀ ██      ▀▀▄
      ██   █████████████ ███████▄▄▀▀███████████▀   ██         ▀
      ▀█    ▀███████████ █████████▀▄██████████▄    ████
       ▀      ██████████ █████████ ████████████    ████
              ▀█████████ ████████▀▄████████████    █▀█▄
               ▄████████▄▀███████ ███████████▀      ▀▀███▄
▄▄▄▄▄▄▄▄▀▀▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀ ██████ ▀▀▀▀▀▀▀▀▀▀█▄▄▄▄▄▄▄▄▄▄▄▄██▄▄▄▄▄▄▄
        █▄    ███████████ █████▀▄█████████▀     ██▀
        ██     ▀█████████ █████ ██████████     ▄█▀
          ▀      ████████ ████▀▄██████████     █
               ▀▄▄▄███▄██ ██▀▀▄█████▀▀▀███▄▄▄ ▀
                 ██▀▀████ ▄▄████████████▀
              ▀▄▄  ▀▀▀█████████▄▄██▄▄▄▀
                 ▀▀▀▀ ▀██▄████████▄
               ▀▀▀      ▀▀▀▀▀▀█▄▄▄▀▀▀
                               ▀▀         ▀
''')
            doDialogText("The light...# something's wrong with it.")
            doDialogText("It's coming from the knife?")
            doDialogText("And why is the light black?# Why is the knife black?!")
            doDialogText("You try to pick up the knife,# but it's very heavy.")
            doDialogText("The light fades,# but the knife is now pitch black.")
            doDialogText("YOU:# What the hell is this knife?!")
            doDialogText("You close and lock the door again.")
            doDialogText("In the process,# the knife falls out of your hands.")
            printGraphic('''          ▀████   ██   ▄█████████▀▀▀██     ▄ ██▄
            ▀█    ███ ▄███████▀███  ██▄█  ▄▄▀██
            ▀▄███▄███▄███████▄████ █████▀▀▀▄▀█
              ▀██▀▀▀▀█████▀▄▀▀▀█████████▀█▀▄▀
               ▄█  ▄█████▀▄███▄▄▀█▀▄███▄▀
               ▄█  ██████ ███▄▄▄▀▄▀▄█▀▀██
                █▄▀█████▀▄████ ▄▀▄▀██ ▄▀
                ▀███████ █████ ██████▀█
                ▀▄██████ ████ ███████▀
                ▀▄██████ ████ ███████▄▀▄
                █▀█████ █▄▄▄▀ ▀██████▄▀▄
                 ▀█████ ███████▄▄▀███  █▀
                ▀█▀████ ██████████ ███ ▄▀▄
                  ▀█████ ███▀▄▀███ ██████▄█▀
                  ▀▄████ ██▄▀▄▀▄██ ████▄█▀▄▀
                  ▀▄▀███ ████▄████ ███▀█▄▀
                 ▀█▄▀▄██ ████████ ███▀▄▀▄▀
                    ▀▄██▄▀█▄▀███▀▄███▀▄▀
                    ▀████ █▄▀██ █▀█▀ ▀
                     ████ █▄█▀▄▀▄▀▄█▀
                    ▀▄███ ██▀ ▄▀ ▀▀
                     ▄███ █▀▄▀▄
                    ▀▄███▄▄██▀▄
                     ▄▀█▀███   ▀▄
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    ▄▀   ▀▄▀▄ ▄
               ▀▀▀▀▀ ▀ ▀ ▀ ▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

                      ▄ ▄ ▄ ▄     ▄ ▄
            ▄▀▄     ▄▀▄█▄██▀▄▀▄    ▀██▄
           ▀██▄      ▀▄▀█▀█▀▄▀       ▀
             █▄▀▄
                 ▀''')
            doDialogText(".#.#.### This time the light engulfs you,# and you fall into the light.")
            doDialogText("(Damn it... i'm losing conciousness...)")
            print()
            doDialogText("...")
            doDialogText("You wake up again.")
            doDialogText("This time you're surrounded by a snowy deserted area.")
            doDialogText("The sky is pitch black.")
            doDialogText("YOU:# Where the hell am I?")
            doDialogText("FLOWERY:# You're in a DARK WORLD.")
            doDialogText("YOU:# Oh,# thanks for telling me.", afterdelay=3)
            doDialogText("     did that flower j-#just talk?")
            doDialogText(f"FLOWERY:# Hello,# {saveFile['name']}!# I'm FLOWERY!# FLOWERY the FLOWER.")
            doDialogText("YOU:# Why are you talking like that,# and WHY DO YOU KNOW MY NAME??")
            doDialogText("FLOWERY:# Relax,# dude,# I'm the flower vase you keep near your apartment entrance.# I've known you as long as you've been living in the apartment.")
            doDialogText("YOU:# W-#Huh?# What do you mean?# This ISN'T my apartment-# its the middle of nowhere!")
            doDialogText("FLOWERY:# *sigh* let me explain...")
            print()
            doDialogText("FLOWERY: ==")
            doDialogText("This is a DARK world.")
            doDialogText("I saw what you two were doing out there.# That VEDANT guy stabbed the ground.")
            doDialogText("What does that have to do with this?# EVERYTHING.")
            doDialogText("By stabbing the ground in the dark,# with will and power,# you create a DARK WORLD that reflects your will.")
            doDialogText("DARK WORLDS are reflection of the real worlds-# just in the dark,# when it's so dark that normal objects begin to distort and morph into something else,# completely based on your own mind and delusion.")
            doDialogText("With one's such tremendous will and distortion,# the EARTH provides a sort of seperate dimension for you to play out your dreams.")
            doDialogText("Basically your dreams,# but more real and cooler.")
            doDialogText("That's basically it.")
            doDialogText("YOU:# That certainly was a lot to take in.")
            doDialogText("FLOWERY:# Do you have any questions?")
            doDialogText("YOU:# So I'm dreaming?")
            doDialogText("FLOWERY:# ...## yeah if you wanna think like that...")
            doDialogText("YOU:# Finally,# something that makes sense.")
            doDialogText("FLOWERY:# Do you wanna know how to get back?")
            doDialogText("YOU:# Sure.")
            doDialogText("""FLOWERY:# You know where you stabbed the knife?# That creates a fountain.###
         A fountain is what gives shape and form to a DARK world.###
         You can recognize a Dark fountain by it's Dark presence.###
         Seal it,# and you'll go dizzy before waking back up in your world.###
         But remember - Dark worlds aren't fully imaginary,# so anything you do in a Dark world WILL be reflected into the light.###
         It's like the saying - anything you do in the dark comes to light,# heh.""")
            doDialogText("YOU:# So where do I find this fountain?")
            doDialogText("FLOWERY:# Somewhere.# But I have a vague idea where it could be,# if you're willing to follow me.")
            doDialogText("YOU:# Okay,# lead the way.")
            doDialogText("""FLOWERY:# Great!# This is gonna be a WONDERFUL journey!#####
         ignore i said that it's very cringy""", afterdelay=0.4)
            print()
            doDialogText("You and Flowery start walking towards something in the distance.")
            doDialogText("YOU:# Soo anything I do in the dark world gets reflected to the real world?")
            doDialogText("FLOWERY:# Yes.# But if you're expecting a change,# you're gonna have to do something drastic.")
            doDialogText("YOU:# So what if I were to kill you right now?")
            doDialogText("FLOWERY:# Then your mom would be sad about her favourite flowers wilting.")
            doDialogText("YOU:# Ohh.")
            doDialogText("You and Flowery end up at a building shaped like a cupboard.")
            doDialogText("YOU:# You have any idea what this building is?")
            doDialogText("FLOWERY:# Yeah,# it's the cupboard you place your shoes in.")
            doDialogText("YOU:# Oh.# It's bigger than us.")
            doDialogText("FLOWERY:# Yeah...# and apparently it's also a shop.")
            doDialogText("YOU:# What are we buying?")
            doDialogText("FLOWERY:# Weapons.# Not every darkner we're coming across will be friendly.")
            doDialogText("YOU:# What do you mean?# What is a darkner?")
            doDialogText("FLOWERY:# You see,# in a dark world,# some objects that have a strong enough will turn into living creatures,# called DARKNERS.", afterdelay=0)
            doDialogText("And not every darkner will think the same about you.# Some will want to fight you, so ofcourse you need to be prepared.")
            doDialogText("YOU:# Oh..")
            doDialogText("FLOWERY:# I'm gonna buy some stuff.")
            doDialogText("YOU:# Where'd you get the money from?")
            doDialogText("FLOWERY:# ...# you kept like 500 rupees under my vase and forgot about it.")
            doDialogText("YOU:# OHHH That's where I kept it!")
            doDialogText("FLOWERY:# ...you have a serious problem with forgetting money...")
            doDialogText("Flowery buys some stuff from the shop.")
            doDialogText("YOU:# So is that money gone forever?")
            doDialogText("FLOWERY:# Actually since I'm on top of the cupboard we just shopped from,# it'll probably stay right where it is.")
            doDialogText("YOU:# Oh nice.")
            doDialogText("FLOWERY:# Better not forget it this time!# Here, take some stuff.")
            doDialogText("YOU GOT THE VELCRO BAT.", spd=5, step=2)
            doDialogText("YOU GOT THE LEATHER BOOTS.", spd=6, step=2)
            player["weapon"] = "VELCRO BAT"
            player["armor"] = "LEATHER BOOTS" # If you have the keychain, the keychain will offer higher defense. You can then give the boots to anyone in need, and your father's boots will be missing while the boots are somewhere else

            if saveFile['route2']['house_roomChoice'] == "CLEANED":
                doDialogText("Something resonates in your pants.")
                doDialogText("YOU:# What is it?")
                doDialogText("You take out your keychain you found!# It's now..# a locket?")
                doDialogText("YOU GOT THE KEYCHAIN LOCKET.", spd=5, step=2)
                doDialogText("FLOWERY:# Wow,# the dark world has shifted your keychain into a locket.# Try it on!")
                doDialogText("You put on the locket.")
                doDialogText("YOUR DEFENSE RAISED FROM 10 TO 12", spd=5, step=2)
                player["defense"] = 12
                player['armor'] = "KEYCHAIN LOCKET"
                inventory.append("KEYCHAIN LOCKET")
                doDialogText("YOU:# I feel tougher now!")
                doDialogText("FLOWERY:# Well that's because your KEYCHAIN LOCKET has more defense than these boots,# and I can't really refund these so Ima hold on to them.")
                doDialogText("YOU:# Oh...# Well that sucks")
                doDialogText("FLOWERY:# Meh,# you never know when it is useful to have a spare boots.", afterdelay=1.4)
                print()

            doDialogText("You and Flowery arrive at what looks like a grand door.# The door is hundreds of times taller than you...")
            doDialogText("YOU:# How do we get past this door?")
            doDialogText("GREAT DOOR:# I am the GREAT DOOR.# Answer my question,# and I shall let you pass.")
            doDialogText("FLOWERY:# Honestly I have no idea what it could be.# You're on your own.")
            doDialogText("YOU:# Bruh,# ok.")
            doDialogText("GREAT DOOR:# ANSWER NOW:")
            doDialogText("Times of sixes and sevens stand at the second position,# the Northern lights point towards the stable first.#.#.#")
            doDialogText("However,# in absolute chaos due the search of freedom,# does one succeed.")
            deAnswer = doDialogChoice("The displacement of which sanctuary,# out of the three but many norths,# lies at the very peak?",
                                      choices = ["First.", "Second.", "Third.", "Fourth."])

            if deAnswer == 3:
                doDialogText("GREAT DOOR:# What?!# Where did you find the answer from?")
                doDialogText("YOU:# Hmmmm...")
                doDialogText("FLOWERY:# That's impressive,# how did you know the answer?")
                if pgFilter:
                    doDialogText("(I have no clue,# I pulled that out of my ass.)")
                else:
                    doDialogText("(I have no idea,# I just said it randomly.)")
                doDialogText("GREAT DOOR:# U-#Uhh...# Very well.# The first test has been concluded.")
                doDialogText("YOU:# The first?")
                doDialogText("GREAT DOOR:# You must now prove your ability to fight!")
                doDialogText("YOU:# Fight?!")
                if pgFilter: doDialogText("FLOWERY:# Oh,# this is bullshit-", afterdelay=0)
                print()
            else:
                doDialogText("GREAT DOOR:# WRONG!# You have failed to prove you get to pass through this door.")
                doDialogText("YOU:# What kinda question was that,# was there some sort of hint?")
                if pgFilter: doDialogText("FLOWERY:# Honestly sounded like bullshit to me.")
                else: doDialogText("FLOWERY:# Honestly sounded like nonsense to me.")
                doDialogText("GREAT DOOR:# You shall now prove yourself worthy to cross me by FIGHT!")
                doDialogText("FLOWERY:# Huh?", afterdelay=0.3)
                print()

            doDialogText("YOUR SENSES HIGHTEN IN RESPONSE TO BATTLE!", spd=5, step=2)
            doDialogText("YOU:# WHAT'S HAPPENING?")
            doDialogText("FLOWERY:# You're in battle now!# God-# lemme explain this quickly-")
            doDialogText('''         You can FIGHT to attack the ENEMY.
             You can perform ACTIONS to distract the ENEMY or do something else.
             You-# no I can cast SPELLS to influence the ENEMY.
             You can also use some ITEMS you collected along the way.
             Or you could BEG FOR MERCY from the enemy if you're really hopeless.
             GET READY!''')

            playSong('assets/soundtrack/guards.ogg', looping=True)
            doDialogText("Two guards emerge from within the doors!")
            guardA = {
                "attack": 15,
                "defense": 6,
                "hp": 30
            }
            guardB = {
                "attack": 15,
                "defense": 6,
                "hp": 30
            }
            turn = 0
            endBattle = False
            chosens = [False, False, False, False, False]
            letDownDefense = False
            firstBreakdance = True
            breakCount = 0

            while not endBattle:
                if player["hp"] <= 0:
                    route4["DEATHS"] += 1
                    player["hp"] = 1
                    doDialogText("Your HP was 0,# but you held on.")
                    doDialogText("HP Regenerated to 1!")

                # YOUR TURN
                btselect = doDialogChoice("What will you do?", choices=["Fight", "Action", "Spell", "Items", "Beg For Mercy"])
                if btselect == 1:
                    if not chosens[0]:
                        doDialogText("FLOWERY:# We both will attack an enemy now.# Prepare to attack!")
                        chosens[0] = True
                    enemy = doDialogChoice("Which enemy will you attack?", choices=['Guard A', 'Guard B'])
                    playingPlayers = ["You"]
                    if flowery['hp'] > 0: playingPlayers += ["Flowery"]
                    doDialogText(f"{", ".join(playingPlayers)} get ready to Attack The Guards!")
                    fightResult = doTimedAttack(3, 3, 2)
                    playingStructs = [player]
                    if flowery['hp'] > 0: playingStructs += [flowery]
                    if fightResult > 0.2:
                        totalAtk = 0
                        for pl in playingStructs:
                            totalAtk += pl['attack']
                        guardDef = [guardA, guardB][enemy-1]['defense']
                        if letDownDefense: guardDef *= 0.6
                        dmg = math.ceil((totalAtk)*fightResult/guardDef)
                        [guardA, guardB][enemy-1]['hp'] -= dmg
                        doDialogText(f"Your party deals {dmg} damage to {['GUARD A', 'GUARD B'][enemy-1]}! ({[guardA, guardB][enemy-1]['hp']}/30)")
                    else:
                        doDialogText("Your party missed!")
                elif btselect == 2:
                    if not chosens[1]:
                        doDialogText("FLOWERY:# Actions are upto your judgement.# Do something you think will help this fight!")
                        chosens[1] = True

                    action = doDialogChoice("ACTIONS:", choices=["Check", "Talk.", "Breakdance...?"])
                    if action == 1:
                        doDialogText(f"""GUARDS:
ATTACK:# 15,
DEFENSE:# 6,
HP:# {guardA['hp']}/30, {guardB['hp']}/30.
They look serious,# but they're actually really bored?""")
                    elif action == 2:
                        if not letDownDefense:
                            doDialogText("You try to talk to the guards.")
                            doDialogText("They do not listen to you.")
                        else:
                            doDialogText("GUARDS:# Haha,# that was a funny performance.# Hadn't seen one in a while.")
                            doDialogText("(The guards did not listen to you,# but you think you might have found something.)")
                    elif action == 3:
                        if firstBreakdance:
                            firstBreakdance = False

                            doDialogText("You attempt to breakdance in order to catch the guards off guard...?")
                            doDialogText("FLOWERY:# Hey!# what are you doing?!?!")
                            doDialogText("YOU:# I HAVE NO IDEA WHY I'M DOING THIS!!!")
                            doDialogText("But the guards are laughing???")
                            doDialogText("The guards let their defense down!")
                            letDownDefense = True
                            continue
                        else:

                            if letDownDefense:
                                doDialogText("You keep breakdancing.")
                                breakCount += 1
                                if breakCount > 4:
                                    doDialogText("You seem to be enjoying this...")
                                    doDialogText("FLOWERY:# are we ever gonna attack?")
                            else:
                                doDialogText("You try to breakdance to get the guards' attention.")
                                doDialogText("The guards let down their defense!")
                                letDownDefense = True
                            continue
                elif btselect == 3:
                    if not chosens[2]:

                        doDialogText("FLOWERY:# I have the ability to use spells!")
                        doDialogText("YOU:# What spell do you have?")
                        doDialogText("FLOWERY:# Actually let me check.#.#.##")
                        doDialogText("YOU:# ..?")

                        if pgFilter: doDialogText("FLOWERY:# W-WHAT THE FUCK?# PHOTOSYNTHESIS?!", step=2)
                        else: doDialogText("FLOWERY:# PHOTOSYNTHESIS?!", step=2)

                        doDialogText("YOU:# What does uh...# Photosynthesis do in this context?")
                        doDialogText("FLOWERY:# It's a healing spell...")
                        doDialogText("YOU:# Isn't that useful?")
                        doDialogText("FLOWERY:# It would be...")
                        doDialogText("         IF IT WASNT FREAKING PHOTOSYNTHESIS!# THIS IS A WEAK SPELL.")
                        doDialogText("YOU:# Oh,# lets try it anyways.")

                    spell = doDialogChoice("SPELLS:", choices=flowery['spells'] + ["Return."])
                    curSpell = flowery["spells"][spell-1]
                    if curSpell == "PHOTOSYNTHESIS":
                        doDialogText("Flowery channeled nearby sunlight!")
                        player["hp"] += 1
                        flowery["hp"] += 1
                        if player['hp'] > getMaxHP(1): player['hp'] = getMaxHP(1)
                        if player['hp'] > getMaxHP(4): player['hp'] = getMaxHP(4)
                        doDialogText(f"{saveFile['name'].upper()} was HEALED. ({str(player['hp'])}/{str(getMaxHP(1))})")
                        doDialogText(f"FLOWERY was HEALED. ({str(flowery['hp'])}/{str(getMaxHP(4))})")
                        if not chosens[2]:
                            chosens[2] = True
                            doDialogText("YOU:# Well I don't think that was strong at all...")

                    elif curSpell == "Return.":
                        chosens[2] = True
                        continue
                    
                elif btselect == 4:
                    if not chosens[3]:
                        chosens[3] = True
                        doDialogText("FLOWERY:# From here,# you can use ITEMS you have in your inventory.# Not every item can be used,# usefully.")
                    if inventory == []:
                        doDialogText("Your inventory is empty.")
                        continue
                    else:
                        item = doDialogChoice("CHOOSE AN ITEM", choices=inventory + ["Return."])
                        if item > len(inventory):
                            continue
                        elif inventory[item-1] == "KEYCHAIN LOCKET":
                            doDialogText("You are already wearing the Keychain Locket.")
                            continue
                        else:
                            doDialogText("HOW DO YOU HAVE AN ITEM THIS EARLY IN THE GAME.", spd=6, step=2)
                            continue
                elif btselect == 5:
                    if not chosens[4]:
                        chosens[4] = True
                        doDialogText("FLOWERY:# If the enemy feels charitable enough,# maybe they don't really want to fight so you could get spared.")
                        doDialogText("         But you might wanna win their mercy first.")
                    if not firstBreakdance:
                        doDialogText("GUARDS:# Kid,# we wanna spare you,# but it's our job to defeat you now!# I'm sorry.")
                    else:
                        doDialogText("You asked the guards for mercy,# but they refused!")
                        doDialogText("GUARDS:# It's our job to kill you.# No mercy can be spared.")

                    doDialogText("It seems no mercy is possible.# You will have to defeat them.")

                # IF GUARD DIED:
                if guardA['hp'] <= 0 or guardB['hp'] <= 0:
                    stopSong()
                    if guardA['hp'] <= 0:
                        doDialogText("GUARD A was turned to dust.")
                        doDialogText("You:# What just happened?")
                        doDialogText("FLOWERY:# We defeated a guard.")
                        doDialogText("GUARD B:# WAIT PAUSE PAUSE.###", afterdelay=0)
                        doDialogText("         Guard A.#.#.#")
                        doDialogText("FLOWERY:# I feel kinda bad now...")
                        doDialogText("GUARD B:# ...### I guess you win now.# I don't really wanna die,# I'd rather get fired.")
                        doDialogText("Guard B leaves with what's left of Guard A's dust.")
                    elif guardB['hp'] <= 0:
                        doDialogText("GUARD B was turned to dust.")
                        doDialogText("You:# What just happened?")
                        doDialogText("FLOWERY:# We defeated a guard.")
                        doDialogText("GUARD A:# WAIT STOP.###", afterdelay=0)
                        doDialogText("         Guard B.#.#.## No.#.#.#")
                        doDialogText("FLOWERY:# I feel kinda bad now...")
                        doDialogText("GUARD A:# ...###### I guess you win now.# I can't fight without my buddy.")
                        doDialogText("Guard A leaves with what's left of Guard B's dust.")

                    spare = doDialogChoice("Spare the remaining guard?", choices=["Spare him.", "Don't Spare him."])

                    route4["guard_spared"] = [True, False][spare-1]

                    if spare == 2:
                        doDialogText("You channel all your energy at once...")
                        printGraphic("insert guard struck \n")
                        doDialogText("YOU DEALT 99999 DAMAGE TO THE REMAINING GUARD.", spd=6, step=3)

                        if guardA['hp'] <= 0: doDialogText("GUARD B was turned to dust.")
                        if guardB['hp'] <= 0: doDialogText("GUARD A was turned to dust.")
                        route4["on_weirdRoute"] = True
                        doDialogText("FLOWERY:# DAMN Dude I didn't know you could deal that much damage!")
                        doDialogText("YOU:# I feel.#.#.# stronger.")
                        player['lv'] = 3
                        doDialogText("YOU LEVELED UP. (LV 3)", step=2, spd=6)
                        player['attack'] += 10
                        player['defense'] += 10
                    break



                
                # GUARDS ATTACK

                doDialogText("THE GUARDS GET READY TO ATTACK!", spd=5, step=2)
                attackN = random.randint(1, 3)
                targetN = random.randint(0, 1)
                targetName = ["YOU", "FLOWERY"][targetN]
                targetStruct = [player, flowery][targetN]
                guardsATK = (guardA['attack'] + guardB["attack"])*0.7

                if attackN == 3:
                    if not firstBreakdance:
                        doDialogText("The guards took inspiration from your performance and.#.#.# perform a classical dance?")
                        doDialogText("|| SLAP! ||", spd=6, step=2)

                        dmg = 1
                        targetStruct['hp'] -= dmg
                        doDialogText(f"The guards slapped {targetName} with beautiful coordination!")
                        doDialogText(f"{targetName} lost {dmg} HP! ({targetStruct['hp']}/{getMaxHP(targetN+1)})")
                    else:
                        attackN = random.randint(1, 2)
                if attackN == 1:
                    doDialogText("The guards launch a unison attack with their spears!")
                    fResult = doTimedAttack(3, 1, 2)
                    if 0.9 <= fResult <= 1:
                        doDialogText("The Guards missed their attack!")
                    else:
                        dmg = getDamageDealt(guardsATK, targetStruct, fResult)
                        targetStruct['hp'] -= dmg

                        doDialogText(f"The guards struck {targetName}!")
                        doDialogText(f"{targetName} lost {dmg} HP! ({targetStruct['hp']}/{getMaxHP(targetN+1)})")
                elif attackN == 2:
                    doDialogText("The guards pull out GUNS?!# GET READY TO DODGE THE GUNFIRE!")
                    fResult = doTimedSpam(30)
                    if 0.7 <= fResult <= 1:
                        doDialogText("Somehow,# you dodged the bullets.")
                    else:
                        dmg = getDamageDealt(guardsATK, targetStruct, fResult)
                        targetStruct['hp'] -= dmg
                        doDialogText(f"{targetName} got caught in the gunfire!")
                        doDialogText(f"{targetName} lost {dmg} HP! ({targetStruct['hp']}/{getMaxHP(targetN+1)})")

                turn += 1
                letDownDefense = False

            if not route4['guard_spared']:
                doDialogText("FLOWERY:# That's because you just REALLY killed two guards.# The more you fight,# the stronger you get.")
                doDialogText("YOU:# Huh.#.#.# like,# I can get really strong?")
                doDialogText("FLOWERY:# Yeah,# but only if you work hard on it.")
                doDialogText("YOU:# Interesting.#.#.#")
                doDialogText("FLOWERY:# anyways you just OBLITERATED THAT TOUGH GUARD!# HE WAS ALL ARMORED UP AND STUFF?# WHAT'S UP WITH THAT?")
                doDialogText("YOU:# I don't know.#.#.# I just hit him with all I had.")
                print(end='     ')
                doDialogText("I wanna do it again.")
                doDialogText(f"FLOWERY:# You certainly have a lot of potential,# {saveFile['name']}.")
                print(end='         ')
                doDialogText("Just remember,# with great power comes great responsibility.")
                doDialogText("(.#.#.#)")


            print()
            money += 20
            doDialogText(f"YOU WON!# You now have {money} DARK DOLLARS!")
            doDialogText("FLOWERY:# Well, let's continue through the door.")
            doDialogText("YOU:# Okay.#.#.#")
            doDialogText("FLOWERY:# Hey door,# not so confident now,# huh?")
            doDialogText(".#.#.#", afterdelay = 3)
            doDialogText("It's silent.", afterdelay=3)

            print()
            save1 = getPrompt("Save this chapter here?")

            if save1:
                route4["startIndex"] = 1
                route4['players'] = [player, ashish, knight, flowery]
                saveFile["route4"] = route4


                saveFile['route4']['inventory'] = inventory
                saveFile['route4']['money'] = money

                try:
                    saveGame(curSaveName, saveFile)
                    doDialogText("The game was saved.")
                except:
                    doDialogText("There was an error in saving the game.")
            
            continue1 = getPrompt("Continue your journey?")

            if continue1:
                startindex = 1
                doDialogText("Continuing from GREAT DOOR Fight.#.#.#", afterdelay=2)
    
    if startindex == 1:

        if saveFile['route3']['rude_stay'] != "UNFORGIVED":
            doDialogText("KNIGHT:# Well,# let's continue with this journey.")
            doDialogText("ASHISH:# Okay,# let's go!")
            doDialogText("You and Ashish start following the KNIGHT.")
            print()
            doDialogText("YOU:# So where are we headed to now?")
            doDialogText("KNIGHT:# I'll tell you when we get there.")

            doDialogText("Your party eventually reaches a city covered with colors of pinkish deep red and white.")
            doDialogText("KNIGHT:# People like to call this place SNAPSHOT CITY.")
            doDialogText("ASHISH:# Snapshot...")
            doDialogText("YOU:# Hey,# look,# is something happening right now?")
            doDialogText("You, Ashish and the KNIGHT look towards a small house where a couple seems to be in an argument.")
            doDialogText("GEORGE:# Annie how many times have I told you,# I like my tea WITHOUT SUGAR.")
            doDialogText("ANNIE:# B-#But you said you like it WITH sugar-", spd=5)
            doDialogText("GEORGE:# ENOUGH!# I don't want to hear from you again.# Get out of my sight.")
            doDialogText("ANNIE:# *starts sobbing*")
            doDialogText("A woman runs out of the house and is standing outside.")
            doDialogText("ASHISH:# HEY,# THAT'S IN OUR ENGLISH TEXTBOOK!")
            doDialogText("YOU:# Yeah,# this is Mother's Day,# by that priest guy!")
            doDialogText("ASHISH:# By J.B Priestley!# Are we in my english textbook?")
            doDialogText("KNIGHT:# I think this could be your study table,# Ashish.")
            doDialogText("ASHISH:# We have to help them,# right?")
            doDialogText("KNIGHT:# Actually,# maybe the story is playing out by itself,# so I don't know if its a good idea to intervene.")
            doDialogText("YOU:# But I don't see any Mrs. Fitzgerald character here...")

            helpAnnie = doDialogChoice("Help Annie?", choices=["Help her.", "Do not help."])

            route4["helped_annie"] = ["HELPED", "NOT HELPED"][helpAnnie-1]

            if helpAnnie == 1:
                doDialogText("YOU:# Let's help her.")
                doDialogText("ASHISH:# Wait,# but what if all this was a play?")
                doDialogText("You,# Ashish and the KNIGHT walk to where Annie is.")
                doDialogText("ASHISH:# Uhm,# excuse me...")
                doDialogText("ANNIE:# *still crying*.. yes,# may i help you?")
                doDialogText("YOU:# Is your husband mistreating you?")
                doDialogText("ANNIE:# OH NO No no,# I don't think my husband is like that,# please its just.#.#.#", spd=3)
                doDialogText("KNIGHT:# Ma'am,# we can help.# We've heard everything that happened right now,# and no husband should be yelling at their wife for such a trivial matter.")
                doDialogText("ANNIE:# *sniffling* .#.#.#really?")
                doDialogText("ASHISH:# Yes,# you have to stand up for yourself!")
                doDialogText("ANNIE:# B-#but I can't.#.#.# I don't want to make trouble.")
                doDialogText(f"KNIGHT:# I have a plan.# Ashish and {saveFile['name']},# please hold Ms.Annie's hands.")
                doDialogText("YOU:# Uh,# sure,# but why?")
                doDialogText("You and Ashish hold Annie's hands.")
                doDialogText("KNIGHT USED THE SPELL BODY SWAP!", spd=5, step=2)
                doDialogText("ASHISH:# WAIT WHAT?!# YOU CAN BODY SWAP?!?!", spd=2)
                doDialogText("YOU:# OH MY GOD I'M IN MS.ANNIE'S BODY?!?!?!", spd=2)
                doDialogText("KNIGHT:# Yes,# This is one of my hidden spells.# Takes a lot out of me,# but I've been practicing.")
                doDialogText("YOU:# You had such a spell??")
                doDialogText("KNIGHT:# Now go and get back Ms.Annie's respect in the household.")
                doDialogText("ASHISH:# What about Ms. Annie?")
                doDialogText("ANNIE:# Please don't be too cruel...")
                doDialogText(f"KNIGHT:# I will spend some time with Ms. Annie.# Ashish,# keep an eye on {saveFile['name']} and help him.")
                doDialogText(f"ASHISH:# OKAY.# {saveFile['name']},# go in!")
                doDialogText("YOU:# ALRIGHT.# Let's teach this guy what he's messing with.")

                doDialogText("You walk into the house and come face to face with George Peason.")

                choices1 = ["Yes,# and I'm here to settle this."]
                if pgFilter: choices1 += ["I know honey,# I wanted to make up for what happened~"]

                mothersDay1 = doDialogChoice("GEORGE:# Annie,# I thought I told you to get lost.", choices=choices1)
                if mothersDay1 == 1:
                    doDialogText("YOU AS ANNIE:# Yes,# and I'm here to settle this.")
                    doDialogText("GEORGE:# Settle what?")
                    doDialogText("YOU AS ANNIE:# You have been mistreating me and showing me disrespect.# I won't stand for this!")
                    doDialogText("GEORGE:# Oh shut up woman,# I know you won't do anything.###", afterdelay=0)
                    doDialogText("        Well,# now that you're here,# go make me some more tea with sugar.")
                    doDialogText("YOU:# No I won't.")

                    choices2=["I won't make you tea."]
                    if pgFilter: choices2 += ["Go make your own tea,# you dick!"]
                    revenge1 = doDialogChoice("GEORGE:# What was that?", choices=choices2)
                    if revenge1 == 1:
                        doDialogText("YOU AS ANNIE:# I said I won't make you tea.")
                        doDialogText("GEORGE:# Yes you will.")
                        doDialogText("YOU AS ANNIE:# NO I WONT'T.# Until you learn to treat me with respect,# I will NOT do anything around here anymore.")
                        doDialogText("GEORGE:# You're just the housewife.# Just shut up and do what you're supposed to do.")
                        doDialogText("YOU AS ANNIE:# I am not JUST a housewife.# Is that all you see in me?")
                        doDialogText("GEORGE:# well...")
                        doDialogText("YOU AS ANNIE:# Unbelievable.# I am not doing ANY work until you apologize for neglecting me.")
                        doDialogText("GEORGE:# Annie,# wait-", afterdelay=0)
                        doDialogText("You storm off as Annie into her room.# Now to play the waiting game.", afterdelay=2)
                        doDialogText(".#.#.#")
                        doDialogText("It's taking a while.")

                    elif revenge1 == 2:
                        doDialogText("YOU AS ANNIE:# GO MAKE YOUR OWN TEA,# YOU DICK!")
                        doDialogText("GEORGE:# Annie,# what the heck has gotten into you?!")

                        doDialogText("You storm off as Annie into her room.")
                        doDialogText("GEORGE:# Annie,# wait-", afterdelay=0)
                        doDialogText("Now to play the waiting game.", afterdelay=2)
                        doDialogText(".#.#.#")
                        doDialogText("It's taking a while.")

                    doDialogText("\"psst\"")
                    doDialogText("You look over to your window,# and see ASHISH checking up on you.")
                    doDialogText("ASHISH:# *whispering* how's it going?")
                    doDialogText("YOU:# *whispering* i'm playing the waiting game.#.#.# wait until he realizes he needs me.")
                    doDialogText("ASHISH:# *still whispering* but that could take a long time!# lemme help.")
                    doDialogText("YOU:# *still whispering* what are you gonna do?")
                    doDialogText("ASHISH: *whispering* i'll make a mess in the kitchen.")
                    print(end='        ')
                    doDialogText("when he sees the mess,# he'll think of calling you to clean up the mess,# but then he will realize that he has to apologize.")
                    doDialogText("YOU:# *whispering* woah,# good plan!## leaving it to you.")
                    doDialogText("Ashish goes around the house and breaks in from another angle.")
                    doDialogText("Sure enough,# you hear sounds of someone making a mess in the kitchen.")
                    doDialogText(".#.#.# you then realize that George can also hear those sounds.")
                    doDialogText("GEORGE:# ANNIE,# IS THAT YOU?")
                    doDialogText("YOU AS ANNIE:# SHUT UP.", spd=3)
                    doDialogText("(WHAT IS HE DOING?# GEORGE WILL FIND OUT!)")
                    doDialogText("GEORGE: *from the other room* aw who the hell was here?# ANNIE!# Come clean this mess up.")
                    doDialogText("You do not respond.")
                    doDialogText("GEORGE:# Annie.#.#.#")
                    print()
                    doDialogText("""GEORGE: ==###
(Why is that woman being so stubborn today.#.#.#)###
(Did I miss her anniversary or something?)###
(Oh,# shoot.# When was it again?)###
(.#.#.# I'm gonna have to check my calendar.)###
(November 3rd.#.#.# could've never guessed that.)###
(I have an important business meeting on November 3rd.# Guess I'll skip the anniversary-)#

(.#.#.#### what am I doing?)######
(Annie's my wife.# Not just.#.#.# my housewife.)###
(I loved her.# Truly did.# Still do,# or atleast I hope.)###
(.#.#.# but do i really show that?)###
(Looking at this mess,# I can't handle all this on my own.)###
(Only if I had someone to help me.#.#.#)###
(Someone to help me.#.#.# Annie.#.#.#)
(.#.#.## is that how she felt?)###
(God damn it,# my whole life, I grew up having my parents do everything for me.)###
(They got my job for me,# I'm merely continuing my dad's business.)###
(I've never actually,# done anything for myself.)###
(Jeez,# my living situation with Annie has been basically a repeat of my privileged childhood.)###

(November 3rd,# huh?# That's easy to remember,# my phone number ends with 311,# or 3/11.)###
(I should apologize to her.#.#.#)""", spd=4, step = 1, afterdelay=3)
                    print()
                    doDialogText("You see Ashish back on your window.")
                    doDialogText("YOU:# *whispering again* how did it go?")
                    doDialogText("ASHISH:# *whispering* i almost got caught,# but mission accomplished.# now to play the waiting game.")
                    doDialogText("YOU:# *whispering* oh no i hear footsteps!# go before he sees you!")
                    doDialogText("You lie on your bed as if you're upset at your husband for forgetting your anniversary.")
                    doDialogText("GEORGE:# *knocks on your door* Annie?")
                    doDialogText("YOU AS ANNIE:# What do you want now?")
                    doDialogText("GEORGE:# May I come in?")
                    doDialogText("YOU AS ANNIE:# .#.#.#")
                    doDialogText("GEORGE:# I realize this is the first time I have asked for your permission in a long time.")
                    doDialogText("YOU AS ANNIE:# .#.#.#")
                    doDialogText("George walks in.## He's holding a broom and a towel.")
                    doDialogText("GEORGE:# Someone broke into our house and made a mess in the kitchen.")
                    print(end='        ')
                    doDialogText(".#.#.#I can't clean this up on my own.# Will you help me?")
                    doDialogText("YOU AS ANNIE:# .#.#.#")
                    if pgFilter: doDialogText("(Holy shit did that actually work?)")
                    else: doDialogText("(No way,# did that actually work?)")
                    doDialogText("Suddenly,# everything goes black.")
                    doDialogText("Your eyes feel like they are glued shut.")
                    doDialogText("When you open your eyes,# you're back in your body.")
                    doDialogText("YOU:# Wait,# what happened?")
                    doDialogText("KNIGHT:# I switched your bodies back.# Seemed like the perfect moment,# because he is going to apologize now.")
                    doDialogText("YOU:# Did I do it?")
                    doDialogText(f"KNIGHT:# Yes,# you did it.# Good job,# {saveFile['name']}.# Listen.")
                    doDialogText("You press your ear against the wall to try and hear the couple's conversation.")
                    doDialogText('"We Need to talk."')
                    doDialogText('"I realize I haven\'t been treating you right at all.# You deserve some respect.')
                    doDialogText('"I just want to say.#.#.# I\'m really sorry,# Annie."')
                    doDialogText('".#.#.# oh george!"')
                    doDialogText("You receive a pat on your shoulder:")
                    doDialogText(f"ASHISH:# Good job, {saveFile['name']}.")
                    doDialogText("YOU:# Same to you too.")

                    print()
                    doDialogText("KNIGHT:# Well,# now that the couple's marriage has been fixed,# let's go-", afterdelay=0)
                    doDialogText("\"May I ask who you three are?\"")
                    doDialogText("You turn around to see a woman holding a pack of cards,# and a pack of cigarettes.")
                    doDialogText("YOU:# You must be Mrs. Fitzgerald.")
                    doDialogText("FITZGERALD:# And how'd you know my name?")
                    doDialogText("ASHISH:# You're here to help Ms. Annie,# right?")
                    doDialogText("FITZGERALD:# Not really.")
                    doDialogText("ASHISH:# Huh?# What do you mean?")
                    doDialogText("FITZGERALD:# You dummy,# I saw you talk to her outside,# so I watched.")
                    print(end='            ')
                    doDialogText("I came here to thank y'all for doing my job for me.# Take this:")
                    doDialogText("YOU GOT THE VALENCE CHOCOLATE!", spd=5, step=2)
                    doDialogText("FITZGERALD:# A reward for your good work.# Share this with everyone.")
                    doDialogText("YOU:# Will do.")
                    inventory.append("VALENCE CHOCOLATE")
                    doDialogText("VALENCE CHOCOLATE was added to your inventory.")
                    doDialogText("ASHISH:# That looks tasty!")
                    doDialogText("KNIGHT:# Thank you,# Mrs. Fitzgerald for this gift.# We will use it wisely.")
                    doDialogText("FITZGERALD:# Shut up and let me be the one to thank you.# Now go on with your journey.")
                    doDialogText(f"KNIGHT:# Very well.# Let's go,# Ashish and {saveFile['name']}.")
                    doDialogText("You and Ashish start to follow KNIGHT once again.")
                    print()

                else:
                    doDialogText("YOU AS ANNIE:# I know hon,# I'm sorry I got you mad.#.#.#")
                    doDialogText("GEORGE:# Whatever,# make me some tea with sugar this time.")
                    doDialogText("YOU AS ANNIE:# I can give you something even better~")

                    doDialogChoice("GEORGE:# What are you hinting at?", choices=["Point towards the bedroom.", "Give him something special."])
                    doDialogText("Before you say anything,# KNIGHT breaks open the front door,# shattering the entire wall with it.", spd=2)
                    doDialogText("KNIGHT:# NOPE.# NOT HAPPENING.", spd=3)
                    doDialogText("GEORGE:# WHO IN THE WORLD ARE YOU?# AND WHY DID YOU BREAK MY FRONT DOOR-", afterdelay=0)
                    doDialogText("KNIGHT hands GEORGE a broom.")
                    doDialogText("KNIGHT:# Now that I've made a mess,# get to cleaning.# Annie won't help you clean this up until you apologize to her.")
                    print(end='        ')
                    doDialogText("She's your wife.# Maybe treat her better.", afterdelay=2)
                    doDialogText("Suddenly,# everything goes black.")
                    doDialogText("Your eyes feel like they're glued shut for a moment.")
                    doDialogText("When you open your eyes,# you're met with a speechless Ashish and a KNIGHT with her helmet in her hands.")
                    doDialogText("ASHISH:# I-# uh.#.#.#")
                    doDialogText("KNIGHT:# NEVER# do ANYTHING# like that again.#.#.## Just.#.#")
                    doDialogText("ASHISH:# I'm gonna pretend like nothing happened at all.##")
                    doDialogText("KNIGHT:# *sigh* i am not built for this type of stuff.#.#.#")
                    doDialogText("YOU:# .#.#.#")
                    doDialogText("You all collectively agree to never speak of this moment again.")
                    doDialogText("Mrs. Fitzgerald watches in complete horror of everything that just happened.", afterdelay=3)
                    print('\n')  
            else:
                doDialogText("YOU:# Let's continue with our journey.# Maybe a Fitzgerald character will appear soon.")
                doDialogText("ASHISH:# Good point.# Let's go.")

            doDialogText("Next,# you follow KNIGHT into what looks like a village.")

            # ENTERING THE WORLD OF ARAM AND THE BEAUTIFUL SUMMER HORSE
            doDialogText("YOU:# Woah,# is this an old village?")
            doDialogText("ASHISH:# Where could this place be?")
            doDialogText("You see two kids riding a beautiful white horse.")
            doDialogText("YOU:# Well that answers our question.")
            doDialogText("ASHISH:# The Summer Of The Beautiful White Horse!")
            doDialogText("KNIGHT:# There's not much we can do here,# we could just walk.")
            doDialogText("YOU:# Hey what is that guy doing?")
            doDialogText("ASHISH:# Huh?")
            doDialogText("You look over to a cliff,# with an old man on top.")
            doDialogText("He's trying to pull up what looks like a heavy box,# but the old man looks like he's struggling with it.")
            doDialogText("ASHISH:# Isn't there a pulley right next to him?# Why doesn't he do that?")
            doDialogText("YOU:# Hey look around us-# people are struggling with problems you'd see in our Physics questions!")
            doDialogText("ASHISH:# Since when did physics creep into English?# Did I keep both textbooks open?")
            doDialogText("KNIGHT:# Well,# we could help them...# or we could continue on with our journey.")

            helpPeople = doDialogChoice("Help everyone?", choices=["Help the people with their problems.", "Continue onto your journey."])

            if helpPeople == 1:
                route4["helped_everyone"] = "HELPED"
                doDialogText("ASHISH:# Sure,# let's help everyone!")
                doDialogText("YOU:# Okay.")

                doDialogText("You go to where the old man is.")
                doDialogText("ASHISH:# Excuse me,# mister,# but I think you would find it easier if you were to use that pulley here.")
                doDialogText("OLD MAN:# Oh gee,# thanks for telling me.")
                doDialogText("The OLD MAN uses the pulley.")
                doDialogText("OLD MAN:# WEEEE! THIS IS MUCH EASIER!# THANK YOU,# YOU LITTLE YOUTHLINGS!")
                doDialogText("ASHISH:# No problem,# we're just helping people.")

                doDialogText("You go to a man with a dog.")
                doDialogText("MAN WITH DOG:# Hey can I ask for help?# I need to train my dog to move through this rough muddy patch.##", afterdelay=0)
                doDialogText("              But I can't figure out how much energy he needs.# I have pills that give him 10J of energy each,# and I don't want to deal with a hyperactive dog afterwards.")
                doDialogText("YOU:# (Is this another physics question?)")
                doDialogText("MAN WITH DOG:# The patch is 8m long, and the friction is 0.2. My dog moves with an acceleration of 3m/s².# How many pills should I give him?")
                doDialogText("""ASHISH:# This is an oddly specific scenario,# but lets see...
the patch is eight metre long,# and coefficient of friction is 0.2, soo... frictional force is 0.2 x mg...""")
                doDialogText("YOU:# The force on the Dog would be: F = ma = 5x3 = 15N.")
                doDialogText("ASHISH:# And frictional force would be 0.2xmg = 0.2x10x5= 10N.")
                doDialogText("YOU:# Net resultant is 5N!")
                doDialogText("ASHISH:# And to get work done,# W = F.s = (15-10)x8 = 40J!")
                doDialogText("KNIGHT:# Watching you two work out problems together is quite amusing...")
                if pgFilter:
                    doDialogText("ASHISH:# A-#Ah...# t-#together?")
                    doDialogText("YOU:# Uhh...")
                doDialogText("ASHISH:# Give your dog 4 pills.")
                doDialogText("MAN WITH DOG:# Okay,# will do.# Thanks,# you're a lifesaver!")
                doDialogText("YOU:# Dunno how that saves lives,# but okay.")
                doDialogText("The dog was given 5 pills to get 50J.# It crosses the muddy patch succesfully,# and the dog uses it's remaining energy to fight an armed burglar that was trying to rob a house.")
                doDialogText("MAN WITH DOG:# No literally,# you're a livesaver!")
                doDialogText("YOU: ...### oh.## I see.")
                doDialogText("Next,# you approach an man holding a few bottles and writing something down frantically.")
                doDialogText("""MAN WITH BOTTLES:# Gosh darn it,# I made a Hydrocarbon by mixing Hydrogen,# Carbon and Oxygen together...
                       I know that it has 42.1% carbon,# 6.4% hydrogen,# and the remaining is oxygen.# But I am struggling to find the chemical formula for this compound...""")
                doDialogText("ASHISH:# To get the C:H:O ratio,# just divide the percentages by the mass.")
                doDialogText("YOU:# The remaining percent of oxygen has to be 100 - (42.1 + 6.4) = 51.5%")
                doDialogText("MAN WITH BOTTLES:# Then,# the ratio of the atoms would be...")
                doDialogText("The man does some quick calculations.")
                doDialogText("MAN WITH BOTTLES:# 3.5,# 6.4,# and 3.2.")
                doDialogText("YOU:# Dividing by the smallest number should give us an idea of the chemical formula.")
                doDialogText("ASHISH:# 3.5/3.2 ≈ 1,# 6.4/3.2 = 2, and 3.2/3.2 is 1.# So the formula is CH₂O?")
                doDialogText("KNIGHT:# It's C₆H₁₂O₆,# Glucose.")
                doDialogText("MAN WITH BOTTLES:# Nice,# thank you,# kids!# You're a lifesaver!")
                doDialogText("ASHISH:# No problem,# mister.")
                doDialogText("YOU:# Don't see how making glucose is really lifesaving...")
                doDialogText("MAN WITH BOTTLES:# I'm sure you know,# I'm making high energy glucose pills for the man with the dog.")
                doDialogText("YOU:# o h .")
                doDialogText("MAN WITH BOTTLES:# That dog is quite the hero,# isn't he?")
                doDialogText("KNIGHT:# What's his name?")
                doDialogText("MAN WITH DOG:# Dog man.")
                doDialogText("YOU:# .#.#.###")
                doDialogText("     Let's move on...")
                doDialogText("You move to a guy that's looking at what looks like a trap or contraption.")
                doDialogText("MAN AT PUZZLE:# I wonder...")
                doDialogText("ASHISH:# May we help you?")
                doDialogText("MAN AT PUZZLE:# Sure,# someone set a trap for my cat.# They really hate my cat.")
                doDialogText("ASHISH:# Oh thats awful!")
                doDialogText("MAN AT PUZZLE:# Yeah,# but I couldn't care less...# I'm more concerned about whether this trap even works properly.")
                doDialogText("ASHISH:# what.")
                doDialogText("MAN AT PUZZLE:# Look at this - ")
                # Symbol List wowzie:»│ ┤ ╡ ╢ ╖  ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌ 
                printGraphic("""
══════════════════╤═══════╤═══╤═══════════════════
                 (_)-----(_)  │
                 │        │   │
                 │        │ (___) <- pulley
                 │        │ │   │
                 │        │ │   │
                 │        │ │   │
              ╔══╧══╗     │ │ ╔═╧═══╗ 
              ║|2kg|║     │ │ ║|5kg|║ 
              ╚══╦══╝     (_) ╚═════╝
                 ║         │  
                 ║         │  
                 ║         │  
                 ║         │    <(O)>-?  <- cat
═════════════════╩═════════╧══════════════════════
""")
                doDialogText("MAN AT PUZZLE:# I don't think this is enough to kill my cat.#", afterdelay=0)
                doDialogText("""               From what I see,# The thick wire below the 2kg box has to be cut to activate and crush the cat.###
               but even I can tell,# with that 2kg box's weight,# the 5kg block ain't crushing no one.###
               SO tell me,# what amount of weight should I remove from the 2kg box to crush and kill my cat if it takes 25N to kill it?""")
                doDialogText("ASHISH:# Why would you want to kill your cat-", afterdelay=0)
                doDialogText("YOU:# Sure,# this is a dream anyways so let me hone my physics skills.")
                doDialogText(f"ASHISH:# {saveFile['name'].upper()}!")
                doDialogText("""YOU:# ==###
     Looking at the trap,# I can find the acceleration by taking the net force and dividing by total mass which gives us:##
     a = (5-2)g / (5+2) = 30/7 ≈ 4.2xxx##

     Thus the force delivered would be:###
     F = ma = 5x4.2 ≈ 21 N.###
     This would fall short to kill the cat,# so:
     lets see by removing 1kg from the weight.# Then the figure becomes:###""")
            
                printGraphic("""
══════════════════╤═══════╤═══╤═══════════════════
                 (_)-----(_)  │
                 │        │   │
                 │        │ (___) <- pulley
                 │        │ │   │
                 │        │ │   │
                 │        │ │   │
              ╔══╧══╗     │ │ ╔═╧═══╗ 
              ║|1kg|║     │ │ ║|5kg|║ 
              ╚══╦══╝     (_) ╚═════╝            
                 ║         │  
                 ║         │  
                 ║         │  
                 ║         │    <(O)>-?  <- cat
═════════════════╩═════════╧══════════════════════
""")
                doDialogText("""
YOU:# Then,# the acceleration would be:##
a = (5-1)g / (5+1) = 40/6 = 20/3 ≈ 6.xxx##

Then the force delivered would be:##
F = ma = 5*6 = 30,# 
More than enough to kill the cat!""")
                doDialogText("YOU:# I got it!")
                doDialogText("(SURELY this doesn't make me a lifesaver now,# does it?)")
                doDialogText("YOU:# Remove 1 kilogram from the box,# and it will be effective enough to kill the cat.")
                doDialogText("MAN AT PUZZLE:# Thanks,# you're a lifesaver!")
                doDialogText("YOU: bruh.", spd=2)
                doDialogText("""MAN AT PUZZLE:# I should probably tell you the reason why I want my cat dead:
               I actually hired someone to help me make a trap to put my cat down,# because she has been attacking people way too much nowadays.###
               Last week she killed a child,# and almost killed another one yesterday.###
               But the person I hired didn't do a very good job as you can see,# so thanks for helping me put down my cat.""")
                doDialogText("ASHISH:# Oh,# I'm so sorry.")
                doDialogText("YOU:# ........# Y'all are in life threatening situations.", spd=6)
                doDialogText("KNIGHT:# Let's not stick around for the death row.#.#.#")
                doDialogText("ASHISH:# Let's continue onto our journey.")
                doDialogText("YOU:# Wait,# I think I see someone aggressively typing on a laptop.")
                doDialogText("Indeed,# there's a guy that's raging at his laptop.")
                doDialogText("ASHISH:# Didn't know they had laptops during this time..")
                doDialogText("SD Card:# God DAMN IT!# WHY won't ANACONDA# just# RUN?!?!")
                doDialogText("YOU:# May I help you?")
                doDialogText("SD Card:# If you know how to work ANACONDA,# then sure.")
                doDialogText("ASHISH:# Anaconda?")
                doDialogText("SD Card:# I'm trying to run a code to check the output cuz I was curious,# but ANACONDA just found the PERFECT timing to stop working!")
                doDialogText("YOU:# Show me the code,# maybe I can figure it out?")
                doDialogText("SD Card shows you the code.")
                printGraphic("""
╔══════════════════════════╗
║print(10, 20, 30, end=" ")║
║print(40)                 ║
╚══════════════════════════╝
""")
                outp = doDialogChoice("What's the output?", choices=["10 20 30 \n   40", "10 20 30 40"])

                if outp == 1:
                    doDialogText("SD Card:# Okay,# let's see...")
                    doDialogText("""
- - - - - - - - - - - - - - - 
|Honestly,# I'm disappointed.|
 - - - - - - - - - - - - - - -
""")
                    doDialogText("SD Disappeared into thin air.")
                    doDialogText("ASHISH:# ...was that the wrong answer?", spd=5)
                    doDialogText("YOU:# I dunno,# never heard of ANACONDA,# but I think he meant python.")
                elif outp == 2:
                    doDialogText("SD Card:# Okay let's see...")
                    doDialogText("|I'm glad you remembered.|")
                    doDialogText("SD Disappeared into thin air.")
                    doDialogText("YOU:# W-#What just happened?")
                    doDialogText("ASHISH:# He just...# disappeared.")
                    doDialogText("YOU: ...")
                    doDialogText("ASHISH:# Let's just continue onto our journey now.")
            else:
                doDialogText("YOU:# Let's continue onto our journey now.")

            print()

            doDialogText("You now follow the KNIGHT to an Inn...?")
            doDialogText("KNIGHT:# For now,# let's take some rest at this Inn.")
            doDialogText("The KNIGHT books two rooms.")
            doDialogText("KNIGHT:# You two don't mind sharing a room together,# right?")

            blush = False
            if nameChoice == "NORMAL": blush = True
            elif nameChoice == "RUDE" and saveFile['route1']['rude_choice']: blush = True
            if blush and pgFilter:
                doDialogText("ASHISH:# T-#Together?")
                print(end="        ")
                doDialogText("I guess not.#.#.#")
                doDialogText("He tries to hide it,# but you can see him blushing.")

                doDialogText("YOU:# O-#kay,# I'm# fine with it as well.#.#.#")
            else:
                doDialogText("ASHISH:# Uhh,# go ahead.")

            doDialogText("KNIGHT:# Alright,# let's go in.")
            doDialogText("You and Ashish walk into the Inn with KNIGHT.")
            doDialogText("KNIGHT:# Two rooms please,# one for me and one for these two.")
            doDialogText("RECEPTIONIST:# Will do.# That'll be 40 DARK DOLLARS.")
            doDialogText("Your room has been #purchased.")
            doDialogText("You walk into your room with Ashish.")
            doDialogText("YOU:# Nice place,# huh?")
            doDialogText("ASHISH:# Yea.#.#.## It actually resembles my bedroom a lot.")
            doDialogText("YOU:# Huh,# you're right.# It does look like your bedroom.# Just a little emptier.")
            doDialogText("ASHISH:# Yea...### there are also some books here.# Maybe they're mine as well?")
            doDialogText("You flip through the pages of the books.")
            doDialogText("YOU:# Nothing familiar to me.")
            doDialogText("ASHISH:# .#.#.#")
            print(end="        ")
            doDialogText("I've read these books as well.# But they shouldn't be in my study table.#.#.#")
            doDialogText("YOU:# Oh,# I guess this entire world really is just your room.#.#.## with other people in it.")
            doDialogText("ASHISH:# Yeah.#.#.#")

            if blush and pgFilter:
                doDialogText("(It's awkward.)")
                doDialogText("(It's HELLA awkward.)")
                doDialogText(f"ASHISH:# (It's strange,# and awkward as well.#.#.## Having {saveFile['name']} next to me.#.#.#)")
                doDialogText("YOU AND ASHISH:# (In the same room.#.#.#)", afterdelay=2)

            # GAMING MOMENT
            doDialogText("You suddenly spot a faint flicker tucked beneath one of the beds.")
            doDialogText("YOU:# Ashish,# is that your computer?")
            doDialogText("ASHISH:# My computer?# Let me see.#.#.#")
            print(end="        ")
            doDialogText("It is my computer.#.#.# wonder what it's doing here.")
            doDialogText("YOU:# What's on it?")
            doDialogText("ASHISH:# Let me boot it up.")
            doDialogText("You and Ashish boot up the computer.")
            doDialogText("The screen turns on with a quick flicker.")
            doDialogText("As if it knows what we're looking for,# it takes us directly to the desktop without the boot sequence.")
            doDialogText("Only one folder remains on the desktop.#.#.#")
            doDialogText("ASHISH:# A heart folder?")
            doDialogText("YOU:# What's inside it?")
            doDialogText("Ashish opens the folder.")
            doDialogText("ASHISH:# It's a game.")
            doDialogText("YOU:# What game is it?")
            doDialogText("ASHISH:# Its.#.#.# the one I played last week?# But something's different.#.#.#")
            doDialogText("YOU:# Do you wanna play it,# together?")
            doDialogText("ASHISH:# UHH,### sure.##")
            doDialogText("Ashish opens the game.")
            skipIntro = False
            if saveFile['route4']['COMPLETED']:
                skipIntro = getPrompt("Skip this intro?")
            if not skipIntro:
                doEpicIntro(soundImportSuccesful)
            doDialogText("YOU:# Wow,# that's interesting.# What's the game about?")
            doDialogText("ASHISH:# About a boy who discovers the realm of darkness and saves people from having nightmares.")
            doDialogText("YOU:# Woah,# that's kinda cool.")
            doDialogText("As Ashish did say,# this game follows a young boy who finds a way to enter people's dreams.")
            doDialogText("He uses this power to save people from having bad dreams and encouraging them.")
            doDialogText("He discovers a knife that can cut through the real realm and step into the world of dreams.#.#.#")
            doDialogText("He doesn't know which person's dream he is in,# but he tries his best to make their dreams better.")
            doDialogText("Even if it ends up hurting him in the process.", afterdelay=1.2)
            print()
            rudeChoice = saveFile['route1']['rude_choice']
            if pgFilter:
                if nameChoice == "NORMAL" or (nameChoice == "RUDE" and rudeChoice == "APOLOGISED"):
                    doDialogText("Watching Ashish play this game,# completely invested in it, not even paying mind to you.#.#.#")
                    doDialogText("You start to fall for him.#.#.#")
                    doDialogText("(Wait,# what the hell am I thinking?# I'm not gay!)")
                    doDialogText(f"ASHISH:# {saveFile['name']},# you okay?")
                    doDialogText("YOU:# U-#uh,# yeah I'm alright.")
                    doDialogText("(Am I really.#.#.# falling for him?)")
            doDialogText("YOU:# Is anything different?")
            doDialogText("ASHISH:# Uhm,# yeah.# The story is still the same,# but the artwork and gameplay is more polished.")
            print(end="        ")
            doDialogText("Also everything is a dark color now,# like it's in dark mode.# But it's really soothing,# and I honestly prefer this over the original.")
            doDialogText("YOU:# Must be the dream.")
            doDialogText("ASHISH:# .#.#.# I haven't gotten this far quickly.#.#.#")
            doDialogText("YOU:# What do you mean?")
            doDialogText("ASHISH:# It's like the game knows I've played this already upto this part and sped everything up.")
            doDialogText("YOU:# Wow.# Guess this dream is really alive.")
            doDialogText(f"ASHISH:# {saveFile['name']},# what do I do here?# I'm stuck on a decision.")
            doDialogText("YOU:# Uh,# what is it?")
            doDialogText("ASHISH:# Do I recruit this guy into my team or do I kill him?")
            doDialogText("You look at the screen.# It looks like you have an option to recruit the enemy into your party or to kill him.")
            recruit = doDialogChoice("Recruit him?", choices=['Recruit the enemy.', 'Kill the enemy.'])
            if recruit == 1:
                doDialogText("YOU:# You could recruit that guy.")
                check = doDialogChoice("ASHISH:# Are you sure?# This could change some important parts of the game.")
                if check == 1:
                    route4['on_weirdRoute'] = False
                    doDialogText("YOU:# Yeah,# I'm sure.# Recruit him.")
                    doDialogText("ASHISH:# Okay.")
                    doDialogText("The enemy was recruited.")
                else:
                    doDialogText("YOU:# Nevermind.")
                    doDialogText("ASHISH:# Okay,# kill it is.")
                    doDialogText("The enemy was slain.")
            else:
                doDialogText("YOU:# Nah,# don't recruit him.# What if he tries to attack you while you're vulnerable?")
                doDialogText("ASHISH:# Good point.# Kill it is.")
                doDialogText("The enemy was slain.")
            doDialogText(".#.#.#")
            doDialogText("You feel like your choice had an effect.")
            doDialogText("ASHISH:# The game closed.")
            doDialogText("YOU:# Did you finish it?")
            doDialogText("ASHISH:# No-# it just closed on its own after saying that this was the demo.")
            doDialogText("YOU:# Oh.")
            doDialogText("ASHISH:# Maybe it's because this is a dream and the game is incomplete cuz I haven't played the whole thing yet.")
            doDialogText("YOU:# Hmm.#.#.# That's solid.")
            doDialogText("ASHISH:# Well.#.#.# I guess I shall sleep now.")
            doDialogText("YOU:# I'll go to sleep as well.# Good night.")
            doDialogText("ASHISH:# Goodnight.", afterdelay=5)

            save2 = getPrompt("Save this chapter here?")

            if save2:
                route4["startIndex"] = 2
                route4['players'] = [player, ashish, knight, flowery]
                saveFile["route4"] = route4
                saveFile['route4']['inventory'] = inventory
                saveFile['route4']['money'] = money

                try:
                    saveGame(curSaveName, saveFile)
                    doDialogText("The game was saved.")
                except:
                    doDialogText("There was an error in saving the game.")
            
            continue2 = getPrompt("Continue your journey?")

            if continue2:
                startindex = 2
                doDialogText("Continuing from INN.#.#.#")
                doDialogText("The Finale Approaches.", afterdelay=2)
        else:
            doDialogText("After passing through the great door,# you find yourself in a huge white room.")
            doDialogText("The walls are shiny enough to reflect your image.")

            doDialogText("YOU:# What is this place?")
            doDialogText("FLOWERY:# I think this is supposed to be the living room.")
            doDialogText("         Let's keep walking.")
            print()

            doDialogText("Soon,# you end up on a gray section of the ground,# with little squares on it.")
            doDialogText("You pressed the red square.")
            doDialogText("YOU:# Are these buttons?")
            doDialogText("FLOWERY:# Oh,# I think this might be the TV remote.")
            doDialogText("YOU:# If this is a TV remote,# where's the TV?")
            doDialogText("FLOWERY:# There?")
            doDialogText("Flowery points to a section of a wall,# which is now covered with static.")
            doDialogText("YOU:# That wasn't there before,# right?")
            doDialogText("FLOWERY:# No,# I don't think so.")
            doDialogText("YOU:# Wait,# can we actually get something on the TV?# I wonder.")
            doDialogText("FLOWERY:# Go hit the channel button!")
            print()
            doDialogText("You find the channel buttons and start hitting them.")
            doDialogText("The static flickers,# but it still is static.")
            doDialogText("You notice with each press of the button,# the static slowly fades away.")
            doDialogText("FLOWERY:# Keep hitting them!# I think we're getting closer!")
            
            doDialogText("Until suddenly,# the landscape changes.")
            doDialogText("The entire room suddenly turns into a long red hallway that slowly closes into a smaller box.")
            doDialogText("A long table and some chairs appear out of the ground with a carpet as well.")
            doDialogText("The giant TV on the screen flashes a logo that says.#.#.#")
            doDialogText("...REVIEWER'S PARADOX?",afterdelay = 1.6)
            print()

            playSong('assets/soundtrack/tv_show_1.ogg', looping = False)
            doDialogText("???:# WELCOME,# TO REVIEWER'S PARADISE!!!!!!!!!!!", step=3, spd = 9)
            doDialogText("SR. CAR:# I'm your host,##### SR.###### CAR########,# and you're on the FAMOUS NIGHTLY PREMIERE OF THE NIGHT!!!!!")
            doDialogText("SR. CAR:# WE HOPE YOU HAVE FUN!", afterdelay = 3)
            print()

            
            if pgFilter: 
                doDialogText("YOU:# Who the fuck?!?!")
                stopSong()
                print()
                doDialogText("SR. CAR:# Ooohhhh.#.#.# sorry,# but on this show,# we don't tolerate swears!")
                doDialogText("SR. CAR:# WHITE,###### CENSOR HIS ASS!")
                print()
                
                # UPDATE: REMASTER THIS GOOFY AHH SONG PLEASEEE
                playSong('assets/soundtrack/lie.ogg')
                doDialogText("A Giant Whitener appears out from the TV with the host.")
                doDialogText("YOU:# WHAT THE FUCK ARE YOU?!??!")
                doDialogText("SR. CAR:# I suggest you don't struggle,# WHITE hates that.")
                doDialogText("YOU:# N-#NO WAIT,## I TAKE THAT BACK-# WHAT ARE YOU DOING GET AWAY FROM ME NO# NO# NONONONO-#", afterdelay=1, spd=3)
                print()
                stopSong()
                doDialogText("You got whitened.")
                print()

            else: doDialogText("YOU:# Who the heck?!?!")

            stopSong()
            
            playSong('assets/soundtrack/tv_show_2_loop.ogg', looping=True)
            doDialogText("SR. CAR:# Welcome to our WEDNESDAY NIGHT GAMESHOW!")
            doDialogText("         And we already have two contestants up here.# PLEASE enter your names right about.#.#.#")
            doDialogText("         Here: ", line=False, afterdelay=0)
            input("")

            print()
            doDialogText("SR. CAR:# Well then,# let's explain how this works for anyone that's new here.")
            doDialogText("         Three rounds will be held.# Each round will be a different game played by these contestants.")
            doDialogText("         If they finish all the games with the highest accuracy,# then they will get rewarded with the best prize we have in stock:")
            doDialogText("         Yes,# that's right!# The fabled,## rumored to be,## rarest mechanic machinery to ever machine out a mechanic,### INORGANIC WINNER:")
            print()
            doDialogText("         THE AUTO COOKER!!!")
            doDialogText("SR. CAR pulls off a table cloth to reveal what looks like an airfryer on screen.")
            doDialogText("SR. CAR:# This may look like an ordinary airfryer,# but DON'T BE FOOLED.")
            doDialogText("         Simply explained,# this machine dispenses INFINITE FOOD,# depending on your view of food and whether or not you accept:", afterdelay=0.4)
            print()
            doDialogText("         OUR BELOVED MALABAR CHICKEN CURRY!### Designed to heal you to FULL HEALTH in one use.")
            doDialogText("(What is going on.#.#.#)")
            doDialogText("SR. CAR:# Now,# without further ado,", afterdelay=1.6)
            doDialogText("         LETS GET STARTED!!!!!", spd=5, afterdelay=3)
            print()

            doDialogText("ROUND 1:# BOOKSWEEPER!")
            doDialogText("SR. CAR:# Have you ever played MINESWEEPER?")
            doDialogText("         It's the same thing.# A book will be hidden in a square inside a square grid,# and each square will be labeled with a number.")
            doDialogText("         After each guess,# the distance from the correct position will be given to you,# based of which you have to make your next guess.")
            doDialogText("         Now,#### ENJOY!")

            stopSong()
            # GAME STARTS
            books = ['HARDCOVER BOOK', 
                     'SIGNED BOOK', 
                     'RUINED BOOK', 
                     'BESTSELLING BOOK', 
                     'COLLECTORS BOOK', 
                     'SOME NERDS DIARY']
            yourBooks = []

            attempts = 0

            playSong('assets/soundtrack/tv_show_3.ogg', looping=True)

            # ROUND 1
            print('\n')
            doDialogText("LEVEL 1:",spd = 7)
            print()
            coords = (random.randint(0, 2), random.randint(0, 2))
            while True:
                attempts += 1

#Symbol List wowzie:»│ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌ 
                printGraphic(''' 
╔═══╦═══╦═══╗
║ 1 ║ 2 ║ 3 ║
╠═══╬═══╬═══╣
║ 4 ║ 5 ║ 6 ║
╠═══╬═══╬═══╣
║ 7 ║ 8 ║ 9 ║
╚═══╩═══╩═══╝
''')
                doDialogText("Pick a square:# ", spd=1, line=False)
                n = int(askNum())
                x = n%3
                y = (n-1)//3

                d = round(((x - coords[0])**2 + (y - coords[1])**2)**0.5, 2)

                print("DISTANCE:", d)
                if d == 0: 
                    print()
                    book = books.pop(random.randint(0, len(books)-1))
                    if book != 'SOME NERDS DIARY':
                        doDialogText(f"YOU GOT {book}!")
                    else:
                        doDialogText("YOU GOT.#.#.# what looks like some nerd's diary.")
                        doDialogText("SR. CAR:# How did that get there.")
                        doDialogText("         Give me that.")
                        book = books.pop(random.randint(0, len(books)-1))
                        doDialogText(f"       Here,# take this {book} instead.")
                        yourBooks.pop()
                    yourBooks.append(book) 
                    break
            
            
            # ROUND 2
            print('\n')
            doDialogText("LEVEL 2:", spd=7)
            print()
            coords = (random.randint(0, 3), random.randint(0, 3))
            while True:
                attempts += 1

#Symbol List wowzie:»│ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌ 
                printGraphic(''' 
╔═══╦═══╦═══╦═══╗
║ 1 ║ 2 ║ 2 ║ 4 ║
╠═══╬═══╬═══╬═══╣
║ 5 ║ 6 ║ 7 ║ 8 ║
╠═══╬═══╬═══╬═══╣
║ 9 ║ 10║ 11║ 12║
╠═══╬═══╬═══╬═══╣
║ 13║ 14║ 15║ 16║
╚═══╩═══╩═══╩═══╝
''')
                doDialogText("Pick a square:# ", spd=1, line=False)
                n = int(askNum())
                x = n%4
                y = (n-1)//4

                d = round(((x - coords[0])**2 + (y - coords[1])**2)**0.5, 2)

                print("DISTANCE:", d)
                if d == 0: 
                    print()
                    book = books.pop(random.randint(0, len(books)-1))
                    if book != 'SOME NERDS DIARY':
                        doDialogText(f"YOU GOT {book}!")
                    else:
                        doDialogText("YOU GOT.#.#.# what looks like some nerd's diary.")
                        doDialogText("SR. CAR:# How did that get there.")
                        doDialogText("         Give me that.")
                        book = books.pop(random.randint(0, len(books)-1))
                        doDialogText(f"       Here,# take this {book} instead.")
                        yourBooks.pop()
                    yourBooks.append(book) 
                    break
            
            # ROUND 3
            print('\n')
            doDialogText("LEVEL 3:", spd=7)
            print()
            coords = (random.randint(0, 5), random.randint(0, 3))
            coordBox = {
                    1: (0, 0),
                    2: (1, 0),
                    3: (2, 0),
                    4: (3, 0),
                    5: (0, 1),
                    6: (1, 1),
                    7: (2, 1),
                    8: (3, 1),
                    9: (4, 1),
                    10: (0, 2),
                    11: (1, 2),
                    12: (2, 2),
                    13: (3, 2),
                    14: (4, 2),
                    15: (5, 2),
                    16: (0, 3),
                    17: (1, 3),
                    18: (2, 3),
                    19: (3, 3),
                    20: (4, 3)
                }
            
            while coords not in coordBox.values(): 
                if coords: coords = (random.randint(0, 5), random.randint(0, 4))
                print(coords)
            while True:
                attempts += 1

#Symbol List wowzie:»│ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌ 
                printGraphic(''' 
╔═══╦═══╦═══╦═══╗
║ 1 ║ 2 ║ 2 ║ 4 ║
╠═══╬═══╬═══╬═══╬═══╗
║ 5 ║ 6 ║ 7 ║ 8 ║ 9 ║
╠═══╬═══╬═══╬═══╬═══╬═══╗
║ 10║ 11║ 12║ 13║ 14║ 15║
╠═══╬═══╬═══╬═══╬═══╬═══╝
║ 16║ 17║ 18║ 19║ 20║
╚═══╩═══╩═══╩═══╩═══╝
''')
                doDialogText("Pick a square:# ", spd=1, line=False)
                n = int(askNum())
                x, y = coordBox[n]

                d = round(((x - coords[0])**2 + (y - coords[1])**2)**0.5, 2)

                print("DISTANCE:", d)
                if d == 0: 
                    print()
                    book = books.pop(random.randint(0, len(books)-1))
                    if book != 'SOME NERDS DIARY':
                        doDialogText(f"YOU GOT {book}!")
                    else:
                        doDialogText("YOU GOT.#.#.# what looks like some nerd's diary.")
                        doDialogText("SR. CAR:# How did that get there.")
                        doDialogText("         Give me that.")
                        book = books.pop(random.randint(0, len(books)-1))
                        doDialogText(f"       Here,# take this {book} instead.")
                        yourBooks.pop()
                    yourBooks.append(book) 
                    break
            
            # ROUND 4
            print('\n')
            doDialogText("FINAL LEVEL:", spd=7)
            print()
            coords = (random.randint(0, 5), random.randint(0, 3))
            coordBox = {
                    1: (1, 0),
                    2: (2, 0),
                    3: (4, 0),
                    4: (5, 0),
                    5: (0, 1),
                    6: (1, 1),
                    7: (2, 1),
                    8: (3, 1),
                    9: (4, 1),
                    10: (5, 1),
                    11: (6, 1),
                    12: (0, 2),
                    13: (1, 2),
                    14: (2, 2),
                    15: (3, 2),
                    16: (4, 2),
                    17: (5, 2),
                    18: (6, 2),
                    19: (1, 3),
                    20: (2, 3),
                    21: (3, 3),
                    22: (4, 3),
                    23: (5, 3),
                    24: (2, 4),
                    25: (3, 4),
                    26: (4, 4),
                    27: (3, 3)
            }
            while coords not in coordBox.values(): coords = (random.randint(0, 5), random.randint(0, 3))

            while True:
                attempts += 1

# Symbol List wowzie:»│ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌ 
                printGraphic(''' 
    ╔═══╦═══╗   ╔═══╦═══╗ 
    ║ 1 ║ 2 ║   ║ 3 ║ 4 ║         
╔═══╬═══╬═══╬═══╬═══╬═══╬═══╗
║ 5 ║ 6 ║ 7 ║ 8 ║ 9 ║ 10║ 11║
╠═══╬═══╬═══╬═══╬═══╬═══╬═══╣
║ 12║ 13║ 14║ 15║ 16║ 17║ 18║
╚═══╬═══╬═══╬═══╬═══╬═══╬═══╝  
    ║ 19║ 20║ 21║ 22║ 23║   
    ╚═══╬═══╬═══╬═══╬═══╝
        ║ 24║ 25║ 26║
        ╚═══╬═══╬═══╝
            ║ 27║
            ╚═══╝
''')
                doDialogText("Pick a square:# ", spd=1, line=False)
                n = int(askNum())
                
                x, y = coordBox[n]

                d = round(((x - coords[0])**2 + (y - coords[1])**2)**0.5, 2)

                print("DISTANCE:", d)
                if d == 0: 
                    print()
                    book = books.pop(random.randint(0, len(books)-1))
                    if book != 'SOME NERDS DIARY':
                        doDialogText(f"YOU GOT {book}!")
                    else:
                        doDialogText("YOU GOT.#.#.# what looks like some nerd's diary.")
                        doDialogText("SR. CAR:# How did that get there.")
                        doDialogText("         Give me that.")
                        book = books.pop(random.randint(0, len(books)-1))
                        doDialogText(f"       Here,# take this {book} instead.")
                        yourBooks.pop()
                    yourBooks.append(book) 
                    break
            
            stopSong()
            if attempts >= 56:
                route4['srcar_1'] = 'ASS'
                doDialogText("SR. CAR:# Well.#.#.#")
                doDialogText("         I think you would've done better if you just guessed every single square.")
            elif 56 > attempts >= 38:
                route4['srcar_1'] = 'BAD'
                doDialogText("SR. CAR:# I could see a little suffering in your tries.")
            elif 38 > attempts >= 20:
                route4['srcar_1'] = 'OK'
                doDialogText("SR. CAR:# Good job!# It was FUN,# right?")
            elif 20 > attempts >= 10:
                route4['srcar_1'] = 'GOOD'
                doDialogText("SR. CAR:# Great job!# You did fairly well.")
                doDialogText("         That was FUN,# right?")
            elif 10 > attempts >= 5:
                route4['srcar_1'] = 'GREAT'
                doDialogText("SR. CAR:# Wow,# that was insanely good!")
            elif 5 > attempts >= 4:
                saveFile['srcar_1'] = 'PERFECT'
                doDialogText("SR. CAR:# That.#.# was an impossible achievement.")
                doDialogText("         YOU GOT EVERYTHING PERFECTLY RIGHT!")
                doDialogText("         This deserves a great prize,# but since we didn't actually expect anyone to guess everything perfectly because of how rare it is.#.#.#")
                doDialogText("         .#.#.#unfortunately you have to keep playing for the prize.")
            else:
                route4['srcar_1'] = 'CHEATER'
                doDialogText("SR. CAR:# How did you.#.#.#")
                doDialogText("         Nevermind.")
            
            

            
            doDialogText("         Well,# it's time to move on to the next game:")

            print()
            
            doDialogText("ROUND 2:# BEFRIENDMENT!")
            doDialogText("SR. CAR:# This one is a unique minigame that we came up with.")
            doDialogText("         We put almost all our budget into this one!")
            doDialogText("         Now spin this wheel!")
            doDialogText("You spin the wheel that you feel came out of nowhere.")
            doDialogText(".#.#.#")
            
            doDialogText("A white light fills the room.")
            print()
            doDialogText("SR. CAR:# Welcome.#.#.#")
            doDialogText("         To The Institute of Magic and Wizardry!")
            doDialogText("The light fades away,# and you find yourself at Hogwarts.")
            doDialogText("YOU:# A-### Are we in Harry Potter??")
            doDialogText("SR. CAR:# Not exactly, You're in our version of Hogwarts.")
            doDialogText("         This is a simulated experience of.#.#.#")
            stopSong()

            doDialogText("         A Dating Sim!")
            doDialogText("YOU:# .#.#.####what.")
            doDialogText("SR. CAR:# I feel like I don't need to explain more.#")
            doDialogText("         Find your sweetheart,# and ENJOY!")
            doDialogText("YOU:# HEY WAIT A MINUTE GET BACK HERE!", spd=3)
            doDialogText("SR. CAR Disappeared.")
            doDialogText("YOU:# .#.#.#")
            doDialogText("     Well,# guess we're on our own now.")
            doDialogText("FLOWERY:# I've never been to school before.")
            doDialogText("YOU:# Oh,# you're no longer a massive flower now.#.#.#")
            doDialogText("     You're in a flower pot.")
            doDialogText("FLOWERY:# Oh yeah.# Guess he must've done that.")
            doDialogText("YOU:# I think you could pass off as a talking flower.")
            doDialogText("FLOWERY:# Good idea actually.")
            print()

            doDialogText("YOU:# Oh,# it seems I also got a bag of resources when we spawned here.")
            doDialogText("FLOWERY:# What's in it?")
            doDialogText("YOU:# There's only a flask.#.#.#")
            doDialogText("You take a sip of the flask.")
            doDialogText("YOU:# .#.#.# it's hot chocolate.")
            doDialogText("FLOWERY:# Oh,# does it restore HP?")
            doDialogText("YOU:# Not really,# I didn't feel anything.")
            doDialogText("FLOWERY:# okay.#.#.# Well let's head inside now.")
            
            print()
            playSong('assets/soundtrack/magic.ogg', looping=True)
            doDialogText("You make your way into the building.")
            doDialogText("RECEPTIONIST:# Oh!# We've been expecting you.", spd=3)
            doDialogText("              Uhh,# you must be.#.#.#", spd=3)
            doDialogText(f"YOU:# {saveFile['name']}.")
            doDialogText("     Can you tell me where my class is?")
            doDialogText("RECEPTIONIST:# Right.# Your class is.#.#.#")
            doDialogText("              D 11, under Ms. Shilda.")
            doDialogText("              But right now,# you have to attend the opening ceremony!# Go straight,# take a right,# get on the floating stairs and go to the seventh floor,# and keep going straight until you find a rope hanging from the ceiling.# Grab onto that rope and close your eyes.", spd=2)
            doDialogText("YOU:# Oh,# uh.#.#.# could you repeat that-", spd=5, afterdelay=0)
            doDialogText("RECEPTIONIST:# No time!# Give me the flower,# I'll put it in your dorm room.")
            
            giveUp = doDialogChoice('Give up FLOWERY?', choices=['Give FLOWERY to the RECEPTIONIST', 'Keep FLOWERY'])

            if giveUp == 1:
                doDialogText("YOU:# Oh.#.#.# here.")
                doDialogText("You gave FLOWERY to the RECEPTIONIST.")
                doDialogText("RECEPTIONIST:# I'll keep him in your dorm room.# The rest of your belongings are already there.")
                doDialogText("YOU:# Okay.#.#")
                doDialogText("RECEPTIONIST:# Now hurry!")
                print()
                doDialogText("You start running.")
            else:
                doDialogText("YOU:# Oh no thanks,# I'll keep him.")
                doDialogText("RECEPTIONIST:# Okay,# now hurry up!")
                print()
                doDialogText("You start running with FLOWERY in your hand.")
            
            doDialogText("YOU:# Wait a minute,# did she say to get on floating stairs?")
            doDialogText("And there,# right in front of you are the floating stairs.")
            doDialogText("(This is bizzare).")
            'SR. CAR:# I\'d say that is indeed.#.#.#'
            '         Pretty Bizzare.' 
            doDialogText("You make your way to the seventh floor.")
            doDialogText("After walking enough,# you find a rope hanging from the ceiling.")
            doDialogText("YOU:# I have to grab this and close my eyes?")
            doDialogText("You grab the rope and close your eyes.")
            doDialogText("When you open your eyes,# you find yourself in a seat in a hall with murmuring students.")
            doDialogText("YOU:# What the-", afterdelay=0)
            doDialogText('"SHH!# The Dean\'s almost here!"')
            
            doDialogText("The very next second,# you spot someone walking onto the stage.")
            print()
            doDialogText("DEAN:# Welcome,# everyone,# to the magical institute of Devagiri.")
            doDialogText("The crowd is still murmuring.")
            doDialogText("DEAN:# .#.#.#")
            pauseSong()
            doDialogText("      SILENCE.")
            doDialogText("The crowd became silent.")
            print()
            doDialogText("DEAN:# Anyways.#.#.## as I was saying.#.#.#")
            pauseSong()
            doDialogText("      My name is Saint Dumbledore Cardeacurus,# and I'm the humble DEAN of this institute.")
            doDialogText("      Welcome to your new school of Magic and Wizardry.")
            doDialogText("      This school is a highly prestigious school of magic,# one of the top schools in the district...###")
            doDialogText("The DEAN starts yapping about how the school is prestigious and historious and stuff.#.#.#")
            doDialogText("The details bore you to death.")
            print()
            doDialogText("\"As he looks towards his right,# he comes eye to eye with a student.#.#.#")
            doDialogText("A shy student named.#.#.### ASHTON.\"")
            doDialogText("(Yo who is narrating this?)")

            ashtonChoices1 = ['Ask about the DEAN\'s speech.', 'Ask about the school.', 'Ask about ASHTON.']

            while ashtonChoices1:
                ashton1 = doDialogChoice('What do you say to ASHTON?', choices = ashtonChoices1)

                action = ashtonChoices1.pop(ashton1 - 1)
                if action == 'Ask about the DEAN\'s speech.':
                    doDialogText("YOU:# Boring speech,# right?")
                    doDialogText("ASHTON:# O-# oh,# I actually find it quite interesting to learn more about the school's history and heritage.")
                    doDialogText("YOU:# Oh.#.#.#")
                    doDialogText("     Nerd.")
                    print()
                elif action == 'Ask about the school.':
                    doDialogText("YOU:# What's so great about this school anyways?")
                    doDialogText("ASHTON:# U-#uh,# I don't know if you didn't hear,# but the DEAN was talking about it the whole time.")
                    doDialogText("YOU:# That's true.#.#.#")
                    print()
                elif action == 'Ask about ASHTON.':
                    doDialogText("YOU:# So why'd you come to this school?")
                    doDialogText("ASHTON:# U-#uh,# to study magic?")
                    doDialogText("YOU:# Well,# duh.# Why do you want to study magic?")
                    doDialogText("ASHTON:# T-#To be a wizard??")
                    doDialogText("YOU:# Oh my god.#.#.#")
                    doDialogText("ASHTON:# I want to be a wizard.#.#.# just like my dad.")
                    doDialogText("        Really get into the world of magic.")
                    doDialogText("        Then maybe I can find my dad.#.#.#")
                    doDialogText("        And also I just love magic in general.")
                    doDialogText("YOU:# Oh.# Sweet.")
                    doDialogText("ASHTON:# What about you?")
                    doDialogText("YOU:# oh.#.#.#", spd=5)
                    doDialogText("      i dunno.")
                    doDialogText("ASHTON:# oh.#.#.#", spd=6)
                    print()
                
            
            doDialogText("ASHTON:# O-#oh,# by the way,# my name is ASHTON.# Nice to meet you.")
            doDialogText("YOU:# Well.#.#.# nice to meet you too,# ASHTON.")
            doDialogText("     Or more like ASHCHEEKS.")
            'SR. CAR:# WHAT?!# WHO WROTE THIS STORY?!?!'
            '         I THOUGHT THIS WAS SUPPOSED TO BE CUSS-FREE!'
            doDialogText("As you said that,# you felt a WHITE-ning sensation crawling behind your back.")
            doDialogText("ASHTON:# H-#hey,# that's mean!")
            doDialogText("YOU:# It may not be nice,# but its sure as hell what's written on your book.")
            doDialogText("ASHTON:# WHAT?!")
            doDialogText("Ashton checks his book that he was holding.# Indeed,# someone wrote ASHCHEEKS on his book.")
            'SR. CAR:# Whoever proofread this script is getting fired tonight.#.#.#'
            doDialogText("ASHTON:# Oh my gosh,# I'm so sorry.#.#.#")
            doDialogText("        Someone must have written that on my book.#.#.#")
            doDialogText("YOU:# Don't worry,# I'd say it's a funny nickname.")
            doDialogText("ASHTON:# .#.#.#")
            if giveUp == 2:
                doDialogText("        A-#Also,# I hope you don't mind me asking,# but.#.#.#")
                doDialogText("        What's with the flower?")
                doDialogText("YOU:# Oh,# this guy?")
                doDialogText("FLOWERY:# Hello Ashton.")
                doDialogText("ASHTON:# A-#AH! It speaks?!")
                doDialogText("YOU:# What?# Never seen a talking flower before?")
                doDialogText("ASHTON:# N-#No!# Where'd you get him from?")
                doDialogText("YOU:# U-#uh,# you see I found him on the gro-", afterdelay=0)
                doDialogText("FLOWERY:# I was a gift from a powerful wizard.")
                doDialogText("YOU:# .#.#.#")
                doDialogText("ASHTON:# .#.#.?")
                doDialogText("YOU:# .#.#.#yeah.")
                doDialogText("FLOWERY:# I sure do miss Hagrid.")
                doDialogText("ASHTON:# Oh.#.#.# that's pretty cool.")
            print()
            pauseSong()
            doDialogText("DEAN:# HEY,# YOU TWO LOVEBIRDS!")
            doDialogText("YOU:# ?")
            doDialogText("ASHTON:# Oh no.#.#.#")
            doDialogText("DEAN:# Are you two talking in the middle of my speech?")
            doDialogText("ASHTON:# OH,# NONO,# IT WAS NOTHING LIKE THAT-#", afterdelay=0)
            doDialogText("DEAN:# QUIET!")
            doDialogText("      And you,# stand up right now.")
            doDialogText("YOU:# M-#me?")
            doDialogText("DEAN:# Tell me what I was talking about right now,# and you may sit down.")
            doDialogText("YOU:# Uh.#.#.#")
            doDialogText("     That your school is one of the top schools in the district?")
            doDialogText("     And about how prestigious it is?")
            doDialogText("DEAN:# .#.#.#")
            doDialogText("YOU:# .#.#.#")
            doDialogText("ASHTON:# .#.#.#")
            if giveUp == 2: doDialogText("FLOWERY:# .#.#.#",afterdelay=3)
            print()
            pauseSong()
            doDialogText("DEAN: .#.#.### you may sit down.")
            doDialogText("YOU:# (phew.)")
            doDialogText("ASHTON:# Nice save!")
            doDialogText("YOU:# Thanks.#.#.#")
            doDialogText("(Why does this feel like deja vu?)", afterdelay=2)
            print()

            doDialogText("Eventually the DEAN stops talking about the school's prestigious heritage or smth.")
            
            doDialogText("DEAN:# Well,# at the end of the day,# we hope you find Devagiri a welcoming home, as well as a school capable of helping you grow not only as a wizard or witch,# but as a person as well.")
            doDialogText("      You may move to your respective dorms now.")
            
            print()
            doDialogText("You and the rest of the students move to your respective dorms.")
            doDialogText("Unaware of where your dormroom is,# you decide to follow ASHTON to the way.")
            doDialogText("YOU:# Hey,# ASHTON,# you think we're in the same dorm?")
            doDialogText("ASHTON:# Hmm,# the RECEPTIONIST is supposed to tell you that.")
            doDialogText("YOU:# Well,# I guess I came late,# so the RECEPTIONIST had no time to tell me.")
            doDialogText("     I think I'll stick with you for now.")
            print()

            if pgFilter:
                doDialogText("You and ASHTON soon make it to his dormitory.")
                doDialogText("YOU:# Hey,# there's my stuff!")

                if giveUp == 1:
                    doDialogText("     and FLOWERY too.#.#.#")
                    doDialogText("FLOWERY:# Heya.# Can't believe you would abandon me like that.")
                    doDialogText("YOU:# Listen man,# i-#", afterdelay=0)
                    doDialogText("ASHTON:# I-#Is that a talking flower?!")
                    doDialogText("FLOWERY:# What?# Have you never seen a talking flower before?")
                    doDialogText("ASHTON:# N-#NO!# I'VE NEVER SEEN A TALKING FLOWER BEFORE!")
                    doDialogText("YOU:# uh.#.#.#")

                elif giveUp == 2:
                    doDialogText("FLOWERY:# Stuff?# Only thing you got there is Hot Chocolate-", afterdelay=0)

                doDialogText('PERSON 1:# OH MY GOSH IS THAT A TALKING FLOWER?!', spd=2)
                doDialogText("PERSON 2:# OMG HE'S SO CUTEE", spd=2)
                doDialogText("PERSON 3:# CAN I HOLD HIM?!?!")
                doDialogText("YOU:# What- WHERE DID ALL THESE PEOPLE COME FROM?!")
                doDialogText("SOME GUY OUTSIDE:# HEY EVERYONE!# ASHTON BROUGHT A TALKING FLOWER!")
                print()
                doDialogText("In an instant,# you could hear the rapid marching of about 20 students moving into your dorm room.")
                doDialogText("FLOWERY:# what the fuck")
                'SR. CAR: THE CENSORS ARE DOWN!!!! I REPEAT THE CENSORS ARE DOWN!'
                '         WHITE, STOP SLACKING OFF YOU...'
                '         ... oh white.'
                doDialogText("SOME OTHER GUY:# ASHTON LET ME TOUCH HIMMM")
                doDialogText("ASHTON:# WAIT WAIT HE'S NOT MINE!# HE BELONGS TO.#.#.#")
                doDialogText("        I'm sorry,# what was your name?")
                doDialogText(f"YOU:# {saveFile['name']}.")
                print()

                doDialogText(f"SOME GIRL:# {saveFile['name'].upper()}!# PLEASE LET ME HOLD HIM!")
                doDialogText("FLOWERY:# Hey, pal, don't you dare-", afterdelay=0)
                doDialogText("YOU:# Ladies and Gentlemen,# he's yours.")
                doDialogText("You gently pass FLOWERY to ASHTON,# and quickly move out of the way.")
                doDialogText("As soon as you leave the circle of students,# the ring collapses onto ASHTON like a star collapsing right before it's death.")
                print()
                doDialogText("You take your flask and take a sip of Hot Chocolate as you watch the chaos unfold.")
                doDialogText("Eventually ASHTON makes it out of the chaos and stands beside you.")
                doDialogText("ASHTON:# ...why.", spd=6)
                doDialogText("        why did you give it to me?")
                doDialogText("YOU:# Come on,# if I was there,# I would've gotten crushed in there.")
                doDialogText("ASHTON:# ...## so did i.", spd=7)
                doDialogText("YOU:# Well.#.#.# sorry about that.")
                print()
                bunk = doDialogChoice("ASHTON:# Well,# it looks like we're bunkmates.", choices=['Top Bunk', 'Bottom Bunk'])

                if bunk == 1:
                    doDialogText("YOU:# I call dibs on the top bunk.")
                    doDialogText("ASHTON:# That's fine,# I usually prefer bottom anyways.")
                else:
                    doDialogText("YOU:# I'll go with the bottom bunk.")
                    doDialogText("ASHTON:# Well,# then I guess I'll take the top bunk.")

                print()
                doDialogText(".#.#.#", afterdelay=3)
            
            stopSong()
            doDialogText("Suddenly,# the entire world freezes.")
            doDialogText("A popup appears in front of you which states:")
            print()
            doDialogText("|| YOU HAVE REACHED THE END OF THE DEMO. ||")
            doDialogText("|| PLEASE SUBSCRIBE TO THE PATREON TO PLAY THE FULL VERSION OF THIS GAME. ||", spd=2)
            print()
            doDialogText("YOU:# .#.#.#what?")
            
                    




            # SKIP MINIGAME
            doDialogText("INTERMISSION!")
            print()
            doDialogText("SR. CAR:# Let's take a break here.")
            doDialogText("         Our participants are clearly tired.# Let's give them a treat!")
            doDialogText("YOU:# What just.#.#.# happened?")
            doDialogText("     WAIT DID THE GAME RUN OUT OF FREE TRIAL?")
            doDialogText("SR. CAR:# uh.#.#.#")
            doDialogText("YOU:# LMAOOOO YOU SPENT ALL OF YOUR MONEY ON A DEMO")
            if pgFilter:
                doDialogText("FLOWERY:# t-#thank god.#.#.# it's.#.# over.", spd=6)
            doDialogText("SR. CAR:# W-#whatever.# I will have a word with whoever's in charge for development.")
            doDialogText("         For now,# let's take a break,# shall we?")
            
            doDialogText("You got teleported to what looks like a grand dining room.")
            playSong('assets/soundtrack/bach.mp3')
            doDialogText("SR. CAR:# Please,# take a seat.")
            doDialogText("As you take a seat,# a plate appears out of thin air,# with food on it.")
            doDialogText("SR. CAR:# Taste the brilliance of our special MALABAR CHICKEN CURRY.")
            print()
            doDialogText("YOU:# This doesn't look that bad.")
            doDialogText("FLOWERY:# No thanks,# I don't like meat.# I eat sun.")
            doDialogText("SR. CAR:# Our MALABAR CHICKEN CURRY is a dish for all.# Try it!")
            doDialogText("You and FLOWERY take a small bite.")
            print()

            player['hp'] = getMaxHP(1)
            doDialogText(f"YOUR HP WAS RESTORED TO MAX! ({getMaxHP(1)})")
            print()
            doDialogText("(This.#.#.# is really good!)")
            if pgFilter: doDialogText("FLOWERY:# HOLY SHIII-# DAMN THE CENSOR!")
            else: doDialogText("FLOWERY:# WOAAAAAHHHHHH")
            doDialogText("         IS THIS WHAT CHICKEN TASTES LIKE?!?!")
            doDialogText("         IT'S SO GOOOOD!")
            print()
            doDialogText(f"FLOWERY'S HP WAS RESTORED TO MAX! ({getMaxHP(4)})")
            print()
            doDialogText("YOU:# Yeah,# not gonna lie,# this is REALLY good!")
            doDialogText("SR. CAR:# We're glad you enjoy it!")
            doDialogText("         O-#oh,# excuse me,# I'll be right back.")
            doDialogText("         You can take a short rest in the meantime.")
            doDialogText("SR. CAR disappears offstage.")
            print()
            doDialogText("YOU:# Wonder what that was about?")


            stopSong()
            save2 = getPrompt("Save this chapter here?")

            if save2:
                route4["startIndex"] = 2
                route4['players'] = [player, ashish, knight, flowery]
                saveFile["route4"] = route4

                saveFile['route4']['inventory'] = inventory
                saveFile['route4']['money'] = money

                try:
                    saveGame(curSaveName, saveFile)
                    doDialogText("The game was saved.")
                except:
                    doDialogText("There was an error in saving the game.")
            
            continue2 = getPrompt("Continue your journey?")

            if continue2:
                startindex = 2
                doDialogText("Continuing from TV SHOW.#.#.#")
                doDialogText("The Finale Approaches.", afterdelay=2)
    # POSSIBLE SPLIT

    if startindex == 2:
        blush = False
        if saveFile['route1']['name_choice'] == "NORMAL": blush = True
        elif saveFile['route1']['name_choice'] == "RUDE" and saveFile['route1']['rude_choice']: blush = True
        if saveFile['route3']['rude_stay'] != "UNFORGIVED":
            if route4['on_weirdRoute']:
                doDialogText("You woke up in the middle of the night.# It's 4:11 AM.")
                doDialogText("The computer screen is flickering.")
                doDialogText("Ashish is asleep.")

                play = doDialogChoice("Play the game?", choices=["Play it.", "Go back to sleep."])

                if play == 2:
                    doDialogText("You decide to go back to sleep.")
                    route4['on_weirdRoute'] = False
                elif play == 1:
                    route4['played_conjuring'] = True
                    doDialogText("You decide to try the game for yourself.# A quick session can't hurt,# right?")
                    doDialogText("You boot up the computer.# The game opens up on it's own before you can even touch the controller.")
                    print()
                    doDialogText("CONJURER.", spd=2)
                    doDialogText("FOR YOU AWAITS A JOURNEY YOU'RE NOT READY FOR YET.", spd=2)
                    doDialogText("YOU WILL FALL TO THE DARKNESS.", spd=2)
                    doDialogText("FRET NOT,# YOU WILL GET STRONGER.", spd=2)
                    doDialogText("STRONGER.", spd=2)

                    print()
                    doDialogText("There's only one option.")
                    action = doDialogChoice("", choices=['Fight.'])

                    doDialogText("FIGHT.", spd=2)
                    doDialogText("THE NATURAL INSTINCT TO TACTFUL DANGER.", spd=2)
                    doDialogText("FOR NOW,# YOU MUST CONNECT YOUR SOUL TO YOUR BODY.", spd=2)

                    doDialogChoice("Connect your soul?")

                    doDialogText("YOU HAVE NO CHOICE,# BUT TO GET STRONGER.", spd=2)
                    doDialogText("CLOSE YOUR EYES,# CONJURER.")
                    doDialogText("FEEL THE SOULS RESONATE.")
                    doDialogText("EXECUTE RESONANCE.", afterdelay=2)
                    print()
                    doDialogText(".#.#.#")
                    doDialogText("Wait,# you're in the game now.")
                    doDialogText("Crazy.")

                    doDialogText("YOUR SENSES HEIGHTEN IN RESPONSE TO BATTLE!#", spd=5, step=2, afterdelay=0)
                    doDialogChoice("", choices=["Fight."])
                    doDialogText("There's no enemy?")
                    doDialogChoice("", choices=["Fight."])
                    doDialogText("But there's no enemy.")
                    doDialogChoice("", choices=["Fight."])
                    doDialogText("*sigh* you take a blind shot in the dark.")
                    doDialogText("Owch-# that hurt.#.#?")
                    doDialogText("GAME:# ACT SERIOUS,# CONJURER.", spd=2)
                    doDialogText("       DONT WORRY ABOUT THE LACK OF AN ENEMY.# WHAT YOU HAVE TO ATTACK IS THERE.", spd=2)
                    doDialogText("YOU:# What are you talking about?")
                    doDialogText("GAME:# YOU MAY NOT SEE IT,# BUT YOU CAN FEEL IT.", spd=2)
                    doDialogText("YOU:# Feel it?")
                    doDialogText("YOU:# Hey,# why'd you go silent?# Tell me more!")
                    doDialogText(".#.#.#")
                    doDialogText("You decide to feel it.#.#.#")
                    doDialogText(".#.#.#")
                    doDialogText(".#.#.#########!", afterdelay=0.3)
                    atkResult = doTimedAttack(3, 1, 5)

                    doDialogText("You struck something!")
                    doDialogText("GAME:# VERY WELL,# CONJURER.# KEEP FIGHTING.", spd=2)

                    turn = 0
                    exp = 0
                    while turn < 15:
                        if turn == 1: doDialogText("GAME:# EXCELLENT.# YOU'VE GOT THIS.", spd=2)
                        elif turn == 2: doDialogText("GAME:# KEEP GOING AT THIS STEADY PACE.", spd=2)


                        doDialogChoice("", choices=["Fight"])

                        atkResult = doTimedAttack(3, 1, 5)
                        exp += atkResult*100*(1.3)

                        if exp > 100: 
                            exp -= 100
                            player['attack'] += 1
                            doDialogText(f"YOUR ATTACK WAS RAISED BY 1. ({player['attack']})")
                            turn += 1

                    doDialogText("GAME:# GOOD JOB.# YOU HAVE COMPLETED YOUR TRAINING.", spd=2)
                    doDialogText("      YOU MAY NOW CLOSE YOUR EYES.", spd=2)
                    doDialogText("You close your eyes.")
                    doDialogText(".#.#.#", afterdelay=2)
                    doDialogText("You woke up back on your bed.")



            doDialogText("It's morning.#.#.#?")
            doDialogText("Though the air feels warm,# the outside sky is still dark.# Only a little lighter.")
            doDialogText("YOU:# The darkness still makes it feel like nighttime,# even though I swear I feel the sunlight.")
            doDialogText("KNIGHT:# Are you two awake?# We have to get ready now.# Our final destination awaits.")
            doDialogText("ASHISH:# Our final one?")
            doDialogText("KNIGHT:# Yes.# After this,# we will reach the fountain.")
            doDialogText("ASHISH:# So our journey is almost over.#.#.#")
            doDialogText("YOU:# .#.#.#")
            print(end='     ')
            doDialogText("This journey has been really fun.# Thank you for your time,# you two.")
            doDialogText("ASHISH:# O-#Oh,# it's no big deal.# I also had some fun today.")
            print(end='        ')
            doDialogText("It was nice exploring this dark world,# fighting Edwin,# reliving English chapters in Snapshot city and helping people.")
            doDialogText("KNIGHT:# I can't lie,# it's been a wonderful experience with you two.")
            doDialogText("YOU:# I'm deeply grateful for your help,# Ms. KNIGHT.# Thank you for helping us get back home and showing us around.")
            doDialogText("ASHISH:# Yeah,# thank you Ms. Knight!")
            doDialogText("KNIGHT:# Aw,# I'm flattered.# I'm only doing what I think is the best.")
            print(end='        ')
            doDialogText("Well,# formalities aside,# we have a fountain to seal.# Let's go!")
            doDialogText("ASHISH:# Okay!")
            doDialogText("Ashish steps ahead.")
            doDialogText("Before you go,# you notice something on the computer...")
            doDialogText("(Is this like a secret drawer or something?)")
            doDialogText("You open the drawer.")

            if route4['played_conjuring']:
                doDialogText("""It says:##
- - - - - - - - - - - - - - - - - 
THANK YOU FOR PLAYING THIS GAME.
YOUR JOURNEY NOW COMES TO A STOP.
TAKE THESE AS A PARTING GIFT.
YOUR HARD WORK MUST BE PAID.
- - - - - - - - - - - - - - - - - 
""")
                doDialogText("YOU GOT DREAM KNIFE AND VISCOSITY SHIELD.", step=2, spd=4)
                doDialogText("LEVEL UPGRADED TO 3.", step=2, spd=4)
                doDialogText("ATTACK RAISED TO 25.# DEFENSE RAISED TO 25.", step=2, spd=4)
                player['weapon'] = "DREAM KNIFE"
                player['armor'] = "VISCOSITY SHIELD"
                player['attack'] = 25
                player['defense'] = 25
                player['lv'] = 3
                player['hp'] = getMaxHP(1)
                inventory += ["DREAM KNIFE", "VISCOSITY SHIELD"]
            else:
                doDialogText("The drawer was empty.")

            # ENTER TO TUT'S PYRAMID PALACE
            doDialogText("You,# Ashish and The KNIGHT step outside of the Inn.")
            doDialogText("The warm darkness welcomes your last adventure in this world.") 
            doDialogText("KNIGHT borrows two horses from the Inn.")
            doDialogText("KNIGHT:# Hope you two can share a horse,# I'll take the other horse.")
            doDialogText("ASHISH:# But I've never rode a horse before!")
            doDialogText("KNIGHT:# Well,# then this is your chance to learn.# Hop on!")
            doDialogText("You and Ashish get into a horse together.")
            # INSERT GAY SECTION HERE
            doDialogText("YOU:# Comfortable?")
            doDialogText("ASHISH:# N-#Not really.#.#.# Can I sit at the back?")

            if blush:
                doDialogText("YOU:# Alright.")
                doDialogText("You get off the horse,# but forgot your feet don't reach the ground.")
                doDialogText("You're falling off the horse when ASHISH reaches out and catches you reflexively.")
                doDialogText("You and Ashish both fall onto the ground,# with him falling on top of you.")
                player['hp'] -= 1
                if player['hp'] <= 0: player['hp'] = 1
                doDialogText("ASHISH:# .#.#.#")
                doDialogText("YOU:# .#.#.#")
                doDialogText(".#.#.#")
                doDialogText("ASHISH:# O-#Oh my god,# I'm so sorry!# Let me get up.", spd=3)
                doDialogText("Ashish frantically gets off of you.")

                reach = doDialogChoice("", choices=["Reach out your hand.", "Get up by yourself."])
                if reach == 1:
                    doDialogText("You reach out your hand to Ashish.")
                    doDialogText("YOU:# Don't worry about it.")
                    doDialogText("ASHISH:# ...# okay.")
                    doDialogText("(He blushes wildly.#.#.#)")
                    doDialogText("(Then a smile comes across his face.)")
                    doDialogText("Ashish pulls you back up.")
                    doDialogText("This time you sit in the front,# and Ashish sits on the back.")
                    doDialogText("Ashish holds onto you.#.#.# for balance.#.")
                    doDialogText("(... stop thinking about it stop thinking stop stop stop)", spd=3, afterdelay=0.1)
                    route4['peak_horseRiding'] = "ACHIEVED"
                else:
                    doDialogText("YOU:# Don't worry about it.")
                    doDialogText("ASHISH:# O-#okay.#.#.#")
                    doDialogText("You get up by yourself.")
                    doDialogText("This time you sit in the front,# and Ashish sits on the back.")


            else:
                doDialogText("YOU:# Sure.")
                doDialogText("You both get off and sit in the front.")

            doDialogText("KNIGHT:# Ready?# Off we go!")

            doDialogText("You take off into the distance.")
            doDialogText("As you run,# the world around you shifts.# The horses are moving at an unattainable speed.")
            doDialogText("KNIGHT:# Hold tight!")
            doDialogText("It feels like the world revolves around you.")
            doDialogText("Watching as the world warps around your immense speed and integrity...##")

            if route4['on_weirdRoute']: doDialogText("You feel determined.")
            else: doDialogText("You feel unstoppable.")
            print()
            doDialogText("As the world slows down,# you realize you're near the foot of a large pyramid,# in the middle of a golden yellow desert.")
            doDialogText("ASHISH:# Is this old Egypt?")
            doDialogText("KNIGHT:# If we're following the pattern of your textbook,# then this is probably where Tutankhamun is.")
            doDialogText("YOU:# Something feels off...")
            doDialogText("KNIGHT:# You're correct.# Look up.")
            doDialogText("You and Ashish look up to the top of the pyramid.")
            doDialogText("The tip has a dark covering,# and something black is shooting out into the sky.")
            doDialogText("KNIGHT:# That is a FOUNTAIN.# This is the fountain that gives this dark world shape.")
            doDialogText("        ofcourse to protect itself,# it affects the darkners nearby,# so everyone we come across will likely try to stop us from sealing the dark fountain.")
            doDialogText("YOU:# I can feel it's dark presence...")
            doDialogText("ASHISH:# Me too.# It's so.#.#.# dark.")
            doDialogText("KNIGHT:# This is it.# The hardest part of our journey.# Get READY!")
            doDialogText("You and team enter the pyramid.")
            doDialogText("It's...# built like a fortress inside!# The egyptian darkners prepare for battle.")
            doDialogText("KNIGHT:# Quick,# let's rush!")

            if route4['on_weirdRoute']:
                doDialogText("YOU:# Let me handle this.")

                doDialogText("YOUR SENSES HEIGHTEN IN RESPONSE TO BATTLE.## GET READY TO KILL EVERYONE.", spd=5, step=2)
                doDialogText("KNIGHT:# Are you sure?!# This could be dangerous!")
                doDialogText("YOU:# I got this.")

                endMontage = False

                tutATK = 25

                turn = 0
                while not endMontage:
                    launch = random.randint(0, 3)

                    if turn == 0: launch = 1

                    if launch == 1:
                        doDialogText("A DARKNER LAUNCHES AT YOU!# DODGE!", step=2)
                        launchResult = doTimedAttack(3, 1, 3)
                        if 0 <= launchResult <= 0.7:
                            dmg = getDamageDealt(tutATK, player, launchResult)
                            player['hp'] -= dmg
                            doDialogText(f"YOU lost {dmg} HP. ({player['hp']}/{getMaxHP(1)})")
                        else:
                            doDialogText("You dodged the enemy.")

                    if player['hp'] <= 0:
                        player['hp'] += 1
                        route4['DEATHS'] += 1
                        doDialogText("You keep persisting. (HP restored to 1)")

                    if turn == 2: doDialogText("KNIGHT: You're holding up well!")
                    elif turn == 5: doDialogText("KNIGHT: We're approaching the second layer!")
                    elif turn == 7: doDialogText("KNIGHT: Wow,# you're doing really well...")
                    elif turn == 9: doDialogText(f"ASHISH: {saveFile['name']}, are you okay?")
                    elif turn == 10:
                        doDialogText("KNIGHT:# We're gonna stop here.# Time to open this door by solving it's puzzle-")
                        doDialogText("You broke through the door.")
                        doDialogText("KNIGHT:# .#.#.#")
                        doDialogText("ASHISH:# WOAH when did you get so strong?# I was sure that door was indestructible!")
                    elif turn == 15:
                        doDialogText("KNIGHT:# This is it.# The dark fountain should be past this door.")
                        doDialogText("YOU:# Well,# let's go then.")
                        doDialogText("KNIGHT:# No wait.# The darkner guarding the dark fountain must be strong.")
                        doDialogText("ASHISH:# Let me heal everyone.")
                        doDialogText("ASHISH cast the spell HEALING SONG.")
                        doDialogText("It was truly wonderful.")
                        doDialogText("His song healed everyone to full health!")
                        player['hp'] = getMaxHP(1)
                        ashish['hp'] = getMaxHP(2)
                        knight['hp'] = getMaxHP(3)

                        doDialogText(f"{saveFile['name'].upper()} was healed. ({player['hp']}/{getMaxHP(1)})")
                        doDialogText(f"ASHISH was healed. ({ashish['hp']}/{getMaxHP(2)})")
                        doDialogText(f"KNIGHT was healed. ({knight['hp']}/{getMaxHP(3)})")

                        print()
                        doDialogText("KNIGHT:# Let's go now.")
                        endMontage = True
                        break

                    

                    btselect = doDialogChoice(f"You keep taking darkners. ({player['hp']}/{getMaxHP(1)})", choices=["Fight"])


                    if btselect == 1:
                        attack = random.randint(1, 3)

                        if attack == 1: result = doTimedAttack(3, 1, 2)
                        elif attack == 2: result = doTimedAttack(5, 7, 2)
                        elif attack == 3: result = doTimedSpam(50)
                        if 0 <= result <= 0.5:
                            dmg = getDamageDealt(tutATK, player, result)
                            player['hp'] -= dmg
                            doDialogText(f"You lost {dmg} HP. ({player['hp']}/{getMaxHP(1)})")
                        else:
                            doDialogText("Enemy subsided.")

                    turn += 1

            else:
                doDialogText("YOUR SENSES HEIGHTEN IN RESPONSE TO BATTLE.## PREPARE!", spd=5, step=2)

                endMontage = False
                turn = 0

                tutATK = 25

                hasWeapon = False

                while not endMontage:

                    if player['hp'] <= 0:
                        doDialogText("Your HP dropped to 0,# but you held on!")
                        doDialogText("HP Regenerated to 1.")
                        player['hp'] = 1
                        route4['DEATHS'] += 1
                    launch = random.randint(0, 3)

                    if turn == 0: launch = 1

                    if launch == 1:
                        tutATK = 25
                        doDialogText("A DARKNER LAUNCHES AT YOU!# DODGE!", step=2)
                        launchResult = doTimedAttack(3, 1, 3)
                        if 0 <= launchResult <= 0.7:
                            dmg = getDamageDealt(tutATK, player, launchResult)
                            player['hp'] -= dmg
                            doDialogText(f"YOU lost {dmg} HP. ({player['hp']}/{getMaxHP(1)})")
                        else:
                            doDialogText("You dodged the enemy.")

                    if turn == 0:
                        doDialogText("You come across a Darkner!")
                        doDialogText(".#.#.# There are more Darkners!")
                        doDialogText("KNIGHT:# Get ready to handle all of them!")

                    elif turn == 8:
                        doDialogText("KNIGHT: COME ON! WE'RE CLOSE!")
                    elif turn == 10:
                        doDialogText(f"KNIGHT:# Good Job,# {saveFile['name']} and Ashish!# We should be almost there.")
                        print(end='        ')
                        doDialogText("Now we face a door with a puzzle we must solve.")
                        doDialogText("ASHISH:# i-#is this wordle?!")
                        doDialogText("KNIGHT:# Yeah.#.#.# It's wordle.")
                        doDialogText(f"ASHISH:# well,# let's try solving this together,# {saveFile['name']}.")

                        # WORDLE SECTION
                        word = "LIGHT"
                        letters:set = {' '}
                        orders = ["_", "_", "_", "_", "_"]
                        attempts = 0
                        while True:

                            if attempts == 6:
                                doDialogText("Well,# you now know that you can have as many tries.")
                            elif attempts > 25:
                                doDialogText("The door broke because of your constant failures.#.#.#")
                                doDialogText("ASHISH:# .#.#.#")
                                doDialogText("KNIGHT:# A-#Atleast the door's open now.# Let's head in!")
                                route4['wordle'] = "BROKE THE DOOR"
                                turn += 1
                                break
                            guess = input(f"({attempts+1})->").strip().upper()[0:5]

                            if attempts == 0 and guess == word:
                                doDialogText("The door unlocked!")
                                doDialogText("ASHISH:# Woah,# how did you do that?# You guessed it in one try!")
                                doDialogText("YOU:# I did NOT expect that.")
                                print()

                                route4['wordle'] = "YOU KNEW THE WORD"
                                turn += 1
                                break
                            elif attempts < 6 and guess == word:
                                doDialogText("The door unlocked!")
                                doDialogText("ASHISH:# Good job!# You guessed it!")
                                doDialogText("YOU:# I don't know if it let us try only 6 times,# or we could have as many tries.#.#.#")
                                print()

                                route4['wordle'] = "TRUE WORDLE"
                                turn += 1
                                break
                            elif 6 <= attempts <= 25 and guess == word:
                                doDialogText("The door unlocked!")
                                doDialogText("ASHISH:# Nice,# we can move now!")
                                route4['wordle'] = "NORMAL WORDLE"
                                turn += 1
                                break

                            for l in range(len(guess)):
                                LETTER = guess[l]
                                if LETTER in word:
                                    if guess[l] == word[l]:
                                        orders[l] = LETTER

                                    if guess[l] != word[l]:
                                        letters.add(LETTER)

                            doDialogText(f"-> {''.join(orders)} {letters}")
                            attempts += 1

                    elif turn == 15:
                        doDialogText("KNIGHT:# This is it.# The dark fountain should be past this door.")
                        doDialogText("YOU:# Well,# let's go then.")
                        doDialogText("KNIGHT:# No wait.# The darkner guarding the dark fountain must be strong.")
                        doDialogText("ASHISH:# Let me heal everyone.")
                        doDialogText("ASHISH cast the spell HEALING SONG.")
                        doDialogText("It was truly wonderful.")
                        doDialogText("His song healed everyone to full health!")
                        player['hp'] = getMaxHP(1)
                        ashish['hp'] = getMaxHP(2)
                        knight['hp'] = getMaxHP(3)
                        doDialogText(f"{saveFile['name'].upper()} was healed. ({player['hp']}/{getMaxHP(1)})")
                        doDialogText(f"ASHISH was healed. ({ashish['hp']}/{getMaxHP(2)})")
                        doDialogText(f"KNIGHT was healed. ({knight['hp']}/{getMaxHP(3)})")

                        print()
                        doDialogText("KNIGHT:# Let's go now.")
                        endMontage = True
                        break



                    
                    flv = ""
                    if turn < 10: flv = "DARKNERS are chasing you."
                    else: flv = "You're nearing the FOUNTAIN!"

                    if not hasWeapon: btselect = doDialogChoice(flv, choices=['Fight', 'Action', 'Spell'])
                    else: btselect = doDialogChoice(flv, choices=['Fight', 'Spell'])

                    if btselect == 1:

                        playingPlayers = ["You"]
                        if ashish['hp'] > 0: playingPlayers += ["Ashish"]
                        if knight['hp'] > 0: playingPlayers += ["The Knight"]
                        doDialogText(f"{', '.join(playingPlayers)} get ready to attack!")
                        fightResult = doTimedAttack(3, 3, 2)

                        if fightResult > 0.4:
                            doDialogText("Enemy subsided.# Move on!")
                            turn += 1
                        else:
                            doDialogText("Your party missed!")
                    if btselect == 2:
                        if not hasWeapon:
                            actions = doDialogChoice("ACTIONS:", choices=["Borrow KNIGHT's weapon.", "Return."])

                            if actions == 1:
                                doDialogText("YOU:# Hey KNIGHT,# can I borrow one of your weapons?")
                                doDialogText("KNIGHT:# Hm?## Oh,# I can't give you my weapon because I'm using mine to hold off the darkners.")
                                print(end='        ')
                                doDialogText("But I can conjure one for you.# It won't be as effective,# but try it!")
                                doDialogText("KNIGHT cast CONJURE!# A sword was made for you.")
                                doDialogText("YOU:# Sweet,# thanks!")
                                player['attack'] += 30
                                hasWeapon = True
                        else: btselect = 3
                    if btselect == 3:
                        choiceIndex = doDialogChoice("ASHISH's SPELLS:", choices=ashish['spells'] + ['Return'])


                        if choiceIndex > len(ashish['spells']):
                            continue
                        else:
                            curSpell = ashish['spells'][choiceIndex-1]

                        if curSpell == "SUMMON ALLY":
                            doDialogText("ASHISH:# Uhh,# I'm having trouble casting this spell!")
                            continue
                        if curSpell == "HEALING SONG":
                            doDialogText("ASHISH cast HEALING SONG!")
                            doDialogText("The soothing song was greatly healing!")
                            player['hp'] += 7
                            ashish['hp'] += 5
                            knight['hp'] += 7
                            player['hp'] = getMaxHP(1)
                            ashish['hp'] = getMaxHP(2)
                            knight['hp'] = getMaxHP(3)
                            doDialogText(f"{saveFile['name']} was healed. ({player['hp']}/{getMaxHP(1)})")
                            doDialogText(f"ASHISH was healed. ({player['hp']}/{getMaxHP(2)})")
                            doDialogText(f"KNIGHT was healed. ({player['hp']}/{getMaxHP(3)})")

            doDialogText("TUTANKHAMUN:# You're here.")
            doDialogText("You arrive in a hallway with your two friends.")
            doDialogText("Almost everything in the room is coated with a dark coloured gold.")
            doDialogText("KNIGHT:# We're here to seal the fountain.")
            doDialogText("TUTANKHAMUN:# Yes,# I'm aware.# After sealing the fountain,# this world will cease to exist.")
            print(end="             ")
            doDialogText("Even if struck again,# this world will never be the same again.# Every dark world is different.")
            doDialogText("TUTANKHAMUN: ==")
            doDialogText("""
This DARK WORLD,# a place created by one with her own two hands,# with the necessary will and power.###
When one must step into the dark and forget.#.#.###
Holding sharp their hands,# striking the body of the EARTH.#.#.####
Is when one creates a FOUNTAIN.###
As if asking the EARTH for a place to go to,# she provides her a seperate dimension to work things out.####
A Realm of Dreams,# and Connections.#.#.###
Fueled by your imagination.#####

KNIGHT:# However,###
A Dark world is merely a lesser reflection of reality.###
In the presence of the dark,# it hides the pain in the artist,# and replaces it with what it's mind desires.###
Despite being less of the real world,# it offers much more than any reality could.###
That,# perhaps,# is what makes a Dark world,# 
Beautiful.#######

TUTANKHAMUN:# Precisely.###
The wonders of a dark world are truly limitless.###
Because,# the only limitations to a Dark world,###

is your imagination.""")
            doDialogText("ASHISH:# .#.#.# I'm speechless.#.#.#")
            if route4["on_weirdRoute"]: doDialogText("YOU: .#.#.#")
            else: doDialogText("You're left in awe.")
            doDialogText("TUTANKHAMUN:# You must pass now.# The darkness awaits.")
            doDialogText("The Fountain is Calling us.", afterdelay=3)
            print()
            doDialogText("Tutankhamun opens a trapdoor.")
            doDialogText("TUTANKHAMUN:# Beneath,# there's nothing but pure darkness.# Once you look ahead,# there will be a geyser spewing darkness.")
            doDialogText("TUTANKHAMUN:# That is the FOUNTAIN.# Go seal it.# Fulfill the purpose of your visit,# heroes.")
            doDialogText("KNIGHT:# Will do.")
            doDialogText("You hop into the Trapdoor and fall towards the darkness.")
            doDialogText("As you approach the fountain,# you feel the darkness slowing down your fall.")
            doDialogText("You stick the landing with a satisfying click.")
            doDialogText("YOU:# Is that.#.#.#")
            printGraphic('''
                   ▄██▀                    ▀███▄▀▀
                   ███                ▄█▄  ▄█▀▀▀█
                  ▄██▀                 █▄█▀     ▀
                  ███       ▄         ▄▀        █        ▄▄
                  ███      ▀█▀   ▄█▀▀▀ ▄        ▀
                   ███        ▄█▀       ▀    ▀▄
                   ███        █             ▄  ▀
                    ███       ▀▀▄▄▄         ▀ ▄
                     ███           ▀▀▀▀▀▀█▄███
                     ███   ▄              ▀▀███▄▄▄▄▄▀▀▀▀▀▀▀▄▄▄▄█▀
                   ▄██▀   ▀█▀                ▀██▄
                  ▄██▀                        ███
▄▄▀▀▀█▄           ███              ▄█▄         ███             █▀
       █         ███                ▀          ███            █
       ▀▄        ███     ▄             ▄█▄    ▄██▀           ▄▀
       █▀        ▀██▄   ▀█▀             ▀     ███   ▄▄▄▀▀▀▀▀▀
       ▀▀▀▀▀▀▄▄   ███                        ███ ▀▀▀
               ▀▄▄▀██▄                      ▄██▀
                   ▀██▄                     ███         ▄▀
                     ███▄         ▄         ███
                     ███     ▄   ▀█▀         ███
     ▀▀▀▀       ▀▀▀ ███▀    ▀█▀       ▄█▄    ███▀▄▄▄▄▄▄ ▀▀▀▀    ▀
              ▄▄▀▀▀▀███                ▀     ███   ▄  ▀▀▀▄▄
            ▄██      ▀██▄▄               ▄▄███▀   ▄█      ▀█
      ▄  ▄▄█▀  █▄      ▀███████▄▄▄▄▄███████▀▀   ▄█▀         ▀▀▄
    ▄▄▀▀▀▀      ▀█▄       ▀▀▀▀▀█████▀▀▀▀▀      █▀              ▀▀
 ▄▄▀              ▀▀▀▄                                    ▄▄
▀                                                     ▄▄█▀▀

                                           ▀▀▀▀▀
           ▀▀▀▀▄▄▄▄
                   ▀▀

''')
            doDialogText("The FOUNTAIN.")
            doDialogText("You're right in front of it.")
            doDialogText("It's presence is overwhelming.")
            doDialogText("ASHISH:# Geez,# this darkness is making me feel uneasy.")
            doDialogText("YOU:# How do we seal it?")
            doDialogText("KNIGHT:# I can seal it-", afterdelay=0)
            doDialogText("Someone emerges from the darkness.")
            doDialogText("???:# .#.#.#")
            doDialogText("KNIGHT:# .#.#.#")
            doDialogText("YOU:# Who is that?")

            doDarkIntro(soundImportSuccesful)

            # RAJITH/RANJITH FIGHT
            rHP = 250
            rATK = 66
            rDEF = 3

            hasAlly = False
            turn = 0

            fixAshish = False

            spellCheck = False
            learningQuantity = 10

            while turn < 30:
                if player["hp"] <= 0:
                    route4["DEATHS"] += 1
                    player["hp"] = 1
                    doDialogText("Your HP was 0,# but you held on.")
                    doDialogText("HP Regenerated to 1!")

                btselect = doDialogChoice("DARK FIGURE STANDS IN FRONT OF YOU.", choices=["Fight", "Action", "Spell", "Item", "Beg for Mercy"])
                if btselect == 1:
                    playingPlayers = ["You"]
                    if ashish['hp'] > 0: playingPlayers += ["Ashish"]
                    if knight['hp'] > 0: playingPlayers += ["The Knight"]
                    doDialogText(f"{', '.join(playingPlayers)} get ready to attack the DARK FIGURE!")
                    fightResult = doTimedAttack(3, 3, 2)

                    if fightResult > 0.2:
                        dmg = math.ceil((player["attack"] + ashish["attack"])*fightResult/rDEF)
                        rHP -= dmg

                        if rHP <= 0: rHP = 0
                        doDialogText(f"Your party deals {dmg} damage to the DARK FIGURE! ({str(rHP)}/250)")
                    else:
                        doDialogText("Your party missed!")
                elif btselect == 2:
                    if not spellCheck:
                        actions = doDialogChoice("ACTS:", choices=["Check", "Return."])
                        if actions == 1:
                            doDialogText("DARK FIGURE??")
                            doDialogText("ATTACK: 66,# DEFENSE: ???")
                            doDialogText("A Formidable Foe.")
                        doDialogText("Nothing you can do now.")
                        continue
                    else:
                        if learningQuantity > 0:
                            actions = doDialogChoice("ACTS:", choices=["Check", "KNIGHT's Idea!", "Return."])
                            if actions == 1:
                                doDialogText("DARK FIGURE??")
                                doDialogText("ATTACK: 66,# DEFENSE: ???")
                                doDialogText("A Formidable Foe,# but KNIGHT has a plan.")
                                continue
                            elif actions == 2:
                                doDialogText("You tried to learn MAGIC!")
                                learningQuantity -= random.randint(1, 2)
                                doDialogText(f"You made {(10-learningQuantity)*10}% progress!")
                        else:
                            doDialogText("You can cast spells now!# Go to the SPELLS menu:")
                            continue


                elif btselect == 3:
                    if learningQuantity > 0:
                        if fixAshish == True:
                            spell = doDialogChoice("ASHISH's SPELLS:", choices=ashish['spells'] + ['Return.'])
                            if spell > len(ashish["spells"]):
                                continue
                            else:
                                selSpell = ashish['spells'][spell-1]
                                if selSpell == "HEALING SONG":
                                    doDialogText("ASHISH sings a soothing melody.# Some notes are off.")
                                    player["hp"] += 7
                                    knight["hp"] += 7
                                    if player['hp'] > getMaxHP(1): player['hp'] = getMaxHP(1)
                                    if ashish['hp'] > getMaxHP(2): ashish['hp'] = getMaxHP(2)
                                    if knight['hp'] > getMaxHP(3): knight['hp'] = getMaxHP(3)
                                    doDialogText(f"{saveFile['name'].upper()} was HEALED. ({(player['hp'])}/{(getMaxHP(1))})")
                                    doDialogText(f"ASHISH was unable to be HEALED. ({(ashish['hp'])}/{(getMaxHP(2))})")
                                    doDialogText(f"KNIGHT was HEALED. ({(knight['hp'])}/{(getMaxHP(3))})")
                                if selSpell == "SUMMON ALLY":
                                    if not hasAlly:
                                        doDialogText("ASHISH casts SUMMON ALLY!#")
                                        doDialogText("SHARATH WAS SUMMONED.")
                                        doDialogText("SHARATH:# Yo guys,# what's popping-")
                                        doDialogText("The DARK FIGURE vaporized SHARATH.")
                                        doDialogText("ASHISH:# SHARATH!")
                                    else:
                                        doDialogText("ASHISH:# .#.#.#")
                                        continue
                                    hasAlly = True
                        else:
                            doDialogText("Ashish is DOWNED!")
                            continue
                    else:
                        spell = doDialogChoice("YOUR SPELLS:", choices=["RUDEGRAVE", "Return."])

                        if spell == 1:
                            doDialogText("You get ready.#.#.#")
                            doDialogText("YOU cast RUDEGRAVE!")
                            dmg = math.ceil((player["attack"]*5)*fightResult/rDEF)
                            rHP -= dmg

                            if rHP <= 0: rHP = 0
                            doDialogText(f"YOU dealt {dmg} damage to the DARK FIGURE! ({str(rHP)}/250)")
                elif btselect == 4:
                    if inventory == []:
                        doDialogText("Your inventory is empty.")
                        continue
                    else:
                        item = doDialogChoice("CHOOSE AN ITEM", choices=inventory + ["Return."])
                        if item > len(inventory):
                            continue
                        elif inventory[item-1] == "KEYCHAIN LOCKET":
                            doDialogText("You are already wearing the Keychain Locket.")
                            continue
                        elif inventory[item-1] == "VALENCE CHOCOLATE":
                            if ashish['hp'] <= 0:
                                doDialogText("You give the VALENCE CHOCOLATE to a downed ASHISH.")
                                doDialogText("He's concious again,# and protected.")
                                if not fixAshish: 
                                    fixAshish = True

                                inventory.remove("VALENCE CHOCOLATE")
                            else:
                                doDialogText("Give this to someone in need.")
                                continue
                elif btselect == 5:
                    doDialogText("You beg the DARK FIGURE for mercy.#.#.#")
                    doDialogText("You could feel it had no effect on the DARK FIGURE.")

                # DARK FIGURE ATTACK
                if rHP <= 0: break

                if turn == 0:
                    doDialogText("The DARK FIGURE STRUCK ASHISH!")
                    ashish['hp'] = 0
                    doDialogText(f"ASHISH WAS DOWNED! ({ashish['hp']}/{getMaxHP(2)})")
                    doDialogText("It focuses on you.")

                if 0 <= turn < 5: # PHASE 1
                    atIndex = random.randint(1, 3)

                    if atIndex == 1:
                        doDialogText("The DARK FIGURE draws a DARK SHOT!# AVOID IT!")

                        fResult = doTimedAttack(5, 1, 4)
                        dmg = getDamageDealt(rATK, player, fResult)

                        if fResult >= 0.9:
                            doDialogText("You barely dodged the shot!")
                        else:
                            player['hp'] -= dmg
                            doDialogText(f"YOU GOT HIT BY THE SHOT!")
                            doDialogText(f"{saveFile['name'].upper()} LOST {dmg} HP! ({player['hp']}/{getMaxHP(1)})")
                            route4['rajith_noHit'] = False
                    elif atIndex == 2:
                        doDialogText("The DARK FIGURE throws stars into the air?", afterdelay=0.4)
                        doDialogText("THE STARS FORM SWORDS!# DODGE!", spd=2, afterdelay=0.3)
                        fResult = doTimedAttack(3, 3, 3)
                        dmg = getDamageDealt(rATK, player, fResult)
                        if fResult >= 0.9:
                            doDialogText("You barely dodged the stars!")
                        else:
                            player['hp'] -= dmg
                            doDialogText(f"YOU GOT HIT BY THE STARS!")
                            doDialogText(f"{saveFile['name'].upper()} LOST {dmg} HP! ({player['hp']}/{getMaxHP(1)})")
                            route4['rajith_noHit'] = False
                    elif atIndex == 3:
                        doDialogText("The DARK FIGURE pulls out a HANDGUN.# DODGE THE BULLETS", afterdelay=0.4)
                        fResult = doTimedAttack(3, 5, 3)
                        dmg = getDamageDealt(rATK, player, fResult)
                        if fResult >= 0.9:
                            doDialogText("You barely dodged the bullets!")
                        else:
                            player['hp'] -= dmg
                            doDialogText(f"YOU GOT HIT IN THE CROSSFIRE!")
                            doDialogText(f"{saveFile['name'].upper()} LOST {dmg} HP! ({player['hp']}/{getMaxHP(1)})")
                            route4['rajith_noHit'] = False
                elif turn == 5:# PHASE 2 CUTSCENE
                    printGraphic('''
             ▄                                        ▄
           ▀▀▀▀▀                                    ▄▄▄▄▄
             ▀                      ▀                 ▀
      ▀                 ▀         ▀▀█▀▀
    ▀▀█▀▀             ▀▀█▀▀
               ▄                         ▄▄█▄▄
             ▀▀▀▀▀                         ▄
               ▀         ▄▄▄▄▄▄▄                  ▄
▄▄█▄▄                  ▄████████████▄▄▄         ▄▄▄▄▄
  ▄                  ▄██████████████████▄         ▀
                    ██████████████████████▄
       ▄           ██████▀▀            ▀▀███
            ▄▄▄    ████▀            ▄      █            ▀
 ▄       ▄█████▄  ███▀              █      █
       ▄████████▄ ▀▀                █      █   ▀█▄
     ▄████████████▄                  █     █   ████▄▄
    ████████████████▄                █     ▀ ▄████████▄     ▄
    ██████████████████▄          ▄▄▄ ▄ ▄▄  ▄████████████▄
    ▀███████████████████▄                ▄███████████████
▄     ▀███████████████████▄▄           ▄████████████████
         ▀▀███████████████████▄     ▄▄█████████████████▀    ▀
             ▀▀████████████████▀▀ ▄███████████████████▀
                 ▀▀████████▀▀ ▄▄████████████████████▀
              ▄▄▄▄▄  ▀▀▀▀ ▄▄█████████████████████▀▀  █▀▀▀▀▀█▄
 ▄▄▄▄▄▄▄  ▄█▀▀▀       ▄▄█████████████████████▀▀▀ ▄  ▀▀      ▀█
█▀     ▀█    ▄▄▄▄▄███████████████████▀▀▀▀▀ ▄▄▄████████▄▄▄▄   █
█     ▄▄▄▄███████████████████▀▀▀▀▀                  ▀▀▀▀▀▀▀▀ █
█ ▀▀▀▀████████▀▀▀▀▀▀▀▀                              █▄▄▄▄▄▄█▀▀
█▄     ▄▄       █
 ▀▀▀▀▀▀▀        █                              █
                ▀                              ▀

''')
                    doDialogText("The DARK FIGURE readies two blades!")
                elif 6 <= turn < 10:
                    atIndex = random.randint(1, 3)

                    if atIndex == 1:
                        doDialogText("The DARK FIGURE swiftly throws a Blade sharply at you!# DODGE!", spd=2, afterdelay=0.3)

                        fResult = doTimedAttack(3, 1, 3)
                        dmg = getDamageDealt(rATK, player, fResult)
                        if fResult >= 0.9:
                            doDialogText("You barely dodged the Blade!")
                        else:
                            player['hp'] -= dmg
                            doDialogText(f"YOU GOT SLICED BY THE BLADE!")
                            doDialogText(f"{saveFile['name'].upper()} LOST {dmg} HP! ({player['hp']}/{getMaxHP(1)})")
                            route4['rajith_noHit'] = False
                    elif atIndex == 2:
                        doDialogText("The DARK FIGURE throws a blade into the air.", afterdelay=0.3)
                        doDialogText("It uses it's other blade to send it flying at you!# DODGE!", spd=2, afterdelay=0.3)

                        fResult = doTimedAttack(3, 1, 3)
                        dmg = getDamageDealt(rATK, player, fResult)
                        if fResult >= 0.9:
                            doDialogText("You barely dodged the Blade!")
                        else:
                            player['hp'] -= dmg
                            doDialogText(f"YOU GOT SLICED BY THE BLADE!")
                            doDialogText(f"{saveFile['name'].upper()} LOST {dmg} HP! ({player['hp']}/{getMaxHP(1)})")
                            route4['rajith_noHit'] = False
                    elif atIndex == 3:
                        doDialogText("The DARK FIGURE charges at you!", afterdelay=0.3)
                        doDialogText("DODGE IT'S SWINGS!", spd=2, afterdelay=0.3)

                        fResult = doTimedAttack(4, 7, 3)
                        dmg = getDamageDealt(rATK, player, fResult)
                        if fResult >= 0.9:
                            doDialogText("You barely dodged the Blade!")
                        else:
                            player['hp'] -= dmg
                            doDialogText(f"YOU GOT CHOPPED BY THE BLADES!")
                            doDialogText(f"{saveFile['name'].upper()} LOST {dmg} HP! ({player['hp']}/{getMaxHP(1)})")
                            route4['rajith_noHit'] = False
                elif turn == 10:
                    doDialogText(f"KNIGHT:# I can tell we're not going to last for much longer!# {saveFile['name']},# I need your help.")
                    doDialogText("YOU:# Of course,# what is it?")
                    doDialogText("KNIGHT:# It's only attacking you so far.# We can use that to our advantage.")
                    doDialogText("YOU:# Ok what's the plan?")
                    doDialogText("KNIGHT:# I'll defend you.# I'm good at parrying DARK attacks like his.")
                    print(end='        ')
                    doDialogText("You'll have to learn a powerful spell.")
                    doDialogText("YOU:# I have to learn a spell?")
                    doDialogText("KNIGHT:# Yes.")
                    doDialogText("YOU:# I have no clue how it works,# but I will try my best.")
                    doDialogText("You can learn spells now through the ACTION menu!")
                    spellCheck = True

                elif 11 <= turn <= 30:
                    doDialogText("DARK FIGURE readies 5 SLASHES!")
                    printGraphic('''


                             ▄▄█████▄▄
                             ██████████▄
                             ▀ ▀████████
                                 ▀███████
                                  ███████
                                   ██████
                                   ▀█████
                                    █████
                                    ████▀
                                    ████
                                    █████
                                    █████
                                    ██▀██
                                    ██ ██
                                    ▀█ ██
                                   █████▀
                                   █ █▄▄
                                  ██▄██
                                 ▄▄▄██▀
                                 ██ ▀▀
                                  ▀██
                                 █
                                 █▄
                                 █▀
                               ▄
                               █
                               █
                             ▀


''', step=150, afterdelay=0.3)
                    printGraphic('''
 
















                                                        ▀███
                                                        ▄████
                                                       ███████
                                                   ▄▄████████
                                                ▄▄██████████▀
                                       ▄▄▄▄▄██████████████▀
          ▄▄▄▄    ▄▄▄▄ ▄██▄ ██▄▀█▄▄█████████████████▀▀▀▀
                ▀▀▀   ▄█ ▄███▄▄▀██▀▄▄▄▄████▀
                          ▀▀▀▀▀  ▀█▀▀▀▀






 
''', step=150, afterdelay=0.3)
                    printGraphic('''
 
















    ▄▄█▀
    ████▄
    █████▄▄
   ▀█████████▄▄
     ████████████▄▄▄▄▄   ▄▄           ▄  ▄▄           ▄▄▄▄
      ▀▀████████████████████████▄████▀▀▄█ ▀▄ ▀▀▀▀▀▀
           ▀▀▀▀▀▀▀▀▀ ▀██████▄▄▄ ███▀▄▄███▀▀
                       ▀    ▀▀▀▀▀▀







 

''', step=150, afterdelay=0.3)
                    printGraphic('''
 










                        ▄
                        █
                         ▀ ▄▄
                           █▀
                              ▀
                            ▀▀ ▀██
                              ▀▄███▄
                               ▀██▀██
                                ▀█▄▀█▄
                                 █████
                                 ▀████
                                  ████▄
                                  █████▄
                                 ▄██████
                                 ███████
                               ▄███████▀
                             ████▀▀▀▀




 
''', step=150, afterdelay=0.3)
                    printGraphic('''
                                              ▄▄▄▄
                                            ▄███████▄
                                              ███████▄
                                               ███████
                                               ███████
                                               ██████▀
                                               ██████
                                               █████
                                              █████
                                             ▄███▀
                                            ▄███▀
                                           ▄████
                                          ▄████▀
                                          ██ ██
                                        ▄▄█ ██
                                      ▄███▀██
                                     ▄█▄██▄
                                   █▄▄▄██
                                   ██ ▀
                                 █  ▀
                                ▄█
                                █▀
                            ▄█
                            ▀








 
''', step=150, afterdelay=0.3)
                    fResult = doTimedSpam(5)
                    dmg = getDamageDealt(rATK + 5, player, fResult)
                    if fResult >= 0.9:
                        doDialogText("You dodged the swings!")
                    else:
                        player['hp'] -= dmg
                        doDialogText(f"YOU GOT SWOONED BY THE swings!")
                        doDialogText(f"{saveFile['name'].upper()} LOST {dmg} HP! ({player['hp']}/{getMaxHP(1)})")
                        route4['rajith_noHit'] = False





                turn += 1

            if soundImportSuccesful:
                pygame.mixer.music.stop()

            doDialogText("The DARK FIGURE is getting sharper.")
            doDialogText("YOU:# What do we do?# It's getting harder to stand against it.")
            doDialogText(f"KNIGHT:# {saveFile['name']},# thanks for buying me the time.")
            doDialogText("YOU:# Huh?", afterdelay=0.5)
            doDialogText("The KNIGHT gets ready to use a powerful spell:")
            print()
            printGraphic('''

                   █▀        ▄█▀▀         ▀▀█      █
                  █▀        █▀              ▀█▄    █▄
                  █        ▄█                 █     █
                 █▀        █           ▄█▀   █▀     █
                 █         █   ▄▄           ▄█      █▄
                ▄█        ▄█▄   ▀           █▄▄▄▄▄   █
                █▄▄█▀▀▀▀▀▀▀ ▀▀█▄           █▀    ▀▀█▄█
             ▄█▀▀▀             ▀█▄  ▄▄▄▄█▀▀▀        ▀▀█▄▄
           █▀▀                   ▀▀▀▀                   ▀█▄▄
         ▄█▀                                               ▀█
        ▄█                                                  █
  ▄▄▄▄▄ █                                                   █▄
   █  ▀██▄                                                  █▀█▄
   █▄    █     ██▄▄▄                              ▄▄▄▄█     █  ▀▀█▄▄
    ▀█   ▀█    █████████▄▄▄                 ▄▄▄████████    █▀     █▀
 ▄▄▄▄█    █    ███████████████▄▄▄▄   ▄▄▄███████████████    █      █
 █▄       █     ███████████████████████████████████████    █    ▄█▀
  ▀█      █     ██████████████████████████████████████     █   █▀
   ▀█▄    ▀█    ██████████████████████████████████████    █▀   ▀██
    ▄█     █      ▀▀▀████████████████████████████▀▀▀      █   ▄█▀
  █▀▀      █            ▀▀▀▀████████████████▀▀            █   █▄
  ▀▀█▀█▄▄▄▄█▄▄                 ▀▀▀████▀▀▀                ██    ▀█
   ▄█       █▀▀█▄▄                                   ▄▄███▀▀██▀▀▀▀
 ▄█▀        █▄   ▀▀█▄▄                           ▄▄█▀▀  ██  ███▄▄
▀▀           █       ▀▀█▄▄                   ▄▄█▀▀     █▀█  █▀█▄▀▀█▄▄
             █▄          ▀▀█▄▄           ▄▄█▀▀         █ █  █  ▀█▄▄ ▀▀
           ▄█▀█▄             ▀▀█▄▄   ▄▄█▀▀           ▄▄█ ▀█ ▀█    ▀█▄▄
        ▄▄█▀▄█▀▀▀█▄              ▀▀▀▀▀           ▄▄█▀█    █  █▄      ▀
   ▄▄▄█▀▀▄▄█▀    ▄██▄▄           ▄▄█▀▀█      ▄▄█▀▀ ▄ ▀█   ▀█  █▄
▄█▀▀▀ ▄▄█▀    ▄▄█▀ ▄ ▀▀▀█▄▄▄    █▀    █  ▄▄█▀▀ ▄▄████ ▀█   █▄  █▄
  ▄▄█▀▀      █▀ ▄▄█████▄▄▄▄▀█████     █▀▀▀ ▄▄█████████ ▀█▄  █▄  █▄
█▀▀          ▀█▄ ▀▀█████████▀  █      █▄██████████████▀ ▄█   █   █▄
          ▄▄▄█▀▀▀█▄ ▀███████▄▄ █    ▀█████████▀▀▀▀▀▀▀ ▄█▀▀▀█▄▀█   █▄
     ▄▄▄█▀▀       ▀█▄ ▀▀▀▀▀▀█  █     █ ▄▄▄▄▄▄▄▄█▀▀▀▀▀▀▀     █▄▀█▄  █
   ▄█▀              ▀▀▀▀▀▀▀█▀  █▀    █▀▀                     ▀██   █▄

''', afterdelay=2)
            
            doDialogText("KNIGHT casts: METEOR BEAM!")
            printGraphic('''
                       ▄▄█████▄▄
▄▄▄                 ▄█▀       ▀███▄
█████████████▄▄▄▄▄▄ ▀▄▄         ▀███
███████████████████ ███████▀██████▀▀▄▄▄▄▄▄▄
███████████████████████████ ██████▀▄█████████████████▄▄▄▄▄▄▄▄▄▄
███████████████████▄████▀▀█▀█▀█████ █████████████████████████████
███████████████████▄███████▀███████▀█████████████████████████████
███████████████████▄███████▄██████ ██████████████████████████████
███████████████████▀▄███████▀███▀████████████████████████████████
████████████████▀ ██████████▄▄▄▄███▀█████████████████████████████
██████████████▀█▄████████████████████▀███████████████████████████
████████████▀ ▄███████████████████████▀██████████████████████████
▀▀▀▀▀▀▀▀▀▀▀▀▄▀█████████▀▄████████████▀▄██████████████████████████
█▄▄▄▄▄▄▄▄▄▄▄▀▄▄▄▄▄▄▄▄▄ █▄▄▄▄▄▄▄  █ ▀▀▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀████
█████████████▀███████ ▄██████████ ███ █████████████████▄▄▄▄▄▄▄▄▄▄
█████████████▄███████▀███████████ ██  ███████████████████████████
█████████████ ███████ ███████████▄██ ████████████████████████████
█████████████ ███████▀██████████████▄████████████████████████████
█████████████ ███████▀███████████████ ███████████████████████████
██████████████▀██████ ████████████▀███▄██████████████████████████
████████████▄████████▄████████████ ███ ██████████████████████████
█████▀▀▀▀▀▀▀██████████ ▀▀▀▀▀▀▀▀▀▀▀ ▀   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀
█████  ▄▄▄▄▄▀████████▀          ▄▄▄▄▄▄▄▄▄▄▄███████████
███████████▀▀  ██▀▀▀▄█████████████████████████████████
                ▀▀▀▀▀█▀▀▀███████████████████████████▀
                     █      ▀▀▀▀▀▀▀██████████████▀▀
                     █             ▀█
                    █         █     █▄
                    ▀        ▀▀      ▀

''', step=37)
            doDialogText("The DARK FIGURE was struck by it!")

            doDialogText("The DARK FIGURE collapsed.")
            doDialogText("The FOUNTAIN weakened.")
            doDialogText("ASHISH:# ughhh,## did we do it?")
            print()
            doDialogText("THE DARK FIGURE:# i.#.#.# j-")
            doDialogText("The darkness releases from the figure.")
            doDialogText("A man falls to the ground.")
            doDialogText("ASHISH:# is that.#.#.#")
            print(end='        ')
            doDialogText("DAD!!")
            doDialogText("Ashish runs over to the man.")
            doDialogText("ASHISH:# Dad,# are you okay?# We didn't mean to-#")
            doDialogText("RAJITH:# ashish.#.#.#", spd=5)
            doDialogText("It was ASHISH's father,# Rajith Nair.")
            doDialogText("ASHISH:# Dad.#.#.#")
            doDialogText("RAJITH:# sorry.#.#.# for.#.# hurting.#.#.##.##")
            doDialogText("ASHISH cast HEALING SONG!")
            doDialogText("RAJITH was healed.")
            doDialogText("RAJITH:# .#.#.#")
            doDialogText("ASHISH:# Dad?# Are you better now?")
            doDialogText(f"RAJITH:# I have to apologise.# Forgive me for trying to harm you,# {saveFile['name']}.")
            doDialogText("YOU:# Huh?")
            doDialogText("""RAJITH:# You see,# I was pretty worried and insecure about my son joining a new school.####
            When Ashish mentioned about a \"childhood friend\" that supposedly knew him, but didn't really exist,# that's when I really started to lose it.###
            And now that you came over for a sleepover,# I was on high alert.""")
            doDialogText("YOU:# Oh.")
            doDialogText("RAJITH:# I must apologize,# I got the wrong idea.")
            doDialogText("YOU:# Oh no it's okay.")
            doDialogText("ASHISH:# Oh,# dad.#.#.#")
            print()
            doDialogText("YOU:# Soooo.#.#.#")
            doDialogText("KNIGHT:# Yep,# this was ASHISH's dad's dream.")
            doDialogText("RAJITH:# I was taken by the darkness,# and even hurt my own son.#.#.#")
            doDialogText("ASHISH:# DAD it's alright!# It's just a little dream,# nothing will happen.")
            doDialogText("RAJITH:# You sure?", spd=4.5)
            doDialogText("ASHISH:# Yes,# I'm sure.")
            doDialogText("RANJITH:# KNIGHT,# was it?# You should seal the fountain now.#.#.#")
            doDialogText("KNIGHT:# Yes.")
            doDialogText("KNIGHT readies a spell:# SEAL")
            doDialogText("RANJITH:# Thank you everyone.#.#.#")
            doDialogText("\"...for freeing me from my darkness.\"")
            doDialogText("KNIGHT casts SEAL!")
            doDialogText("The room is filled with a bright light.")
            doDialogText("This is it.", afterdelay=3)
            print('\n')


            # BACK TO LIGHT WORLD
            doDialogText("You wake up gasping for air.")
            doDialogText("You're in the NORMAL world now.# The magic has lifted.")
            doDialogText("You look towards ASHISH and.#.#.###")
            doDialogText("...someone else is in the room.", spd=3)
            doDialogText("???:# Well.#.#.# I've been caught.")
            doDialogText("Ashish turns on the light.")
            doDialogText("ASHISH:# There's no way.#.#.#")
            print(end='        ')
            doDialogText("SIS?!?!?!")
            doDialogText(f"SEPT:# Well,# hello,# Ashish and {saveFile['name']}.")
            doDialogText("YOU:# You're the KNIGHT!")
            doDialogText("It was SEPTEMBER R NAIR,# Ashish's older sister.")
            doDialogText("SEPT:# Heh eh,# how's the bed that I lent you doing?")
            doDialogText("ASHISH:# SIS,# WERE YOU IN OUR DREAMS?!?!", spd=3)
            doDialogText("SEPT:# Well duh,# I was the KNIGHT.# Look,# I even got my helmet.")
            doDialogText("You look at the helmet kept on the ground.# It resembles the KNIGHT's helmet.")
            doDialogText("SEPT:# I was gonna try to convince you two that the KNIGHT really was a darkner - #this helmet.")
            print('      ')
            doDialogText("Buut# you guys already caught me.")
            doDialogText("ASHISH:# SIS HOW DID YOU EVEN GET INTO OUR DREAMS?!?!", spd=2)
            doDialogText("Ashish is bewildered beyond definition.")
            doDialogText("SEPT:# Using the dark world, ofcourse.")
            doDialogText("ASHISH:# BUT THAT'S A MADE UP THING!# ITS FROM A VIDEO GAME!")
            doDialogText("SEPT:# Not for tonight.# It's a special night -# Look outside.")
            doDialogText("You look outside,# and see a BLUE MOON.# Perhaps,# it's the DARKEST blue moon you've ever seen.")
            doDialogText("SEPT:# Haven't you heard of the ancient prophecy?")
            print(end='      ')
            doDialogText("On the night of the DARK BLUE MOON,# all fantasies come to life.# People used to use this moon to make their wishes come true,# but nowadays people just sleep through the night,# so no one actually uses it anymore.")
            doDialogText("ASHISH:# WHY PUT US ON THAT WHOLE ADVENTURE IN THE FIRST PLACE?!?!", spd=2)
            doDialogText("SEPT:# Come on,# you two absolutely suck at spending time together,# so I decided to put you on a little adventure.")
            print(end='      ')
            doDialogText("Brought you closer,# didn't it?")
            doDialogText("ASHISH:# SIS!!!!!", spd=3)
            doDialogText("SEPT:# Actually,# the real reason I wanted to do this was because Dad was having nightmares,# and y'know that stuff's not healthy.")
            print(end='    ')
            doDialogText("But I also discovered about you two,# so I decided to multitask and give you the adventure of your lives while saving dad.")
            doDialogText("YOU:# .#.#.## Are you the one that came here in the middle of the night and tried to stab me?")
            doDialogText("SEPT:# Oh dear,# I did NOT try to stab you.# I was just making the dark world.")
            print(end='      ')
            doDialogText("I wanted it to be fun,# so I also kept the video game running on your pc.# That game I recommended you last week.")
            doDialogText("ASHISH:# SIS GET OUT OF MY ROOM ALREADY!!!", spd=3.4)
            doDialogText("SEPT:# Okay,# it was nice having met you two.# Bye!")
            doDialogText("SEPT leaves the room.")
            doDialogText("ASHISH:# .#.#.# SIS WAIT!")
            doDialogText("SEPT pops her head back in.")
            doDialogText("SEPT:# Yes Ashish?")
            doDialogText("ASHISH:# Is dad doing okay?")
            doDialogText("SEPT:# Dad should be fine now,# but I'm gonna check on him just in case.# Don't worry.")
            doDialogText("ASHISH:# Okay.#.#.#")
            doDialogText("SEPT leaves the room again.")
            doDialogText("ASHISH:# .#.#.# i'm so sorry...")
            doDialogText("YOU:# Ehh,# it's fine.# The adventure was also fun.")
            doDialogText("ASHISH:# You're right about that,# I did have fun.#.#.#")
            print('        ')
            doDialogText("*yawn* are you also feeling sleepy right now?")
            doDialogText("YOU:# Actually yeah.#.#.#")
            doDialogText("ASHISH:# Wanna call it a night?")
            doDialogText("YOU:# Sure.# Goodnight.")
            doDialogText("ASHISH:# Goodnight.")
            doDialogText("You lie down on your bed.# Ashish is sound asleep already.#.#.##")
            doDialogText("Before you get ready to lose conciousness,# you get some notifications from the class group chat:")

            doCreditsSequence(soundImportSuccesful)

            finalSave = True
        else:

            doDialogText("As you and FLOWERY eat,# SR. CAR comes back.")
            doDialogText("SR. CAR:# Please excuse me for the trouble,# but it seems on your way here,# you ran into the guards of the Great Door.")
            if pgFilter: doDialogText("FLOWERY:# Oh shit.#.#.#")
            else: doDialogText("FLOWERY:# Oh no.#.#.#")
            doDialogText("YOU:# .#.#.#yes we did.")


            if route4['on_weirdRoute']:
                doDialogText("SR. CAR:# I've just been informed.#.#.#")
                doDialogText("         ...that both my best friends have died.")
                doDialogText("         I can't forgive that.")
                doDialogText("YOU:# uhh...")
                doDialogText("SR. CAR:# I'm afraid you have to die now.")
                doDialogText("FLOWERY:# Please,# it's what we had to do!")
                doDialogText("SR. CAR:# I know those two buffoons well.# If one of them died,# then the other would submit immediately.")
                doDialogText("         You didn't have to kill them both.#.#.# but you still did.")
                print()
                playSong('assets/soundtrack/enraged.ogg')
                doDialogText("SR. CAR grabs your throat.")
                doDialogText("YOUR SENSES FAIL TO HEIGHTEN DUE TO THE MALABAR CURRY!")
                doDialogText(f"FLOWERY:# {saveFile['name'].upper()}!# I'LL HELP-", afterdelay=0)
                doDialogText("Flowery got crushed by a falling piano that appeared out of nowhere.")
                doDialogText("YOU:# No..# Let go of me!")
                doDialogText("SR. CAR:# Mercy no longer deserves you.", spd=5)
                doDialogText("You equip the HARDCOVER AXE")
                if pgFilter: doDialogText("YOU HACK THE AXE INTO SR. CAR'S NECK!")
                else: doDialogText("YOU STRIKE SR. CAR WITH YOUR AXE!")
                doDialogText("SR. CAR:# ACK!")
                doDialogText("He lets go of you.")
                doDialogText("SR. CAR:# So,# you still have something left in you.#.#.#")
                doDialogText("         WHITE,# let's combine.")
                print()
                doDialogText("SR. CAR shines with a powerful glow.")
                doDialogText("He starts floating up into the air,# slowly transforming into a huge figure.")
                if pgFilter: doDialogText("YOU:# What the fuck is happening...")
                else: doDialogText("YOU:# What the heck is happening...")
                doDialogText(f"FLOWERY:# {saveFile['name'].upper()}!")
                doDialogText("You turn around to find FLOWERY,# who has lifted the piano off of him.")
                doDialogText("FLOWERY:# I'm feeling a strong sense of overwhelming energy.")
                if pgFilter: doDialogText("YOU:# What the fuck is happening up there?!")
                else: doDialogText("YOU:# What is happening up there?!")
                doDialogText("FLOWERY:# It seems like he's transforming.#.#.# and giving off a lot of energy as light.")
                stopSong()
                doDialogText("         Hey,# wait!# I can use this energy to transform!")
                doDialogText("YOU:# You can transform?!")
                doDialogText("FLOWERY:# I probably could.#.#.# but I've never tried it before.")
                doDialogText("YOU:# What are you waiting for?!# Let's do it!")

                playSong('assets/soundtrack/mechfight_intro.ogg')
                doDialogText("FLOWERY spreads its petals,# absorbing the light emitted by SR. CAR.")
                doDialogText("FLOWERY starts growing!")
                doDialogText("You also focus on absorbing energy.")
                doDialogText("Before you know it,# you're floating in the sky with FLOWERY as well.")
                doDialogText("You can feel your SOULS unite,# even if just for this one fight.")
                doDialogText("You begin transformation along with FLOWERY.")
                doDialogText(".#.#.#", afterdelay=3)
                doDialogText("You have now transformed into a giant flower.#.#.#")
                doDialogText("...with somewhat muscular arms.", afterdelay=2)
                print()

                if not saveFile['route4']['COMPLETED']:
                    doDialogText("DEVELOPER NOTE:")
                    doDialogText("This is a very experimental setup.# You will soon see a display on screen.")
                    doDialogText("Please use your ARROW keys to change the screen size to your liking,# and confirm it by pressing enter.")
                    doDialogText("Also since I'm making this in a rush,# PLEASE make sure you enabled KEYBOARD INPUT.")
                    print()
                

                loadModule('lib/fightplayer/setup.py')


                playSong('assets/soundtrack/mechfight.ogg', looping=True)
                loadModule('lib/fightplayer/mechfight.py')

                stopSong()

                doDialogText("SR. TRANSFORMER has been defeated.", afterdelay=3)
                print()
                doDialogText("You and FLOWERY split into your original forms.")
                doDialogText("FLOWERY:# That was insane.#.#.#")
                doDialogText("You notice two items on the ground.")
                doDialogText("YOU:# Are these.#.#.# gloves?")
                doDialogText("You equip the TRUCK GLOVES.")
                doDialogText("ATTACK raised by 30!")
                doDialogText("FLOWERY:# What are those?")
                doDialogText("YOU:# Woah,# I feel insanely strong!")
                doDialogText("Suddenly,# an elevator appears in front of you.")
                doDialogText("FLOWERY:# Why is there an elevator here?")
                doDialogText("YOU:# Maybe it could take us to the fountain.")
                doDialogText("FLOWREY:# .#.#.#eh,# let's try our luck.")
                

            else:
                doDialogText("SR. CAR:# I've received a call from the Royalty.# I've been instructed to kill you both if I find you.")
                doDialogText("YOU:# what.")
                doDialogText("FLOWERY:# Those guards must've been pretty important to the Royalty.#.#.#")
                doDialogText("SR. CAR:# Worry not,# however.# I can understand where you're coming from.")
                doDialogText("         Despite having killed a Great Guard,# I know it's what you probably had to do.")
                doDialogText("         So I won't kill you.")
                doDialogText("FLOWERY:# Oh wait really?")
                doDialogText("YOU:# So are we safe?")
                doDialogText("SR. CAR:# For now,# yes.# I won't do anything to you.")
                doDialogText("         However,# you're trying to \"leave\" this Dark World,# aren't you?")
                doDialogText("YOU:# Yeah,# we're looking for the Dark Fountain.")
                doDialogText("SR. CAR:# The only way to exit is to seal the fountain itself,# and other darkners will definitely try to stop you.")
                doDialogText("          Though I have no objection,# it won't be easy for you.")
                doDialogText("YOU:# We'll deal with it.# We'll seal the fountain.")
                doDialogText("SR. CAR:# Im afraid I can only help you get to the Fountain.")
                doDialogText("         But first,# we must end this show.# If it goes on,# people will find you,# and I won't be able to help you.")
                doDialogText("         What do you say,# folks?")
                doDialogText("One of the walls suddenly collapses to reveal a stage full of people cheering.")
                playSong("assets/soundtrack/tv_show_2_loop.ogg", looping=True)
                doDialogText("SR. CAR:# FOLKS!# I'm afraid we'll have to end this show early!# It's time for our participants to depart!")
                doDialogText("         Shall we give them a send-off?")
                doDialogText("The Crowd cheers very aggressively.")
                doDialogText("SR. CAR:# You two,# thank you for participating in our famous late night game show.")
                doDialogText("         Though this time it had to end early,# we will be here every night.")
                doDialogText("         And to make up for this abrupt ending,# the next one will be MUCH MORE FUN,# CHALLENGING,# THRILLING.#.#.#")
                doDialogText("         and we hope to see you in the next one!# Thanks for stopping by in the Reviewer's Paradise!.")
                stopSong()
                playSong('assets/soundtrack/tv_show_2_end.ogg')
                doDialogText("         See you on the next one!")
                doDialogText("The crowd continues to cheer,# even louder this time.")
                doDialogText("SR. CAR:# Please,# stand by folks.")
                doDialogText("A huge Elevator spawns in the stage.")

                doDialogText("SR. CAR:# Once you enter this elevator,# you'll be transported to the Queen's Castle.")
                doDialogText("         I can't take you directly to the fountain,# but the castle can.")
                doDialogText("         Inside the castle lies a door which takes you straight to the fountain is.")
                doDialogText("         Right now,# it's in the middle of nowhere,# and only the door can take you there.")
                doDialogText("FLOWERY:# We'll have to be ready to face the darkners.#.#.#")
                doDialogText("         The closer we get to the fountain,# the stronger the darkners get.")
                doDialogText("SR. CAR:# You're right about that.")
                doDialogText("         That's right!# We almost forgot about your prize!")
                doDialogText("         here, take this.")
                doDialogText("YOU GOT THE AUTO COOKER!", spd=6, step=2)
                inventory += ['AUTO COOKER']
                doDialogText("YOU:# Oh sweet,# thanks!")
                doDialogText("SR. CAR:# Let this help you on your journey.")
                doDialogText("         Now,# step into the elevator,# and good luck.")
            
            doDialogText("You and FLOWERY step into the elevator.")
            doDialogText("The Elevator starts moving with a faint hum.")
            doDialogText("FLOWERY:# Are you ready?")
            doDialogText("YOU:# I'm ready.")
            doDialogText("YOU AND FLOWERY:# Lets do this.", afterdelay=3)
            print()
            doDialogText("The Elevator door opens.# You're faced with a huge,# black castle.")
            doDialogText("The darkness from the castle dulls your senses.")
            doDialogText("FLOWERY:# Wow,# that's.#.#.# really dark.")
            doDialogText("YOU:# Let's go inside.")
            print()
            doDialogText("You approach the castle and open the door.")
            playSong('assets/soundtrack/castle_walls.ogg', looping=True)
            doDialogText("A strange atmosphere of sound fills your ears.")
            doDialogText("You can hear distant noise.#.#.# a PULSING.")
            doDialogText("YOU:# .#.#.#okay,# so far there's no one.")
            doDialogText("The castle is completely black inside,# with white outlines on objects.")
            doDialogText("FLOWERY:# We have to get to the center of the castle,# so let's keep going straight.")
            doDialogText("YOU:# Okay.")
            doDialogText("You and FLOWERY walk along the hallways of the castle.")
            doDialogText("The Hallways are pitch black colored,# with torches of white flames on the walls.")
            doDialogText("There's a pitch black carpet on the floor.")
            doDialogText("YOU:# You think anyone would have noticed us by now?")
            doDialogText("FLOWERY:# Not sure.#.#.#")
            doDialogText("         Wait stop.# shh.")
            doDialogText("You stop in your tracks.", afterdelay=2)
            doDialogText("YOU:# what happened?")
            doDialogText("FLOWERY:# I can hear a guard.# Take the left hallway.")
            doDialogText("YOU:# oh,# okay.")
            doDialogText("You quietly navigate through the castle,# somehow avoiding all the other guards in the castle with the help of FLOWERY.", afterdelay=3)
            doDialogText("YOU:# is that snoring?")
            doDialogText("FLOWERY:# It's coming from this room.")
            doDialogText("You and FLOWERY slowly enter the room.")
            doDialogText("You find a sleeping rook.")
            doDialogText("YOU:# Are you thinking what I'm thinking?")
            doDialogText("FLOWERY:# Yep.# Say it at the same time?")
            doDialogText("YOU:# Yep.### 3,###### 2,######, 1..######")
            print('\n' + "YOU: We ride the rook and use it to navigate.\nFLOWERY: We tie him up and interrogate him.")
            time.sleep(1.5)
            doDialogText("FLOWERY:# excuse me-# what?")
            doDialogText("YOU:# This rook is huge!# There's enough space for both of us.")
            if pgFilter:
                doDialogText("FLOWERY:# How the hell are we gonna ride it??")
            else: doDialogText("FLOWERY:# How would we even ride it??")
            doDialogText("YOU:# Just get on it.")
            doDialogText("FLOWERY:# .#.#.#fine.")
            doDialogText("You and FLOWERY get on top of the rook, waking it up.")
            doDialogText("ROOK:# Huh,# what the-")
            doDialogText("      WHO'S ON TOP OF ME?!")
            doDialogText("      GET OFF,# PLEASE IT HURTS!")
            doDialogText("YOU:# Take us to the fountain door.")
            doDialogText("ROOK:# I CAN'T DO THAT.# YOU GUYS ARE OUTSIDERS.")
            doDialogText("      PLEASE,# I HAVE NO ARMS,# I CAN'T TAKE YOU OFF MYSELF.")
            doDialogText("      IT HURTS SO BAADD,# PLEASE.")
            doDialogText("YOU:# Take us to the fountain.")
            doDialogText("ROOK:# OKAY OKAY FINE,# PLEASE GET OFF FIRST.")
            doDialogText("YOU:# No,# take us to the fountain first.")
            doDialogText("ROOK:# PLEASEEEE,# I'LL TAKE YOU TO THE FOUNTAIN RIGHT NOW.")
            doDialogText("YOU:# Okay,# great!# See?")
            doDialogText("FLOWERY:# what the heck did i just witness?")
            doDialogText("The rook starts moving.# You breeze throught the hallways so fast the guards don't even see you.")
            doDialogText("YOU:# Holy hell you're fast.")
            doDialogText("ROOK:# PLEASE,# I JUST NEED YOU TO GET OFF OF ME.")
            print()
            doDialogText(".#.#.#", afterdelay=3)
            doDialogText("After a while,# the rook stops in front of a door.")
            doDialogText("FLOWERY:# Are we here?")
            doDialogText("ROOK:# Yes,# PLEASE GET OFF!")
            doDialogText("You and FLOWERY get off of the rook.")
            doDialogText("YOU:# Hey,# this door is locked.")
            doDialogText("     Do you know what the passwo-", afterdelay=0.6)
            doDialogText("The rook is gone.")
            doDialogText("FLOWERY:# He probably went to alert the guards.# We better hurry!")
            doDialogText("YOU:# Okay,# let's solve this quick then.")
            doDialogText("The door is locked behind a puzzle.#")
            doDialogText("Below the puzzle it says \"N b1 -> c3\"")
            doDialogText("YOU:# What does this mean?")
            doDialogText("FLOWERY:# Isn't that chess notation?")
            doDialogText("YOU:# Chess notation?")
            doDialogText("FLOWERY:# Yeah,# it represents a move you make in a chess game.")
            print()
            doDialogText("There's an interface that lets you enter three directions,# and a keypad which lets you enter the four directions up, down, left and right.")
            doDialogText("FLOWERY:# Maybe you have to trace the knight's path?")
            doDialogText("YOU:# Let's see.#.#.#")
            doDialogText("     The hint suggests that the Knight is at b1,# and moves to c3.")
            doDialogText("FLOWERY:# Lets start inputting things.")
            doDialogText("YOU:# Wait.# a1 is at the bottom left corner of the board right?")
            doDialogText("FLOWERY:# Yes,# and remember:# The squares from a1-a8 are a vertical file.")
            doDialogText("YOU:# Okay got it.")
            print()
            tries = 0
            move = ''
            doDialogText("TYPE L, R, U, or D in a sequence to enter your input.")
            while move not in ['UUR', 'RUU', 'URU']:
                move = ''
                if tries == 10:
                    doDialogText("FLOWERY:# Damn,# this is taking a while.")
                elif tries == 20:
                    doDialogText("FLOWERY:# I thought the guards would be here by now,# where are they?")
                elif tries == 25:
                    doDialogText("FLOWERY:# Move over,# let me try.")
                    doDialogText("FLOWERY unlocked the door.")
                    doDialogText("FLOWERY:# See?# First try.")
                    doDialogText("YOU:# I-#I was gonna input that next!")
                    doDialogText("FLOWERY:# Blatant lie,# bro.# Let's go already.")
                    break
                moveInput = input("INPUT: ").upper()
                tries += 1
                for i in moveInput:
                    if i in 'LURD':
                        move += i
            if tries < 25:
                doDialogText("FLOWERY:# Yes,# we got it!")
                doDialogText("YOU:# I'm pretty surprised we didn't have to fight anyone.#")
                doDialogText("FLOWERY:# Yeah,# we got really lucky.")
            
            stopSong()
            doDialogText("You open the door.")
            doDialogText("It reveals a path that slowly grows darker the further you get.")
            doDialogText("There's a faint light at the end of the tunnel.")
            doDialogText("FLOWERY:# I can sense it.#.#.#")
            doDialogText("         THE FOUNTAIN.", spd=5, afterdelay=3)
            print()
            doDialogText("YOU:# Let's seal it then.")
            print()
            doDialogText("You and FLOWERY slowly take a step.")
            doDialogText("A Dark sensation pushes back.")
            doDialogText("With each step,# the Darkness pushes back further.#.#.#")
            doDialogText("...until it doesn't.")
            doDialogText("Slowly,# the Darkness begins to nudge you closer,")
            doDialogText("pushing you closer into the darkness.")
            doDialogText("It pushes you in faster than you can think,# and-#", afterdelay=0)
            print()
            doDialogText("|| CRASH! ||", spd=6, step=2, afterdelay=2)
            print()
            doDialogText("You find yourself on a different ground.")
            doDialogText("You and FLOWERY are out of the castle.")
            doDialogText("???:# No way...")
            doDialogText("You quickly look upto the familiar voice.")
            doDialogText("YOU:# No way...")
            doDialogText("FLOWERY:# It's the fountain!")
            doDialogText("WAYDANT:# I found you!")
            doDialogText("         Listen guys,# I found a way out.")
            doDialogText("         These guys called \"Darkners\" told me they would take us to a place,# and from there we can go back to our old world!")
            doDialogText("         But in return,# I have to guard this,# uh,# \"Fountain\" from two bad guys that are about to come here.")
            doDialogText("         You can help me right?")
            doDialogText("YOU: .#.#.#####what?")
            doDialogText("WAYDANT:# Who's your big flower friend,# by the way?")
            doDialogText("FLOWERY:# WAYDANT.#.#.# ", afterdelay=0, line=0)
            playSong('assets/soundtrack/enraged.ogg', looping=True)
            doDialogText("we need to seal that fountain.")
            doDialogText("WAYDANT:# What?!# No!# We have to guard it,# the Darkners will take us out of this world!")
            doDialogText("YOU:# What is going on?# I thought we had to seal it!")
            doDialogText("FLOWERY:# WAYDANT,# they're lying to you.")
            doDialogText("WAYDANT:# W-#what.#.## No!")
            doDialogText("         Theres no way!")
            doDialogText("FLOWERY:# WAYDANT.#.#.# there's no way to simply get out of a Dark World.")
            doDialogText("         The fountain is what gives shape to this world.# We must destroy it.")
            doDialogText("WAYDANT:# But then what about the exit?!# They told me there was an exit!")
            doDialogText("FLOWERY:# There's no exit out of a dark world.#.#.# You must seal it.")
            doDialogText("         ...god this is annoying...")
            doDialogText("???:# What's the hold up,# WAYDANT?")
            doDialogText("WAYDANT:# The Bishop!")
            if pgFilter: doDialogText("YOU:# What the fuck.#.#.#")
            else: doDialogText("YOU:# A bishop?")
            doDialogText("WAYDANT:# Bishop,# are you lying to me?")
            doDialogText("BISHOP:# Lying about what?")
            doDialogText("WAYDANT:# How to leave the dark world.# They told me I have to seal it.")
            doDialogText("BISHOP:# UTTER FOOLISHNESS!# THE FOUNTAIN MUST REMAIN INTACT!")
            doDialogText("        Listen WAYDANT,# these must be the enemies the prophecy warns us about.")
            doDialogText("        They are NOT your friends.# They're here to simply seal the fountain.")
            doDialogText("        Whatever they tell you,# do not believe them.")
            doDialogText("        If this Dark World collapses while we're in it.#.#.#")
            doDialogText("        You will die.")
            doDialogText("WAYDANT:# .#.#.#")
            doDialogText("         So,# you tried to kill me?")
            doDialogText("FLOWERY:# He's lying!# You guys will be fine!")
            doDialogText("BISHOP:# So this one's the mastermind.")
            doDialogText("        WAYDANT,# do not forgive a single one of them.")
            doDialogText("WAYDANT:# .#.#.#")
            doDialogText("         Yes,# Bishop.")
            doDialogText("YOU:# WAYDANT,# are you gonna fight us?")
            doDialogText("WAYDANT:# I'm afraid I got no other choice.")
            doDialogText("BISHOP:# That you're right about,# WAYDANT...")
            doDialogText("         ...heh.")
            doDialogText("FLOWERY:# Oh boy.#.#.# I can tell this guy's strong.")
            
            stopSong()
            if route4['on_weirdRoute']:
                doDialogText("YOU:# Leave it to me then.")
                doDialogText("FLOWERY:# What?")
                print()
                playSong('assets/soundtrack/guardian.ogg', looping=True)
                doDialogText("You use TRUCK GLOVES to speed up to WAYDANT.")
                doDialogText("WAYDANT:# WHAT THE-#", afterdelay=0)
                doDialogText("YOU:# You ever been hit by a truck?")
                doDialogText("You smash two POWERFUL hits into WAYDANT's body,# enough force to equal a truck.")
                doDialogText("WAYDANT:# EUGH.#.#")
                doDialogText("WAYDANT spits blood on the floor.")
                doDialogText("WAYDANT:# so...# strong...")
                doDialogText("YOU:# Damn,# these gloves are handy as hell.")
                doDialogText("WAYDANT:# I.#.#.## I.#.#.#")
                doDialogText("YOU:# You still think you can stop me?")
                doDialogText("WAYDANT takes out a dark tinted crystal.")
                doDialogText("WAYDANT:# ...In Tenembre...")
                doDialogText("YOU:# ?")
                doDialogText("WAYDANT:# ...### TENEBRAE IN CORDE MEO FREMANT!")
                doDialogText("Suddenly,# the fountain flashes.")
                doDialogText("Three powerful dark attacks stand above you.")
                doDialogText("You use your TRUCK SPEED to swiftly weave through the attacks.")
                doDialogText("YOU:# Impressive latin you've got there.")
            else:
                doDialogText("YOU:# Yeah,# he's pretty strong.")
                doDialogText("     It's gonna be a tough battle if we have to fight him.")
                print()
                playSong('assets/soundtrack/guardian.ogg', looping=True)
                doDialogText("YOUR SENSES HEIGHTEN IN RESPONSE TO WAYDANT'S CHARGE!")
                doDialogText("You narrowly dodge it.")
                print()
                # BATTLE LOOP
                turn = 0
                wayHP = 500
                guardDef = 5
                guardAtk = 40
                guarde = 0
                shownSpells = False
                spellCooldown = 0
                firstSpell = True
                castSpell = False
                while turn < 15:
                
                    if player['hp'] <=0:
                        player['hp'] = 1
                        doDialogText("Your HP reached 0...")
                        doDialogText("...but you held on!", afterdelay=1)
                        doDialogText("HP regenerated to 1.")
                    if turn == 5:
                        doDialogText("BISHOP:# WAYDANT!# You haven't taken care of these small fry yet?")
                        doDialogText("WAYDANT:# SHUT UP!# IM TRYING!")
                        doDialogText("WAYDANT's attack increased.")
                        guardAtk += 20
                    if spellCooldown > 0: spellCooldown -= 1
                    btselect = doDialogChoice("What will you do?", choices=['Fight', 'Acts', 'Spell', 'Item', 'B̶e̶g̶ f̶o̶r̶ m̶e̶r̶c̶y̶'])
                    
                    print()
                    if btselect == 5:
                        doDialogText("Mercy isn't an option to WAYDANT.")
                        
                    elif btselect == 1:
                        playingPlayers = ["You"]
                        if flowery['hp'] > 0: playingPlayers += ["Flowery"]
                        doDialogText(f"{", ".join(playingPlayers)} get ready to strike!")
                        fightResult = doTimedAttack(3, 3, 2.8)
                        playingStructs = [player]
                        if flowery['hp'] > 0: playingStructs += [flowery]
                        if fightResult > 0.2:
                            totalAtk = 0
                            for pl in playingStructs:
                                totalAtk += pl['attack']
                            dmg = math.ceil((totalAtk)*fightResult/guardDef)
                            wayHP -= dmg
                            doDialogText(f"Your party deals {dmg} damage to WAYDANT! ({wayHP}/500)")
                        else:
                            doDialogText("Your party missed!")
                    elif btselect == 2:
                        action = doDialogChoice("ACTS:", choices=['Check', 'Talk'] + ['Return.'])
                        
                        if action == 1:
                            doDialogText("WAYDANT:\nATK: 40\nDF: 15")
                            doDialogText("Your final obstacle.")
                            print()
                            continue
                        elif action == 2:
                            doDialogText("You try to talk to WAYDANT.")
                            doDialogText("He does not listen to you.")
                            print()
                        else: continue
                    elif btselect == 3:
                        if not shownSpells:
                            shownSpells = True
                            doDialogText("From the exposure of darkness,# FLOWERY's PHOTOSYNTHESIS evolved into DARKSYNTHESIS!")
                            flowery['spells'][0] = 'DARKSYNTHESIS'
                            flowery['spells'].append('VON GUARDE')
                            doDialogText("FLOWERY learnt VON GUARDE!")
                        spell = doDialogChoice("SPELLS:", choices=flowery['spells'] + ['Return.'])
                        spell = (flowery['spells'] + ['Return'])[spell-1]
                        if spell == "DARKSYNTHESIS":
                            if spellCooldown == 0:
                                spellCooldown = 3
                                if firstSpell:
                                    doDialogText("Flowery channeled the dark presence...")
                                    doDialogText("His petals turned dark!")
                                    firstSpell = False
                                doDialogText("FLOWERY LAUNCHES HIS DARK PETALS TOWARDS WAYDANT!")
                                dmg = 24 + random.randint(-12, 12)
                                wayHP -= dmg
                                doDialogText(f"THE PETALS DEAL {dmg} DAMAGE TO WAYDANT! ({wayHP}/500)")
                            else:
                                doDialogText(f"FLOWERY can only use this spell after {spellCooldown} turn{'s'*(spellCooldown != 1)}.")
                        elif spell == "VON GUARDE":
                            if guarde < 2:
                                doDialogText("FLOWERY used VON GUARDE!")
                                doDialogText(f"Your party's defensed has been raised by {(3 - guarde)}.")
                                guarde += 1
                                player['defense'] += 3-guarde
                                flowery['defense'] += 3-guarde
                            else:
                                doDialogText("FLOWERY used VON GUARDE!")
                                doDialogText("But it failed to raise your defense any further!")
                        else: continue
                    elif btselect == 4:
                        item = doDialogChoice("ITEMS:", choices=inventory + ["Return."])
                        curItem = (inventory + ['Return.'])[item-1]
                        if curItem == "AUTO COOKER":
                            doDialogText("The AUTO COOKER spits out a Chicken Curry.")
                            if flowery['hp'] == 0:
                                doDialogText("FLOWERY wakes up to the smell of the Chicken Curry.")
                            doDialogText("You and FLOWERY quickly share a meal before getting ready to battle.")
                            player['hp'] = getMaxHP(1)
                            doDialogText(f"{saveFile['name']} was HEALED. ({player['hp']}/{getMaxHP(1)})")
                            flowery['hp'] = getMaxHP(4)
                            doDialogText(f"FLOWERY was HEALED. ({str(flowery['hp'])}/{str(getMaxHP(4))})")
                        else:
                            doDialogText("You cannot use this item.")
                    
                    print()
                    # WAYDANT's TURN
                    target = random.randint(0, 1)
                    targetStruct = [player, flowery][target]
                    targetName = ["You", 'FLOWERY'][target]
                    if 0 <= turn < 5:
                        attack = random.randint(0, 2)
                        if attack == 0:
                            doDialogText("WAYDANT RUSHES IN FOR A PUNCH!")
                            fResult = doTimedAttack(3, 1, 2)
                            dmg = getDamageDealt(guardAtk, targetStruct, fResult)
                            
                            if fResult >= 0.9:
                                doDialogText(f"{targetName} narrowly avoided his punch.")
                            else:
                                targetStruct['hp'] -= dmg
                                doDialogText(f"{targetName} was struck!")
                                if targetStruct['hp'] <= 0: targetStruct['hp'] = 0
                                doDialogText(f"{targetName} lost {dmg} HP! ({targetStruct['hp']}/{getMaxHP(target*3+1)})")
                                if flowery['hp'] == 0:                                    
                                    doDialogText("FLOWERY fainted.")
                        elif attack == 1:
                            doDialogText("WAYDANT LIFTS A GIANT ROCK!")
                            fResult = doTimedAttack(3, 1, 2)
                            dmg = getDamageDealt(guardAtk, targetStruct, fResult)
                            
                            if fResult >= 0.9:
                                doDialogText(f"{targetName} quickly ducks, narrowly dodging the rock.")
                            else:
                                targetStruct['hp'] -= dmg
                                doDialogText(f"{targetName} was hit by the rock!")
                                if targetStruct['hp'] <= 0: targetStruct['hp'] = 0
                                doDialogText(f"{targetName} lost {dmg} HP! ({targetStruct['hp']}/{getMaxHP(target*3+1)})")
                                if flowery['hp'] == 0:                                    
                                    doDialogText("FLOWERY fainted.")
                        elif attack == 2:
                            doDialogText(f"WAYDANT RUNS TOWARDS {targetName.upper()}!")
                            fResult = doTimedAttack(3, 1, 2)
                            dmg = getDamageDealt(guardAtk, targetStruct, fResult)
                            
                            if fResult >= 0.9:
                                doDialogText(f"{targetName} moves out of the way,# barely avoiding the attack.")
                            else:
                                targetStruct['hp'] -= dmg
                                doDialogText(f"{targetName} was struck!")
                                if targetStruct['hp'] <= 0: targetStruct['hp'] = 0
                                doDialogText(f"{targetName} lost {dmg} HP! ({targetStruct['hp']}/{getMaxHP(target*3+1)})")
                                if flowery['hp'] == 0:                                    
                                    doDialogText("FLOWERY fainted.")
                    
                    elif 5 <= turn < 12:
                        attack = random.randint(0, 2)
                        if not castSpell: attack = 2
                        if attack == 0:
                            doDialogText("WAYDANT PUNCHES THE GROUND HARD!")
                            doDialogText("A SHOCKWAVE EMERGES FROM THE GROUND.# DODGE IT!")
                            fResult = doTimedAttack(3, 1, 2)
                            dmg = getDamageDealt(guardAtk, targetStruct, fResult)
                            
                            if fResult >= 0.9:
                                doDialogText(f"You and FLOWERY jumped on time.")
                            else:
                                player['hp'] -= dmg
                                flowery['hp'] -= dmg
                                doDialogText(f"YOU and FLOWERY were caught in the shockwave!")
                                if flowery['hp'] <= 0: flowery['hp'] = 0
                                doDialogText(f"FLOWERY lost {dmg} HP! ({flowery['hp']}/{getMaxHP(4)})")
                                if player['hp'] <= 0: player['hp'] = 0
                                doDialogText(f"YOU lost {dmg} HP! ({player['hp']}/{getMaxHP(1)})")
                                if flowery['hp'] == 0:                                    
                                    doDialogText("FLOWERY fainted.")
                        elif attack == 1:
                            doDialogText("WAYDANT TRIPS AND FALLS!")
                            doDialogText("HE CREATES A POWERFUL SHOCKWAVE!.# DODGE IT!")
                            fResult = doTimedAttack(3, 1, 3)
                            dmg = getDamageDealt(guardAtk, targetStruct, fResult)*1.3
                            
                            if fResult >= 0.9:
                                doDialogText(f"You and FLOWERY jumped on time.")
                            else:
                                player['hp'] -= dmg
                                flowery['hp'] -= dmg
                                doDialogText(f"YOU and FLOWERY were caught in the shockwave!")
                                if flowery['hp'] <= 0: flowery['hp'] = 0
                                doDialogText(f"FLOWERY lost {dmg} HP! ({flowery['hp']}/{getMaxHP(4)})")
                                if player['hp'] <= 0: player['hp'] = 0
                                doDialogText(f"YOU lost {dmg} HP! ({player['hp']}/{getMaxHP(1)})")
                                if flowery['hp'] == 0:                                    
                                    doDialogText("FLOWERY fainted.")
                        elif attack == 2:
                            if not castSpell:
                                doDialogText("WAYDANT:# Let's see if this works.")
                                doDialogText("WAYDANT pulls out a dark tinted crystal.")
                                doDialogText("WAYDANT:# ...In Tenebris Mergere...")
                                doDialogText("The FOUNTAIN momentarily shined.")
                                doDialogText(f"A DARK ATTACK SPAWNS ABOVE {targetName.upper()}!# DODGE!")
                            else:
                                doDialogText("WAYDANT casts DARKNESS!# DODGE!")
                            fResult = doTimedAttack(3, 1, 4)
                            dmg = getDamageDealt(guardAtk, targetStruct, fResult)*1.6
                            
                            if fResult >= 0.9:
                                doDialogText(f"YOU and FLOWERY dodged the darkness!")
                            else:
                                player['hp'] -= dmg
                                flowery['hp'] -= dmg
                                doDialogText(f"YOU and FLOWERY got caught in the darkness!")
                                if flowery['hp'] <= 0: flowery['hp'] = 0
                                doDialogText(f"FLOWERY lost {dmg} HP! ({flowery['hp']}/{getMaxHP(4)})")
                                if player['hp'] <= 0: player['hp'] = 0
                                doDialogText(f"YOU lost {dmg} HP! ({player['hp']}/{getMaxHP(1)})")
                                if flowery['hp'] == 0:                                    
                                    doDialogText("FLOWERY fainted.")
                            
                            if not castSpell:
                                doDialogText("WAYDANT:# Woah.#.#.#")
                                castSpell = True
                                
                    turn += 1
            
            stopSong()
            doDialogText("WAYDANT collapses.")
            doDialogText("WAYDANT:# I can't.#.#.# I have to.#.#.# protect.#.#.#")
            doDialogText("???:# Useless.")
            doDialogText("YOU:# What?")
            doDialogText("WAYDANT:# KING!# I'm sorry!# I let you down.")
            doDialogText("KING:# That you have.")
            doDialogText("      You're no longer useful to me.# I shall have you discarded now.")
            doDialogText("WAYDANT:# ...what?")
            doDialogText("FLOWERY suddenly grabs WAYDANT.")
            doDialogText("FLOWERY:# WATCH OUT!")
            doDialogText("Before you can even comprehend,# something moves past you at a speed high enough to kill someone.")
            doDialogText("QUEEN:# Tch.# Almost had him.")
            playSong('assets/soundtrack/enraged.ogg', looping=True)
            doDialogText("WAYDANT:# QUEEN!# Why would you.#.#.#")
            doDialogText(f"FLOWERY: {saveFile['name'].upper()}!# QUICK,# SEAL THE FOUNTAIN!", spd=2)
            doDialogText("YOU:# What?# But I don't know-", afterdelay=0)
            doDialogText("FLOWERY:# YOU'LL FIND YOUR WAY!# I'LL HOLD THEM OFF,# SO QUICK!", spd=2)
            doDialogText("YOU:# O-#OKAY!")
            doDialogText("You start running towards the fountain as fast as you can.")
            doDialogText("KING:# Get him!")
            doDialogText("QUEEN:# Got it,# King-", afterdelay=0)
            doDialogText("FLOWERY:# Not so fast!")
            doDialogText("FLOWERY stands in the way of QUEEN,# restraining her for a few seconds.")
            doDialogText("QUEEN:# Damn you insolate flower.#.#.#")
            doDialogText("       Take this!")
            printGraphic('''
████████████████████████▀▄▄████▄ ▀████████████████████████████████████
████████████▀█████████▀▄▄████████▄ ▀██████████████████████████████████
██████████▀  ▄▄▄▄▄▄▀ ▄█████████████▄▀█████████████████████████████████
█████████▀ █▄██████ █████████████████ ████████████████████████████████
█████████ █████████▀▀▀▀██████████████▄▀▄▄▄▀███████████████████████████
████████▀▄████████     █▀██████████████▄██ ███████████████████████████
████████ ████████      ▄█▀███████████▄█▀██ ███████████████████████████
████████ ▀██████         ▀███████████▀ ███ ███████████████████████████
█████████ █████▀        ▄ ▀████████▀▄▄████ ███████████████████████████
█████████▀ ████       ▄███ ████▀▀ ▄██████▀█▄███████▀▀▀ ▀██████████████
████████▀▄█▄▄██    ▄▄█████ ███▄▄████████ ████████▀      ██████████████
████████ ██████  ▄████████ ████████████▄█████████       ██████████████
████████▄▀█████▄▀████████ ████████████▀▄███████████     ████████████▀▀
██████████ █████ ▀█████▀ ███▀▀▀▀▀▀▀▄█▀▀▄███████████     ██████▀▀▀
███████████ ▀▀███▄  ▄▄▄█████████ ███▄█████████████     █▀▀▀
█████████████  ▄█████▀██████████ ████████████████▀▄▄▄█▀
█████████████▄▀▀█▀███▄ ██████▀▀ ██▀██████████▀▀▀▄███▀
███████████████▄▄█▄█▀▀█ ▄▄▄▄▄▄█▀▀  ████▀▀▀    ▄████
███████████████████▄██▀████████▄█▀▀▀        ▄████▀
███████████████████████████▀▀▀   ▄▄       ▄████▀
█████████████████████▀▀▀      ▄███      ▄████▀
████████████████▀▀▀           ████    ▄███▀▀
██████████▀▀▀        ▄▄▄▄     ██▀▀ ▄ ▀▀▀
████▀▀▀                █▀▀     ▄  ▀▀
▀                          ▄▄██▀        ▄▄ ▀█▀
                     ▄▄▄    ▀▀▀
         ▄▄▄▄▄▄▄████▀▀▀        ▄  █    ▀█▀  ██▀▀
       ▀▀            ▄▄▄▄▄█▄   █▀          ▀▀
                      ▀▀███▀      ▄  ▀  ▀
                      ▄█▀ ▄▄   █▄██
                       ▄▄▀▀█    ▀████
                       ▀   ▀     ▀███
                                   ███▄
                                   ▀███
                                    ▀▀█▄

''')
            doDialogText("FLOWERY was snapped in half.")
            doDialogText("YOU:# FLOWERY!")
            doDialogText("SEVERED FLOWERY:# ...go...# seal it.")
            doDialogText("QUEEN:# Next,# that kid-", afterdelay=0)
            doDialogText("WAYDANT:# IN TENEBRIS MONGERE!", spd=3)
            doDialogText("QUEEN dodges WAYDANT's dark attack.")
            doDialogText("QUEEN:# You brat...# I regret giving you that Shadow Crystal.")
            doDialogText("WAYDANT:# Don't worry about us!# SEAL IT!")
            doDialogText("YOU:# Okay.")
            print()
            doDialogText("You focus deep inside.")
            doDialogText(".#.#.#")
            doDialogText("You feel a growing light within your heart.", spd=5)
            doDialogText("Soon,# everything goes bright.", spd=6)
            print()
            stopSong()
            doDialogText(".#.#.#", spd=7)
            doDialogText("You open your eyes.")
            doDialogText("Everything is black.")
            doDialogText("You feel a crushing weight against your body.")
            doDialogText("YOU:# MAN GET OFF OF ME!")
            doDialogText("WAYDANT:# Oh sorry.")
            print()
            doDialogText("Well,# you're back in the real world.")
            if pgFilter: doDialogText("YOU:# What the fuck was that.#.#.#")
            else: doDialogText("YOU:# What the heck was that.#.#.#")
            doDialogText("WAYDANT:# That was a crazy adventure.#.#.#")
            doDialogText("         What even happened in there?")
            doDialogText("YOU:# I have no clue...")
            doDialogText("     Oh yeah,# I remember now.# I dropped the knife.")
            doDialogText("WAYDANT:# I think I almost died in there.#.#.#")
            doDialogText("         Can't believe I was tricked like that.")
            doDialogText("YOU:# ...WAYDANT,# is that a chess piece stuck on your finger?")
            doDialogText("WAYDANT:# Oh yeah,# it's the queen.")
            doDialogText("WAYDANT takes the queen out of his finger.")
            doDialogText("YOU:# How'd it even fit on your finger?")
            doDialogText("WAYDANT:# I don't know,# it hurts...")
            doDialogText("         Oh yeah.#.#.# I'm sorry.")
            doDialogText("         I got tricked,# and tried to stop us from leaving the...# the \"dark world\".")
            if pgFilter: doDialogText("YOU:# It's okay,# shit happens sometimes.")
            else: doDialogText("YOU:# It's okay,# stuff happens.")
            print()
            doDialogText("You notice a torn flower on your bed.")
            doDialogText("YOU:# Flowery.#.#.#")
            doDialogText("WAYDANT:# Who's flowery?")
            doDialogText("YOU:# This lil fella.# It was a name my mom gave to this flower.")
            doDialogText("WAYDANT:# Oh.#.#.#")
            doDialogText("YOU:# I need to get tape.")
            doDialogText("WAYDANT:# Can tape fix it?")
            doDialogText("YOU:# I don't know,# but I gotta try.#.#.#")
            doDialogText("     ...or my mom's gonna be sad.")
            print()
            doDialogText("Suddenly,# you both lock eyes on a 500 rupee note on the bed.")
            doDialogText("YOU:# .#.#.#")
            doDialogText("WAYDANT:# .#.#.#")
            doDialogText("         DIBS!")
            doDialogText("WAYDANT grabs the 500 rupee note.")
            doDialogText("YOU:# HEY,# THAT'S MINE!")
            doDialogText("WAYDANT:# I CALLED IT FIRST,# IT'S MINE NOW!")
            doDialogText("YOU:# Buddy,# don't you dare mess with me right now.")
            doDialogText("WAYDANT:# Okay chill,# I was just kidding.")
            doDialogText("WAYDANT hands the money back.")
            doDialogText("WAYDANT:# I think I should leave now.# It's pretty late.")
            doDialogText("YOU:# Yeah,# get out of my room already.")
            doDialogText("     Actually,# why'd you even come to my house in the first place?")
            doDialogText("WAYDANT:# Oh,# to give you the knife.# And to also warn you about ADITHYA.# He's getting suspicious.")
            doDialogText("YOU:# Okay,# but why the knife?")
            doDialogText("WAYDANT:# ...i thought you dropped it.", spd=5)
            doDialogText("YOU:# Dropped it?")
            doDialogText("WAYDANT:# Yeah.# I wasn't sure if it was yours,# so I kept it temporarily.")
            doDialogText("         But then I remembered later that I had to give it back,# so that's why i came in the middle of the night.")
            doDialogText("YOU:# Bro,# I don't carry a knife around.# Who does anyways?")
            doDialogText("WAYDANT:# ...#you're right.", spd=5)
            if pgFilter: doDialogText("YOU:# Dumbass...")
            else: doDialogText("YOU:# Moron...")
            doDialogText("     now get out of my house already!")
            doDialogText("WAYDANT:# Yeah yeah,# I'll be on my way.")
            doDialogText("         See ya.")
            doDialogText("YOU:# See you too...# I guess.")
            doDialogText("WAYDANT leaves.")
            doDialogText("You focus on taping back the snapped flower.")
            doDialogText("After careful craftsmanship,# you can breathe in relief that the flower can live to bloom another day.")
            doDialogText("You head back to lock your front door,# and place \"FLOWERY\" in his respective place.")
            doDialogText("YOU:# Get well soon.")
            print()
            doDialogText("You head back to your room and plop down on your bed.")
            doDialogText("Before you can fall asleep,# you notice some messages coming from the group chat:")

            doCreditsSequence(soundImportSuccesful)



                



            
            finalSave = True
        
    


    # THE SAVE SHENANIGANS
    if finalSave:
        if saveFile['route4']['COMPLETED'] == True:
            doDialogText("You have already completed this chapter.# Would you like to save over your progress? (Y/N):", line=False)
            confirm = input("")

            if confirm.lower() in "n":
                doDialogText("The Game was not Saved.")
            else:
                route4["COMPLETED"] = True
    
                saveFile["route4"] = route4

                try:
                    saveGame(curSaveName, saveFile)
                    doDialogText("The game was saved.")
                except:
                    doDialogText("There was an error in saving the game.")
        else:
            route4["COMPLETED"] = True

            saveFile["route4"] = route4

            try:
                saveGame(curSaveName, saveFile)
                doDialogText("The game was saved.")
            except:
                doDialogText("There was an error in saving the game.")


def start(funcs):
    
    funcs['doDialogText']("Loading Chapter 4.#.#.#", afterdelay=3)
    print()
    chapter_4(funcs)