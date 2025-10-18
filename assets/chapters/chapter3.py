

def chapter_3(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, stopSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful):
    route3 = {
        "surrender": 0,
        "rude_stay": 0
    }
    adithyaNameList = ["aditya", "aaditya", "adithya", "aadithya", "adhitya", "aadhitya", "adhithya", "aadhithya", 
                   "adityan", "aadityan", "adithyan", "aadithyan", "adhityan", "aadhityan", "adhithyan", "aadhithyan"]
    doDialogText("CHAPTER 3:## Him.", spd = 25, step = 3)
    print()

    doDialogText("You're walking to school.# It's a rainy tuesday,# and you forgot to bring an umbrella.")
    doDialogText("At this point,# you're walking to class drenched in the rain.")
    doDialogText("Someone,# is following you.")
    doDialogText("Suddenly,# you get a tap on your shoulder right as you are about to enter the class-", afterdelay=0.4)
    doDialogText("|| TAP ||", step=2, spd=10)
    doDialogText("ADITHYA: .#.#.#")
    doDialogText("YOU:# Uhh,# can I help you?")
    doDialogText("ADITHYA: ...#.#.#")
    print("         ", end="")
    doDialogText("Hey.")
    doDialogText("YOU:# Hello?")
    doDialogText("It's ADITHYA.# A guy in your class,# you think.")
    doDialogText("(Why is he just.#.#.# standing there,# and not saying anything?)")
    doDialogText(f"ADITHYA:# SO,## you're {saveFile['name'].upper()},# right?")
    if saveFile['name'].lower() in adithyaNameList:
        print("         ", end="")
        doDialogText("Very Interesting.#.#.# Very Very Interesting.")
    doDialogText("YOU:# Yes.#.#.# and you're Adithya?")
    doDialogText("ADITHYA:# Mhm.# Yeah.")
    doDialogText("YOU:# Well.#.#.# nice to meet you-", afterdelay=0)
    doDialogText("ADITHYA:# So what's your deal with Ashish?")
    doDialogText("YOU:# Excuse me?")
    doDialogText("ADITHYA:# What?# You are sitting next to Ashish,# right?")
    doDialogText("YOU:# Yeah,# you know him?")
    doDialogText("ADITHYA:# I'm his childhood best friend,# GANG.")
    doDialogText("YOU:# Oh,# I see-", afterdelay=0)
    doDialogText("ADITHYA: So what's your deal with Ashish?", spd=3)

    if saveFile["route1"]["name_choice"] == "NORMAL":
        doDialogText("YOU: We're friends????", spd=2)
        doDialogText("ADITHYA:## Hmmmm....", spd=6)
        doDialogText("YOU:# What?# We just met like a few days ago.")
        doDialogText("ADITHYA:# Interesting.#.#.#")
        doDialogText("YOU:# Hey,# idk if you know this,# but you're.#.#.# walking away.# Okay then.")
        doDialogText("Adithya walks away mid-sentence.")
        doDialogText("(Okay then.)")
    elif saveFile["route1"]["name_choice"] == "LUNATIC":
        doDialogText("YOU:# Uh,# we're friends?")
        doDialogText("ADITHYA:# Hmm.#.#.# I guess so.# You haven't made any moves on him yet.")
        doDialogText("YOU:# Moves like.#.#.# what-", afterdelay=0)
        doDialogText("Adithya is already walking away.")
        doDialogText("(Bruh.)")
    elif saveFile["route1"]["name_choice"] == "RUDE":
        doDialogText("YOU:# Idk,# I barely know him.")
        doDialogText("ADITHYA:# Oh?")
        doDialogText("YOU:# Yeah.#.#.#")
        doDialogText("ADITHYA:# Why?# You don't get along with him?")
        doDialogText("YOU:# I guess so.#.#.# he does seem a little annoying.")
        doDialogText("(His hand shakes.)")
        doDialogText("ADITHYA:# Hmmm,# I see.# Okay.# Then.# Alright.")
        doDialogText("Adithya walks away.")
        doDialogText("(Okay then.)")
    
    doDialogText("You're about to go back to class when-", afterdelay=0.1)
    doDialogText("ADITHYA:# *pulls you over* you better not be lying to me or something,# alright?")
    doDialogText("YOU:# Why would I lie about-", afterdelay=0)
    doDialogText("He walks away mid-sentence again.")

    doDialogText("You enter your classroom now.")
    doDialogText("TEACHER:# You're late.", afterdelay=3)
    print()
    doDialogText("It's now the first break of the school day.")
    if saveFile["route1"]["name_choice"] == "RUDE":
        if saveFile['route1']['rude_choice'] == "APOLOGISED":
            doDialogText("It seems that Ashish is absent today.# Hope you didn't come off as rude to him.#.#.#")
    else:
        doDialogText("It seems Ashish hasn't come to school today.")
    doDialogText(".#.#.#")
    doDialogText("Adithya is walking up to you again,# with some more people behind him.")
    doDialogText("ADITHYA:# HEY!")
    doDialogText("YOU:# What now?")
    doDialogText("ADITHYA:# I realise I haven't introduced myself yet, soo.#.#.# LISTEN UP!")
    doDialogText("(Oh brother.)")
    doDialogText("ADITHYA:# I'm#### ADITHYA.## Your WORST Enemy.")
    doDialogText("YOU:# Huh?")
    doDialogText("ADITHYA:# I KNOW what your plan is,# little dingaling.")
    doDialogText("YOU:# My.#.#.# plan?", spd=5)
    doDialogText("ADITHYA:# Don't play dumb with me,# you-#### fellow devagirian.#.#.#")
    doDialogText("(Wha-)",afterdelay=0)
    doDialogText("ADITHYA:# You're in love with ASHISH!")

    # i HAVE to make things easier for myself 😭
    nameChoice = saveFile['route1']['name_choice']

    # THE CONFRONTATION
    if nameChoice == "NORMAL":
        doDialogText("YOU:# W-#What the heck?!")
        doDialogText("ADITHYA:# You can't hide it,# you sick little pervert!# I.## know.## EVERYTHING.")
        doDialogText("(I never thought of Ashish that way,# and this seems ridiculous.)")
        doDialogText("(But then why.#.#.### -NO)", afterdelay=0)
        doDialogText("ADITHYA:# A-#A-#Ahh!# But I won't be letting it happen.", spd=2)
        doDialogText("YOU:# What are you even.#.#.# talking about.#.#.### Huh?")
        doDialogText("ADITHYA:# I got me and my gang behind me to stop you.# We WON'T let a dear friend get corrupted by means of you!")
        doDialogText("YOU:# What the f-", afterdelay=0)
        doDialogText("ADITHYA:# I SHALL NOW SHOW YOU MY TEAM!# I put together this team under quick emergency because of how fast you tried to bag Ashish.")
        doDialogText("(What is going on-)",afterdelay=0)
    elif nameChoice == "LUNATIC":
        doDialogText("YOU:# What?")
        doDialogText("ADITHYA:# You can pretend to,# but you can't hide it,# you PLAYBOY!")
        doDialogText("YOU:# What are you-", afterdelay=0)
        doDialogText("ADITHYA: NO NO NO I won't let it happen.# I can't let a pure soul like him get corrupted by the means of YOU.")
        doDialogText("YOU:# What-", afterdelay=0)
        doDialogText("ADITHYA:# You \"#BEFRIENDED#\" him on the VERY first day of school.# That's predatorial behavior.")
        doDialogText("YOU:# How is that-", afterdelay=0)
        doDialogText("ADITHYA:# ENOUGH TALKING!# Now meet my gang.")
        doDialogText("YOU:# Your what-", afterdelay=0)
    elif nameChoice == "RUDE":
        if saveFile['route1']['rude_choice'] == "APOLOGISED":
            doDialogText("YOU:# W-What?")
            doDialogText("ADITHYA:# You can't hide it,# you fake friend!")
            doDialogText("YOU:# What are you-", afterdelay=0)
            doDialogText("ADITHYA: I KNOW you're trying to gain his trust.# You've just been waiting for the perfect chance.")
            doDialogText("YOU:# What-", afterdelay=0)
            doDialogText("ADITHYA:# You \"#BEFRIENDED#\" him on the VERY first day of school.# That's predatorial behavior.")
            doDialogText("YOU:# How is that-", afterdelay=0)
            doDialogText("ADITHYA:# ENOUGH TALKING!# Now meet my gang.")
            doDialogText("YOU:# Your-# huh?!", afterdelay=0.3)
        else:
            doDialogText("YOU:# Uh,# what?")
            doDialogText("ADITHYA:# It is my duty to SAVE Ashish from people like you!")
            doDialogText("YOU:# What-", afterdelay=0)
            doDialogText("ADITHYA:# I know everything that will happen.# You will only HURT Ashish further!")
            doDialogText("YOU:# Hurt him?")
            doDialogText("ADITHYA:# Yeah.# Ok NOW ENOUGH!")
    
    # GANG INTRODUCTION AND MONOLOGUE
    doDialogText("ADITHYA:# BOYS!# *snaps fingers* INTRODUCE YOURSELVES!")
    doDialogText("EARWIND:# Hi,# I'm EARWIND.#.#.# I came from his school,# and I guess I am helping him now.")
    
    # You played Badminton with EARWIND, so he recognizes you
    if nameChoice == "RUDE" and saveFile['route1']['rude_choice'] != "APOLOGISED": 
        print("        ", end="")
        doDialogText(f"Oh Hey!# Hello {saveFile['name']}!")
        doDialogText("YOU:# Oh,# EARWIND.# You're.#.#.# friends with that guy?")
        doDialogText("EARWIND:# Yeah,# he's usually chill, but I don't know what's happening-", afterdelay=0)
        doDialogText("ADITHYA: ENOUGH!### Now continue the introduction!", afterdelay=2)
        print("         ", end="")
        doDialogText("also you know him-", afterdelay=0)

    doDialogText("A.R RAMHAN:# I'm Rahman.# Arakkal Rahman,# but for some reason you all call me A.R Rahman.")
    doDialogText("Arakkal is tearing up...?")
    doDialogText("ADITHYA:# See,# you've already made him cry.")
    doDialogText("YOU: Excuse Me What-", afterdelay=0)
    doDialogText("A.R RAHMAN:# But I can cry on command.# I was just fooling you.") # VERY IMPORTANT
    doDialogText("SAVAN:# I'm SAVAN.# Pronounced like \"SEVEN\".")
    doDialogText("TEJAS:### WHO ARE YOU GUYS?!## WHY DID YOU GUYS PULL ME OVER HERE?!## WHAT IS HAPPENING-", spd=2, afterdelay=0)
    doDialogText("ADITHYA:# And Together.#.#.#")
    doDialogText("ALL IN UNISON:# WE ARE THE FANTASY GANG!!!!!!!", step=2, spd=6, afterdelay=3)
    print()
    doDialogText(".#.#.#")
    doDialogText("(Holy cornballs)")
    
    # THE GREAT MONOLOGUE
    doDialogText("ADITHYA:# Step aside,# AMIGOS.# I must make the importance of my presence well known:")
    doDialogText("As Adithya raises his hand,# the bell rings as if he summoned the voice of the bell.")
    doDialogText("ADITHYA: ==")
    doDialogText("I am simply the greatest alive. My full name is ADITHYA KRISHAN of class XI D of Devagiri High, a school that shall be blessed within my RIGHTEOUS presence and sense of justice that fails to no other, the one person alone that brings true glory and heritage and prestige to this prestigious prestige school, truly a GUARDIAN of GALAXIES, the HIGHEST standing winner from the Zero Reference Level, the one that just has the most POTENTIAL, the human that GODS worship, the lone soul that has no pair - but seeks an octet of beautiful spirits #(one that particularly starts with the letter 'A')#, the one consistent throughout all multiverses simply because he is too great to change, the LIGHT that shines even in the DARK, the GOATED engine that runs over any deer at sight, the one who donated the school theater to the school, the one that defines the mechanics of logic, the orbital with PURE s% CHARACTER, the one that BREAKS DOWN the DANCE and slows down TIME by adjusting his ROLEX wristwatch, the prophet that sees the future sitting cross-legged in his home theater, the one that is too grand to be theft-autoed by Rockstars, the Grandiose Harmony Of Perfection and Beauty, the engine that never runs out of gas-#-#-#", afterdelay=5)

    doDialogText("Adithya falls to the ground.# He passed out.")
    doDialogText("Seems like he forgot to breathe through that long ass monologue.#.#.#")
    doDialogText("SAVAN:# Oops he died again")
    doDialogText("YOU:# Does he uh.#.#.# always do that?")
    doDialogText("EARWIND:# It certainly is ADITHYA for him to do something like that,# but he's usually really chill with others.")
    doDialogText("A.R RAHMAN:# Bro are you in love with Ashish?")
    doDialogText("YOU:# Uh I-", afterdelay=0)
    doDialogText("TEACHER:# Either way you'll have to take him to the infirmary.")
    doDialogText("YOU:# Huh?")
    doDialogText("The teacher emerges out of nowhere.# You realized that the bell had already rang.")
    doDialogText("TEACHER:# What were you two doing?# Were you arguing?")
    doDialogText("YOU:# Uh no ma'am,# he just.#.#.# forgot to breathe,# I guess.")
    doDialogText("TEACHER:# .#.#.#")
    doDialogText("YOU:# .#.#.#")
    doDialogText("TEACHER:# Just carry him to the infirmary,# will ya?")
    doDialogText("YOU:# Ok ma'am.")
    doDialogText("You are now tasked to bring Adithya to the Infirmary.")
    doDialogText(".#.#.#", afterdelay=3)
    print()
    doDialogText("You are now in the Infirmary,# waiting for a nurse.")
    doDialogText("You have put Adithya on the bed.# You try to wake him up.")
    doDialogText("YOU:# Hey,# Adithya.")
    doDialogText("ADITHYA:# .#.#.#######......tthheeeeeee.#.#.# the one that never backs down, aaand never gives up:# ADITHYA KRISHAN!")
    doDialogText("YOU:# .#.#.### you're really finishing your monologue.")
    
    doDialogText("ADITHYA:# Tell me this:# are you feining for more?")
    doDialogText("YOU:# What does that mean-", afterdelay=0)
    doDialogText("ADITHYA:# I can tell the time to take perfect action,# every expected outcome.")
    print("         ", end="")
    doDialogText("I am a prophet that can predict the future,# and this was my plan all along to bring you to the infirmary.")
    doDialogText("YOU:# What?")
    doDialogText("ADITHYA:# What?# Outsmarted by my genius?# Now I can talk with you privately with stuff that would have me thrown out otherwise.")
    doDialogText("YOU:# You.#.#.# you really thought passing out in front of me was the best course of action just to talk to me privately?")
    doDialogText("ADITHYA:# Heh heh heh,# you wouldn't understand.")
    doDialogText("Adithya stands up.# He wobbles a little bit before walking over to you.")
    doDialogText("ADITHYA:# Listen,# bucko.")
    print("         ", end="")
    doDialogText("ASHISH,# is MINE.")
    doDialogText("YOU:# uh,## what?")
    doDialogText("ADITHYA:# You heard me.# Ashish is MINE.")
    print("         ", end="")
    doDialogText("He is perfectly pure.# His shy and captivating facial structure invites me to be intimate with him,# daring me to challenge his fortress of cuteness-", afterdelay=0)
    doDialogText("YOU:# Hold on.# You like ASHISH?")
    doDialogText("ADITHYA:# Of course I do.# Who wouldn't?# He's perfect.")

    if nameChoice == "NORMAL":
        doDialogText("YOU:# .#.#.#")

        surrender = doDialogChoice("ADITHYA:# I WON'T let you take Ashish.", choices=["Tell him to back off.", "Surrender Ashish."])
        if surrender == 1: # You defend Ashish
            route3["surrender"] = "DEFENDED"
            doDialogText("YOU:# Stop bothering him.")
            doDialogText("ADITHYA:# Oh,# so I'M# the one bothering him now,# hmm?")
            doDialogText("YOU:# Look,# it just looks like you're gonna be annoying as hell.# What do you even mean he's 'yours'?")
            doDialogText("ADITHYA:# I will protect ASHISH from FILTH like you.")
            doDialogText("YOU:# Why do you think I will hurt ASHISH?# Do you even know ASHISH that well?")
            doDialogText("ADITHYA:# SHUT UP.# I know ASHISH better than you do.# I know you more than you know yourself.")
            doDialogText("YOU:# I've like-# never seen you two talk either-", afterdelay=0)
        elif surrender == 2: # You... surrendered him.
            route3["surrender"] = "SURRENDER"
            doDialogText("YOU:# ...you can have him.")
            doDialogText("ADITHYA:# What?")
            doDialogText("YOU:# It's not like we're dating,# or anything.# If you really like him.#.#.# go for it.")
            doDialogText("ADITHYA:# No-# you don't get it.# I'm making him MINE so you can't reach him.")
            doDialogText("YOU:# Just go ask him out.# You don't have to keep bothering me,# I won't.#.#.# hurt him.#.#.#")
            doDialogText("ADITHYA: .#.#.####oh,# you're playing dumb.")
            doDialogText("YOU:# what-", afterdelay=0)
        doDialogText("ADITHYA:# Listen.# You can't deny it.# I KNOW you like ASHISH.")
        print("         ", end="")
        doDialogText("So from now on,# THIS IS WAR.")
        print("         ", end="")
        doDialogText("And if you get in my way.#.#.#")
        doDialogText("ADITHYA grabs your tie and tightens it up,# trying to choke you.") # PG MARKER
        doDialogText("ADITHYA:# I'll choke you out of your life.")
    elif nameChoice == "LUNATIC":
        doDialogText("YOU:# .#.#.# are you gay?")
        doDialogText("ADITHYA:# What?# No-# that's out of the question-", afterdelay=0)
        doDialogText("YOU:# oooooh is someone into ASHISH?")

        surrender = doDialogChoice("ADITHYA:# I'm just saving him from YOU.", choices=["Tell him to back off.", "Surrender Ashish."])

        if surrender == 1: # You defend Ashish
            route3["surrender"] = "DEFENDED"
            doDialogText("YOU:# Hey man,# I don't know if you're aware.#.#.# but you're being kind of a jackass right now.")
            doDialogText("ADITHYA:# I'm just saving him from YOU.")
            doDialogText("YOU:# Look,# I don't know what your problem is.# But you need to chill.# Stop being so annoying.")
            doDialogText("ADITHYA:# Oh yeah?# Who are you to talk?")
            doDialogText("YOU:# From the impression you have left on me,# I doubt ASHISH will like you as much as you want him to.")
        elif surrender == 2: # You surrendered Ashish
            route3["surrender"] = "SURRENDER"
            doDialogText("YOU:# Man,# What are you talking about!# You can just have him!")
            doDialogText("ADITHYA:# What?")
            doDialogText("YOU:# Yeah.# I don't care about him.# You can have him.")
            doDialogText("ADITHYA:# .#.#.### I can see through your lies,# y'know.# I am the prophecy of-", afterdelay=0)
            doDialogText("YOU:# We're just FRIENDS.# That's it.")
        doDialogText("ADITHYA:# Listen.# You can't deny it.# I KNOW you like ASHISH.")
        print("         ", end="")
        doDialogText("So from now on,# THIS IS WAR.")
        print("         ", end="")
        doDialogText("And if you get in my way.#.#.#")
        doDialogText("ADITHYA grabs your tie and tightens it up,# trying to choke you.") # PG MARKER
        doDialogText("ADITHYA:# I'll choke you out of your life.")
    
    elif nameChoice == "RUDE":
        doDialogText("YOU: .#.#.#Ashish.#.#.#")

        rude_choice = saveFile['route1']['rude_choice']

        if rude_choice != "APOLOGISED":
            doDialogText("YOU:# I couldn't care less,# honestly.")
            doDialogText("ADITHYA:# What?# I'm saving ASHISH from YOUR influence-",afterdelay=0)
            doDialogText("YOU:# I don't even want him.# He's kind of annoying in my opinion.")
            doDialogText("ADITHYA:# you.#.#.#")
            doDialogText("YOU:# What?# You can have him if you want.# I don't want anything to do to him.")
        else:
            surrender = doDialogChoice(".#.#.#", choices=["Tell him to back off.", "Surrender Ashish."])

            if surrender == 1: # You defended him.
                route3['surrender'] = "DEFENDED"
                doDialogText("YOU:# Hey man.#.#.# stop.")
                doDialogText("ADITHYA:# Hm?# Stop what?# Stop trying to save ASHISH?")
                doDialogText("YOU:# You're just gonna.#.#.# end up hurting him more.")
                doDialogText("ADITHYA:# Look who's talking.")
                print("         ", end="")
                doDialogText("Listen.# You can't deny it.# I KNOW you like ASHISH.")
                print("         ", end="")
                doDialogText("So from now on,# THIS IS WAR.")
                print("         ", end="")
                doDialogText("And if you get in my way.#.#.#")
                doDialogText("ADITHYA grabs your tie and tightens it up,# trying to choke you.") # PG MARKER
                doDialogText("ADITHYA:# I'll choke you out of your life.")
            elif surrender == 2: # You surrendered him.
                route3["surrender"] = "SURRENDER"
                doDialogText("YOU:# .#.#.# you can have him.")
                doDialogText("ADITHYA:# What?")
                doDialogText("YOU:# You'd probably be better off with him.")
                doDialogText("Personally,# I don't think he likes me that way.# Go for it")
                doDialogText("ADITHYA:# .#.#.#### lost hope already?# heh.")
                doDialogText("YOU:# Maybe.")
                doDialogText("ADITHYA:# You're lying. You still have feelings for him.")
                print("         ", end="")
                doDialogText(".#.#.#and I have to keep that in check,# so...#### see ya.")

    doDialogText("Adithya walks out of the infirmary.# He meets the nurse on his way out and explains that he's fine now.")
    doDialogText(".#.#.#### you re-adjust your tie and head back to class.")
    doDialogText("Adithya is talking to his friends,# or-## his FANTASY gang.")
    doDialogText("You feel like something deep is starting to brew.#.#.#", afterdelay=2)
    
    print()
    doDialogText(".#.#.# well,# school is over now.")
    doDialogText("You're walking home now.")
    doDialogText("...someone's following you again.")
    doDialogText("YOU:# Who's there?")
    doDialogText("ADITHYA:# It's just me.")
    doDialogText("YOU:# .#.#.# are you kidding me?# Why are you following me now?")
    doDialogText("ADITHYA:# Chill,# I'm just here to get groceries with a friend.")
    doDialogText("You are,# outside a grocery store.# You were hoping to also shop for groceries.")
    doDialogText("ADITHYA:# What a coincidence,# huh?")
    print("         ", end="")
    doDialogText("As if something was telling me to keep an eye on you.")
    doDialogText("TEJAS:# Bro why did you bring me here dude i swear to god i dont have any-", afterdelay=0)
    doDialogText("ADITHYA: *whispering* shhhhh you'll blow our cover.", spd=2)
    doDialogText("(.#.#.#)")
    doDialogText("ADITHYA:# Bro Dap me up-", afterdelay=0.3)
    doDialogText("Adithya reaches his arm out into the air, waiting for a dap.")
    doDialogText("Due to your code to never leave anyone hang,# you dap him up.")
    doDialogText("ADITHYA:# Nice,# dude!# Fist bump!")
    doDialogText("You also fist bump Adithya.# Something seems suspicious.")
    doDialogText("ADITHYA:# Nice!# Your fists are strong.# They could really hurt someone.#.#.#")
    print("         ", end="")
    doDialogText("Wanna see who's stronger?")
    doDialogText("YOU:# What?")
    doDialogText("ADITHYA:# You heard me.# But as you can see,# I'm shorter than you and don't have much muscle mass.")
    print("         ",end="")
    doDialogText("So to make things fair.#.#.#")
    doDialogText("ADITHYA PULLS OUT BRASS KNUCKLES.", spd=8, step=2) # PG MARKER
    doDialogText("ADITHYA:# You don't mind if I got some reinforcements,# do ya?")
    doDialogText("He's trying to fight you.#.#.?")
    doDialogText("TEJAS:# BRO!")
    doDialogText("YOU:# A-#Are you serious?")
    doDialogText("ADITHYA:# Don't worry dude,# you'll be fine.# Though,# I am known for being unusually fast.")
    
    if nameChoice != "RUDE":
        doDialogText("YOU:# I am NOT going to fight you,# no thanks,# goodbye.")
        doDialogText("ADITHYA:# No need to play the hero,# lil bro.")
        print("         ", end="")
        doDialogText("Plus,# you sure you don't need your groceries?")
        doDialogText("(Shoot that's right,# I need the groceries badly.)")
        doDialogText("You stand there clenching your fist,# not knowing what to do.")
        doDialogText("ADITHYA:# Thought so.# Heh.### Hey, we're ENEMIES,# right?# I just wanna see how strong my opps are.")
        doDialogText("YOU: You're insane.", spd=5) # START FIGHT
    else:
        doDialogText("YOU:# .#.#.#you really wanna fight me?")
        doDialogText("ADITHYA:# Yep.# Let's see what you got.")
        doDialogText("YOU:# I'll see the same thing about you.") # START FIGHT
    
    doDialogText("- - - - - - - - - - - - - - -", afterdelay=0)
    doDialogText("  ADITHYA IS CHARGING AT YOU!", afterdelay=0)
    doDialogText("- - - - - - - - - - - - - - -", afterdelay=0)

    doDialogSlow("As his first brass swing approaches you, you feel like time itself slows down around you.", add=1.026)
    doDialogText("(Can I dodge it?)")

    # WAVE 1
    f1 = doTimedAttack(3, 1, 1.6)
    if f1 == 0:
        doDialogText("You couldn't move in time.# You got brass-punched in the face hard") # PG MARKER
        doDialogText("ADITHYA:# You suck,# idiot.# Try and dodge this")
    elif f1 >= 0 and f1 < 0.3:
        doDialogText("You BARELY missed his attack.# His brass knuckles nicked your face.") # PG MARKER
        doDialogText("ADITHYA:# Wow,# you got lucky.# Let's see if that luck lasts.")
    elif f1 >= 0.3 and f1 < 0.6:
        doDialogText("You dodged his attack.# You didn't get scratched.")
        doDialogText("ADITHYA:# Not bad.# Now try and dodge this:")
    elif f1 >= 0.6 and f1 < 0.8:
        doDialogText("You nimbly dodged his attack.# You didn't even get scratched.")
        doDialogText("ADITHYA:# Not bad.# Not bad at all.")
    elif f1 >= 0.8 and f1 < 0.9:
        doDialogText("You expertly dodged his attack.# You didn't even get scratched.")
        doDialogText("ADITHYA:# Whoa.# You're good at this.# This means I can go harder,# right?")
    else:
        doDialogText("|| CATCH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You caught his hand mid punch.")
        doDialogText("ADITHYA:# .#.#.#")
        doDialogText("He pulls his hands back.")
    doDialogText("(Get ready for a fight!)")
    doDialogText("TUTORIAL:", afterdelay=0.3)
    doDialogText("You are entering a FIGHT scene. FIGHTING has THREE Mechanics:", spd=3)
    doDialogText("1) Combo:# Press ENTER key as fast as you can,# but only specified number of times,# otherwise you'll be flagged as spamming and suffer an accuracy reduction of 70%.", spd=3)
    doDialogText("2) Question:# A simple math problem will be asked, requiring a numreic answer.# Answer under a time limit, and accuracy will be granted as long as the answer is within a broad range of error.", spd=3)
    doDialogText("3) Spam:# Similar to combo,# except you spam the enter key. Be careful as you approach the end,# because at the end if it detects spamming then you suffer an accuracy reduction of 80%.", spd=3)
    doDialogSlow("Good luck. Now get ready to fight!", add = 1/1.07, spd=12)
    print()

    nameChoice = saveFile['route1']['name_choice']

    doDialogText("DODGE HIS SWINGS!", spd= 2, step=2, afterdelay=0.3)
    f2 = doTimedAttack(5, 3, 1.3)
    if f2 == 0:
        doDialogText("|| SMACK! 3x ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You got wiped with the swings.")
    elif f2 >= 0 and f2 < 0.3:
        doDialogText("|| SWOOSH! SMACK! ||", step=2, spd=10)
        doDialogText("You BARELY missed his swings.")
    elif f2 >= 0.3 and f2 < 0.6:
        doDialogText("|| SWISH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You quickly jump backwards and dodge him.")
    elif f2 >= 0.6 and f2 < 0.8:
        doDialogText("|| SWISH! SWOSH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You smoothly avoid all his swings.")
    elif f2 >= 0.8 and f2 < 0.9:
        doDialogText("|| SWISH! SWOSH! DODGE! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You expertly dodged his swings.")
    else:
        doDialogText("|| CATCH! 3x ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You knocked off each of his swings by hand.")

    print()
    doDialogText("DODGE HIS RIGHT HOOK! ANSWER THE FOLLOWING QUESTION:", spd= 2, step=2, afterdelay=1)

    f3 = doTimedQuestion("WHAT IS 10 + 8", 18, 5, 4)

    if f3 == 0:
        doDialogText("|| CRASH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("Your face crashed into his right hook.")
    elif f3 >= 0 and f3 < 0.3:
        doDialogText("You slightly got hit by his right hook.")
    elif f3 >= 0.3 and f3 < 0.6:
        doDialogText("|| SWISH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You dodged his right hook.# He stumbles onto the ground.# Now's your chance to land a blow!")
    elif f3 >= 0.6 and f3 < 0.8:
        doDialogText("|| SWOOSH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You calmly yet swiftly dodged his right hook.# He stumbles onto the ground.# Now's your chance to land a blow!")
    elif f3 >= 0.8 and f3 < 0.9:
        doDialogText("|| SWOOSH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You ducked under his right hook.# He stumbles onto the ground.# Now's your chance to land a blow!")
    else:
        doDialogText("|| SWOOSH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You ducked under his right hook and landed a punch on his gut.# ADITHYA moves out of the way,# but still slightly bears the impact.")
        doDialogText("ADITHYA:# That was close.") # PG MARKER

    print()
    doDialogText("LAND A PUNCH ON HIM!", spd= 2, step=2, afterdelay=0.3)
    f4 = doTimedAttack(3, 2, 2.5)

    aditHp = 3

    aditHp -= f4
    if f4 == 0:
        doDialogText("|| GUH!! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You tried to land a punch,# but was too slow and ADITHYA dodged it easily.")
    elif f4 >= 0 and f4 < 0.3:
        doDialogText("|| PUNCH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You barely punched Adithya.")
    elif f4 >= 0.3 and f4 < 0.6:
        doDialogText("|| PUNCH! 2x ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You landed two small punches on Adithya.")
    elif f4 >= 0.6 and f4 < 0.8:
        doDialogText("|| PUNCH! 2x ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You landed two good punches on Adithya.# He jolts back a bit.")
    elif f4 >= 0.8 and f4 < 0.9:
        doDialogText("|| PUNCH! 2x ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You landed a strong punch on Adithya.# He almost wobbles over.")
    else:
        doDialogText("|| HIT! 2x ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You landed two PERFECT punches on Adithya.# He falls over.")
        doDialogText("He gets back up after groaning a little.") # PG MARKER

    print()
    doDialogText("ADITHYA LAUNCHES TOWARDS YOU!", spd= 2, step=2, afterdelay=0.3)
    f5 = doTimedQuestion("WHAT IS 12 + 15", 27, 8, 3)

    aditHp -= f5
    if f5 == 0:
        doDialogText("|| CRASH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You got hit by Adithya's tackle.# He stabs his knucles into your stomach.") # PG MARKER
        doDialogText("He brings you both to the ground.# QUICK,# ATTACK HIM!")
    elif f5 >= 0 and f5 < 0.3:
        doDialogText("Adithya still slightly tackles you.# He trips and falls to the ground.# Now's your chance")
    elif f5 >= 0.3 and f5 < 0.6:
        doDialogText("|| SWOOSH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You roughly avoided Adithya's tackle.# He trips and falls to the ground.# Now's your chance")
    elif f5 >= 0.6 and f5 < 0.8:
        doDialogText("|| SWOOSH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You smoothly avoided Adithya's tackle.# He trips and falls to the ground.# Now's your chance")
    elif f5 >= 0.8 and f5 < 0.9:
        doDialogText("|| SWOOSH! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You dodged his tackle and grabbed his arm.# You try to throw him to the ground,# but he shakes you off and falls over.")
        doDialogText("NOWS YOUR CHANCE!")
    else:
        doDialogText("|| SWOOSH! THROW! ||", step=2, spd=10, afterdelay=0.1)
        doDialogText("You dodged his tackle and grabbed his arm.# You threw him to the ground.# He groans in pain.") # PG MARKER
        doDialogText("ADITHYA:# Ugh.# You're really good at this.# I underestimated you.")
        doDialogText("NOWS YOUR CHANCE!")

    f6 = doTimedSpam(30)
    aditHp -= f6

    if f6 >= 0 and f6 <= 0.6:
        doDialogText("Through your best efforts,# you land a number of punches on Adithya.")
    elif f6 > 0.6 and f6 < 1:
        doDialogText("You drill into his body with your punches.# He can't keep up with every punch.")
    else:
        doDialogText("You unleash a fury of punches on Adithya's body.# He looks like he's in a lot of pain.")

    doDialogText("TEJAS:# BRO!")
    print()
    # NOW TEJAS' TURN
    if f6 > 0.6:
        doDialogText("ADITHYA:# ughhh.#.#.# okay.")
    else:
        doDialogText("ADITHYA:# He has me beat.#.#.# HE HAS ME BEAT.#")
    print("         ", end="")
    doDialogText("what do i do what do i do what do i do", spd=2)
    
    if nameChoice != "RUDE":
        doDialogText("YOU: Guess I really am stronger,# huh?")
        print("     ", end="")
        doDialogText("So this is the end of it.")
    else:
        doDialogText("YOU:# Heh,# I guess I haven't lost my touch from the school fights I got into.")
    
    doDialogText("TEJAS:# Bro.#.#.#")
    print("       ", end="")
    doDialogText("If you're gonna borrow my brass-knuckles without asking,# atleast use them right.# I'll show you.") # PG MARKER
    doDialogText("TEJAS quickly takes back his brass-knuckles from Adithya.") # PG MARKER
    doDialogText("TEJAS:# Sorry bro,# I don't have anything with you,# but this guy said he really needs to learn to use it,# and personally.#.#.# I don't really like how you violated this guy.")
    print("       ", end="")
    doDialogText("No hard feelings,# okay?# I just need to show him how it's done.")
    doDialogText("(What is he doing-)", afterdelay=0)
    doDialogText("|| Hit. ||", spd=5, step=2)
    doDialogText("|| Hit. ||", spd=5, step=2) # PG MARKER?
    doDialogText("|| Hit. ||", spd=5, step=2)
    doDialogText("Suddenly,# everything went black.")
    doDialogText("You feel a sharp pain in the right side of your head.")
    doDialogText("You open your eyes .# You're on the ground now.")
    doDialogText("(Did he do this?)")
    doDialogText("You try to stand up,# but suddenly the whole world is spinning.")
    doDialogText("|| HIT. ||", spd=6, step=2, afterdelay=0)
    doDialogText("|| HIT. ||", spd=6, step=2, afterdelay=0.1)
    doDialogText("|| HIT. ||", spd=6, step=2, afterdelay=0.14) # PG MARKER?
    doDialogText("|| HIT. ||", spd=6, step=2, afterdelay=0.5)
    doDialogText("TEJAS is beating the crap out of you.")
    doDialogText("|| UPPERCUT ||", spd=7, step=2, afterdelay=1)

    doDialogText("BLOCK HIS ATTACK?!", spd=5, step=2, afterdelay=1.3)
    doTimedAttack(7, 1, 4)
    doDialogText("|| Crack. ||", spd=8, step=3)
    doDialogText("Your block had no effect.# TEJAS broke your wrist.") # PG MARKER

    doDialogText("TEJAS IS POWERING A POWERFUL KNOCKOUT?! DO YOUR BEST TO BLOCK IT!", spd=5, step=1.5, afterdelay=2.3)

    fBlock = doTimedQuestion("JW Workbook, Chapter 6, 8: A force (4i + 3j) displaces a body over displacement (3i + 4j) metre. The work done is:^ 1) 12J,# 2) 16J,# 3) 24J,# 4) 14J", 3, 0, 30)
    # PG MARKER BUT MAKE THIS QUESTION DOABLE FOR YOUNGER AUDIENCES
    if fBlock > 0:
        doDialogText("You can't block it.# Instead,# you move out of the way.")
        doDialogText("TEJAS catches you stumbling for balance,# and ends the fight with a small kick that sends you falling to the ground.")
    else:
        doDialogText("You were too dizzy.# TEJAS knocks your forehead out of your skull,# and you fall to the ground.") # PG MARKER
    
    doDialogText("(Too...# strong...)", spd=5)
    doDialogText("As you're about to pass out,# TEJAS is squatting down to your face.")
    doDialogText("TEJAS:# Sorry bro,# I'll patch up your wounds.")

    print()
    doDialogText(".#.#.#", afterdelay=3)
    print()
    doDialogText("\"Hello?# Wake up please.#.#.#\"")
    doDialogText("\"Hey!# Wake up!\"")
    doDialogText("ASHISH:# WAKE UP!")
    doDialogText("(It's.#.#.# Ashish.)")


    skipChapter4 = 0
    if nameChoice == "NORMAL" or (nameChoice == "RUDE" and saveFile['route1']['rude_choice'] == "APOLOGISED"):
        doDialogText("ASHISH:# What the heck happened to you?!?!# Why are you so beat up?!# Why do you have bandages on your head?!")
        doDialogText("YOU:# .#.#.#Ashish?# What are you doing here?")
        doDialogText("ASHISH:# I SHOULD BE ASKING YOU THAT!")
        print("        ", end="")
        doDialogText(".#.#.# s-#sorry for y-#yelling.")
        doDialogText("You look around.# You're still outside the grocery store.# It's late evening.")
        doDialogText("There are bandages on your head.")
        if f3 == 0: doDialogText("Your nose is broken.") # PG MARKER
        doDialogText("YOU:# Right.#.#.# I was grocery shopping,# when.#.#.")
        doDialogText("ASHISH:# I can't leave you like this! Come over to my house,# I will treat you.")
        doDialogText("YOU:# No i-#it's fine!# I'm alright-", afterdelay=0, spd=6)
        doDialogText("ASHISH: NO YOU'RE NOT!# You're coming with me.# I have the groceries.# Do the explaining part after we reach my house.")
        doDialogText("Ashish helps you up.")
        doDialogText("You try to object,# but Ashish still drags you to his house.")
        print()

        doDialogText(".#.#.# you're at his house now.# It's a nice house.")
        doDialogText("Ashish's mother is surprised looking at your injured face.# Ashish explains he found you beside the grocery store beaten up, and brought you home to treat you.")
        doDialogText("Him and his mother help clean up your face and take care of you.")
        doDialogText("Now you're in ASHISH's room.")
        doDialogText("ASHISH:# .#.#.# Explain.")
        doDialogText("You explain the whole thing to ASHISH, how ADITHYA and TEJAS jumped you, and the aftermath.")
        doDialogText("ASHISH:# .#.#.# I know that guy.")
        doDialogText("YOU:# He said he was your childhood best friend?")
        doDialogText("ASHISH:# ...yes?# I've known him for like a year or something,# but he claims he remembers me from 5th grade.")
        print("        ", end="")
        doDialogText("He knew a lot about me though,# so I just assumed I had forgotten him.")
        doDialogText("YOU:# Kinda suspicious.#.#.#")
        doDialogText("ASHISH:# Yeah.#.#.#")
        doDialogText("YOU:# .#.#.#")
        doDialogText("ASHISH:# D-#D-#Do you wanna stay over tonight?")
        doDialogText("YOU:# H-#Huh?")
        doDialogText("ASHISH:# Look,# you're really badly hurt.# I don't know if you can go home safely now.# Are your parents home?")
        doDialogText("Your parents are indeed not home.# You went to buy groceries because you needed to cook for yourself without your parents.# They're on a work related trip.")
        doDialogText("YOU:# I-#I uh.#.#.#")
        doDialogText("ASHISH:# I-#I mean.#.#.# if you really don't want to.#.#.")
        doDialogText("YOU:# Alright.")
        doDialogText("ASHISH:# R-#Really?")
        doDialogText("YOU:# Yeah,# my parents aren't home today,# so I guess s-#staying here beats having to take care of myself.")
        print("     ", end="")
        doDialogText("Ofcourse,# I can help,# since I'm staying here-", afterdelay=0)
        doDialogText("ASHISH:# You're in no condition to help.# Just let us handle it.# Y-#You can stay here then.")
        doDialogText(".#.#.# You are now sleeping over at ASHISH's.", afterdelay=3)
        print()

        doDialogText("Dinner was great.# Ashish's mom can really cook well.# ^Though you're not sure if this was what they had for dinner everyday,# or was the \"Guests are here\" type of dinner.")
        doDialogText("You think it's the latter.")
        doDialogText("The whole dinner thing was awkward.#.#.# Ashish's dad didn't really talk much,# while his mother was terrorist-level bombing us with questions.")
        print()
        doDialogText("After dinner,# it's time to sleep.")
        doDialogText("Ashish moves a spare bed into his room for you to sleep on.")
        doDialogText("Once you settle in the bed,# you share an awkward silence.")
        doDialogText("YOU:# .#.#.#did you see the meme I sent you?")
        doDialogText("ASHISH:# Yes.#.#.# It was kinda funny ngl")
        doDialogText("YOU:# I see.#.#.#")
        doDialogText("ASHISH:# .#.#.#")
        doDialogText("YOU:# Why didn't you come to school today?")
        doDialogText("ASHISH:# U-#Uhm.#.#.#")
        doDialogText("YOU: ...?")
        doDialogText("ASHISH:# uhh.#.#.# I woke up pretty late,# haha.#.#.#")
        doDialogText("YOU:# Oh.# I thought you might be sick or something.")
        doDialogText("ASHISH:# N-#Nono,# I'm fine.", spd=3)
        doDialogText("YOU:# Glad to hear.")
        doDialogText("ASHISH:# .#.#.# you think.#.#.#")
        print("        ", end="")
        doDialogText("Next sleepover,# we can have more fun?")
        doDialogText("YOU:# ......##")
        print("     ", end="")
        doDialogText("Sure.# I'll bring UNO.")
        doDialogText("ASHISH:# Bet.", afterdelay=3)
        print()



    elif nameChoice == "LUNATIC":
        doDialogText("ASHISH:# What the heck happened to you?!?!# Why are you so beat up?!# Why do you have bandages on your head?!")
        doDialogText("YOU:# .#.#.#Ashish?# What are you doing here?")
        doDialogText("ASHISH:# What'd you get yourself into?!")
        doDialogText("You look around.# You're still outside the grocery store.# It's late evening.")
        doDialogText("There are bandages on your head.")
        if f3 == 0: doDialogText("Your nose is broken.")
        doDialogText("YOU:# Right.#.#.# I was grocery shopping,# when.#.#.")
        doDialogText("ASHISH:# I can't leave you like this! Come over to my house,# I will treat you.")
        doDialogText("YOU:# No i-#it's fine!# I'm alright-", afterdelay=0, spd=6)
        doDialogText("ASHISH: Dude,# you're really badly injured. I am TAKING you to my house.")
        doDialogText("Ashish helps you up.")
        doDialogText("You try to object,# but Ashish still drags you to his house.")
        print()

        doDialogText(".#.#.# you're at his house now.# It's a nice house.")
        doDialogText("Ashish's mother is surprised looking at your injured face.# Ashish explains he found you beside the grocery store beaten up, and brought you home to treat you.")
        doDialogText("Him and his mother help clean up your face and take care of you.")
        doDialogText("Now you're in ASHISH's room.")
        doDialogText("ASHISH:# .#.#.# So,# start explaining.")
        doDialogText("You explain the whole thing to ASHISH, how ADITHYA and TEJAS jumped you, and the aftermath.")
        doDialogText("ASHISH:# .#.#.# I know that guy.")
        doDialogText("YOU:# He said he was your childhood best friend?")
        doDialogText("ASHISH:# ...yes?# I've known him for like a year or something,# but he claims he remembers me from 5th grade.")
        print("        ", end="")
        doDialogText("He knew a lot about me though,# so I just assumed I had forgotten him.")
        doDialogText("YOU:# Kinda suspicious.#.#.#")
        doDialogText("ASHISH:# Yeah.#.#.#")
        doDialogText("YOU:# .#.#.#")
        doDialogText("ASHISH:# Do you think.#.#.# you can stay over tonight?")
        doDialogText("YOU:# H-#Huh?")
        doDialogText("ASHISH:# Look,# you're really badly hurt.# I don't know if you can go home safely now.# Are your parents home?")
        doDialogText("Your parents are indeed not home.# You went to buy groceries because you needed to cook for yourself without your parents.# They're on a work related trip.")
        doDialogText("YOU:# I-#I uh.#.#.#")
        doDialogText("ASHISH:# I-#I mean.#.#.# if you really don't want to.#.#.")
        doDialogText("YOU:# Alright.")
        doDialogText("ASHISH:# Really?# Are your parents fine with that?")
        doDialogText("YOU:# Yeah,# my parents aren't home today,# so I guess staying here beats having to take care of myself.")
        print("     ", end="")
        doDialogText("Ofcourse,# I can help,# since I'm staying here-", afterdelay=0)
        doDialogText("ASHISH:# You're in no condition to help.# Just let us handle it.# Y-#You can stay here then.")
        doDialogText(".#.#.# You are now sleeping over at ASHISH's.", afterdelay=3)
        print()

        doDialogText("Dinner was great.# Ashish's mom can really cook well.# ^Though you're not sure if this was what they had for dinner everyday,# or was the \"Guests are here\" type of dinner.")
        doDialogText("You think it's the latter.")
        doDialogText("The whole dinner thing was awkward.#.#.# Ashish's dad didn't really talk much,# while his mother was terrorist-level bombing us with questions.")
        print()
        doDialogText("After dinner,# it's time to sleep.")
        doDialogText("Ashish moves a spare bed into his room for you to sleep on.")
        doDialogText("Once you settle in the bed,# you share an awkward silence.")
        doDialogText("YOU:# .#.#.#did you see the meme I sent you?")
        doDialogText("ASHISH:# Yes.#.#.# It was kinda funny ngl")
        doDialogText("YOU:# I see.#.#.#")
        doDialogText("ASHISH:# .#.#.#")
        doDialogText("YOU:# Why didn't you come to school today?")
        doDialogText("ASHISH:# U-#Uhm.#.#.#")
        doDialogText("YOU: ...?")
        doDialogText("ASHISH:# uhh.#.#.# I woke up pretty late,# haha.#.#.#")
        doDialogText("YOU:# Oh.#.#.# sleepyhead.")
        doDialogText("ASHISH:# .#.#.#")
        doDialogText("YOU:# Next sleepover,# I'll bring UNO.")
        doDialogText("ASHISH:# Bet.", afterdelay=3)
        print()


    else: # YOU WERE REALLY RUDE TO HIM
        doDialogText("ASHISH:# What happened to you?")
        doDialogText("YOU:# .#.#.#")
        doDialogText("ASHISH:# Did you get into a fight?")
        doDialogText("You look around.# You're still outside the grocery store.# It's late evening.")
        doDialogText("There are bandages on your head.")
        if f3 == 0: doDialogText("Your nose is broken.")
        doDialogText("YOU:# Right.#.#.#")
        doDialogText("ASHISH:# sigh.#.#.# come over to my house,# I will treat you.")
        doDialogText("YOU:# What,# No-# I'm alright-", afterdelay=0, spd=6)
        doDialogText("ASHISH: Dude,# you're really badly injured. I am TAKING you to my house.")
        doDialogText("Ashish helps you up.")
        doDialogText("You try to break free,# but you're too weak to fight.")
        print()

        doDialogText(".#.#.# well,# you're at his house now.# It's a nice house.")
        doDialogText("Ashish's mother is surprised looking at your injured face.# Ashish explains he found you beside the grocery store beaten up, and brought you home to treat you.")
        doDialogText("Him and his mother help clean up your face and take care of you.")
        doDialogText("Now you're in ASHISH's room.")
        doDialogText("ASHISH:# .#.#.# So,# what happened to you.")
        doDialogText("YOU:# Your stupid friend beat the shit out of me.")
        doDialogText("ASHISH:# Which.#.#.# friend?")
        doDialogText("YOU:# Well technically not him,# but his other friend.# The guy's name is Adithya Krishan or something.")
        doDialogText("ASHISH:# .#.#.# I know that guy.")
        doDialogText("YOU:# He said he was your childhood best friend?")
        doDialogText("ASHISH:# ...yes?# I've known him for like a year or something,# but he claims he remembers me from 5th grade.")
        print("        ", end="")
        doDialogText("He knew a lot about me though,# so I just assumed I had forgotten him.")
        doDialogText("YOU:# Sounds like a creep.")
        doDialogText("ASHISH:# .#.#.#")
        doDialogText("YOU:# .#.#.#")
        doDialogText("ASHISH:# .#.#.# I'll let you stay over tonight.# I know for some reason, you don't really like me,# but I'm willing to put that aside and try again.")
        doDialogText("YOU:# H-#Huh?")
        doDialogText("ASHISH:# Look,# you're really badly hurt.# I don't know if you can go home safely now.# Are your parents home?")
        doDialogText("Your parents are indeed not home.# You went to buy groceries because you needed to cook for yourself without your parents.# They're on a work related trip.")
        doDialogText("YOU:# I-#I uh.#.#.#")
        doDialogText("ASHISH:# I-#I mean.#.#.# if you really don't want to.#.#.")

        stayOver = doDialogChoice("Stay over at ASHISH's?", choices=["Stay over at his house and be nicer to him.", "Keep being stubborn and head home."])
        if stayOver == 1: # You decide to be niced to him and stay over.
            route3["rude_stay"] = "FORGIVED"
            doDialogText("YOU:# Alright.")
            doDialogText("ASHISH:# Really?# Are your parents fine with that?")
            doDialogText("YOU:# Yeah,# my parents aren't home today,# so I guess staying here beats having to take care of myself.")
            doDialogText("ASHISH:# Alright.")
            doDialogText(".#.#.# You are now sleeping over at ASHISH's.", afterdelay=3)
            print()

            doDialogText("Dinner was great.# Ashish's mom can really cook well.# ^Though you're not sure if this was what they had for dinner everyday,# or was the \"Guests are here\" type of dinner.")
            doDialogText("You think it's the latter.")
            doDialogText("The whole dinner thing was awkward.#.#.# Ashish's dad didn't really talk much,# while his mother was terrorist-level bombing us with questions.")
            print()
            doDialogText("After dinner,# it's time to sleep.")
            doDialogText("Ashish moves a spare bed into his room for you to sleep on.")
            doDialogText("Once you settle in the bed,# you share an awkward silence.")
            doDialogText("ASHISH:# .#.#.#### Goodnight.")
            print()
        else: # You're being stubborn and go back to your house.
            skipChapter4 += 1

            route3["rude_stay"] = "UNFORGIVED"
            doDialogText("YOU:# No thanks.#.#.# I'll head back home.")
            doDialogText("ASHISH:# Are you sure?")
            doDialogText("YOU:# Yes,# I'm really sure.")
            doDialogText("ASHISH:# Okay.", afterdelay=2)
            print()
            doDialogText("You head back home,# stumbling over almost every step.")
            doDialogText("After what felt like 3 hours of walking,# you get back to your home.")
            doDialogText("You feel extremely tired and feel like you could pass out any moment.")
            doDialogText("As soon as you lock the door.#.#.#", afterdelay=1.7)
            doDialogText("|| THUD. ||", step= 2, spd= 8)
            doDialogText(".#.#.# You fell asleep on the floor.")

    if skipChapter4 == 0:
        doDialogText("It's midnight.# You woke up to the sound of.#.#.# footsteps?", spd=5)
        doDialogText("With what's left of your sleepy energy,# you turn your head to look at the door.")
        doDialogText("A Static computer screen,# right next to a shadowy figure watching from the half-open door.")
        doDialogText("In the moonlight,# you see something reflecting from it:")
        doDialogText("A BLADE.", step=2, spd=7)


    # THE SAVE SHENANIGANS
    if saveFile['route3']['COMPLETED'] == True:
        doDialogText("You have already completed this chapter.# Would you like to save over your progress? (Y/N):", line=False)
        confirm = input("")

        if confirm.lower() in "n":
            doDialogText("The Game was not Saved.")
        else:
            route3["COMPLETED"] = True
 
            saveFile["route3"] = route3

            try:
                saveGame(curSaveName, saveFile)
                doDialogText("The game was saved.")
            except:
                doDialogText("There was an error in saving the game.")
    else:
        route3["COMPLETED"] = True
    
        saveFile["route3"] = route3
    
        saveGame(curSaveName, saveFile)


def start(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, stopSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful):
    doDialogText("Loading Chapter 3.#.#.#", afterdelay=3)
    print()
    chapter_3(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, stopSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful)