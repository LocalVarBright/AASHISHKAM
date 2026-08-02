import time
import io
import os
import sys
import importlib.util
import urllib.request
import subprocess
import json
import zipfile
import traceback
import copy
 
# GAME SPEED
global timeControl
global specialFeature
specialFeature = False
timeControl = 1
 
# ENGINE DATA
"""
DEVLOG:

2.2 - CHAPTER 5 RELEASE
    - Updated the name ADVIL to AWAITH in chapter 4 to match with chapter 5
    - Fixed Chapter 3's route checking to not miss a route change in chapter 3
    - Removed the WARNING for when version of save file does not match with version of AASHISHKAM. It has been deemed useless.
    - Ensured dialog consistency in chapter 1 between rude name choice and normal name choice.
    - Changed the way 'pygame' and 'keyboard' modules are imported. (the correct way, I think.)
2.1 - Fixed a bug where declining to load a save file would... reset the save file to default.
2.0 - Released Chapter 4 completely.
    - Added mods, which are basically their own chapters.
    - Added the ability to load custom modules into chapters.

(2.0 BETA 19 - Added functions 'loadModule()' and 'getFilePath()' to modArgs (mod and chapter files).)
(2.0 BETA 18 - Chapters are redownloaded every time you open Aashishkam.)
(2.0 BETA 17 - Stopped any music playing when a mod/chapter finishes unexpectedly crashes.)
(2.0 BETA 16 - Added a fake chapter 5.)
(2.0 BETA 15 - Fixed a soundtrack menu mistake and fixed an error in the saving system (probably))
(2.0 BETA 14 - Fixed some game breaking bugs, mainly because of downloading the soundtrack. Also, pausing music actually works now.)
(2.0 BETA 13 - Recoded the entire program to now work around a launcher-update system.
               You no longer need to redownload Aashishkam every time for a new update,
               just run the aashishkam launcher file and everything should arrange itself.
               Also updated the first three chapters. Now they have their own songs!)


1.8 - School Computer compatibility
1.7 - Added sound support for both pygame and winsound.
1.6 - Changed the game to use pygame for AUDIO.
1.5 - CHAPTER 4 RELEASE, with PG Filter now and more features.
1.4 - Fixed a bug with saving issues at the end of chapters.
1.3 - CHAPTER 3 RELEASE.
1.2 - CHAPTER 2 RELEASE, probable dialog bugs.
1.1 - Fixed buggy save feature.
1.0 - CHAPTER 1 RELEASE, save feature prototype.
"""
global version
version = "2.2"
 
def getVersion():
    global version
    return version
# BASE GAME FUNCTIONS
def doDialogText(text, spd = 4, afterdelay = 0.7, step = 1, line = True, indep = False):# PRINTS TEXT LETTER BY LETTER
 
    if not indep:
        spd *= timeControl
        afterdelay *= timeControl
 
 
    initStep = 0
    foundChar = False
    for lel in range(len(text)):
        char = text[lel]

        if char == ' ' and not foundChar:
            print(char, end='')
            continue
        elif char != ' ' and not foundChar:
            foundChar = True
        
        initStep += 1
 
        if char == "#": # Filter out the unwanted characters first
            time.sleep(spd*5/100)
            continue
        elif char == "^":
            print()
            continue
        elif initStep < step: # Then do the mettaton thing
            print(char, end="")
            continue
        elif initStep >= step: # 'step' number of characters has been waited, now its time to wait
            print(char, end="")
            initStep = 0
            time.sleep(spd/100)
    time.sleep(afterdelay) # Wait for the afterdelay
 
    if line: print()
 
def doDialogSlow(text, spd = 1, afterdelay = 0.7, step = 1, line = True, add=1.1):# PRINTS TEXT LETTER BY LETTER WHILE DECREASING TEXT SPEED
 
    spd *= timeControl
    afterdelay *= timeControl
 
 
    initStep = 0
    for char in text:
        initStep += 1
 
        if char == "#": # Filter out the unwanted characters first
            time.sleep(spd*5/100)
            continue
        elif initStep < step: # Then do the mettaton thing
            print(char, end="")
            continue
        elif initStep >= step: # 'step' number of characters has been waited, now its time to wait
            print(char, end="")
            initStep = 0
            time.sleep(spd/100)
            spd *= add
    time.sleep(afterdelay) # Wait for the afterdelay
 
    if line: print()
 
def askChoice(choices): # DETERMINES THE OPTION CHOSEN BY THE USER. USED IN THE 'doDialogChoice()' FUNCTION.
    choice = input("")
 
    try:
        choice = int(choice)
 
        if choice > len(choices) or choice <= 0: # Invalid Choice
            choice = askChoice(choices)
        return(choice)
    except:
        return askChoice(choices)
 
def askNum(): # ACCEPTS A NUMBER FROM THE USER WITHOUT ANY ERRORS.
    imp = input("")
 
    choice = ""
    for i in imp:
        if i in "1234567890":
            choice += i
 
    try:
        choice = int(choice)
        return(choice)
    except:
        return askNum()
 
def doDialogChoice(text, spd = 3, afterdelay = 0.7, step = 1, choices = ['Yes', 'No']): # ASKS THE USER TO MAKE A CHOICE
    doDialogText(text, spd, afterdelay, step)
 
    for i in range(len(choices)):
        doDialogText(f'{i+1}) {choices[i]}', spd, afterdelay*0.3, step)
 
    choice = askChoice(choices)
 
    return choice
 
def doTimedQuestion(text, answer, error): # ASKS THE USER A QUESTION, AND DETERMINES ACCURACY BASED ON TIME TAKEN AND ANSWER GIVEN.
    doDialogText(text, spd=3.6, step=3, afterdelay=0)

    inp = askNum()
 
    if error <= 0: error = 1
 
    accuracy = 1 - abs(answer-inp/(error))
    if accuracy > 1: accuracy = 1
    elif accuracy < 0: accuracy = 0.0

    return round(accuracy, 1)
 
def doTimedAttack(countdown=3, combo=1, countspeed=1): # COUNTDOWN is how many seconds to count down. combo is how many times to hit enter.
    for count in range(countdown):
        print("SPAM ENTER KEY", combo, "TIMES IN:", countdown - count, "SECONDS.")
        if count != 2:
            time.sleep(timeControl/countspeed)
        else:
            time.sleep(timeControl*0.85/countspeed)
 
    spammed = 0
    combos = [time.time()] # STARTING TIME
    for i in range(combo+5):
        if i in range(combo):
            input(f"HIT ENTER ONLY {str(combo)} TIMES!!! THEN WAIT 0.3 SECONDS")
            combos.append(time.time()) # TIME AT FIRST ENTER HIT, SECOND HIT, ETC.
 
    times = [] # A List of the time taken between each hit
    for tm in range(combo):
        times.append((combos[tm+1] - combos[tm]) / (1/1))
 
    avgAccuracy = sum(times)/len(times) * (6)
 
    finalFinalValue = round(1/avgAccuracy, 2)
    if finalFinalValue > 1: finalFinalValue = 1
 
    if spammed > 0: finalFinalValue *= 0.3
    return finalFinalValue
 
def doTimedSpam(combo=10): # COMBO is how many times you spam.
    combos = [] # STARTING TIME
    spammed = 0
 
    for i in range(combo+25):
        if i in range(combo):
            input(f"HIT ENTER {str(combo-i)} MORE TIMES!!")
            combos.append(time.time()) # TIME AT FIRST ENTER HIT, SECOND HIT, ETC.
        else:
            input("DON'T HIT ENTER! WAIT 0.3 SECONDS")
            combos.append(time.time())
            if combos[i] - combos[i-1] < 0.3:
                print("POTENTIAL SPAMMING DETECTED!!!")
                spammed += 1
            break
 
    times = [] # A List of the time taken between each hit
    for tm in range(combo-1):
        times.append((combos[tm+1] - combos[tm]) / (1/1))
 
    avgAccuracy = sum(times)/len(times) * (10)
 
    finalFinalValue = round(1/avgAccuracy, 2)
    if finalFinalValue > 1: finalFinalValue = 1
 
    if spammed > 0: finalFinalValue *= 0.2
    return finalFinalValue
 
def printGraphic(graphic, spd= 2, step=50, afterdelay=1.5):
 
    i = 0
    while i < len(graphic):
        chunk = graphic[i:i+step]
 
        print(chunk, end="")
 
        time.sleep(spd/100)
        i += step
    time.sleep(afterdelay*timeControl)
 
def getPrompt(text, spd = 2, step=2, leanTrue = True):
    doDialogText(text+" (Y/N): ", spd=spd, step=step, line=False, afterdelay=0)
    ans = input("")
 
    if not leanTrue:
        return ans in "YESYesyes"
    else:
        return not ans in "NOTNotnot"


# TIME CONTROLS

def setTime(timen):
    global timeControl
    timeControl = timen

# PATH FUNCTIONS
 
def getEngineDir():
    base = ""
    if sys.platform == "win32":
        base = os.getenv("APPDATA")
    elif sys.platform == "darwin":  # macOS
        base = os.path.expanduser("~/Library/Application Support")
    else:  # Linux and others
        base = os.path.expanduser("~/.local/share")
 
    folder = os.path.join(base, "AASHISHKAM")
    os.makedirs(folder, exist_ok=True)
    return folder
 
def checkFile(dirName):
    return os.path.exists(os.path.join(getEngineDir(), dirName))
 
def getFilePath(path, makeSure = False):
    if makeSure:
        os.makedirs(os.path.join(getEngineDir(), path), exist_ok=True)
    return os.path.join(getEngineDir(), path)
 
def openFolder(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
 
    if sys.platform == "win32":
        subprocess.Popen(f'explorer "{path}"')
    elif sys.platform == "darwin":  # macOS
        subprocess.Popen(["open", path])
    else:  # Linux / others
        subprocess.Popen(["xdg-open", path])
 
def downloadStuff(force=False):
 
    os.makedirs(getFilePath("chapters"), exist_ok=True)
    os.makedirs(getFilePath("assets/soundtrack"), exist_ok=True)
 
    downloadList = [
        "chapters/chapter1.py",
        "chapters/chapter2.py",
        "chapters/chapter3.py",
        "chapters/chapter4.py",
        "chapters/chapter5.py",
 
        "assets/soundtrack/darkfight.ogg",
        "assets/soundtrack/videogame.ogg",
        "assets/soundtrack/lokahbanger.ogg",
        "assets/soundtrack/light_and_dark.ogg",
        "assets/soundtrack/bach.mp3",
        "assets/soundtrack/first_meet.ogg",
        "assets/soundtrack/second_meet.ogg",
        "assets/soundtrack/espada.mp3",
        "assets/soundtrack/versus.ogg",
        "assets/soundtrack/vs_adithya.ogg",
        "assets/soundtrack/vs_tejas.ogg"
    ]
 
    downloadUrls = {
        "chapters/chapter1.py":                   "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/chapters/chapter1.py",
        "chapters/chapter2.py":                   "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/chapters/chapter2.py",
        "chapters/chapter3.py":                   "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/chapters/chapter3.py",
        "chapters/chapter4.py":                   "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/chapters/chapter4.py",
        "chapters/chapter5.py":                   "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/chapters/chapter5.py",
 
        "lib/fightplayer/__display.py":           "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/lib/fightplayer/__display.py",
        "lib/fightplayer/__matrix.py":            "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/lib/fightplayer/__matrix.py",
        "lib/fightplayer/mechfight.py":           "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/lib/fightplayer/mechfight.py",
        "lib/fightplayer/setup.py":               "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/lib/fightplayer/setup.py",
    
        "assets/soundtrack/darkfight.ogg":        "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/darkfight.ogg",
        "assets/soundtrack/videogame.ogg":        "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/videogame.ogg",
        "assets/soundtrack/lokahbanger.ogg":      "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/lokahbanger.ogg",
        "assets/soundtrack/light_and_dark.ogg":   "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/light_and_dark.ogg",
        "assets/soundtrack/bach.mp3":             "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/bach.mp3",
        "assets/soundtrack/first_meet.ogg":       "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/first_meet.ogg",
        "assets/soundtrack/second_meet.ogg":      "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/second_meet.ogg",
        "assets/soundtrack/espada.mp3":           "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/espada.mp3",
        "assets/soundtrack/versus.ogg":           "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/versus.ogg",
        "assets/soundtrack/vs_adithya.ogg":       "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/vs_adithya.ogg",
        "assets/soundtrack/vs_tejas.ogg":         "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/vs_tejas.ogg",
        "assets/soundtrack/tv_show_1.ogg":        "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/tv_show_1.ogg",
        "assets/soundtrack/tv_show_2_loop.ogg":   "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/tv_show_2_loop.ogg",
        "assets/soundtrack/tv_show_2_end.ogg":    "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/tv_show_2_end.ogg",
        "assets/soundtrack/tv_show_3.ogg":        "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/tv_show_3.ogg",
        "assets/soundtrack/tv_show_full.ogg":     "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/tv_show_full.ogg",
        "assets/soundtrack/magic.ogg":            "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/magic.ogg",
        "assets/soundtrack/guards.ogg":           "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/guards.ogg",
        "assets/soundtrack/mechfight_intro.ogg":  "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/mechfight_intro.ogg",
        "assets/soundtrack/mechfight.ogg":        "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/mechfight.ogg",
        "assets/soundtrack/mechfight_full.ogg":   "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/mechfight_full.ogg",
        "assets/soundtrack/enraged.ogg":          "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/enraged.ogg",
        "assets/soundtrack/castle_walls.ogg":     "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/castle_walls.ogg",
        "assets/soundtrack/guardian.ogg":         "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/guardian.ogg",

        "assets/soundtrack/classroom.ogg":        "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/classroom.ogg",
        "assets/soundtrack/doubted.ogg":          "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/doubted.ogg",
        "assets/soundtrack/third_meet.ogg":       "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/third_meet.ogg",
        "assets/soundtrack/cake_lie.ogg":         "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/cake_lie.ogg",
        "assets/soundtrack/projection_full.ogg":  "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/projection_full.ogg",
        "assets/soundtrack/projection.ogg":       "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/projection.ogg",
        "assets/soundtrack/results.ogg":          "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/results.ogg",
        "assets/soundtrack/musicroom.ogg":        "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/musicroom.ogg",
        "assets/soundtrack/shepherd.ogg":         "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/shepherd.ogg"
        
    }
 
    count = 1
    maxcount = len(downloadUrls)
    canDownload = True
    for item in downloadUrls:
        if (not checkFile(item) or force) or item.startswith("chapters/chapter"): # Actually download the item (if its already downloaded,# then the else statement is executed).
            print(f"Downloading ({count}/{maxcount})")
            try:
                if canDownload:
                    dest_path = getFilePath(item)
                    try:
                        dest_dir = os.path.dirname(dest_path)
                        if dest_dir:
                            os.makedirs(dest_dir, exist_ok=True)
                    except Exception:
                        pass
                    urllib.request.urlretrieve(downloadUrls[item], dest_path)
            except:
                print(f"Unable to download. ({count}/{maxcount}).")
                #canDownload = False
        else:
            print(f"Already downloaded. ({count}/{maxcount})")
 
        count += 1
 
# SOUND FUNCTIONS
 
global soundImportSuccesful
soundImportSuccesful = False
 
def getSoundes():
    importSound = getPrompt("Would you like to enable AUDIO? (will attempt to install pygame)")
    if importSound:
        try: # In case pygame is already present, try to access it
            lib_path = os.path.join(getEngineDir(), "lib")
            if lib_path not in sys.path:
                sys.path.insert(0, lib_path)

            
            import pygame
            pygame.mixer.init()
            globals()['pygame'] = pygame
            global soundImportSuccesful
            soundImportSuccesful = True
            doDialogText("Pygame was found,# AUDIO has been enabled.")
        except:
            print("Pygame wasn't detected.")
            installPygame = getPrompt("Try to install pygame?")
 
            if installPygame:
 
 
                zipf = urllib.request.urlopen("https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/zips/pygame.zip")
                zipd = io.BytesIO(zipf.read())
 
                with zipfile.ZipFile(zipd) as zip_ref:
                    zip_ref.extractall(getFilePath("lib", makeSure=True))
 
    else:
        doDialogText("AUDIO has been disabled.")
    
def getKeyboades():
    keyboardEnabled = getPrompt("Would you like to enable KEYBOARD INPUT? (will attempt to install 'keyboard' library)")
    if keyboardEnabled:
        try: # In case pygame is already present, try to access it
            lib_path = os.path.join(getEngineDir(), "lib")
            if lib_path not in sys.path:
                sys.path.insert(0, lib_path)

            import keyboard
            globals()['keyboard'] = keyboard
            global keyboardImportSuccesful
            keyboardImportSuccesful = True
            doDialogText("KEYBOARD INPUT has been enabled.")
        except:
            print("'keyboard' library wasn't detected.")
            installKeyboard = getPrompt("Try to install 'keyboard'?")
 
            if installKeyboard:
                zipf = urllib.request.urlopen("https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/zips/keyboard.zip")
                zipd = io.BytesIO(zipf.read())
 
                with zipfile.ZipFile(zipd) as zip_ref:
                    zip_ref.extractall(getFilePath("lib", makeSure=True))

# SOUND FUNCTIONS

def playSong(name, interruptable=False, looping=False):
    if soundImportSuccesful:
        songPath = getFilePath(name)
    
        # Load the music file
        pygame.mixer.music.load(songPath)
    
        # Play the song (loop = -1 for infinite, 0 for play once)
        if looping:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()
    
        # If interruptable, wait for input before stopping
        if interruptable:
            input("Press ENTER to stop playing.")
            pygame.mixer.music.stop()
 
def stopSong():
    if soundImportSuccesful:
        pygame.mixer.music.stop()

def pauseSong():
    if soundImportSuccesful:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

def playSound(name, looping=False):
    if soundImportSuccesful:
        soundPath = getFilePath(name)
        sound = pygame.mixer.Sound(soundPath)
        
        if looping:
            sound.play(-1)
        else:
            sound.play()
        
        return sound

# KEYBOARD FUNCTIONS

def keyHeld(key):
    if keyboardImportSuccesful:
        return keyboard.is_pressed(key)
    return False

def keyPressed(key):
    if keyboardImportSuccesful:
        return keyboard.on_press_key(key)
    return False

# MOD LOADING FUNCTIONS
 
global listOfMods # LIST OF ALL THE MODS
global listOfModFolders # DICTIONARY OF ALL THE MOD FOLDERS
 
listOfMods = []
listOfModFolders = []
 
def checkMods():
    global listOfModFolders
    listOfModFolders = []
    # Ensure the mods folder exists
    modsPath = os.path.join(getEngineDir(), "mods")
    os.makedirs(modsPath, exist_ok=True)
 
    for folder in os.listdir(modsPath): # Goes through each folder in the mod folder
        modFolder = os.path.join(modsPath, folder) # AppData/AASHISHKAM/mods/modName
 
        print("Checking for mods...")
 
        if os.path.isdir(modFolder):
            modPath = os.path.join(modFolder, "mod.py") # AppData/AASHISHKAM/mods/modName/mod.py
            if os.path.exists(modPath):
 
 
                listOfModFolders.append((modFolder)) # Adds the Folder Path of the Mod at the same time
 
                #print(f"Mod found at {os.path.basename(modFolder)}")
            else:
                print(f"No mod.py found in {folder}.")
        else:
            print(f"{folder} is not a directory.")
 
def checkChapters():
    # Ensure the chapters folder exists
    chaptersPath = os.path.join(getEngineDir(), "chapters")
    os.makedirs(chaptersPath, exist_ok=True)
    for file in os.listdir(chaptersPath): # Goes through each file in the chapters folder
        chapterFile = os.path.join(chaptersPath, file) # AppData/AASHISHKAM/chapters/chapter1.py
 
        print("Checking for chapters...")
 
        if os.path.isfile(chapterFile) and chapterFile.endswith(".py"):
            global listOfChapters
            listOfMods.append((chapterFile)) # Adds the File Path of the Chapter at the same time
 
                #print(f"Chapter found at {os.path.basename(chapterFile)}")
 
def loadModTest():
    global listOfModFolders
 
    if listOfModFolders != []: # atleast one mod is found
        modIndex = 0
        listOfModNames = []
        for modName in listOfModFolders: # 'modName' comes as a path file, so it should be reduced to the name of the folder
            modName = os.path.basename(modName) # 'modName' gets reduced to the name of the folder
            listOfModNames.append(modName) # Adds the name of the mod to the list of mods
        modIndex = doDialogChoice("SELECT A MOD:", choices=listOfModNames + ["Return"]) - 1
        if listOfModNames[modIndex] != "Return":
            spec = importlib.util.spec_from_file_location("mod", os.path.join(listOfModFolders[modIndex], "mod.py")) # The spec of the module for the mod
            modToLoad = importlib.util.module_from_spec(spec) # The module for the mod
            spec.loader.exec_module(modToLoad)
            if hasattr(modToLoad, "start"):
                funcs = (doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, timeControl)
                modToLoad.start(*funcs)
            else:
                doDialogText("This mod is missing the start function.")
        startEngine(False)
    else:
        doDialogText("No mods found.# Install mods inside the mods folder?", line=False)
        if getPrompt("", leanTrue=False):
            openFolder(os.path.join(getEngineDir(), "mods"))
            doDialogText("Opening mod folder.#.#.#")
 
        startEngine(False)
 
def listMods():
    if listOfModFolders != []: # atleast one mod is found
        modIndex = 0
        listOfModNames = []
        for modName in listOfModFolders: # 'modName' comes as a path file, so it should be reduced to the name of the folder
            modName = os.path.basename(modName) # 'modName' gets reduced to the name of the folder
            listOfModNames.append(modName) # Adds the name of the mod to the list of mods
        if listOfModNames[modIndex] != "Return":
            spec = importlib.util.spec_from_file_location("mod", os.path.join(listOfModFolders[modIndex], "mod.py")) # The spec of the module for the mod
            modToLoad = importlib.util.module_from_spec(spec) # The module for the mod
            spec.loader.exec_module(modToLoad)
            if hasattr(modToLoad, "start"):
                funcs = (doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, timeControl)
                modToLoad.start(*funcs)
            else:
                doDialogText("This mod is missing the start function.")
        startEngine(False)
    else:
        doDialogText("No mods found.# Install mods inside the mods folder?", line=False)
        if getPrompt("", leanTrue=False):
            openFolder(os.path.join(getEngineDir(), "mods"))
            doDialogText("Opening mod folder.#.#.#")
 
# SAVE FUNCTIONS
saveFile = {
    "version": version,
 
    "name" : "DefulatName",
    "achievements": {},
 
    "route1": {
        "COMPLETED": False
        },
    "route2": {
        "COMPLETED": False
        },
    "route3": {
        "COMPLETED": False
        },
    "route4": {
        "COMPLETED": False
    },
    "route5": {
        "COMPLETED": False
    },
    "route6": {
        "COMPLETED": False
    },
    "route7": {
        "COMPLETED": False
    },
    
    }
 
def saveExists(saveName):
    if os.path.exists(os.path.join(getFilePath("saves"), saveName+".json")):
        return True
    else: return False
 
def saveGame(saveName, saveFile):
    os.makedirs(getFilePath("saves"), exist_ok=True)
 
    with open(os.path.join(getFilePath("saves"), saveName+".json"), "w") as file:
        json.dump(saveFile, file, indent=4)
 
def loadGame(saveName):
    if saveExists(saveName):
        confirmLoad = getPrompt(f"Save \"{saveName}.json\" found. Confirm load?")
        if confirmLoad:
            with open(os.path.join(getFilePath("saves"), f"{saveName}.json"), "r") as file:
                dumpFile = json.load(file)

                # I made a mistake with the chapter 3 rude_stay thing. lemme fix
                if 'rude_stay' in dumpFile['route3'] and dumpFile['route3']['rude_stay'] == 0:
                    dumpFile['route3']['rude_stay'] = "FORGIVED"

                # Sometimes save.json only has the string "ERROR", which messes with the loading system.
                if dumpFile == "ERROR": return "ERROR"
 
                # REGENERATION OF THE SAVE FILE:
                # If the save file has missing fields, automatically add them with default values.
 
                # If version doesn't exist, add it manually
                try:
                    if dumpFile['version']:
                        pass
                except:
                    dumpFile['version'] = version
                    doDialogText(f"Field 'version' wasn't detected on this save file,# so version has been added manually. (v{version})", spd=2)
 
                # If achievements doesn't exist, add them manually
                try:
                    if dumpFile['achievements']:
                        pass
                except:
                    dumpFile['achievements'] = []
                    doDialogText("Field 'achievements' wasn't detected on this save file,# so achievements has been added manually.", spd=2)
 
                # If the chapter files don't exist, add them manually
                for rr in range(1, 8):
                    routeName = "route" + str(rr)
 
                    try: # Checks if the route save exists
                        if dumpFile[routeName]:
                            try: # Checks if the COMPLETED field in the route struct exists
                                if dumpFile[routeName]['COMPLETED'] == True or dumpFile[routeName]['COMPLETED'] == False:
                                    pass
                            except:
                                dumpFile[routeName]['COMPLETED'] = False
                    except:
                        dumpFile[routeName] = {"COMPLETED": False}
                        doDialogText(f"Field '{routeName}' wasn't detected on this save file,# so {routeName} has been added manually.", spd=2)
 
 
                if dumpFile["version"] != version:
                    # REMOVED this warning, it's basically useless.
                    #doDialogText(f"WARNING:# This version of the save file ({dumpFile['version']}) does not match the version of this engine ({version}).")
                    dumpCorrupt = getPrompt("Continue Loading?")
                    if dumpCorrupt:
                        dumpFile["version"] = version
 
                        return dumpFile
                    else:
                        doDialogText("The save was not loaded.")
                        return "ERROR"
 
                else: return dumpFile
        else:
            doDialogText("The save was not loaded.")
            return "ERROR"
    else: # CREATE NEW SAVE FILE
        createSave = getPrompt(f"This save file ({saveName}.json) does not exist. Would you like to create a new one?")
        if createSave:
            saveGame(saveName, saveFile)
            return saveFile
        else:
            doDialogText("The save was not created.")
            return "ERROR"

def getAchievementName(achID, saveFile):
    # CHAPTER 1
    if achID == "ach_spotify":
        return saveFile['achievements'][0]['ach_spotify']
    
    # CHAPTER 2
    elif achID == 'ach_study':
        return "Cross Productive"
    elif achID == 'ach_cake':
        return saveFile['achievements'][1]['ach_cake']
    elif achID == 'ach_roomClean':
        return "Organized"
    elif achID == 'ach_shower':
        return saveFile['achievements'][1]['ach_shower']
    elif achID == 'ach_badminton':
        return "Team Player"
    elif achID == 'ach_debayan':
        return "Be The Bigger Man"

    # CHAPTER 3
    elif achID == 'ach_fight':
        return saveFile['achievements'][2]['ach_fight']

def evaluateSaveAchievements(oldFile):
    saveFileNew = copy.deepcopy(oldFile)

    chapter1 = {'visited': False}
    chapter2 = {'visited': False}
    chapter3 = {'visited': False}
    #chapter4 = {'visited': False}

    saveFileNew['achievements'] = []

    # CHAPTER 1 ACHIEVEMENTS
    if saveFileNew['route1']['COMPLETED'] == True:
        chapter1['ach_spotify'] = "Aashishkam"
        if saveFileNew['route1']['name_choice'] == "NORMAL": chapter1['ach_spotify'] = "Aashishkam"
        elif saveFileNew['route1']['name_choice'] == "LUNATIC": chapter1['ach_spotify'] = "Smooth Criminal"
        elif saveFileNew['route1']['name_choice'] == "RUDE": 
            if saveFileNew['route1']['rude_choice'] == "APOLOGIZED":
                chapter1['ach_spotify'] = "Ashakiran"
            else:
                chapter1['ach_spotify'] = "Billie Jean"
    
        saveFileNew['achievements'].append(chapter1)

    # CHAPTER 2 ACHIEVEMENTS
    if saveFileNew['route2']['COMPLETED'] == True:
        chapter2['ach_study'] = False
        if saveFileNew['route2']['house_studyChoice'] == "STUDYING": chapter2['ach_study'] = True

        chapter2['ach_cake'] = 0
        if saveFileNew['route2']['house_kitchenChoice'] == "DAD CAKE":
            chapter2["ach_cake"] = "Dad's Special Cake..."
        elif saveFileNew['route2']['house_kitchenChoice'] == "MOM CAKE":
            chapter2["ach_cake"] = "Mom's Dessert"
        elif saveFileNew['route2']['house_kitchenChoice'] == 0:
            chapter2["ach_cake"] = "Dodged a Bullet?"

        chapter2['ach_roomClean'] = False
        if saveFileNew['route2']['house_roomChoice'] == "CLEANED":
            chapter2['ach_roomClean'] = True

        chapter2['ach_shower'] = False
        if saveFileNew['route2']['house_bathChoice'] == "SHOWERED":
            chapter2['ach_shower'] = "Showered"
        elif saveFileNew['route2']['house_bathChoice'] == "NEAT FREAK":
            chapter2['ach_shower'] = "Neat Freak"
        elif saveFileNew['route2']['house_bathChoice'] == "NEAT MONSTER":
            chapter2['ach_shower'] = "Neatness Monster"

        chapter2['ach_badminton'] = False
        if saveFileNew['route2']['badminton_advice'] == "ADVICED":
            chapter2['ach_badminton'] = True

        chapter2['ach_debayan'] = False
        if saveFileNew['route2']['help_debayan'] == "HELPED":
            chapter2['ach_debayan'] = True

        saveFileNew['achievements'].append(chapter2)

    # CHAPTER 3 ACHIEVEMENTS
    if saveFileNew['route3']['COMPLETED'] == True:
        chapter3['ach_fight'] = False

        # 'fight_result' isn't present in previous save files, so enter a default one:
        if not hasattr(saveFileNew['route3'], 'fight_result'):
            saveFileNew['route3']['fight_result'] = 0

        if saveFileNew['route3']['fight_result'] == 0: chapter3['ach_fight'] = "Absolute Ass"
        if 0 < saveFileNew['route3']['fight_result'] < 6: chapter3['ach_fight'] = "Medium Attack"
        if saveFileNew['route3']['fight_result'] == 6: chapter3['ach_fight'] = "Tajikistan level Threat"

        saveFileNew['achievements'].append(chapter3)




    
    
    
    
    #saveFileNew['achievements'].append(chapter4)


    # CHECKING FOR NEW STUFF
    for i in range(4):
        if len(oldFile['achievements']) > i:
            if saveFileNew['achievements'][i] != oldFile['achievements'][i]:
                saveFileNew['achievements'][i]['visited'] = False
            else:
                saveFileNew['achievements'][i]['visited'] = True

    global saveFile
    saveFile = saveFileNew

curSaveName = "aashishSave"
 
def getSaveFile():
    doDialogText("SAVE NAME (Default Save will be called \"aashishSave\"): ", afterdelay=0.1, line=False)
    saveInput = input("")
 
    if saveInput != "":
        global curSaveName
        curSaveName = saveInput
 
    global saveFile
    saveFile = loadGame(curSaveName)

    if saveFile == "ERROR":
        getSaveFile()

    
 
 
global pgFilter
pgFilter = True
def getPgFilter():
    # PG FILTER
    global pgFilter
    pgFilter = not getPrompt("Would you like to enable the PG Filter?")
    """PG FILTER TRUE - Filter is disabled. 
    PG FILTER FALSE - Filter is enabled."""
 
print()
 
 
# MOD LOADING FUNCTIONS

def loadModule(modulePath, execModule = True, supportsArgs = False): # AASHISHKAM/... | Eg: AASHISHKAM/lib/fightplayer/fights/mechfight.py
    modulePath = getFilePath(modulePath)
    if os.path.exists(modulePath):
        sys.path.insert(0, os.path.dirname(modulePath))
        spec = importlib.util.spec_from_file_location("module", modulePath) # The spec of the module for the mod
        module = importlib.util.module_from_spec(spec) # The module
        if execModule: spec.loader.exec_module(module)

        if supportsArgs:
            if hasattr(module, 'args'):
                modArgs = {'doDialogText':doDialogText, 
                       'doDialogSlow':doDialogSlow, 
                       'askChoice':askChoice,
                       'askNum':askNum, 
                       'doDialogChoice':doDialogChoice, 
                       'doTimedQuestion':doTimedQuestion, 
                       'doTimedAttack':doTimedAttack, 
                       'doTimedSpam':doTimedSpam, 
                       'printGraphic':printGraphic, 
                       'getPrompt':getPrompt, 
                       'playSong':playSong, 
                       'stopSong':stopSong,
                       'pauseSong': pauseSong,
                       'playSound': playSound,
                       'timeControl':timeControl,
                       'setTime': setTime,
                       'pgFilter':pgFilter, 
                       'saveFile':saveFile, 
                       'saveGame':saveGame, 
                       'curSaveName':curSaveName, 
                       'soundImportSuccesful':soundImportSuccesful,
                       'loadModule': loadModule,
                       'getFilePath': getFilePath}
                module.args = modArgs

        if hasattr(module, 'start'):
            module.start()
        
    else: return None
    
def loadMod(modPath): # AASHISHKAM/mods/TestMod/
    if os.path.exists(modPath): 
        spec = importlib.util.spec_from_file_location("mod", os.path.join(modPath, "mod.py")) # The spec of the module for the mod
        modToLoad = importlib.util.module_from_spec(spec) # The module for the mod
        spec.loader.exec_module(modToLoad)
        if hasattr(modToLoad, "start"):
            modArgs = {'doDialogText':doDialogText, 
                       'doDialogSlow':doDialogSlow, 
                       'askChoice':askChoice,
                       'askNum':askNum, 
                       'doDialogChoice':doDialogChoice, 
                       'doTimedQuestion':doTimedQuestion, 
                       'doTimedAttack':doTimedAttack, 
                       'doTimedSpam':doTimedSpam, 
                       'printGraphic':printGraphic, 
                       'getPrompt':getPrompt, 
                       'playSong':playSong, 
                       'stopSong':stopSong,
                       'pauseSong': pauseSong,
                       'playSound': playSound,
                       'timeControl':timeControl,
                       'setTime': setTime,
                       'pgFilter':pgFilter, 
                       'saveFile':saveFile, 
                       'saveGame':saveGame, 
                       'curSaveName':curSaveName, 
                       'soundImportSuccesful':soundImportSuccesful,
                       'loadModule': loadModule,
                       'getFilePath': getFilePath}
            
            modToLoad.start(modArgs)
        else:
            doDialogText("This mod is missing the start function.")
    stopSong()
    startEngine(False)
 
def loadChapter(chapterPath): # AASHISHKAM/chapters/chapter1.py
    "chapterPath: AASHISHKAM/chapters/chapter1.py"
    if os.path.exists(chapterPath): 
        spec = importlib.util.spec_from_file_location("chapter", chapterPath) # The spec of the module for the mod
        chapterToLoad = importlib.util.module_from_spec(spec) # The module for the mod
        spec.loader.exec_module(chapterToLoad)
        if hasattr(chapterToLoad, "start"):
            modArgs = {'doDialogText':doDialogText, 
                       'doDialogSlow':doDialogSlow, 
                       'askChoice':askChoice,
                       'askNum':askNum, 
                       'doDialogChoice':doDialogChoice, 
                       'doTimedQuestion':doTimedQuestion, 
                       'doTimedAttack':doTimedAttack, 
                       'doTimedSpam':doTimedSpam, 
                       'printGraphic':printGraphic, 
                       'getPrompt':getPrompt, 
                       'playSong':playSong, 
                       'stopSong':stopSong,
                       'pauseSong': pauseSong,
                       'playSound': playSound,
                       'timeControl':timeControl,
                       'setTime': setTime,
                       'pgFilter':pgFilter, 
                       'saveFile':saveFile, 
                       'saveGame':saveGame, 
                       'curSaveName':curSaveName, 
                       'soundImportSuccesful':soundImportSuccesful,
                       'loadModule': loadModule,
                       'getFilePath': getFilePath}

            chapterToLoad.start(modArgs)
        else:
            doDialogText("ERROR: This chapter is missing the start function.")
    stopSong()
    startEngine(False)
 
 
# START FUNCTION (THIS FUNCTION STARTS THE ENTIRE ENGINE)
def startEngine(notice=True, offline=False):
    if notice:
        # GAME SPEED
        global specialFeature
        specialFeature = False 
        timeInput = input("ENTER THE GAME SPEED (2 = 2x speed): ")
        global timeControl
        timeControl = 1
        try:
            timeControl = 1 / (float(timeInput))
        except:
            print("GAME SPEED SET TO 1 INSTEAD.")
            time.sleep(1.3)
 
        # ENGINE DATA
        global version
 
        getSoundes()
        getKeyboades() 

        getSaveFile()

        global saveFile
        evaluateSaveAchievements(saveFile)
 
        if not offline: downloadStuff()
        print()
 
        doDialogChoice("NOTICE:# It is recommended to use 'IDLE Dark' Highlight theme and Font: Consolas size 14 if using Python IDLE (Windows).",
                       choices = ["I understand,# and have changed my settings",
                                  "I understand,# but don't mind visual bugs or mistakes."])
 
   # Symbol List wowzie:»│ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌ 
    printGraphic(
'''
╔═════════════════════════════╦════════════╦═════════════════════════════╗
╚╦════════════════════════════╣╡AASHISHKAM╞╠════════════════════════════╦╝   
 ║                            ╚════════════╝      v2.0                  ║
 ╟ A "Bomboclat" Dating Adventure                                       ║
 ║                         - By Siddharth A                             ║
 ╟(1) Play!                                                             ║
 ╟(2) Soundtrack                                ╠═══════════════════════╣
 ╟(3) Achievements                              ║   ╡MENU BY ARAVIND╞   ║
 ╟(4) About                                     ╠═══════════════════════╣
 ╟(5) Mods                                                              ║
 ╟(6) Settings                                                          ║
 ╟(7) Quit                                                              ║
╔╩══════════════════════════════════════════════════════════════════════╩╗
╚════╦════════╤══════════════════════════════════════════════════════════╝
     ╟Select: ''', afterdelay=0)
 
 
    achievements = saveFile['achievements']
 
    menuChoice = askChoice([1, 2, 3, 4, 5, 6, 7])
 
    if menuChoice == 1: # CHAPTER RECOGNITION
        printGraphic('''╔════╩════════╧════════════════════════╗''', afterdelay=0)
 
        chapterChoices = []
        if saveFile["route1"]["COMPLETED"] == True:
            chapterChoices += ["CHAPTER 1: A New Devagiri High."]
            if saveFile["route2"]["COMPLETED"]:
                chapterChoices += ["CHAPTER 2: Booze and Bruises."]
                if saveFile["route3"]["COMPLETED"]: 
                    chapterChoices += ["CHAPTER 3: Him."]
                    if saveFile['route4']["COMPLETED"]:
                        chapterChoices += ["CHAPTER 4: Light and Dark."]
                        if saveFile['route5']['COMPLETED']:
                            chapterChoices += ["CHAPTER 5: Projection."]
                            if saveFile['route6']['COMPLETED']:
                                chapterChoices += ["CHAPTER 6: ???"]
                            else:
                                chapterChoices += ["CHAPTER 6: ???"]
                        else:
                            chapterChoices += ["CHAPTER 5: ???"] # CHANGE THIS TO ??? AFTER THE ACTUAL CHAPTER RELEASES
                    else:
                        chapterChoices += ["CHAPTER 4: ???"]
                else:
                    chapterChoices += ["CHAPTER 3: ???"]
            else:
                chapterChoices += ["CHAPTER 2: ???"]
        else:
            chapterChoices += ["CHAPTER 1: ???"]
 
        chapterChoices += ["Return."]
 
        guiTexty = ""
        for i in range(len(chapterChoices)):
            chapter = chapterChoices[i]
 
            curLine = "\n"
            curLine += f"╟({i+1}) " + chapter
 
            curLine += " "*(40 - len(curLine))
            curLine += "║"
 
            guiTexty += curLine
        print(guiTexty)
        printGraphic('''╚════╦════════╤════════════════════════╝
     ╟Select: ''', afterdelay=0)
 
 
        getChapter = askChoice(chapterChoices)
        print()
 
        if not getChapter >= len(chapterChoices):
            loadChapter(getFilePath("chapters/chapter"+str(getChapter)+".py"))
        
        startEngine(False)
 
 
 
    elif menuChoice == 2: # SOUNDTRACK
 
        if soundImportSuccesful:
            tracks = []
            if saveFile['route1']['COMPLETED']:
                tracks += ['First Meet']
            if saveFile['route2']['COMPLETED']:
                tracks += ['Second Meet']
            if saveFile['route3']['COMPLETED']:
                tracks += ['Clavar La Espada (from BLEACH)', 
                           'Versus']
            if saveFile['route4']['COMPLETED']:
                if saveFile['route3']['rude_stay'] != "UNFORGIVED":
                    tracks += ['Light and Dark', 
                               'Light and Dark (Game Ver)',
                               'Soldier of Dark',
                               'Bach Cello Suite No. 1 in G Major (by Bach)']
                else:
                    tracks += ['Guards Encounter!',
                               'A Wonderful Review TV Show Host',
                               'A School of Magic',]
                    
                    if saveFile['route4']['on_weirdRoute']: tracks += ['Mechfight']
                    tracks += ['Castle Walls',
                               'Enraged',
                               'Guardian']
            if saveFile['route5']['COMPLETED']:
                tracks += ['Classroom',
                           'Doubted']
                if saveFile['route5']['date']: tracks += ['Third Meet']
                tracks += ['Projection']
                if saveFile['route5']['key']:
                    tracks += ['Shepherd Of My Soul (Choir Version)']
            
            if tracks == []: tracks += ["No soundtracks unlocked yet. Play the game!"]
            else: tracks += ['Return']
            soundtrackText = '''
╔════╩════════╧═══════════════════════════════════════════════╗
║ |AASHISHKAM SOUNDTRACK|                                     ║
║═══════════════════════════╣Composed by Siddharth A|╠════════║'''
            
            for i in range(1, len(tracks)+1):
                _trackName = tracks[i-1]
                newLine = f"║ {i}) {_trackName}." + " "*(56-len(_trackName)) + "║"
                soundtrackText += "\n" + newLine
            soundtrackText += """
╚═════╦════════╤══════════════════════════════════════════════╝
      ╟Select: """
            printGraphic(soundtrackText)
            ostChoice = askChoice(tracks)

            track = tracks[ostChoice - 1]

            musicPaths = {
                'First Meet':                                  'assets/soundtrack/first_meet.ogg',
                'Second Meet':                                 'assets/soundtrack/second_meet.ogg',
                'Clavar La Espada (from BLEACH)':              'assets/soundtrack/espada.mp3',
                'Versus':                                      'assets/soundtrack/versus_full.ogg',
                'Light and Dark':                              'assets/soundtrack/light_and_dark.ogg',
                'Light and Dark (Game Ver)':                   'assets/soundtrack/videogame.ogg',
                'Soldier of Dark':                             'assets/soundtrack/darkfight.ogg',
                'A Wonderful Review TV Show Host':             'assets/soundtrack/tv_show_full.ogg',
                'Guards Encounter!':                           'assets/soundtrack/guards.ogg',
                'A School of Magic':                           'assets/soundtrack/magic.ogg',
                'Bach Cello Suite No. 1 in G Major (by Bach)': 'assets/soundtrack/bach.mp3',
                'Mechfight':                                   'assets/soundtrack/mechfight_full.ogg',
                'Castle Walls':                                'assets/soundtrack/castle_walls.ogg',
                'Enraged':                                     'assets/soundtrack/enraged.ogg',
                'Guardian':                                    'assets/soundtrack/guardian.ogg',
                'Classroom':                                   'assets/soundtrack/classroom.ogg',
                'Doubted':                                     'assets/soundtrack/doubted.ogg',
                'Third Meet':                                  'assets/soundtrack/third_meet.ogg',
                'Projection':                                  'assets/soundtrack/projection_full.ogg',
                'Shepherd Of My Soul (Choir Version)':         'assets/soundtrack/shepherd.ogg'}
            
            if track not in ["Return", "No soundtracks unlocked yet. Play the game!"]:
                path = musicPaths[track]
                playSong(path, interruptable=True, looping=True)
 
            startEngine(False)
        else:
            doDialogText("Feature not available. Please enable SOUND.")
            startEngine(False)
    elif menuChoice == 3: # ACHIEVEMENTS
        printGraphic('''\
╔════╩════════╧════════════════════════╗
╠══════╣|WORK IN PROGRESS|╠════════════╣
╚══════════════════════════════════════╝
''')
        startEngine(False)
    elif menuChoice == 4: # ABOUT
        printGraphic('''╚════╩════════╧════════════════════════╝
''', afterdelay=0.1)
        printGraphic('Siddharth A was born on 28th September 2009 to APT and NTR (names hidden for privacy). When he was born, the pure aura he emitted was so much that it caused a black hole to form inside his centre of mass. He was able to contain it, but as a consequence he is now bl. At the age of 2 he built his very first nuclear reactor. When he was 3 years old he accidentally stumbled into a time machine which he had created and soon he founded the Roman Empire, the British Empire and many others. Once under the fake name Alexander the Great, he conquered a large part of the world. When people say Alexander died in reality Siddhu had just time travelled back. He did all of this in 2 months.When he was 5 years old he joined Bharatiya Vidhya Bhavans School Chevayur in Class 1B. Soon when he was 6 years old he mastered the Limitless and its Domain Expansion. Eventually he came to be known as The Honored One. At the age of 8 created a YouTube video with 2B views titled, I Created The Multiverse in my Backyard in 3 Days. Because of this success he soon rose to the top of the world and became the richest man in the world with a net worth of 1 trillion usd. At the age of 11, he singlehandedly took down the King Of Curses and achieved world peace. Eventually after enrolling in Devagiri Caramellites of Mary Immaculate Public School, he met a very interesting person by the name of Aashish R Nair. This inspired Siddhu to make the very game you are playing now.', spd=2, afterdelay=3, step=1)
 
        print('\n')
        startEngine(False)
    elif menuChoice == 5: # MODS
 
        checkMods()
 
        global listOfModFolders
        if listOfModFolders == []:
            doDialogText("No mods found.# Install mods inside the mods folder?", line=False)
            if getPrompt("", leanTrue=False):
                openFolder(os.path.join(getEngineDir(), "mods"))
                doDialogText("Opening mod folder.#.#.#")
 
            startEngine(False)
        else:
            printGraphic('''╔════╩════════╧════════════════════════╗''', afterdelay=0)
 
            guiTexty = ""
 
            returnListOfModFolders = listOfModFolders.copy() + ["Return"]
            for i in range(len(returnListOfModFolders)):
                modname = os.path.basename(returnListOfModFolders[i]) # ModName
 
                curLine = "\n"
                curLine += f"╟({i+1}) " + modname
 
                curLine += " "*(40 - len(curLine))
                curLine += "║"
 
                guiTexty += curLine
            print(guiTexty)
            printGraphic('''╚════╦════════╤════════════════════════╝
         ╟Select: ''', afterdelay=0)
 
 
            getModIndex = askChoice(returnListOfModFolders) - 1
            print()
 
            if getModIndex < len(listOfModFolders):
                try:
                    loadMod(listOfModFolders[getModIndex])
                except Exception as e:
                    stopSong()
                    doDialogText("An ERROR was encountered in the mod:")
                    print()
                    printGraphic(traceback.format_exc())
 
        startEngine(False)
    elif menuChoice == 6: # SETTINGS
        """
╔════╩════════╧════════════════════════╗
╚════╦════════╤════════════════════════╝
     ╟Select: """
 
        printGraphic('''
╔════╩════════╧════════════════════════╗
║  |SETTINGS|                          ║
╟(1) GAME SPEED                        ║
╟(2) CHANGE SAVE FILE                  ║
╟(3) PG FILTER                         ║
╟(4) Return                            ║
╚════╦════════╤════════════════════════╝
     ╟Select: ''')
 
        """
        settingsOption = doDialogChoice("SETTINGS:", choices=["GAME SPEED", "PG FILTER"])
        if settingsOption == 1:
            timeInput = input("ENTER GAME SPEED (2 -> 2x speed): ")
 
            global timeControl
            try:
                timeControl = 1/float(timeInput)
            except:
                pass #timeControl = 1
                print("GAME SPEED WAS SET TO 1 INSTEAD.")
        elif settingsOption == 2:
            global pgFilter
            pgFilter = [True, False, True][doDialogChoice("Would you like to enable the pg Filter?")]"""
 
        settingsOption = askChoice([1, 2, 3, 4])
        if settingsOption == 1:
            timeInput = input("ENTER THE GAME SPEED (2 = 2x speed): ")
            timeControl
 
            timeControl = 1
            try:
                timeControl = 1 / (float(timeInput))
            except:
                print("GAME SPEED SET TO 1 INSTEAD.")
                time.sleep(3)
        elif settingsOption == 2:
            getSaveFile()
        elif settingsOption == 3:
            global pgFilter
            pgFilter = not getPrompt("Would you like to enable the PG Filter?")
 
        startEngine(False)
    elif menuChoice == 7: # QUIT
        doDialogText("Quitting.#.#.#", afterdelay=3, spd=2)
 
#checkChapters()
