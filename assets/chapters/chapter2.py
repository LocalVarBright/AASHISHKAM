def chapter_2(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful):
    route2 = {
        "house_studyChoice": 0,
        "house_kitchenChoice": 0,
        "house_roomChoice": 0,
        "house_bathChoice": 0,
        "badminton_advice": 0,
        "help_debayan": 0
    }

    aahanNameList = ["aahan", "ahan", "ahaan", "aahaan"]
    
    doDialogText("CHAPTER 2:## Booze and Bruises.", spd = 25, step = 3)
    print()

    doDialogText("It's morning.# A Saturday morning.# Great idea to have school start on a Friday only for it to go back to staying at home.")
    doDialogText("Feels like you never even went to school in the first place.")

    if saveFile["route1"]["name_choice"] in ["NORMAL", "LUNATIC"]:
        doDialogText(".#.#.#then you remember him.# Ashish.")

        if saveFile["route1"]["name_choice"] == "NORMAL":
            doDialogText("That introduction was a disaster.# Regardless,# you wish you talked to him more.")
        elif saveFile["route1"]["name_choice"] == "LUNATIC":
            doDialogText("He was fun to have around.# You wish you talked to him more.")
        doDialogText("You realized you never got the chance to exchange CONTACT INFOs with Ashish.")
        doDialogText(".#.#.#")
    elif saveFile["route1"]["name_choice"] == "RUDE":
        if saveFile["route1"]["rude_choice"] == "APOLOGISED":
            doDialogText(".#.#.#then you remember him.# Ashish.")
            if saveFile["route1"]["rude_cancel"] == "CANCELLED": doDialogText("That introduction was a disaster.#.#.")
            doDialogText("You wish you got to know him more.")
    
    doDialogText("Staying at home feels boring.#.#.#")
    print()

    houseChoices = ["Study for no reason.", "Go to kitchen.", "Explore old stuff in your room.", "Take a shower.", "Practice Guitar."]
    showerCount = 0
    while houseChoices != []:
        houseChoice = doDialogChoice("Find something to do around at the house:", choices=houseChoices)

        if houseChoices[houseChoice-1] == "Study for no reason.": # Studying for no reason
            route2["house_studyChoice"] = "STUDYING"
            doDialogText("You decide to be a studious student and read the Physics textbook out of whim like a studious student.")
            doDialogText(".#.#.#you have absorbed knowledge, and now know how to find the cross product of two vectors.")

            houseChoices.remove("Study for no reason.")
        elif houseChoices[houseChoice-1] == "Go to kitchen.": # Went to the kitchen
            doDialogText("You went to the kitchen.# You open the fridge and find a piece of cake.")
            takeCake = doDialogChoice("Take the cake?", choices=["Take it.", "Leave it."])

            if takeCake == 1: # Took the cake
                doDialogText("This cake has your dad's name on it.# You take it anyways.")
                route2["house_kitchenChoice"] = "DAD CAKE"
            else:
                doDialogText("You realize the piece of cake has your dad's name on it.#.#.#")
                doDialogText("So you take your mom's dessert instead.")
                route2["house_kitchenChoice"] = "MOM CAKE"
            houseChoices.remove("Go to kitchen.")
        elif houseChoices[houseChoice-1] == "Explore old stuff in your room.": # Explore your room
            doDialogText("You explore your old room.")
            doDialogText("Your guitar is lying on the bed,# right next to where you slept.# You swear you didn't do anything to the guitar.")
            doDialogText("Oh-# you discover an old keychain you thought you had lost.# It looks kinda cool.# You hang it on your backpack.")
            doDialogText("You keep digging.#.#.# and discover several more guitar picks!# More practicing for you then..")
            doDialogText("You decide to keep digging one last time.#.#.#")
            
            cleanRoom = doDialogChoice("You start to think why not just clean up the place?", choices=["Clean your room.", "No need."])
            if cleanRoom == 1: # You clean your room
                doDialogText("You get to work.#.#.#")
                doDialogText(".#.#.#")
                print()

                doDialogText("Your room is tidier than ever.# You don't feel anything will ever go lost again.")
                doDialogText("Good job.")
                doDialogText("You also found the 300 rupees you lost the other day, and a wallet you don't recall having.#.#.#")
                doDialogText("You realize your room was such a mess before.")

                route2["house_roomChoice"] = "CLEANED"
            else: # You DONT clean your room
                doDialogText("(Nah, too much work.)")
                doDialogText("The search ended here.")

                route2["house_roomChoice"] = "NOT CLEANED"

            houseChoices.remove("Explore old stuff in your room.")
        elif houseChoices[houseChoice-1] == "Take a shower.": # You practice guitar.
            showerCount += 1
            route2["house_bathChoice"] = "SHOWERED"
            if showerCount == 1: # First shower
                doDialogText("You decide to randomly take a shower in the morning.# Nothing wrong with it,# you guess.#.#.#")
            elif showerCount == 2: # Second shower
                doDialogText("You take another shower.# You felt the first one was not as effective.# You put more effort into this shower.")
            elif showerCount == 3: # Third shower... wtf?
                doDialogText("You took a third shower.#.#.### Calm down?????")
                route2["house_bathChoice"] = "NEAT FREAK"
            elif showerCount == 4: # Fourth shower...
                doDialogText("Your mother is yelling at you to stop taking showers.")
            elif showerCount == 5: # FIFTH SHOWER?!?!
                doDialogText("You took another shower despite your mom's order.")

                if saveFile["name"] in aahanNameList:
                    doDialogText("You hear your mother yelling at you while you hum a Michael Jackson song.")
                else: doDialogText("You hear your mother yelling at you while you hum a lil shower song.")
                if saveFile["route1"]["rude_choice"] == "IGNORED":
                    doDialogText("You use your exceptional ability to ignore out people to take an extra long shower.")

                doDialogText("You have wasted water.# Enough.")

                route2["house_bathChoice"] = "NEAT MONSTER"

                houseChoices.remove("Take a shower.")
        elif houseChoices[houseChoice-1] == "Practice Guitar.": # You practice guitar.
            houseChoices = [] # Once you choose this option, you can't go back evil hehehe
            doDialogText("You decide to practice guitar.# A cool song.")
            doDialogText("#.#.#.you practice.#.#.#", afterdelay=1.6)
            doDialogText(".#.#.#you really do practice.#.#.#", afterdelay=1.6)
            doDialogText(".#.#.#you have practiced very hard.#.#.#", afterdelay=1.6)
            doDialogText(".#.#.#oh wow-# You know how to play guitar!# like you always have.#.#.#", afterdelay=1.6)
            doDialogText(".#.#.#you practiced.#.#.# for very.#.#.# long.",  afterdelay=2)
            doDialogText(".#.#.#")
            if route2["house_kitchenChoice"] == "DAD CAKE":
                doDialogText("You pass out from exhaustion...?")
                doDialogText("After you wake up, you feel hungry.")
            else:
                doDialogText("You're tired now. You decide to take a rest.")
            doDialogText("You go into the kitchen to eat.")

            if route2["house_kitchenChoice"] == "DAD CAKE":
                doDialogText("Your dad is waiting for you.")
                doDialogText("DAD:# Boy did you eat my cake?")
                doDialogText("(No use playing dumb.)")
                if pgFilter:
                    doDialogText("DAD:# Young man,# did you know,# that cake contains large amounts of alcohol?")
                    doDialogText(".#.#.# That explains why you passed out mid-practice and were singing slurs.#.#.#")
                doDialogText("DAD:# .#.#.# you're still hungry aren't you?# Eat your mom's leftover dessert then.# i dunno, i was never here.")
                print()
                
                doDialogText(".#.#.# You consumed both cake and dessert.## Yum.")
            elif route2["house_kitchenChoice"] == "MOM CAKE":

                doDialogText("Your mom notices you.")
                doDialogText("MOM:# You ate my leftover dessert,# didn't you?")
                doDialogText("(No use denying it.)")
                doDialogText("MOM:# What?# Are you still hungry?")
                doDialogText("You nod sheepishly.")
                doDialogText("MOM: Bruh.# No more cake for you.# Wait here, I'll make you dinner.")
                doDialogText("You consumed your mother's cooking.")
                doDialogText("She cooked.## Hard.")
                doDialogText("Too hard.# She burnt your food.")
                doDialogText("Seems like that was a message.# Don't mess with her again.")
            else:
                doDialogText("Your mother is preparing dinner, and your dad is taking his cake outside with him.")
                doDialogText("DAD:# I'm gonna go to a work event,# and share these cakes.")
                doDialogText("DAD:# Heh, good thing no one ate them,# because they contain a lot of alcohol.")
                doDialogText(".#.#.#")
                doDialogText("You might have dodged a small bullet.")
                print()

                doDialogText("Dinner was...# yum.# She almost burnt the food,# but it's still fine.")

            doDialogText("You have eaten dinner now.# Now you feel sleepy.")
            if route2["house_kitchenChoice"] == "DAD CAKE": doDialogText("Maybe the effects of cake still linger.")
            doDialogText("You decide to go to bed.")
            doDialogText(".#.#.#")

            if saveFile["route1"]["name_choice"] in ["NORMAL","LUNATIC"] or saveFile["route1"]["rude_choice"] == "APOLOGISED":
                doDialogText("You still think about Ashish.")
                doDialogText("You start thinking about texting him at night,# sharing memes and talking to each other.")
                doDialogText("You quickly snap out of it and try to get some sleep-", afterdelay = 0.3)
                doDialogText("But the thought lingers.#.#.#")
                print()

                doDialogText(".#.#.#")
                doDialogText("you start...# to doze off...#",afterdelay=3)

    doDialogText(".#.#.#it's morning.")
    doDialogText("A classic sunday morning,# waking up at 11 AM.")
    doDialogText("A nice refreshing break from what you feel is gonna be your sleep schedule once school really starts.")
    doDialogText(".#.#.#")
    print()

    doDialogText("You're going to watch a movie with your mom today.# Good luck with that.")
    print()
    if saveFile["route2"]["COMPLETED"] == False:
        doDialogText("""INSERT SHAMELESSLY INSERTED AD BREAK ABOUT MOVIES:###
MMM,# MOVIES.# A WONDERFUL PIECE OF MEDIA INVENTED BY HUMANS.###
HEY,# YOU!# THAT'S RIGHT!# YOU,# THE ONE PLAYING THIS GAME!###
HAVE YOU EVER WATCHED.#.#.# A MOVIE?###
YEAH?# YEAH?!###
YEEEEAAAAHHHHHH?!?!?!?!##??!######
.#.#.#
NOW TELL ME.#.#.#
.##.##.#""", step=3, spd=8)

        doDialogText("Have you ever watched a real movie?", spd=6)
        print("\n")
        doDialogText("Perhaps yes,# perhaps no.")
        doDialogText("Perhaps you do not know what I-", afterdelay=0.3, line=False)
        doDialogText("no,# WE mean,## by# a### real### MOVIE#.")
        doDialogText("In case you don't.#.#.#")
        print("\n\n")
        doDialogText("We're watching you.", afterdelay=3, spd=8)
        doDialogText("And let me warn you:")

        if saveFile["route1"]["name_choice"] == "NORMAL":
            doDialogText("You will soon encounter someone you must stop in their tracks.#.#.# or ASHISH.#.#.#.#.###")
        elif saveFile["route1"]["name_choice"] == "LUNATIC":
            doDialogText("You don't have a choice anymore.")
        elif saveFile["route1"]["name_choice"] == "RUDE":
            if saveFile["route1"]["rude_choice"] == "IGNORED":
                doDialogText("You have steered away from the treasure.")
            elif saveFile["route1"]["rude_choice"] == "APOLOGISED":
                doDialogText("You have a chance to fix your mistakes.# Don't blow it.")
            elif saveFile["route1"]["rude_choice"] == "RUDENAME":
                doDialogText("You have broken a heart you can't fix anymore.")

        print("\n")
        doDialogText(".##.##.###that advertisement was weird.")

    print()
    doDialogText("It's the second day of school now.# Actual stuff is being taken now.")

    if route2["house_studyChoice"] == "STUDYING":
        doDialogText("Well,# because you read that physics textbook, you're slightly ahead on physics.# Good for you.")
        doDialogText("You can intently keep up with physics class.")
    if saveFile["route1"]["name_choice"] != "RUDE" or (saveFile["route1"]["name_choice"] == "APOLOGISED"):
        doDialogText("You look over to Ashish, who's keen and focused on the teacher.# He seems like he knows his stuff.")
        if saveFile["route1"]["name_choice"] == "LUNATIC": doDialogText("(Smartass.)")

    doDialogText(".#.#.#")
    doDialogText("It seems you got blessed with PE on the second day of school.")
    doDialogText("The PE teacher has walked into the class.")
    doDialogText("PE TEACHER:# HELLO CLASS,# I AM YOUR PE TEACHER.")
    doDialogText("He commands like a military seargant.")
    doDialogText("You head to the ground along with the other classmates in an awfully straight line.#.#.# rare.")
    doDialogText("As per standard procedure, you do the laps around the ground before getting started with any activity.")
    doDialogText("People are arranging into groups to play different games.")
    doDialogText("Some are in for FOOTBALL, other ballers are going for BASKETBALL.#.#.#")
    doDialogText("You decide you're not ready for those yet so you play Badminton instead.")

    print()

    # BADMINTON SCENE
    if saveFile["route1"]["name_choice"] == "NORMAL": # You find AASHISH and play Badminton with him.
        doDialogText("You noticed Ashish near the stairs.")
        doDialogText("He's waiting by the stairs to grab the rackets.# You decide to approach him.")
        doDialogText("As you walk near him,# he starts waving at you.")
        doDialogText(f"ASHISH:# Hey, {saveFile['name']}!# Wanted to play Badminton with me?")
        doDialogText("YOU:# Uh,# sure!# You got the rackets?")
        doDialogText("ASHISH:# Uh no, still waiting to get in.# These kids wanted to take basketballs.")
        print()
        doDialogText("You and Ashish find a spot to play Badminton.")
        doDialogText("As you two start playing,# you start noticing that he is.#.#.# not very good at it.")
        doDialogText("But still,# he tries very hard and barely keeps up with you.")
        advice = doDialogChoice("Give him advice?", choices=["Help Ashish.", "Don't give him advice."])

        route2["badminton_advice"] = ["ADVICED", "NOT ADVICED"][advice-1]

        if advice == 1: # You give him advice
            doDialogText("YOU:# Hey Ashish!# Do you need any help?")
            doDialogText("ASHISH:# No thanks! I'm good!")
            doDialogText("YOU:## No you aren't! Look-#", afterdelay = 0)
            print("     ", end="")
            doDialogText("You're holding the racket like this,# and way too tight.# You'll never be able to move fast and use your strength.")
            doDialogText("ASHISH:# O-#oh,# really?")
            doDialogText("YOU:# Instead,# hold it like this-", afterdelay=0.3)
            doDialogText("You hold Ashish's hand to show him how to hold the racket,# and give him tips on swinging.")
            if pgFilter:
                doDialogText("As you're explaining to him,# you catch him blushing.")
                doDialogText("YOU: -#OH- oh sorry about that.#.# my bad.")
                doDialogText("ASHISH:# No worries, i-#its fine.")
                print("        ", end="")
                doDialogText("But thanks for giving me advice. Let's see how much better I can get!")
            else:
                doDialogText("ASHISH:# Oh,# okay.# Thanks for giving me advice.# Let's see how much better I can get!")
            doDialogText("You notice that he has gotten slightly better,# and is now able to play properly.")
            doDialogText("He's still getting used to playing this way,# but he's getting the hang of it.")
            if pgFilter:
                doDialogText("He's hitting his shots with lots of confidence and charisma,# such you can't help but look at.")
                doDialogText("You can't help but get lost in his amazing grace.#.#.#")
            else:
                doDialogText("Eventually,# you get a little tired.")
            doDialogText(f"ASHISH:# Hey, {saveFile['name']}! Are you alright?")
            doDialogText("YOU: Huh oh-# YEAH I'm fine! Just got a little distracted.")
            doDialogText("(Can't be caught lacking now.)")

            doDialogText("Soon,# you two get tired and decide to rest somewhere.")
            doDialogText("ASHISH:# Thanks for giving me advice! Playing Badminton feels a lot more fun ,# and now I'm hitting more shots!")
            doDialogText("YOU:# No problem,# just helping a friend in need.")
            doDialogText("ASHISH:# U-#uh,# yeah.#.#.#")
            if pgFilter:
                doDialogText("He looks down slightly.#.#.#")
                doDialogText("(Is he starting to blush?")
                doDialogText("YOU:# Uh,# everything okay-", afterdelay=0.2)
            doDialogText("YOU:# Anyways-", afterdelay=0.2)
        else:
            doDialogText("You decide not to give him advice and let him get better on his own.# He'd learn better that way,# right?")
            doDialogText("He continues to struggle slightly,# but is getting better with each shot.")
            doDialogText("Watching him push through to try and keep up with you,# staying determined.#.#.#")
            if pgFilter: doDialogText("You can't help but get lost in his.#.#.#")
            doDialogText(f"ASHISH:# Uhm,# {saveFile['name']}?# You alright?")
            doDialogText("YOU:# Uh,# Yeah!# I'm alright,# just got a little distracted.")
            doDialogText("ASHISH:# Oh,# okay!# Well you just missed that shot.")
            doDialogText("YOU:# Yeah,# got a little tired.")
            doDialogText("(Can't be caught lacking.)")
            doDialogText("Soon,# you two get tired and decide to rest somewhere.")
            doDialogText("ASHISH:# Sorry if my game was off.#.#.# I'm not the best at badminton.")
            doDialogText("YOU:# That's alright,# everyone has their own skill.")
            doDialogText("ASHISH:# Yeah.#.#.#")
            doDialogText("He looks down slightly.#.#.#")
            doDialogText("YOU:# Hey,# is everything okay-", afterdelay=0.2)
        doDialogText("\"WAAAAATTCHH OOOUUUUUUUTT!!!!!!\"", step=3, spd=6)
        doDialogText("There's a football flying towards you!# You reach your racket out in front of Ashish to maybe try and deflect it-")
        doDialogText("|| SSMACKK! ||", step=2, spd=10)
        doDialogText("The ball hit you instead.#.#.#")
        doDialogText("ASHISH:# OH-# A-ARE YOU OKAY?!")
        doDialogText("YOU:# Ugh,# yeah I'm fine.")
        doDialogText("ASHISH:# Why did you protect me?!# The ball was coming towards you!")
        doDialogText("YOU: Sorry,# I thought it was going towards you.# I'm fine tho, no need to worry.")
        doDialogText("ASHISH:# B-#but thanks for protecting me though.#.#.#")
        if pgFilter: doDialogText("(He's being cute again.)")
        doDialogText("YOU:# N-#No problem!")
        print() # GO TO PE END SCENE
    
    elif saveFile["route1"]["name_choice"] == "RUDE": # You were Initially rude to him.
        if saveFile["route1"]["rude_choice"] == "APOLOGISED": # You find AASHISH and play Badminton with him.
            doDialogText("You noticed Ashish near the stairs.")
            doDialogText("He's waiting by the stairs to grab the rackets.# You decide to approach him.")
            doDialogText("As you walk near him,# he starts waving at you.")
            doDialogText(f"ASHISH:# Hey, {saveFile['name']}!# Wanted to play Badminton with me?")
            doDialogText("YOU:# Uh,# sure!# You got the rackets?")
            doDialogText("ASHISH:# Uh no, still waiting to get in.# These kids wanted to take basketballs.")
            print()
            doDialogText("You and Ashish find a spot to play Badminton.")
            doDialogText("As you two start playing,# you start noticing that he is.#.#.# not very good at it.")
            doDialogText("But still,# he tries very hard and barely keeps up with you.")
            advice = doDialogChoice("Give him advice?", choices=["Help Ashish.", "Don't give him advice."])

            route2["badminton_advice"] = ["ADVICED", "NOT ADVICED"][advice-1]

            if advice == 1: # You give him advice
                doDialogText("YOU:# Hey Ashish!# Do you need any help?")
                doDialogText("ASHISH:# No thanks! I'm good!")
                doDialogText("YOU:## No you aren't! Look-#", afterdelay = 0)
                print("     ", end="")
                doDialogText("You're holding the racket like this,# and way too tight.# You'll never be able to move fast and use your strength.")
                doDialogText("ASHISH:# O-#oh,# really?")
                doDialogText("YOU:# Instead,# hold it like this-", afterdelay=0.3)
                doDialogText("You hold Ashish's hand to show him how to hold the racket,# and give him tips on swinging.")
                doDialogText("As you're explaining to him,# you catch him blushing.")
                doDialogText("YOU: -#OH- oh sorry about that.#.# my bad.")
                doDialogText("ASHISH:# No worries, i-#its fine.")
                print("        ", end="")
                doDialogText("But thanks for giving me advice. Let's see how much better I can get!")
                doDialogText("You notice that he has gotten slightly better,# and is now able to play properly.")
                doDialogText("He's still getting used to playing this way,# but he's getting the hang of it.")
                if pgFilter:
                    doDialogText("He's hitting his shots with lots of confidence and charisma,# such you can't help but look at.")
                    doDialogText("You can't help but get lost in his amazing grace.#.#.#")
                else:
                    doDialogText("Eventually,# you grow a little tired.")
                doDialogText(f"ASHISH:# Hey, {saveFile['name']}! Are you alright?")
                doDialogText("YOU: Huh oh-# YEAH I'm fine! Just got a little distracted.")
                doDialogText("(Can't be caught lacking now.)")

                doDialogText("Soon,# you two get tired and decide to rest somewhere.")
                doDialogText("ASHISH:# Thanks for giving me advice! Playing Badminton feels a lot more fun ,# and now I'm hitting more shots!")
                doDialogText("YOU:# No problem,# just helping a friend in need.")
                doDialogText("ASHISH:# U-#uh,# yeah.#.#.#")
                doDialogText("He looks down slightly.#.#.#")
                if pgFilter: doDialogText("(Is he starting to blush?")
                doDialogText("YOU:# Uh,# everything okay-", afterdelay=0.2)
            else:
                doDialogText("You decide not to give him advice and let him get better on his own.# He'd learn better that way.")
                doDialogText("He continues to struggle slightly,# but is getting better with each shot.")
                doDialogText("Watching him push through to try and keep up with you,# staying determined.#.#.#")
                doDialogText("You can't help but get lost in his.#.#.#")
                doDialogText(f"ASHISH:# Uhm,# {saveFile['name']}?# You alright?")
                doDialogText("YOU:# Uh,# Yeah!# I'm alright,# just got a little distracted.")
                doDialogText("ASHISH:# Oh,# okay!# Well you just missed that shot.")
                doDialogText("YOU:# Yeah,# got a little tired.")
                doDialogText("(Can't be caught lacking.)")
                doDialogText("Soon,# you two get tired and decide to rest somewhere.")
                doDialogText("ASHISH:# Sorry if my game was off.#.#.# I'm not the best at badminton.")
                doDialogText("YOU:# That's alright,# everyone has their own skill.")
                doDialogText("ASHISH:# Yeah.#.#.#")
                doDialogText("He looks down slightly.#.#.#")
                doDialogText("YOU:# Hey,# is everything okay-", afterdelay=0.2)
            doDialogText("\"WAAAAATTCHH OOOUUUUUUUTT!!!!!!\"", step=3, spd=6)
            doDialogText("There's a football flying towards you!# You reach your racket out in front of Ashish to maybe try and deflect it-")
            doDialogText("|| SSMACKK! ||", step=2, spd=10)
            doDialogText("The ball hit you instead.#.#.#")
            doDialogText("ASHISH:# OH-# A-ARE YOU OKAY?!")
            doDialogText("YOU:# Ugh,# yeah I'm fine.")
            doDialogText("ASHISH:# Why did you protect me?!# The ball was coming towards you!")
            doDialogText("YOU: Sorry,# I thought it was going towards you.# I'm fine tho, no need to worry.")
            doDialogText("ASHISH:# T-Thanks for protecting me though.#.#.#")
            doDialogText("YOU:# No problem.")
            print() # GO TO PE END SCENE
        else: # You play badminton with Earwind
            doDialogText("You look for another person to play Badminton with.")
            doDialogText("You spot ASHISH near the stairs,# but decide not to approach him.")
            doDialogText("You suddenly get a tap on your back:")
            doDialogText("\"Hey,# you,# wanna play Badminton?\"")
            doDialogText("YOU:# Uh,# sure!")
            print("    ", end="")
            doDialogText("Uhm.#.#.# Who are you again?")
            doDialogText("EARWIND:# I'm EARWIND!# What was your name?")
            doDialogText(f"YOU:# Oh,# I'm {saveFile['name']}.# Nice to meet you, Earwind.#.#.#")
            doDialogText("EARWIND:# Let's go over there.")
            doDialogText("You and Earwind find a spot to play Badminton on.")
            doDialogText("Seems Ashish is playing Badminton with someone else.")
            print()
            doDialogText("You start playing Badminton with Earwind.")
            doDialogText("Immediately,# you notice that he's absolute dogshit at Badminton,# missing every other turn.")
            doDialogText("YOU:# Bro you're terrible at this.")
            doDialogText("EARWIND:# Yeah sorry,# I'm not very good at this.")
            doDialogText("YOU:# That's literally what I just said.")
            doDialogText("EARWIND:# Yeah.#.#.# sorry,#### I'll play better.")
            doDialogText("Earwind is now trying harder to play badminton.")
            doDialogText("He is playing even more terribly now,# getting worse by the second.#.#.#")
            doDialogText("YOU:# Hey! You don't have to be hard on yourself.# Calm down")
            doDialogText("EARWIND:# Okay.#.#.#")
            doDialogText("Earwind takes a deep breath.#.#.#", afterdelay=1)
            doDialogText("His stance suddenly changes.")
            doDialogText("He's getting ready to serve in a completely different pose and confidence.")
            doDialogText("He shoots the shuttle high into the air,# so high that you can't think of hitting it.")
            doDialogText("YOU:# What the.#.#.#")
            doDialogText("It's still going higher.#.#.#")
            doDialogText(".#.#.# It landed on the lights of the ceiling of the PE Ground.# Now you can't reach it.")
            doDialogText("EARWIND:# oops,# I was trying to focus.#.#.# My bad.")
            doDialogText("YOU:# Great.#.#.# Now we can't play at all.")
            doDialogText("EARWIND:# Wait hear me out", afterdelay=0.4)
            doDialogText("Earwind is looking around for something.")
            doDialogText("YOU:# What are you gonna do?")
            print("    ", end="")
            doDialogText("Oh,# brother.#.#.# Don't tell me-", afterdelay=0.2)
            doDialogText("Earwind has borrowed another shuttle and prepares himself.")
            doDialogText("He shoots it up into the air high again,# this time hitting the light and knocking both shuttles to the ground.")
            doDialogText("YOU:# Okay,# not gonna lie that was cool as heck.")
            doDialogText("EARWIND:# Thanks!# I have #NO# idea how I managed to hit that again.")
            doDialogText("YOU:# Well,# I guess playing with you isn't gonna be as bad as I thought.")
            print() # GO TO PE END SCENE

    elif saveFile["route1"]["name_choice"] == "LUNATIC":
        doDialogText("You noticed Ashish near the stairs.")
        doDialogText("YOU:# HEY,# ASHISH!", step=2, spd=8)
        doDialogText("Ashish notices you, and starts waving.")
        doDialogText(f"ASHISH:# HEY, {saveFile['name'].upper()}!# WANNA PLAY BADMINTON?")
        doDialogText("YOU:# SURE!# You got the rackets?")
        doDialogText("ASHISH:# Uh no, still waiting to get in.# These kids wanted to take basketballs.")
        doDialogText("YOU:# Young ballers.")
        print()
        doDialogText("You and Ashish find a spot to play Badminton.")
        doDialogText("As you two start playing,# you start noticing that he is.#.#.# not very good at it.")
        doDialogText("But still,# he tries very hard and barely keeps up with you.")
        advice = doDialogChoice("Give him advice?", choices=["Help Ashish.", "Don't give him advice."])

        route2["badminton_advice"] = ["ADVICED", "NOT ADVICED"][advice-1]

        if advice == 1: # You give him advice
            doDialogText("YOU:# Hey Ashish!# Do you need any help?")
            doDialogText("ASHISH:# No thanks! I'm good!")
            doDialogText("YOU:## No,# Look-##", afterdelay = 0)
            print("     ", end="")
            doDialogText("You're holding the racket like this,# and way too tight.# You'll never be able to move fast and use your strength.")
            doDialogText("ASHISH:# Really?")
            doDialogText("YOU:# Yes,# hold it like this instead.", afterdelay=0.3)
            doDialogText("You show Ashish how to hold the racket.")
            doDialogText("ASHISH:# Oh, I see.")
            doDialogText("YOU:# This position gives you more power and accuracy.")
            doDialogText("ASHISH:# Ohhh! Thanks for giving me advice. Let's see how much better I can get!")
            doDialogText("You get back to playing Badminton with Ashish.")
            doDialogText("You notice that he has gotten slightly better,# and is now able to play properly.")
            doDialogText("He's still getting used to playing this way,# but he's getting the hang of it.")

            doDialogText("Soon,# you two get tired and decide to rest somewhere.")
            doDialogText("ASHISH:# Thanks for giving me advice! Playing Badminton feels a lot more fun ,# and now I'm hitting more shots!")
            doDialogText("YOU:# No problem,# just helping a friend in need.")
            doDialogText("ASHISH:# U-#uh,# yeah.#.#.#")
            doDialogText("He looks down slightly.#.#.#")
            if pgFilter: doDialogText("(Is he starting to blush?")
            doDialogText("YOU:# Uh,# everything okay-", afterdelay=0.2)
        else:
            doDialogText("You decide not to give him advice and let him get better on his own.# He'd learn better that way.")
            doDialogText("He continues to struggle slightly,# but is getting better with each shot.")
            doDialogText("Watching him push through to try and keep up with you,# staying determined.#.#.#")
            doDialogText("You can't help but get lost in his.#.#.#")
            doDialogText(f"ASHISH:# Uhm,# {saveFile['name']}?# You alright?")
            doDialogText("YOU:# Uh,# Yeah!# I'm alright,# just got a little distracted.")
            doDialogText("ASHISH:# Oh,# okay!# Well you just missed that shot.")
            doDialogText("YOU:# Yeah,# got a little tired.")
            doDialogText("(Can't be caught lacking.)")
            doDialogText("Soon,# you two get tired and decide to rest somewhere.")
            doDialogText("ASHISH:# Sorry if my game was off.#.#.# I'm not the best at badminton.")
            doDialogText("YOU:# That's alright,# everyone has their own skill.")
            doDialogText("ASHISH:# Yeah.#.#.#")
            doDialogText("He looks down slightly.#.#.#")
            doDialogText("YOU:# Hey,# is everything okay-", afterdelay=0.2)
        doDialogText("\"WAAAAATTCHH OOOUUUUUUUTT!!!!!!\"", step=3, spd=6)
        doDialogText("There's a football flying towards you!# You reach your racket out in front to protect both of you.")
        doDialogText("|| TING! ||", step=2, spd=10)
        doDialogText("The ball hit your racket and knocks it out of your hand.")
        doDialogText("ASHISH:# OH-# Are you alright?")
        doDialogText("YOU:# Ugh,# yeah I'm fine.", line=False)
        print("     ", end="")
        doDialogText("Knocked out my bat tho.")
        doDialogText("ASHISH:# Glad we're both safe.") # GO TO PE END
        print()
    
    # PE END SCENE
    doDialogText("PE Class is over now.# You suspect that the only flavorful part of the day has finished.")

    # DEBAYAN FALL OFF
    doDialogText("Now it's chemistry class.")
    doDialogText("Chemistry is,# as usual,# boring.")

    if saveFile["route1"]["name_choice"] in ["NORMAL", "LUNATIC"]: # Talk about chemistry with Ashish.
        doDialogText("ASHISH:# Hey,# do you like chemistry?")
        doDialogText("YOU:# Nah,# I don't really like chemistry.")
        doDialogText("ASHISH:# Oh,# I hate chemistry as well.")
        
        if route2["house_studyChoice"] == "STUDYING": # THIS MF STUDIED PHYSICSSS
            doDialogText("YOU:# I might be good in physics,# but I dunno.# I just read the textbook after school started.")
            doDialogText("ASHISH:# I think Physics is not as bad as Chemistry.")
            doDialogText("YOU:# Physics is actually kinda fun.#.#.# some parts of it.")
            doDialogText("ASHISH:# Yeah,# I get that too.")
            doDialogText("YOU:# Yeah who knew we'd one day figure out exactly how many seconds it'd take for a stone to reach the ground from.#.#.#")
            doDialogText("    the top.#.#.# of a tower.#")
            doDialogText("(Teacher is looking. Pretend to pay attention.)")
            doDialogText(".#.#.#")
            doDialogText("(Ok green light)")
            doDialogText("ASHISH:# Well,# we just missed that whole lecture.")
            doDialogText("YOU:# Meh Ima just read the textbook at the end.")
            doDialogText("ASHISH:# Me too.")
        else:
            doDialogText("YOU:# I know,# right? It's so confusing,# like what is an orbital?")
            doDialogText("ASHISH:# .#.#.#")
            doDialogText("YOU:# Oh-")
            doDialogText("(Teacher is looking. Pretend to pay attention.)")
            doDialogText(".#.#.#")
            doDialogText("(Ok green light)")
            doDialogText("YOU:# Guess I need to pay more attention in class then.")
        
        doDialogText(".#.#.#") # DO THE DEBAYAN FALLING SCENE AFTER COMPLETING THE OTHER STUDY INTERACTIONS

    doDialogText("Suddenly-", afterdelay=0.2)
    doDialogText("|| THUD! ||", step=2, spd=10)
    doDialogText("Someone fell over.")
    doDialogText("It was DEBAYAN. You don't know how, but he fell off of his desk.")
    doDialogText("The whole class is laughing at him.")

    if saveFile["route1"]["name_choice"] != "RUDE" or (saveFile["route1"]["name_choice"] != "RUDE" and saveFile["route1"]["rude_choice"] != "APOLOGISED"):
        doDialogText("ASHISH:# Hey,# isn't that DEBAYAN?")
        doDialogText("YOU:# Oh yeah,# he's covered in.#.#.## is that choco milk?")
        doDialogText("ASHISH:# Poor guy.#.#.#")
        
        helpDeb = doDialogChoice("Help DEBAYAN?", choices=["Help him to the washroom.", "Stay with Ashish."])

        if helpDeb == 1: # You chose to help DEBAYAN
            route2["help_debayan"] = "HELPED"
            doDialogText("YOU:# I'll help him to the Washroom.")
            doDialogText("You take him to the Washroom.")
            doDialogText("DEBAYAN:# Hey,# thanks for helping me.# You didn't have to tho.")
            doDialogText("YOU:# No problem.")
            doDialogText("DEBAYAN:# I'm DEBAYAN.# Nice to meet you.")
            doDialogText(f"YOU:# Yeah,# I know.# I'm {saveFile['name'].upper()}.# Nice to meet you too.")
            doDialogText("DEBAYAN:# Oh.#.#.## Not the best first impressions,# huh?")
            doDialogText("YOU:# Eh,# don't stress over it.# First impressions sure are important,# but they don't really last for long.")
            print("    ", end="")
            doDialogText("Just be the bigger man.")
            doDialogText("DEBAYAN: .#.#.# yeah.")
            print()
            doDialogText("You return to class with a now sorta-clean Debayan.")
            doDialogText("ASHISH:# Did you help Debayan to the washroom?# That's so nice of you!")
            doDialogText("YOU:# Yeah,# just wanted to help.")
        else:
            route2["help_debayan"] = "NOT HELPED"
            doDialogText("You decide to stay with ASHISH.")
            doDialogText("Debayan rushes himself to the washroom.# A humiliating first impression.")

        if saveFile["route1"]["name_choice"] == "NORMAL": # NORMAL Route
            doDialogText("YOU:# Oh yeah.#.#.# Ashish,# do you, by chance,# want to exchange contact infos?# So we could talk even after school?")
            doDialogText("ASHISH:# U-#uh,# sure!# I'll write down mine i-#in your notebook.")
            doDialogText("YOU:# Oh, okay!")
            doDialogText("You and Ashish swiftly exchange contact infos.")
            doDialogText("ASHISH:# Okay,# done.# L-#lets talk after school,# then.")
            doDialogText("YOU:# Okay.")
        elif saveFile["route1"]["name_choice"] == "LUNATIC": # LUNATIC Route
            doDialogText("YOU:# OH yeah.# Ashish,# let's exchange contact infos.")
            doDialogText("ASHISH:# Uh, sure.# What do you use?")
            doDialogText("YOU:# Tiktok.")
            doDialogText("ASHISH:# .#.#.# you know tiktok is banned here,# right?")
            doDialogText("YOU:# Okay okay,# it's instagram.# My @ is taylorswift.")
            doDialogText("ASHISH:# .#.#.# let's just exchange phone numbers.")
            doDialogText("YOU:# Oh I don't have a phone,# lost it in the year 3000-", afterdelay=0)
            doDialogText("Ashish is holding a compass in his hands.")
            doDialogText(f"YOU:# 93362 24189.# My instagram is @{saveFile['name'].lower()}2009.")
            doDialogText("ASHISH:# Good boy.")
            doDialogText(".#.#.#")
        route2["contact_info"] = "GOT CONTACT INFO"
    else:
        helpDeb = doDialogChoice("Help DEBAYAN?", choices=["Help him to the washroom.", "Stay with Ashish."])

        if helpDeb == 1:
            route2["help_debayan"] = "HELPED"
            doDialogText("YOU:# I'll help him to the Washroom.")
            doDialogText("You take him to the Washroom.")
            doDialogText("DEBAYAN:# Hey,# thanks for helping me.# You didn't have to tho.")
            doDialogText("YOU:# Oh it's nothing.")
            doDialogText("DEBAYAN:# I'm DEBAYAN.# Nice to meet you.")
            doDialogText(f"YOU:# I know dude,# I'm {saveFile['name'].upper()}.")
            doDialogText("DEBAYAN:# Oh.#.#.## Not the best first impressions,# huh?")
            doDialogText("YOU:# Yeah that was mad funny ngl.")
            doDialogText("DEBAYAN: .#.#.# yeah.")
            
            print()
            doDialogText("You return to class with a now sorta-clean Debayan.")
            doDialogText("ASHISH:# .#.#.# didn't know you could be nice.")
            doDialogText("You pretend to ignore him.")
        else:
            route2["help_debayan"] = "NOT HELPED"
            doDialogText("You decide not to help him.")
            doDialogText("Debayan rushes himself to the washroom.# A humiliating first impression.")
            doDialogText("You almost feel bad for him.#.#.#")

    print()
    doDialogText("The rest of the school day goes by in a blur of lectures and notes.")
    doDialogText("You reach home and collapse into your bed.")
    
    if saveFile["route1"]["name_choice"] != "RUDE" or (saveFile["route1"]["name_choice"] == "RUDE" and saveFile["route1"]["rude_choice"] == "APOLOGISED"):
        doDialogText("You think about the fun you had playing Badminton with ASHISH.")
        doDialogText("(I wanna play Badminton with ASHISH again.)")
        doDialogText("(Oh yeah, I have his contact info.)")
        doDialogText("You check your phone to see if Ashish is online.#.#.#")
        doDialogText("He's not.")
        doDialogText("You send him a meme to wake up to in the morning.")

    doDialogText("You soon start dozing off into sleep.#.#.#")

    doDialogText("As you're almost falling into sleep,# your phone dings one time: ")
    doDialogText("- - - - - - - - - - - - - - - - - - - - - - ", step=2, spd=2, afterdelay=0)
    doDialogText("|| HE'S ON HIS WAY. ||", step=2, spd=2, afterdelay=0)
    doDialogText("- - - - - - - - - - - - - - - - - - - - - - ", step=2, spd=2, afterdelay=4)

    # THE SAVE SHENANIGANS
    if saveFile['route2']['COMPLETED'] == True:
        doDialogText("You have already completed this chapter.# Would you like to save over your progress? (Y/N):", line=False)
        confirm = input("")

        if confirm.lower() in "n":
            doDialogText("The Game was not Saved.")
        else:
            route2["COMPLETED"] = True
 
            saveFile["route2"] = route2

            try:
                saveGame(curSaveName, saveFile)
                doDialogText("The game was saved.")
            except:
                doDialogText("There was an error in saving the game.")
    else:
        route2["COMPLETED"] = True
    
        saveFile["route2"] = route2
    
        saveGame(curSaveName, saveFile)


def start(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful):

    doDialogText("Loading Chapter 2.#.#.#", afterdelay=3)
    print()

    chapter_2(doDialogText, doDialogSlow, askChoice, askNum, doDialogChoice, doTimedQuestion, doTimedAttack, doTimedSpam, printGraphic, getPrompt, playSong, timeControl, pgFilter, saveFile, saveGame, curSaveName, soundImportSuccesful)
