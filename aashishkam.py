import time
import os
import sys
import importlib.util
import urllib.request
import subprocess

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

def load():
    print("Attempting to load...")
    spec = importlib.util.spec_from_file_location("AASHISHKAM", getFilePath("src/AASHISHKAM.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module

def download():
    print("Downloading...")
    os.makedirs(getFilePath("src"), exist_ok=True)
    urllib.request.urlretrieve("https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/src/AASHISHKAM.py", getFilePath("src/AASHISHKAM.py"))

def downloadStuff(force=False):

    os.makedirs(getFilePath("chapters"), exist_ok=True)
    os.makedirs(getFilePath("assets/soundtrack"), exist_ok=True)
    
    downloadList = [
        "chapters/chapter1.py",
        "chapters/chapter2.py",
        "chapters/chapter3.py",
        "chapters/chapter4.py",

        "assets/soundtrack/darkfight.ogg",
        "assets/soundtrack/videogame.ogg",
        "assets/soundtrack/lokahbanger.ogg",
        "assets/soundtrack/light_and_dark.ogg"
    ]
    
    downloadUrls = {
        "chapters/chapter1.py": "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/chapters/chapter1.py",
        "chapters/chapter2.py": "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/chapters/chapter2.py",
        "chapters/chapter3.py": "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/chapters/chapter3.py",
        "chapters/chapter4.py": "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/chapters/chapter4.py",

        "assets/soundtrack/darkfight.ogg": "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/darkfight.ogg",
        "assets/soundtrack/videogame.ogg": "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/videogame.ogg",
        "assets/soundtrack/lokahbanger.ogg": "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/lokahbanger.ogg",
        "assets/soundtrack/light_and_dark.ogg": "https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/assets/soundtrack/light_and_dark.ogg"
    }

def start():
    global offlineMode
    offlineMode = False

    os.makedirs(getEngineDir(), exist_ok=True)

    # Get the version
    try: # Got the version.
        urllib.request.urlretrieve("https://github.com/LocalVarBright/AASHISHKAM/raw/refs/heads/main/version.txt", getFilePath("version.txt"))
    except: # Didn't get the version.
        print("Failed to get version info. Starting in offline mode.")
        offlineMode = True
    time.sleep(0.5)
    
    if not offlineMode:
        with open(getFilePath("version.txt"), "r") as f: # Access current version
            onlineVersion = f.read().strip()
        
        downloadStuff(True)
        
        if checkFile("src/AASHISHKAM.py"): # Aashishkam was found
            aashishkam = load()

            if hasattr(aashishkam, "version"): print(True)
            else:print(False)
            if aashishkam.getVersion() == onlineVersion: # Latest version.
                print("You have the latest version.")
                aashishkam.startEngine()
            else: # Update available.
                ad = input("An update is available. Do you want to download it now? (y/n): ").strip().lower()
                if ad.lower() in "yes":
                    download()
                    aashishkam = load()
                    aashishkam.startEngine()
                    
                else:
                    aashishkam.startEngine()
                    

        else: # Aashishkam was not found
            download()
            aashishkam = load()
            aashishkam.startEngine()
    else: # Is on offline mode
        # Check if Aashishkam is present
        if checkFile("src/AASHISHKAM.py"):
            aashishkam = load()
            aashishkam.startEngine()
        else:
            print("AASHISHKAM is not installed and cannot be installed in offline mode. Please connect to the internet and try again.")
            time.sleep(3)


start()
