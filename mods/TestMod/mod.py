import urllib.request
import os
import time

def downloadMusic():
    mod_dir = os.path.dirname(os.path.abspath(__file__)) # gets the path of the mod folder
    musicPath = os.path.join(mod_dir, "music")
    os.makedirs(musicPath, exist_ok=True) # Create the music folder in the same folder as mod.py
    
    print("Downloading 'theme_1.ogg'...")
    if os.path.exists(os.path.join(musicPath, "theme_1.ogg")):
        print("Already downloaded 'theme_1.ogg'.")
    else:
        urllib.request.urlretrieve("https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/mods/TestMod/music/theme_1.ogg", os.path.join(musicPath, "theme_1.ogg"))
    print()

def start(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, stopSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful):
    # If music was succesfully loaded, 'soundImportSuccesful' will be set to True. Use this variable when handling sound.
    if soundImportSuccesful:
        downloadMusic()
        playSong("mods/TestMod/music/theme_1.ogg", looping=True)
        # I BELIEVE THIS FUNCTION RUNS FROM THE ENGINE'S ROOT FOLDER, SO THE MOD FOLDER IS SPECIFIED BEFORE THE MUSIC IS ACCESSED
    
    doDialogText("Welcome to the Test Mod!")
    
    if soundImportSuccesful: doDialogText("Isn't the music nice?")
    print()
    doDialogText("We shall test the capabilities mods can bring us.")
    
    # Demonstration of choice
    choice = doDialogChoice("Do you like this mod so far?", choices=["Yes", "No"])
    
    if choice == 1:
        doDialogText("Glad to hear that,# Though this mod has just started.")
    else:
        doDialogText("I see.# Well the mod just started, so do stick around.")
    
    # 'print()' function to leave gaps in the text for better format.
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

    musicChoice = doDialogChoice("Would you like to listen to the music further?", choices=["Yes", "No"])

    if musicChoice == 1:
        doDialogText("Very well.# Press ENTER when you would like to stop.")
        input("Press ENTER to finish the mod.")
    
    doDialogText("Very well.# Thank you for testing out this test mod.")
    doDialogText("Also yeah this test mod is also BETA.# I plan to demonstrate many features of mods in the future through this mod.")
    print()
    doDialogText("If you ran into any errors,# please do report them back to the developer, aka me.", afterdelay=1.1)

    print()
    doDialogChoice("Well,# that's it.# Goodbye.", choices=["Goodbye."])

    time.sleep(5)

    if soundImportSuccesful:
        stopSong()