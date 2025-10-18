def chapter_4(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful):
    route4 = {
        "DEATHS": 0,

        "on_weirdRoute": False,
        "battle_firstChoice": 0,
        "battle_noHit": True,
        "helped_annie": 0,
        "helped_everyone": 0,
        "played_conjuring": False,
        "peak_horseRiding": 0,
        "wordle": 0,
        "rajith_noHit": True,

        "guard_spared": 0 
    }
    
    doDialogText("CHAPTER 4:##  Light and Dark..", spd = 25, step = 3)
    print()

    nameChoice = saveFile['route1']['name_choice']


    """
    PLANS FOR CHAPTER 4:
    Basically we take a dive into a videogame: DELTARUNE.
    To avoid copyright, ima switch up the name
    DELTA -> CHANGE IN -> CHANGING
    RUNE -> RUNES

    therefore, CHANGING RUNES

    If you took the normal route, ASHISH's older sister SEPT (SEPTEMBER R NAIR instead of DECEMBER HOLIDAY [or december r nair]) spawns a dark fountain in ASHISH's bedroom.
    According to her reasoning, watching the slow pace of these two getting together was so painful to watch, that
    she put us on an adventure to help us get close quicker.
    This is a jab at how I suck at planning progression for the two fellas, and how i got a brainstorming idea

    If you're on the NORMAL or LUNATIC route, you have no choice but to accept the sleepover. You can also get into the dark world by
    being on the RUDE route and accepting the sleepover invitation.
    Then once the dark fountain is created, you and Ashish are together, and a mysterious figure emerges, claiming to be a darkner.
    This is actually Ashish's SISTER in disguise, helping you through the dark world and placing you two in romantic situations.
    commence the MAPPING:
    1) SNOWY DESERTED AREA:
        This is where you spawn, alongside ASHISH. This area is meant to be the bedroom. The snow is fluffy,# and you can do nothing else other
        than advance from the area, while encountering some creepy things.
    2) LIBRARY WORLD:
        This area is meant to represent ASHISH's multiple study guides.

    NOTE TO SELF: WAYDANT IS AWARE OF ADITHYA'S PLAN AND SNEAKS INTO ADITHYA'S GROUP AS A SPY.
    If you're on the RUDE route and went back home by yourself, WAYDANT follows you home, concerned after finding you beat up.
    then WAYDANT spawns a dark fountain in your house, and you go through a different, rough experience where you're initially seperated from
    Waydant at the beginning of the fountain world, and when you reach the end of the fountain to try and seal the fountain,
    you find Waydant on the opposite team. The darkners have convinced him that he needs to PROTECT the dark fountain, and you face off against
    Waydant as a boss.
    You then beat Waydant, maybe apologize for downing him, and seal the fountain.
    Then Waydant realizes that he was wrong and apologizes for trying to do the wrong thing and protecting the fountain.
    Then the chapter ends as Waydant heads back home and you patch yourself up.
    """
    
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
        damage = math.ceil(max(1-fResult, 0.45)*enemyATK/targetStruct["defense"])
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

            playSong("OST/credits_intro.wav")

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
            playSong("OST/battle.wav", looping=True)
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
            playSong("OST/lokahbanger.wav")
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
        "spells": "PHOTOSYNTHESIS",
        "weapon": "VINE WHIP",
        "armor": "SAND BAG"
    }
    

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
                
                fResult = doTimedQuestion(question, 41, 5, 10)
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
            doDialogText("(It's awkward.)")
            doDialogText("(It's HELLA awkward.)")
            doDialogText(f"ASHISH:# (It's strange,# and awkward as well.#.#.## Having {saveFile['name']} next to me.#.#.#)")
            doDialogText("YOU AND ASHISH:# (In the same room.#.#.#)", afterdelay=2)
        
        # GAMING MOMENT
        doDialogText("You spot a faint flicker tucked beneath one of the beds.")
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

        if route4['on_weirdRoute']:
            doDialogText("You woke up in the middle of the night.# It's 4:11 AM.")
            doDialogText("The computer screen is flickering.")
            doDialogText("Ashish is asleep.")

            play = doDialogChoice("Play the game?", choices=["Play it.", "Go back to sleep."])

            if play == 2:
                doDialogText("You decide to go back to sleep.")
                route4['on_weirdRoute']
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
                doDialogText("CLOSE YOUR EYES,# CONJURER.", afterdelay=2)
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
        doDialogText("Before you get ready to lose conciousness,# you get some notifications from the group chat:")

        doCreditsSequence(soundImportSuccesful)


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
                    player['lv'] = 2
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
                    doDialogText(f"{targetName} lost {dmg} HP! ({targetStruct['hp']}/{getMaxHP(targetN)})")
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
                    doDialogText(f"{targetName} lost {dmg} HP! ({targetStruct['hp']}/{getMaxHP(targetN)})")
            elif attackN == 2:
                doDialogText("The guards pull out GUNS?!# GET READY TO DODGE THE GUNFIRE!")
                fResult = doTimedSpam(30)
                if 0.7 <= fResult <= 1:
                    doDialogText("Somehow,# you dodged the bullets.")
                else:
                    dmg = getDamageDealt(guardsATK, targetStruct, fResult)
                    targetStruct['hp'] -= dmg
                    doDialogText(f"{targetName} got caught in the gunfire!")
                    doDialogText(f"{targetName} lost {dmg} HP! ({targetStruct['hp']}/{getMaxHP(targetN)})")
            
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
        doDialogText("It's silent.")

    # THE SAVE SHENANIGANS
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


def start(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful):
    doDialogText("Loading Chapter 4.#.#.#", afterdelay=3)
    print()
    chapter_4(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful)