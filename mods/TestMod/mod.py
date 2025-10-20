import urllib.request
import os

def downloadMusic():
    os.makedirs("music", exist_ok=True) # Create the music folder in the same folder as mod.py
    # NOTE: THE ABOVE LINE RUNS DIRECTLY FROM THE MODULE'S LOCATION, SO THE MUSIC FOLDER WILL BE CREATED IN THE SAME FOLDER AS mod.py

    print("Downloading 'theme_1.ogg...")
    urllib.request.urlretrieve("https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/mods/TestMod/music/theme_1.ogg", "music/theme_1.ogg")
    print()

def start(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, stopSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful):
    if soundImportSuccesful:
        downloadMusic()
        playSong("mods/TestMod/music/theme_1.ogg", looping=True)
        # I BELIEVE THIS FUNCTION RUNS FROM THE ENGINE'S ROOT FOLDER, SO THE MOD FOLDER IS SPECIFIED BEFORE THE MUSIC IS ACCESSED
    
    doDialogText("Welcome to the Test Mod!")
    
    if soundImportSuccesful: doDialogText("Isn't the music nice?")
    print()
    doDialogText("We shall test the capabilities mods can bring us.")
    choice = doDialogChoice("Do you like this mod so far?", ["Yes", "No"])
    
    if choice == 1:
        doDialogText("Glad to hear that,# Though this mod has just started.")
    else:
        doDialogText("I see.# Well the mod just started, so do stick around.")
    
    print()

    doDialogText("Let's talk about how 2.0 is coming along so far.")
    doDialogText("I plan to release 2.0 with the full release of CHAPTER 4's RUDE ROUTE.# More updates will be coming soon.")
    doDialogText("AASHISHKAM v2.0 will take a new approach to the update mechanic.")
    doDialogText("Instead of manually redownloading the entire game,# updates will be carried out by externally downloading parts of the game.")
    doDialogText("As long as you have the launcher file and internet,# you will be able to play the latest version of AASHISHKAM.")
    print()
    doDialogText("2.0 also brings the ability to create MODS,# such as one you are playing right now.")
    doDialogText("Chapters in Aashishkam take a similar approach to how modding works,# so if you want a reference,# look at the chapter modules in the AppData folder.")
    doDialogText("AASHISHKAM is stored in %AppData%/AASHISHKAM now.")

    if soundImportSuccesful:
        stopSong()