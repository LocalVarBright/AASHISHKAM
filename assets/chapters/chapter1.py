def chapter_1(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful):
    
    aahanNameList = ["aahan", "ahan", "ahaan", "aahaan"]
    
    route1 = {
        "name_choice": "NORMAL",
        "rude_choice": 0,
        "rude_cancel": 0,
        "lunatic_choice": 0
    }

    doDialogText("AASHISHKAM: A \"Bomboclat\" Dating Experience#", spd = 25, step = 3)
    print()
 
    doDialogText("ENTER YOUR NAME: ", spd = 3, line = False)
    saveFile['name'] = input("")
 
    doDialogText("CHAPTER 1:## A New Devagiri High.", spd = 25, step = 3)
 
    doDialogText(f"Your name is now {saveFile['name'].upper()}.### You're a new student at Devagiri High.",spd=5)
    doDialogText("It is your first day at this new,# prestigious school...", spd=5)
    doDialogText("...and the kid that sits next to you is a shy kid,# named ASHISH.", spd=5, afterdelay=1.4)
 
    doDialogText("ASHISH:# Hello,# my name is Ashish. What's your name?")
    if pgFilter: doDialogText("(He's cute...)")
    name_choice = doDialogChoice("", choices=["Answer him nicely.", "Answer him rudely.", "Say you don't know."])
 
    if name_choice == 1: # You just tell him your name. Best option.
        route1["name_choice"] = "NORMAL"
        doDialogText(f"YOU:# Hello Ashish, I'm {saveFile['name']}. Nice to meet you.")
        doDialogText("    # ...but on your pencil box it says# \"Ashishk\"?")
        doDialogText("ASHISH: Huh?!## O-#Oh god!### Who wrote that?### N-#No that's not my name!#### Jerk-",spd=2,afterdelay=0.3)
        doDialogText("       # ...#I'm sorry,# one of my friends must've played a prank on me and wrote that.")
 
        doDialogText("YOU:# Oh don't worry,# its fine.# Besides,# I think Aashishk is a cute nickname.")
        doDialogText("ASHISH:# H-#Huh?!# O-oh,# thanks...# I guess?", afterdelay = 0.4)
        doDialogText("(He's extremely flustered.#.#.#)")
        doDialogText("YOU:# -", afterdelay=0.1) # After this dialog, teacher interrupts you.
    elif name_choice == 2: # You're rude to him.
        route1["name_choice"] = "RUDE"
        doDialogText("YOU:# I don't even know you.")
        doDialogText("ASHISH:# Yeah...# thats why I wanted to ask for your name,# and get to know you.#.#.", line=False)
        rude_choice = doDialogChoice("", choices=["Ignore him.", "Apologise and tell him your name.", "Rudely tell him your name."])
 
        if rude_choice == 1: # You ignored him.
            route1["rude_choice"] = "IGNORED"
            if saveFile['name'].lower() in aahanNameList: # You're aahan, so you sing a mj song lmfao:
                doDialogText("You ignored him,# and start humming a michael jackson song.")
            else:
                doDialogText("You turn away, and ignore him.")
 
            doDialogText("ASHISH:# Hey!# Answer me!")
            doDialogText("        Fine then.#")
            doDialogText("(He's moody.)")
 
            doDialogText("...", spd=17, afterdelay=1.5)
            doDialogText("The teacher is about to say something.", afterdelay=1.4) # After this dialog, teacher interrupts.
        elif rude_choice == 2: # You apologised.
            route1["rude_choice"] = "APOLOGISED"
            doDialogText(f"YOU:# Ok, I'm sorry.# I'm {saveFile['name']}. Nice to meet you, Ashishk.")
            doDialogText("ASHISH:# Huh?# My name is not Ashishk.# There is no k.")
            doDialogText("YOU:# ...but it's written on your pencil box?")
            doDialogText("ASHISH:# Huh- What?", afterdelay = 0.4)
            doDialogText("Ashish quickly whips around to his pencil box, with \"ASHISHK\" written on it.")
 
            doDialogText("ASHISH:## O-#Oh god!### Who wrote that?### N-#No that's not my name!",spd=2,afterdelay=0.3)
            doDialogText("       # ...#I'm sorry,# one of my friends must've played a prank on me and wrote that.")
            doDialogText("YOU:# Oh, I understand.")

            if pgFilter: doDialogText("(He looks incredibly flustered.)", line=False)
 
            rude_cancel = doDialogChoice("", choices=["Compliment him.", "Say nothing of it."])
            if rude_cancel == 1: # You complimented his newfound nickname.
                route1["rude_cancel"] = "CANCELLED"
                if pgFilter:
                    doDialogText("YOU:# I do think that Ashishk.#.#.# sounds kinda cute.")
                    doDialogText("ASHISH:# H-#Huh?!# O-oh,# thanks...# I guess-", afterdelay = 0.4) # After this dialog, teacher interrupts.
                else:
                    doDialogText("YOU:# I do think that Ashishk is a nice nickname.")
                    doDialogText("ASHISH:# Oh,# thanks...# I guess-", afterdelay = 0.4) # After this dialog, teacher interrupts.
            else:
                route1["rude_cancel"] = "NOT CANCELLED"
                doDialogText("You decide not to say anything.")
 
            doDialogText("Suddenly-",afterdelay=0.5) # After this dialog, teacher interrupts.
 
        elif rude_choice == 3: # You rudely told him your name.
            route1["rude_choice"] = "RUDENAME"
 
            doDialogText(f"YOU:# It's {saveFile['name']}, man. {saveFile['name']}. Now what do you want?")
            doDialogText(f"ASHISH:# Hey, you don't to be so damn rude about it...",afterdelay=0.5)
            doDialogText("YOU:# How about you stop bothering me then?")
            doDialogText("ASHISH:# I wasn't trying to bother you.#.#.#",spd=6, afterdelay=1.4)
            doDialogText("...# Ashish does not talk to you anymore.",spd=5)
 
            doDialogText("...", spd=17, afterdelay=1.5)
            doDialogText("The teacher is about to say something.", afterdelay=1.4) # After this dialog, teacher interrupts.
 
    elif name_choice == 3: # You say you don't know your name.
        route1["name_choice"] = "LUNATIC"
 
        doDialogText("YOU:# I dunno,# bro.# I dunno.#")
        doDialogText("ASHISH:# Huh?# Just tell me.# What is your name?")
        doDialogText("(He seems interested in finding your name.)")
        lunatic_choice = doDialogChoice("(Pretend further?)", choices=["Keep playing dumb.", "Tell him your name."])
 
        if lunatic_choice == 1: # You keep playing dumb.
            route1["lunatic_choice"] = "PLAYED DUMB"
            doDialogText("YOU:# Hey,# which school are we in?")
            doDialogText("ASHISH:# Come on,# stop playing dumb!# You KNOW which school this is.")
            doDialogText("YOU: ...##are you a cat?",spd=15)
            doDialogText("ASHISH: ...", spd=10)
 
            doDialogText("Ashish looks at your name on your books.")
            doDialogText(f"ASHISH:# {saveFile['name']},# huh?# Nice to meet you then.")
            doDialogText("YOU: -", afterdelay = 0.2)
            doDialogText("ASHISH:# Also if you keep playing dumb, I'm going to uhh-# hit you.")
            doDialogText("(He has your umbrella in his hand.# Best to drop the act.)")
 
            doDialogText(f"YOU:# Okay okay,# I'm {saveFile['name']}.")
            doDialogText(f"ASHISH:# Hmph.# It's nice to meet you,# {saveFile['name']}.")
        elif lunatic_choice == 2: # You told him your name.
            route1["lunatic_choice"] = "TOLD HIM"
            doDialogText(f"YOU:# Okay I'll tell you my name.# It's #{saveFile['name']}.")
            doDialogText(f"ASHISH:# Hmph.# It's nice to meet you,# {saveFile['name']}.")
 
        # From here on, Ashish gets flustered about his name, so no need to put that in both scenarios individually
        doDialogText("YOU:# Nice to meet you too,# uh,# ASHISHK was it?")
        doDialogText("ASHISH:# Huh?# No.# My name is not ASHISHK.# Where did you get that?")
        doDialogText("YOU:# But.#.#.# it's written on your pencil box?")
        doDialogText("ASHISH: Huh?!## O-#Oh god!### Who wrote that?### N-#No that's not my name!#### Jerk-",spd=2,afterdelay=0.3)
        doDialogText("       # ...#I'm sorry,# one of my friends must've played a prank on me and wrote that.")
 
        doDialogText("YOU:# Oh don't worry,# its fine.# Besides,# I think Aashishk is a cute nickname.")
        doDialogText("ASHISH:# H-#Huh?!# O-oh,# thanks...# I guess?", afterdelay = 0.4)
        if pgFilter: doDialogText("(He's extremely flustered.#.#.#)")
 
        doDialogText("Suddenly-",afterdelay=0.5) # After this dialog, teacher interrupts.
 
    # Teacher starts talking
    doDialogText("TEACHER:# OKAY CHILDREN, EVERYONE LISTEN.", afterdelay=1.4)
    doDialogText("(The students are still talking.)")
    doDialogText("TEACHER: #", spd=15, line=False)
    doDialogText("IIII SSSAAAAAIIIIDDDDDD LLLIIIISSSTTTTEEEENNNNNN, YYYOOOUUUU UUUNNNGRAAATEFULLL BRRAATTTSSS!!!", step=2)
 
    doDialogText("(... The class is silent now.)")
    doDialogText("TEACHER: Ahem.# Now that I have everyone's attention,# I have a few words to say.#", afterdelay=0)
    doDialogText("         ", spd=0, line=False)
    doDialogText("Since this is the beginning of your new school year,# I should tell you about the school.")
    doDialogText("The teacher is talking about the school, how prestigious it is and how important it's history is and what not.")
    doDialogText("The details pretty much bore you to death.")
 
    # INTRODUCTION AND ENDING PART
    if route1["name_choice"] == "NORMAL": # Ashishlove <3
        print()
        doDialogText("You look over to Ashish,# who also looks bored.#")
        doDialogText("You share glances with Ashish every now and then,# and he shyly looks away each time.")
        doDialogText("...# you get lost looking at his face.#.#.")
        doDialogText("(Why he kinda.#.#.#)-")
 
        doDialogText("TEACHER: ", spd=0, afterdelay=0, line=False)
        doDialogText(f"{saveFile['name'].upper()}!!!")
 
        doDialogText("(What the-)", afterdelay=0.01)
        doDialogText("You realize you have to introduce yourself.")
        doDialogText("... You stand up,# take a deep breath,# and...")
        doDialogText("YOU:## Hello, my name is ASHISH-#", afterdelay=0, line=False) # This instant confirms that you like Ashish.
        doDialogText(f" I MEAN {saveFile['name'].upper()}-#", spd=3, afterdelay=0, line=False)
        doDialogText(" (Damn.)", spd=7, step=2)
 
        doDialogText("Everyone is now looking at you awkwardly.# You feel the eyes drilling into your skin.# You haven't felt more uncomfortable.")
        doDialogText("(WHY DID I SAY ASHISH?!?!)")
        doDialogText("You stutter through the rest of the introduction,# wrapping it up quickly.# You sit down, extremely embarassed.")
        doDialogText("You can still hear the snickering of some students.#.#.#")
        doDialogText("Ashish awkwardly stands up and does his introduction too.# He also stutters through most of it.")
        doDialogText("He arguably does worse than you.")
        doDialogText("He finishes his introduction and sits down.# You look at him and.#.#.#")
        doDialogText("ASHISH is...# giggling?", spd=10, afterdelay=1.4)
 
        doDialogText("ASHISH:# Haha,# you said my name!# Lol")
        doDialogText("YOU:# yeah...# sorry about that.# I got words mixed up.")
        doDialogText("ASHISH:# Oh don't worry about that!# Everyone makes mistakes.")
        doDialogText("YOU: Yeah.")
        doDialogText("ASHISH: Also, you mentioned that you played guitar?")
        doDialogText("YOU:# Yeah I do!# I've been playing it for about nine years.# I mostly do lead guitar.")
        doDialogText("ASHISH:# Wow! That's so cool!# I've been trying to sing for a while,# but I can never seem to hit the notes!")
 
        doDialogText("YOU:# I'm sure you will get better soon.")
        doDialogText(f"ASHISH: Thank you {saveFile['name'].upper()}!# I also hope so.")
        doDialogText("YOU:# You're welcome.", spd=6, afterdelay = 2)
 
        print()
        doDialogText("The rest of the school day goes by normal.# You barely get time to talk with Ashish between rushed classes,#")
        doDialogText("and you get home rather quickly.# Also the school time table is kinda goofy.# Who eats lunch at 10:45 AM???")
        print()
        doDialogText("You get home after school.# It was exhausting.# You plop down on your bed and decide to practice guitar.")
        doDialogText("After practicing the same song for 3 weeks,# you decide to finally learn a new song.")
 
        doDialogText("A song floats into your Spotify app: ", line=False)
        doDialogText("Aashishkam.", step=3, spd=20)
        # ENDING OF CHAPTER 1
    elif route1["name_choice"] == "RUDE": # Ashishlove broken </3
        print()
 
        if route1["rude_choice"] == "IGNORED": # machaan got ignored
            doDialogText("Soon,# it's your turn to introduce yourself.")
            doDialogText("You stand up.#.#.# take a deep breath,# and begin to introduce yourself.")
            doDialogText("...", spd=13)
            doDialogText("You did fine.# You sit down and listen to Ashish's introduction.")
            doDialogText(".#.#.You eventually get bored and focus your mind on something else.", afterdelay=3)
 
            doDialogText("The rest the school day went by quickly.", afterdelay=0.3)
            doDialogText("ASHISH tried to talk to you a few more times throughout the day, but you turned him down.")
 
            doDialogText("After you get home from school, you plop down on your bed and decide to practice guitar.")
            doDialogText("You decide to practice the same song you practiced yesterday: ", line=False)
            doDialogText("Billie Jean.", spd=10)
            # ENDING OF CHAPTER 1
        elif route1["rude_choice"] == "APOLOGISED":
            if route1["rude_cancel"] == "CANCELLED":
                doDialogText("You look over to Ashish,# who also looks bored.#")
                doDialogText("You share glances with Ashish every now and then,# and he shyly looks away each time.")
                doDialogText("...# you start thinking about how you feel bad about being rude to him first.#.#.")
 
                doDialogText("TEACHER: ", spd=0, afterdelay=0, line=False)
                doDialogText(f"{saveFile['name'].upper()},# introduce yourself please.")
                doDialogText("You realize you have to introduce yourself now.")
                doDialogText("Without thinking,# you stand up and start speaking-", afterdelay = 0.3)
                doDialogText("YOU:## Hello, my name is ASHISH-#", afterdelay=0, line=False) # This instant confirms that you like Ashish.
                doDialogText(f" I MEAN {saveFile['name'].upper()}-#", spd=3, afterdelay=0, line=False)
                doDialogText(" (DAMN it.)", spd=7, step=2)
 
                doDialogText("Everyone is now looking at you awkwardly.# You feel the eyes drilling into your skin.# You haven't felt more uncomfortable.")
                doDialogText("(WHY DID I SAY ASHISH?!?!)")
                doDialogText("You stutter through the rest of the introduction,# wrapping it up quickly.# You sit down, extremely embarassed.")
                doDialogText("You can still hear the snickering of some students.#.#.#")
 
                doDialogText("You look over to Ashish.#.#.#")
                doDialogText("...you can tell he's slightly blushing.#.#.")
                doDialogText("He stands up for his introduction...")
                doDialogText("...your mind fades...")
 
                doDialogText("...as soon as you snap back,# Ashish is done with his introduction.")
                doDialogText("YOU:# (whispering)# sorry about that...")
                doDialogText("ASHISH:# (also whispering)# don't mind it.#.#", afterdelay = 1)
 
                print()
                doDialogText("The rest of the school day goes by quickly.")
                doDialogText("You occasionally share glances with Ashish,# and he shyly looks away each time.")
                doDialogText("He seemed embarrassed.# damn.")
                print()
                doDialogText("You get home after school.# You plop down on your bed and take a quick nap.")
                doDialogText("You decide to practice guitar after waking up from the refreshing nap.")
                doDialogText("The song starts playing: ", afterdelay=2, line=False)
                doDialogText("Ashakiran.", step=2, spd=25)
                # ENDING OF CHAPTER 1
            elif route1["rude_cancel"] == "NOT CANCELLED":
                doDialogText("You look over to Ashish,# who also looks bored.#")
                doDialogText("You share glances with Ashish every now and then,# and he shyly looks away each time.")
                doDialogText("...# you start thinking about how you feel bad about being rude to him first.#.#.")
 
                doDialogText("TEACHER: ", spd=0, afterdelay=0, line=False)
                doDialogText(f"{saveFile['name'].upper()},# introduce yourself please.")
                doDialogText("You realize you have to introduce yourself now.")
                doDialogText("You take a deep breath.#.#.# stand up and #start talking.")
                doDialogText("...")
                doDialogText("After your introduction,# the teacher asks ASHISH to introduce himself.")
                doDialogText("He stands up for his introduction...")
                doDialogText("...your mind fades...")
 
                doDialogText("...as soon as you snap back,# Ashish is done with his introduction.")
                doDialogText("YOU:# (whispering)# sorry about that...")
                doDialogText("ASHISH:# (also whispering)# don't mind it.#.#", afterdelay = 1)
                print()
 
                doDialogText("The rest of the school day goes by quickly.")
                doDialogText("You occasionally share glances with Ashish,# and he shyly looks away each time.")
                print()
                doDialogText("You get home after school.# You plop down on your bed and take a quick nap.")
                doDialogText("You decide to practice guitar after waking up from the refreshing nap.")
                doDialogText("The song starts playing: ", afterdelay=2, line=False)
                doDialogText("Ashakiran.", step=2, spd=25)
                # ENDING OF CHAPTER 1
        elif route1["rude_choice"] == "RUDENAME":
            doDialogText("Soon,# it's your turn to introduce yourself.")
            doDialogText("You stand up.,# and begin to introduce yourself.")
            doDialogText("...", spd=13, afterdelay=1.4)
            doDialogText("You did fine.# You sit down and focus your mind on something else.", afterdelay=3)
 
            doDialogText("The rest the school day went by quickly.", afterdelay=0.3)
            doDialogText("Ashish hasn't talked to you since.")
 
            doDialogText("After you get home from school, you plop down on your bed and decide to listen to some songs.")
            doDialogText("A Song pops into your playlist: ", line=False)
            doDialogText("Billie Jean.", spd=10)
            # ENDING OF CHAPTER 1
    elif route1["name_choice"] == "LUNATIC":
        doDialogText("Soon,# its time to indroduce yourself.")
        doDialogText("You stand up,# and quickly start introducing yourself.")
        doDialogText("...it ends swiftly.# Now it's Ashish's turn to introduce himself.")
        doDialogText("...he stutters through his introduction,# you could've done better.")
        print()
 
        doDialogText("The rest of the school day goes by quickly.")
        doDialogText("You make quick talk with Ashish,# despite the rushed school schedule.")
        doDialogText("You get home after school and plop down on your bed.")
        doDialogText("You decide you are gonna practice a song you haven't touched in a while.")
        doDialogText("You open up spotify, and search up the song: ", afterdelay=3, line=False)
        doDialogText("Smooth## Criminal.")
        # ENDING OF CHAPTER 1
    
    # THE SAVE SHENANIGANS
    if saveFile['route1']['COMPLETED'] == True:
        doDialogText("You have already completed this chapter.# Would you like to save over your progress? (Y/N):", line=False)
        confirm = input("")

        if confirm.lower() in "n":
            doDialogText("The Game was not Saved.")
        else:
            route1["COMPLETED"] = True
 
            saveFile["route1"] = route1

            try:
                saveGame(curSaveName, saveFile)
                doDialogText("The game was saved.")
            except:
                doDialogText("There was an error in saving the game.")
    else:
        route1["COMPLETED"] = True
    
        saveFile["route1"] = route1
    
        saveGame(curSaveName, saveFile)
 
    

def start(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful):

    doDialogText("Loading Chapter 1.#.#.#", afterdelay=3)
    print()

    chapter_1(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful)
    