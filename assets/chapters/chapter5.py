import urllib.request
import os
import time


'''
WHEN RELEASING THE CHAPTER,# replace the following:
'mods/Chapter 5/soundtrack/' -> 'assets/soundtrack/'
'''

def chapter_5(funcs):
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
    stopSong = funcs['stopSong']
    timeControl = funcs['timeControl']
    setTime = funcs['setTime']
    pgFilter = funcs['pgFilter']
    saveFile = funcs['saveFile']
    saveGame = funcs['saveGame']
    curSaveName = funcs['curSaveName']
    soundImportSuccesful = funcs['soundImportSuccesful']

    route5 = {
        'COMPLETED': False,
        'index': 0,
        'team': ['NOONE']*4,
        'date': False,
        'test': None,
        'key': False,

        'flower': False,

        'presentation_points': 0
    }

    index = 0

    if saveFile['route5']:
        if 'index' not in saveFile['route5']:
            saveFile['route5']['index'] = 0
        index = saveFile['route5']['index']

        # Loading the Save file's route5 data
        for i in saveFile['route5']:
            route5[i] = saveFile['route5'][i]
    
    def relationship():
        # USELESS HOTPOINTS: 
        r = "GOOD"
        hotpoints = 0

        # CHAPTER 1
        if saveFile['route1']['name_choice'] != "RUDE":
            r = "GOOD"
            if saveFile['route1']['name_choice'] == "NORMAL":
                hotpoints += 1
        
        elif saveFile['route1']['name_choice'] == "RUDE":
            if not saveFile['route1']['rude_cancel']: r = "BAD"
            else: r = "GOOD"
        
        # CHAPTER 2
        if saveFile['route2']['badminton_advice'] == 'ADVICED':
            hotpoints += 1
        
        # CHAPTER 3
        if saveFile['route3']['surrender'] == "DEFENDED" and (saveFile['route1']['name_choice'] == "NORMAL" or saveFile['route1']['rude_cancel']):
            hotpoints += 1
        if saveFile['route3']['rude_stay'] == "UNFORGIVED":
            r = "BAD"
        elif saveFile['route3']['rude_stay'] == "FORGIVED":
            r = "GOOD"
        
        # CHAPTER 4
        if saveFile['route4']['peak_horseRiding'] == "ACHIEVED":
            hotpoints += 1

        # CHAPTER 5
        if saveFile['route5']['date']:
            r = "GOOD"
        else:
            r = "MID"
        
        if saveFile['route5']['flower']:
            hotpoints += 1


        return r, hotpoints

    doDialogText("CHAPTER 5:##  Weekdays.", spd = 25, step = 3)

    if index == 0:    
        print()
        doDialogText("PART ONE:### PROJECT.", spd=6)
        print()
        doDialogText("It's Thursday.", afterdelay=1.6)
        doDialogText("After the events of the weird dream.#.#.#")
        if saveFile['route3']['rude_stay'] == 'FORGIVED':
            doDialogText("You woke up at 5:00 AM and went back to your house.")
        else: print()
        doDialogText("A week has gone by from then.", afterdelay=3)
        print()
        
        doDialogText("You're at school now.# It's English.")
        doDialogText("ENGLISH TEACHER:# Today.#.#.# I'm thinking about assigning a project.")

        playSong('assets/soundtrack/classroom.ogg', looping=True)

        doDialogText("                 A group project.# Present anything you want.# Make your own teams.")
        doDialogText("                 I want to see how creative you guys can get.")
        print()
        doDialogText("(A Group Presentation.#.#.#)")
        doDialogText("(What qualities do I have for that?)")
        doDialogText("(.#.#.#)")
        doDialogText("(i'm useless for this.#.#.#)")
        doDialogText("YOU:# Oh well,# I'll just let everyone else do the work and motivate them.")
        doDialogText("     Let's see,# what qualities are needed for a presentation?")
        doDialogText(".#.#.#")
        doDialogText("After like 9 seconds of thinking,# you come up with 5 roles:")
        doDialogText("SPEECH,# DESIGN,# FACTS,# ART,# AND.#.#.## Coordination.")
        doDialogText("YOU:# Coordination for me.")
        doDialogText("You categorize everyone in class with what you know about them so far.")
        print()

        # SELECTION BEGINS.

        speechGang = ['ADITHYA', 'A.R RAHMAN', 'SIBI', 'SAVAN', 'BAPPE']

        

        speechSel = doDialogChoice('Who will you choose to speak?', choices=speechGang)
        
        route5['team'][0] = speechGang[speechSel - 1]
        if speechSel == 1:
            doDialogText("(Eh,# really?)")
            doDialogText("Okay fine,# whatever.")
            print()
            doDialogText("You walk upto Adithya.")
            print()

            doDialogText("ADITHYA:# Well,# look who we have here.")
            doDialogText("YOU:# I-#", afterdelay=0)
            doDialogText("ADITHYA:# Fret not,# I know what you're thinking.")
            doDialogText("YOU:# What-#", afterdelay=0)
            doDialogText("ADITHYA:# You came to me so you could ask for my help with the project.")
            doDialogText("         Because I'm so great,# you will benefit from having me in your team,# and you may even think you can get close to me and sabotage my plan to seperate you from ASHISH.")
            doDialogText("YOU:# No-#", afterdelay=0)
            doDialogText("ADITHYA:# I will help you,# but you won't trick me so easily.")
            doDialogText("         Think of this as pity upon you.")
            doDialogText("YOU:# Okay.#.#.#")
            doDialogText("ADITHYA:# SO,### what do you want me to do?")
            doDialogText("YOU:# .#.#.#speak.")
            doDialogText("ADITHYA:# Bet.# That's actually one thing I'm good at.")
            doDialogText("YOU:# cool.# bye.# Gotta recruit others.", afterdelay=1.3)

            print()
            doDialogText("ADITHYA has been added to your team.")

        elif speechSel == 2:
            doDialogText("You spot A.R RAHMAN and walk upto him.")
            print()
            doDialogText("A.R RAHMAN:# Oh it's you.# Hello.")
            doDialogText("YOU:# Hello.# Would you like to join my team for the project?")
            doDialogText("A.R RAHMAN:# Wow,# so quick!# I'll join.# What do I do?")
            doDialogText("YOU:# Can you do the speaking role for the project?")
            doDialogText("A.R RAHMAN:# Oh,## sure thing.")
            doDialogText("YOU:# Okay thanks.")
            doDialogText("A.R RAHMAN:# By the way what's with you and ADITHYA?")
            doDialogText("YOU:# Uhh.#.#.# I don't really know.")
            doDialogText("A.R RAHMAN:# Yeah he seems to have beef with you for some reason.")
            doDialogText("            I think it has something to do with ASHISH.")
            doDialogText("YOU:# Yeah.#.#.# not much to say about that.")
            doDialogText("A.R RAHMAN:# Well,# thanks for adding me to your team.")
            doDialogText("            Don't know much about you,# but I hope we will cook.")
            doDialogText("            I'll try me best!")
            doDialogText("YOU:# Me too.# Thanks for joining our team.", afterdelay=1.6)
            
            print()
            doDialogText("A.R RAHMAN has been added to your team.")
        
        elif speechSel == 3:
            doDialogText("You find SIBI and approach him.")
            print()
            doDialogText("YOU:# Hey SIBI.# Can you join our team?")
            doDialogText("SIBI:# Oh,# sorry,# but I was thinking of teaming up with AWAITH.")
            
            doDialogText("SIBI:# You're really quick with it tho.# Wasting no time.")
            doDialogText("YOU:# Yeah.# I figured I can't do anything,# so I should start by finding someone that can.")
            doDialogText("SIBI:# Damn.")

            doDialogText("      Also I uh,# saw you last week.# I think.")
            doDialogText("YOU:# Oh,# where did you see me?")
            doDialogText("SIBI:# Near a supermarket,# you were fighting with ADITHYA.")
            doDialogText("YOU:# Oh.# you saw that.")
            doDialogText("SIBI:# Yeah,# I went away quickly so I wouldn't get caught up in it.")
            doDialogText("YOU:# Can you keep this a secret?")
            doDialogText("SIBI:# Okay sure.")
            doDialogText("YOU:# Thanks.# See ya.", afterdelay=1.6)

            print()
            doDialogText("SIBI was not added to your team.")
            print()
            doDialogText("(Welp,# I'll just look for others).")
        
        elif speechSel == 4:
            doDialogText("You search the class and find SAVAN.")
            print()
            
            doDialogText("YOU:# Hey, SAVAN.# Wanna join my team?")
            doDialogText("SAVAN:# Hey,# you're the guy who made Adithya faint!")
            doDialogText("YOU:# Uh,# no,# he did that to himself.")
            doDialogText("SAVAN:# Yeah,# but you took him to the infirmary right?")
            doDialogText("YOU:# Yeah.")
            doDialogText("SAVAN:## Sorry,# but what did you ask me again?")
            doDialogText("YOU:# .#.#would you like to join my team?")
            doDialogText("SAVAN:# Oh yeah sure!# You're really quick at asking!")
            doDialogText("       What do I have to do?")
            doDialogText("YOU:# Could you speak for the presentation?")
            doDialogText("SAVAN:# Oh,# I don't think speaking's my best game,# but I'll try my best!.")
            doDialogText("YOU:# Me too.# Thanks for joining!", afterdelay=1.6)
            
            print()
            doDialogText("SAVAN has been added to your team.")
        elif speechSel == 5:
            doDialogText("(I've never talked to BAPPE yet.#.#.#)")
            doDialogText("You walked up to BAPPE.")
            print()
            
            doDialogText("YOU:# Hi.# BAPPE,# right?")
            doDialogText("BAPPE:# yeas.# M. BAPPE.")
            doDialogText("YOU:# Cool,# do you want to join my team?")
            doDialogText("BAPPE:# uhh i can't i wanted to be with KICHAN.")
            doDialogText("YOU:# Oh,# that's alright.")
            doDialogText("BAPPE:# Lemme talk to kichan.")
            doDialogText("BAPPE walks to KICHAN.")
            doDialogText("YOU:# Oh.#.#.", spd=5)
            print()
            doDialogText(".#.#.#", afterdelay=1.8)
            doDialogText("BAPPE is walking back again.")
            doDialogText("BAPPE:# i saw that bastard talking with someone else,# he told me hed join me.")
            doDialogText("YOU:# oh.#.#")
            doDialogText("BAPPE:# recruit me i want revenge.")
            doDialogText("YOU:# Okay.#.#.#", afterdelay=1.6)

            print()
            doDialogText("BAPPE has been added to your team.")

        doDialogText("(Now,# to find the ones to design the presentation.)")
        print()

        designGang = ['ANNA', 'SAHUR', 'TENMAY', 'WAYDANT', 'DEBAYAN']
        designSel = doDialogChoice('Who will you choose to speak?', choices=designGang)
        
        route5['team'][1] = designGang[designSel-1]

        print()

        if designSel == 1:
            doDialogText("You find ANNA across the classroom.")
            print()

            doDialogText("YOU:# Hey Anna,# would you like to join our team for the presentation?")
            doDialogText("ANNA:# Oh,# sure thing.# Maybe I could do something like# the PowerPoint?")
            doDialogText("YOU:# That's# actually what I came here to ask you to do.")
            doDialogText("ANNA:# Oh,# that's perfect.# I'm in.")
            doDialogText("YOU:# Thanks.# We've got three people including you now.")
            doDialogText("ANNA:# Who's the other one?")
            doDialogText(f"YOU:# {route5['team'][0]}.")
            doDialogText("ANNA:# Oh.")
            doDialogText("      Oh yeah,# I may not be able to work on the presentation soon,# but when I do get the chance,# I'll do my best to get it finished.")
            doDialogText("YOU:# As long as we make it.")
            doDialogText("ANNA:# Good luck.", afterdelay=1.6)

            print()
            doDialogText("ANNA has been added to your team.")

        elif designSel == 2:
            doDialogText("You spot SAHUR and walk up to him.")
            print()

            doDialogText("YOU:# Hey,# SAHUR.# Would you like to join my team?")
            doDialogText("SAHUR:# Oh,# uh sure.# What do I do?")
            doDialogText("YOU:# Can you design the slides for the PowerPoint?")
            doDialogText("SAHUR:# Sure.# What topic?")
            doDialogText("YOU:# Uh.#.#.#")
            doDialogText("     We'll decide that in the team meeting.")
            doDialogText("SAHUR:# Okay,# I shall join your team then.")
            doDialogText("YOU:# Okay,# thanks.")
            doDialogText("SAHUR:# Is anyone else in the team?")
            doDialogText(f"YOU:# Just {route5['team'][0]}.")

            if speechSel == 1:
                doDialogText("SAHUR:# Oh,# Adithya's on your team?# I was thinking MAYBE I'd ask him.")
                doDialogText("YOU:# Well that makes this perfect.")
            else:
                doDialogText("SAHUR:# Oh.")
                doDialogText("YOU:# Well,# I'll try my best for the presentation.")
            
            doDialogText("SAHUR:# Yeah,# I'll do my best to make the slides.")
            doDialogText("YOU:# Again,# thanks for joining my team.", afterdelay = 1.6)
            
            print()
            doDialogText("SAHUR has been added to your team.")

        elif designSel == 3:
            doDialogText("You go to TENMAY.")
            print()

            doDialogText("YOU:# Hey,# TENMAY.")
            doDialogText("TENMAY:# Wassup dawg?")
            doDialogText("YOU:# Want to join my team for the presentation?")
            doDialogText("TENMAY:# Sure,# how many people are there?")
            doDialogText(f"YOU:# I think the number is 5 people,# but I've only got {route5['team'][0]} so far.")
            doDialogText("TENMAY:# Oh,# okay.# What should I do?")
            doDialogText("YOU:# Can you design the slides?")
            doDialogText("TENMAY:# In PowerPoint?# Shi I don't think I'm too familiar with PowerPoint,# but I can try.")
            doDialogText("YOU:# It's alright,# as long as we have someone to make the slides.")
            doDialogText("TENMAY:# Thanks for asking me to join.# What role do you have?")
            doDialogText("YOU:# I uh.#.#.# I can't do anything for this presentation.#.#.#")
            doDialogText("     So I figured I'd just watch from the sides and encourage everyone.")
            doDialogText("TENMAY:# Oh,# don't say stuff like that,# I'm sure you have a talent for something.")
            doDialogText("YOU:# Uh.#.#.# I play guitar,# if that counts.")
            doDialogText("TENMAY:# What!# No way,# me too!")
            doDialogText("        I used to play the guitar,# but I stopped a while ago.")
            doDialogText("YOU:# Oh,# that's nice to hear.")
            doDialogText("      unfortunately playing guitar won't be needed for the presentation.#.#.#")
            doDialogText("TENMAY:# Maybe you're good at coordinating the team!")
            doDialogText("        You never know until you try.")
            doDialogText("YOU:# y'know what?# You're right.# I will try my best.")
            doDialogText("TENMAY:# Now that's the spirit!", afterdelay = 1.6)

            print()
            doDialogText("TENMAY has been added to your team.")
        
        elif designSel == 4:
            if saveFile['route3']['rude_stay'] == "UNFORGIVED":
                doDialogText("(WAYDANT,# huh?)")
                doDialogText("(After what happened last week.#.#.#)")
                print()
                doDialogText("You walk upto WAYDANT.")
                print()
                doDialogText("YOU:# Hey,# WAYDANT.")
                doDialogText(f"WAYDANT:# Oh,# hey {saveFile['name']}.")
                doDialogText("         What's up?")
                doDialogText("YOU:# Uhh,# I was wondering if you would like to join my team for the presentation?")
                doDialogText("WAYDANT:# Oh sure thing.# How many people do you have now?")
                doDialogText(f"YOU:# Me and {route5['team'][0]}.")
                if route5['team'][0] == "ADITHYA":
                    doDialogText("WAYDANT:# Adithya.#.#.#", afterdelay=2)
                    print()
                
                doDialogText("WAYDANT:# Okay.# What should I do?")
                doDialogText("YOU:# I was hoping you could help design the slides for the presentation.")
                doDialogText("WAYDANT:# Oh okay.# I can do that.")
                doDialogText("YOU:# Thanks.")
                doDialogText("    Also.#.#.#")
                doDialogText("WAYDANT:# ?")
                doDialogText("YOU:# Was that really a dream?")
                doDialogText("WAYDANT:# What dream?")
                doDialogText("YOU:# ...nevermind.", afterdelay=1)
                print()

                doDialogText("WAYDANT has been added to your team.", afterdelay=1.6)
                print()
                doDialogText("WAYDANT:# (so that wasn't a dream at all.)")
            else:
                doDialogText("You walk upto WAYDANT.")
                print()
                doDialogText("YOU:# Hey WAYDANT, I was wondering if you would like to join my team for the presentation.#.#.")
                doDialogText("WAYDANT:# Oh uhh,# sure thing.# How many people do you have now?")
                doDialogText(f"YOU:# Me and {route5['team'][0]}.")
                if route5['team'][0] == "ADITHYA":
                    doDialogText("WAYDANT:# Adithya.#.#.#", afterdelay=2)
                    print()
                
                doDialogText("WAYDANT:# Okay.# What should I do?")
                doDialogText("YOU:# I was hoping you could help design the slides for the presentation.")
                doDialogText("WAYDANT:# Oh okay.# I can do that.")
                doDialogText("         You were really quick to ask btw,# I mean the presentation was literally just announced.")
                doDialogText("YOU:# Yeah,# that's because I uhh,## can't do anything else.# So I decided I'd recruit people.")
                doDialogText("WAYDANT:# Oh.# Well,# good luck.# I'll try my best.")
                doDialogText("YOU:# Thanks,# same to you.", afterdelay=1.6)
                print()

                doDialogText("WAYDANT has been added to your team.")
        elif designSel == 5:
            doDialogText("You spot DEBAYAN at the back of the class.")
            print()

            doDialogText("YOU:# Hey,# DEBAYAN.# You want to join my team?")
            doDialogText("DEBAYAN:# Oh,# sure.# What should I do?")
            doDialogText("YOU:# Will you help with designing the slides?")
            doDialogText("DEBAYAN:# Ooh,# I'm not sure I'm the best person to ask for that.#.#.#")
            doDialogText("       But I'm not sure if I can do anything else,# so sure.")
            doDialogText("YOU:# Okay sweet,# thanks.", afterdelay=1.6)

            print()
            doDialogText("DEBAYAN has been added to your team.")
        
        factsGang = ['EARWIND', 'TEJAS', 'AWAITH', 'KICHAN', 'ASHAK']
        factsSel = doDialogChoice("Who will you choose to gather the facts?", choices=factsGang)
        route5['team'][2] = factsGang[factsSel-1]
        
        if factsSel == 1:
            doDialogText("(EARWIND,# the brainiac.# Also from Adithya's Gang.)")
            doDialogText("You walk up to EARWIND.")
            print()
            doDialogText("YOU:# Hey EARWIND.")
            doDialogText(f"EARWIND:# Oh,# hi {saveFile['name']}.# The project?")
            doDialogText("YOU:# Uh yes.")
            doDialogText("EARWIND:# Sure thing.# You're the first one to ask me.# I was thinking of going with Ashish.")
            if saveFile['route3']['rude_stay'] == 'FORGIVED':
                doDialogText("YOU:# Uh,# Ashish was already taken by SARBATH.")
                doDialogText("EARWIND:# Oh.# Then I shall join your team.# What should I do?")
            else:
                doDialogText("         But I'll join your team.# What do you want me to do?")
            doDialogText("YOU:# Can you gather the facts for our topic?# And possibly help with writing the script?")
            doDialogText("EARWIND:# Oh sure,# I think I know a lot of things.# I could also help with coming up with an interesting topic for the presentation.")
            doDialogText("YOU:# You don't have to be ChatGPT bro,# we'll decide during the group meeting.")
            doDialogText("EARWIND:# Oh.# By the way,# how many people have you recruited so far?")
            doDialogText(f"YOU:# Two other people,# {route5['team'][0]} and {route5['team'][1]}.")
            doDialogText("EARWIND:# Damn,# that's fast.")
            doDialogText("         Well,# looking forward to work with y'all.")
            doDialogText("YOU:# Same.# Anyways thanks for joining our team.")
            doDialogText("EARWIND:# You're welcome.", afterdelay=1.6)
            print()

            doDialogText("EARWIND has been added to your team.")
        
        elif factsSel == 2:
            doDialogText("(A direct confrontation,# huh.#.#.#)")
            doDialogText("You spot TEJAS at the perfect centre of the classroom.")
            doDialogText("He's drinking.#.#.# chai?# Is he reading the school newspaper?")
            doDialogText("You walk upto TEJAS.")
            print()

            doDialogText("YOU:# Hey,# TEJAS.")
            doDialogText("TEJAS:# Hm?## Oh it's you.")
            doDialogText("       Hey,# no hard feelings okay?# I'm sorry about the other day.")
            if saveFile['route1']['name_choice'] == "RUDE":
                doDialogText("YOU:# .#.#.#whatever.")
            else:
                doDialogText("YOU:# It's alright.#.#.#")
            
            doDialogText("     I just wanted to ask you to join my team for the presentation.")
            doDialogText("TEJAS:# Oh,# um,# sure.# What should I do?")
            doDialogText("YOU:# Can you gather the facts and do the main research?")
            doDialogText("TEJAS:# That's like one of the most boring things one could do.#.#.#")
            doDialogText("      But actually I might be able to enlighten the class with my knowledge.")
            doDialogText("      Sure,# I'll join your team.")
            doDialogText("YOU:# Okay,# thanks a bunch.", afterdelay=1.6)
            print()

            doDialogText("TEJAS was added to your team.")

        elif factsSel == 3:
            doDialogText("You walk upto AWAITH.")
            doDialogText("YOU:# Hey,# AWAITH.# Do you want to join my team for the presentation?")
            doDialogText("AWAITH:# Uhh,# I was thinking of adding SIBI to my team..")
            if route5['team'][0] == 'SIBI':
                doDialogText("YOU:# Oh I did ask SIBI earlier.# I think he wanted to join your team as well.")
                doDialogText("AWAITH:# Oh fr?# I'll join yours then.# I'll ask SIBI to join yours as well.# Let's make him speak.")
            else:
                doDialogText("YOU:# Oh,# how many people are on your team?")
                doDialogText("AWAITH:# Not really a team,# it's just me.# But sure I'll join your team.")
                doDialogText("        What should I do though?")
            doDialogText("YOU:# Thanks,# can you do the research and stuff?# And also help writing the script?")
            doDialogText("AWAITH:# Sure bro,# I'll use ChatGPT to make a script.")
            doDialogText("YOU:# Uh we have time,# we can discuss this.")
            doDialogText("AWAITH:# Okay bro.#.#.# I'll do it.")
            doDialogText("        What are you doing?")
            doDialogText("YOU:# Uhmm,# I'll just motivate everyone and get the team coordinated,# I can't do anything.")
            doDialogText("AWAITH:# Ahhh,# the lazy one.")
            doDialogText("YOU:# .#.#.#")
            doDialogText("AWAITH:# Okay,# I'll help you.")
            doDialogText("YOU:# Thanks.", afterdelay=1.6)

            print()
            if 'SIBI' in route5['team']:
                doDialogText("AWAITH and SIBI were added to your team.")
            else:
                doDialogText("AWAITH was added to your team.")
            
            print()
            doDialogText("AWAITH: (I'll use gemini instead.)")
        
        elif factsSel == 4:
            doDialogText("You spot KICHAN talking with BAPPE.")
            if route5['team'][0] == 'BAPPE':
                doDialogText(f"BAPPE:# Oh,# {saveFile['name'].lower()}! i found kichan,# he wants to join your team.")
                doDialogText("KICHAN:# Hello I want to join your team.")
                doDialogText("YOU:# Oh um,# I was looking for someone to do the research and-", afterdelay=0)
                doDialogText("KICHAN:# Bet bro,# I'll do research.")
                doDialogText("YOU:# Okay.# Thanks.", afterdelay=1.6)
                print()
            else:
                doDialogText("YOU:# Hey,# do you want to join my team for the presentation?")
                doDialogText("KICHAN:# Hmm,# if BAPPE is already taken.# brb")
                doDialogText("BAPPE:# Bro i got taken by YUNAS bro,# join his team.", afterdelay=3)
                doDialogText("KICHAN:# Ok I join your team.")
                doDialogText("YOU:# Uh,# great.# Can you do the research and stuff?")
                doDialogText("KICHAN:# Bet bro,# I'll do the best researching.")
                doDialogText("YOU:# Thanks.#.#")
                doDialogText("KICHAN:# You welcome.", afterdelay=1.6)
                print()
            
            doDialogText("KICHAN was added to your team.")
        
        elif factsSel == 5:
            doDialogText("You spot ASHAK in the back of the class.")
            doDialogText("YOU:# Hey,# do you want to join my team for the presentation?")
            doDialogText("ASHAK:# What? Oh uh sure.# What should I do?")
            doDialogText("YOU:# Can you do the research and maybe even help writing the script?")
            doDialogText("ASHAK:# Oh bet,# I have my phone rn I can google something.")
            doDialogText("YOU:# .#.#.# what")
            doDialogText("ASHAK:# Don't worry we got this.")
            doDialogText("YOU:# .#.#we're not supposed to have our phones out during class.# The punishment's pretty harsh.")
            doDialogText("ASHAK:# Don't worry bro,# as long as you don't snitch we're good.")
            doDialogText("YOU:# .#.#.#if you get caught,# I never knew about this.", afterdelay=1.6)
            print()
            doDialogText("ASHAK was added to your team.")


        artGang = ['FRIEDEL', 'JANET', 'FARWANA', 'SURYA', 'ENAMEL']

        artSel = doDialogChoice("Who will you choose for art?", choices=artGang)

        route5['team'][3] = artGang[artSel -1]

        if artSel == 1:
            doDialogText("You catch Friedel doodling on his notebook.")
            doDialogText("YOU:# Hey FRIEDEL.# Do you wanna join my team for the presentation?")
            doDialogText("FRIEDEL:# Uh,# sure.# What's my task?")
            doDialogText("YOU:# I noticed you were really good at drawing.# Can you handle the art for the slides?")
            doDialogText("FRIEDEL:# Your presentation's going to have art?")
            doDialogText("YOU:# .#.#yea?")
            doDialogText("FRIEDEL:# Well that's one heck of a presentation,# I'm in!")
            doDialogText("YOU:# Thanks!# Nice drawing by the way.")
            doDialogText("FRIEDEL:# Oh um# thank you.", afterdelay=1.6)

            print()

            doDialogText("FRIEDEL was added to your team.")
        elif artSel == 2:
            doDialogText("You walk upto JANET.")
            doDialogText("YOU:# Hey JANET,# would you like to join my team?")
            doDialogText("JANET:# ...NO GIRL SHUT UPPPP-# oh wait.#.#", afterdelay=0)
            doDialogText("       yes?")
            doDialogText("YOU:# Yeah.#.# would you want to join my team?")
            doDialogText("JANET:# Oh,# um no one else asked me so,# sure?")
            doDialogText("       I don't think I can be of use though.#.#.# i could draw something idk.#.#")
            doDialogText("YOU:# Well we got everything else covered,# so you could,# infact,# draw something.")
            doDialogText("JANET:# Oh that's cool,# I'm in.")
            doDialogText("YOU:# Alright,# thanks.", afterdelay=1.6)

            print()
            doDialogText("JANET was added to your team.")
        elif artSel == 3:
            doDialogText("You find FARWANA and walk upto her.")
            doDialogText("YOU:# Hey,# would you like to join my team?# We just need one more person.")
            doDialogText("FARWANA:# Sure..# what should I do?")
            doDialogText("YOU:# Can you work on the art for the presentation?")
            doDialogText("FARWANA:# I'm not confident about my drawing,# but sure.")
            doDialogText("YOU:# Okay,# thanks.", afterdelay=3)

            print()
            doDialogText("FARWANA was added to your team.")
        elif artSel == 4:
            doDialogText("You locate SURYA and head over to his seat.")
            doDialogText("YOU:# Hey,# do you want to join my team?")
            doDialogText("SURYA:# Uhh,# sure.# I'm kind of struggling to find a team.")
            doDialogText("YOU:# Well we just need one more person,# so you could join us.")
            doDialogText("SURYA:# Okay,# what should I do?")
            doDialogText("YOU:# Can you do art?")
            doDialogText("SURYA:# No.")
            doDialogText("YOU:# Well.#.#.# meh it's fine.# Join anyways.")
            doDialogText("SURYA:# ...ok", afterdelay=3)

            print()
            doDialogText("SURYA was added to your team.")
        elif artSel == 5:
            doDialogText("You find ENAMEL and walk to him.")
            doDialogText("YOU:# Hey ENAMEL,# you want to join my team?")
            doDialogText("ENAMEL:# Oh,# sure.")
            doDialogText("        What should I be in charge of?")
            doDialogText("YOU:# Well,# we need one more person to do art,# but I don't really know anyone else.")
            doDialogText("     Think you can do it?")
            doDialogText("ENAMEL:# Uhh,# I've never drawn anything before.#.#.# like seriously.")
            doDialogText("YOU:# Well.#.#.#")
            doDialogText("ENAMEL:# Will I get to talk tho?")
            doDialogText("YOU:# Uhh,# yeah sure.")
            doDialogText("ENAMEL:# Can I AURAFARM?")
            doDialogText("YOU:# What?# Uhhh,# sure?")
            doDialogText("ENAMEL:# Yes!# Okay,# I'll join your team.# Thanks!")
            doDialogText("YOU:# No.#.#.# problem.", afterdelay=3)

            print()
            doDialogText("ENAMEL was added to your team.")



        # Holy discussion time
        # DISCUSSION TIME

        doDialogText("(Okay,# I found everyone.)")
        doDialogText("(Should we start discussing the tasks?)")
        doDialogText("(.#.#.# no harm in starting early.)")
        print()
        doDialogText("You call everyone to your desk.")

        print()
        topics = {
            'ADITHYA': "SEVEN WONDERS OF THE WORLD",
            'TENMAY': "MOTIVATION AND DETERMINATION",
            "TEJAS": 'THE HISTORY OF TEA',
            'EARWIND': "THEORY OF RELATIVITY",
            'ENAMEL': "RACISM AND DISCRIMINATION"
        }

        doDialogText("YOU:# Alright everyone,# what should the topic be?")

        c = 0
        global chosenOne
        chosenOne = 'SD CARD'
        for guy in topics:
            if guy in route5['team']:
                c += 1

                if c == 1: chosenOne = guy

                if guy == "ADITHYA":
                    doDialogText("ADITHYA:# Easy.# The Seven Wonders of the World.")
                elif guy == "TENMAY":
                    doDialogText("TENMAY:# Let's present a simple but crucial element:# Motivation and Determination.")
                elif guy == "TEJAS":
                    doDialogText("TEJAS:# I like chai,# what if we present on The History of Tea?")
                elif guy == "EARWIND":
                    doDialogText("EARWIND:# I was thinking about the Theory of Relativity.#.#.#")
                    doDialogText("         It may be a complex topic,# but I could explain it well.")
                    if 'ADITHYA' in route5['team']:
                        doDialogText("ADITHYA:# Well you better explain it to me buddy,# or we're all cooked.")
                elif guy == "ENAMEL":
                    doDialogText("ENAMEL:# Let's talk about Sexism, and how women have been-", afterdelay=0)
                    doDialogText("EVERYONE:# NO.")
                    doDialogText("ENAMEL:# Fine,# just racism then.")
                    doDialogText("EVERYONE:# better.")
        
        if c == 0:
            doDialogText(".#.#.#")
            doDialogText("YOU:# So uh,# no one has an idea?")
            doDialogText("     That's fine.#.#.# I got one.")
            doDialogText("     'How to bake a cake?'")
            if pgFilter:
                doDialogText("EVERYONE:# That's kinda ass ngl.")
            else:
                doDialogText("EVERYONE:# That's cringe ngl.")
            doDialogText("YOU:# Well does anyone else have a better idea?")
            doDialogText("EVERYONE:# .#.#.#")
            doDialogText("YOU:# That's what I thought.")
        else:
            doDialogText(f"YOU:# Well,# let's go with {topics[chosenOne]}.# Any objections?")
            doDialogText("EVERYONE:# Nope.")
            doDialogText("YOU:# Okay,# that settles the topic discussion.")
            doDialogText("     Everyone,# let's get to work!")
        
        print()
        doDialogText(f"You and team {saveFile['name'].upper()} get to work on the topic.")
        doDialogText(".#.#.#")
        
        # EARLY EVALUATION
        presentationPoints = 5

        for member in route5['team']:
            if member in   ['ADITHYA',    'ANNA',    'EARWIND', 'FRIEDEL']:
                presentationPoints += 5
            elif member in ['A.R RAHMAN', "SAHUR",   'TEJAS',   'JANET']:
                presentationPoints += 4
            elif member in ['SIBI',       'TENMAY',  'AWAITH',  'FARWANA']:
                presentationPoints += 3
            elif member in ['SAVAN',      'WAYDANT', 'KICHAN',  'SURYA']:
                presentationPoints += 2
            elif member in ['BAPPE',      'DEBAYAN', 'ASHAK',   'ENAMEL']:
                presentationPoints += 1

        # SYNERGIES + DESYNERGIES
        if 'ADITHYA' in route5['team']:
            doDialogText("(Adithya's taking the lead and being rather assertive.)")
            doDialogText("(As much as I'd rather not say,# but he is being a good leader.)")
            doDialogText("(But he doesn't leave much room for me to help coordinate everyone,# so I'm basically jobless.)")
            
            if 'EARWIND' in route5['team']:
                doDialogText("(.#.#.#Atleast he seems to get along with EARWIND.# That's a plus.)")
                presentationPoints += 2
            print()
            presentationPoints -= 3

        
        if 'AWAITH' in route5['team'] and 'SIBI' in route5['team']:
            doDialogText("You look over to another corner and see SIBI and AWAITH talking.")
            doDialogText("They may look like they're just talking,# but they're actually blasting away with productivity.")
            print()
            presentationPoints += 4

        if 'BAPPE' in route5['team'] and 'KICHAN' in route5['team']:
            doDialogText("You notice BAPPE and KICHAN working together.")
            doDialogText("KICHAN is helping BAPPE memorise the lines.")
            print()
            presentationPoints += 3

        if 'EARWIND' in route5['team'] and 'A.R RAHMAN' in route5['team']:
            doDialogText("EARWIND and A.R RAHMAN are also having a good time.#.#.#")
            doDialogText(".#.#.# though EARWIND gets weirded out sometimes.")
            print()
            presentationPoints += 1
        
        if 'SAVAN' in route5['team'] and 'SAHUR' in route5['team']:
            doDialogText("SAVAN and SAHUR are getting along.#.#.# more than you expected.")
            print()
            presentationPoints += 2
        
        if 'SIBI' in route5['team'] and 'FARWANA' in route5['team']:
            doDialogText("SIBI and FARWANA don't seem to sit well together.")
            print()
            presentationPoints -= 3
        
        if 'ASHAK' in route5['team']:
            doDialogText("You can see ASHAK on his phone.#.#.#")
            if 'ENAMEL' in route5['team']:
                doDialogText("You can also see ENAMEL next to him telling him what to browse.")
                presentationPoints += 2

                if 'TENMAY' in route5['team']:
                    doDialogText("TENMAY is also telling him what to search,# but it doesn't look like he's seraching anything presentation-related.")
            doDialogText("(Hope he doesn't get caught.#.#.#)")
            print()

        stopSong()
        # LIBRARY TIME
        doDialogText("You decide to stay after school to do some more research.")
        
        if saveFile['route3']['rude_stay'] == 'FORGIVED':
            doDialogText("You receive a tap on your shoulder.")
            doDialogText("ASHISH:# Hi!")
            doDialogText("YOU:# Oh,# Hi ASHISH.")
            doDialogText("ASHISH:# How's the presentation going?# I saw you already have a full team.")
            doDialogText(f"YOU:# Yeah.# I was just researching right now with {route5['team'][2]}.")
            doDialogText("ASHISH:# Ah.# SARBATH and I still need two more people.")
            doDialogText("YOU:# Oh,# hope you find them soon.")
            doDialogText("ASHISH:# Thanks.# Wishing you good luck for the presentation.")
            doDialogText("YOU:# You too.", afterdelay=3)
            
            print()
            doDialogText("(That was a very dry conversation.#.#.)")
            doDialogText("(Do I make an abrupt decision?)")
            print()
            ch = doDialogChoice("Ask him out?")

            if ch == 1:
                route5['date'] = True
                if saveFile['route1']['name_choice'] in ['NORMAL', 'RUDE']:
                    doDialogText("YOU:# Hey-# wait!")
                    doDialogText("ASHISH:# Yeah?")
                    doDialogText("YOU:# U-Um.#.#.")
                    if pgFilter: doDialogText("(Shit.#.#.# what do i say?)")
                    else: doDialogText("(Ahh.#.#.# what do i say?)")
                    doDialogText("YOU:# Do you.#.#.# like.#.# wanna hang out sometime later?# Like after school or something?", spd=5)
                    doDialogText("ASHISH:# Oh,# um.#.#")
                    doDialogText("        S-#Sure.")
                    doDialogText("YOU:# Oh, okay so how about we meet at Johnny's cafe on saturday?")
                    doDialogText("ASHISH:# That works for me.")
                    doDialogText("YOU:# So.#.#.# it's a date then?")
                    doDialogText("ASHISH:# H-#Hahaha,# um.#.#.#")
                    doDialogText("        Yeah,# like a date.")
                    doDialogText("YOU:# Great.# See you then.")
                    doDialogText("ASHISH:# Yeah.#.# b-#bye.")
                    print()
                    doDialogText("(.#.#.#)", afterdelay=3)

                    if pgFilter:
                        doDialogText("(WHAT THE FUCK WAS THAT?!?!?# WHY DID I CALL IT A DATE?!?!)")
                        doDialogText("(THAT'S SO GAY,# BRUHH.)")
                        doDialogText("(AHHHHHH,# HE'S GONNA THINK IM GAY!")
                    else:
                        doDialogText("(AAAAAA WHY DID I CALL IT A DATE?!?!?!# I'M SO WEIRD!!)")
                    
                    doDialogText("(.#.#.#ugh,# lets just forget about it.# We hang out on saturday,# lets not ruin that.)")
                else:
                    doDialogText("YOU:# Hey-# wait!")
                    doDialogText("ASHISH:# Yeah?")
                    doDialogText("YOU:# Do you want to hang out some time later?")
                    doDialogText("ASHISH:# Uhh.#.# sure I'm free on saturday if it works.")
                    doDialogText("YOU:# Yeah that works for me.# So Saturday at Johnny's Cafe at 9?")
                    doDialogText("ASHISH:# Okay that works.# See ya on saturday!")
                    doDialogText("YOU:# You too.# And you better not think this is a date or anything!")
                    doDialogText("ASHISH:# Duh.# See ya.")
            else:
                route5['date'] = False
                doDialogText("You decide to keep your mouth shut.")

        print()
        doDialogText(".#.#.#")
        doDialogText("You notice ADITHYA approaching you again.")
        doDialogText("ADITHYA:# Sup.")
        
        if 'ADITHYA' in route5['team']:
            doDialogText("YOU:# Hey,# you need anything?")
        else:
            doDialogText("YOU:# What do you want?")

        doDialogText("ADITHYA:# Nah,# I just want to test ya.")
        doDialogText("YOU:# Test me?")
        doDialogText("ADITHYA:# Let's see how much you know about ASHISH.")
        doDialogText("YOU:# Oh brother.#.#.#")
        print()


        points = 0
        global negative
        negative = False
        doDialogText("ADITHYA: FIRST QUESTION:#")
        
        if saveFile['route3']['rude_stay'] != 'FORGIVED':
            doDialogText("YOU:# Nah,# I'm leaving.# Leave me out of this.")
            doDialogText("You leave the library.")
            doDialogText("ADITHYA:# Huh,# suspicious.#.#.#")
        else:
            q1 = doDialogChoice("Who does ASHISH spend the most time with?", choices=['EARWIND', 'SARBATH', f'ME ({saveFile['name'].upper()})', 'He\'s always lonely.'])

            if q1 == 1:
                doDialogText("ADITHYA:# WRONG!# Though they are good friends,# ASHISH doesn't spend as much time with EARWIND as much as he does with:# SARBATH.")
                doDialogText("YOU:# Oh.# I see now.")
                print()
                doDialogText("ADITHYA:# 0 POINTS!# Better try again on the next question.")
                doDialogText("NO POINTS WERE ADDED TO YOUR POINTS.#.#.##?")
            elif q1 == 2:
                doDialogText("ADITHYA:# Well done.# ASHISH spends most of the time with SARBATH - # His tuition buddy.")
                doDialogText("         +1 POINTS for you.")
                print()
                doDialogText("1 POINT(s) HAS BEEN ADDED TO YOUR.#.#.# POINTS?")
                points += 1
            elif q1 == 3:
                if pgFilter:
                    doDialogText("ADITHYA:# HELL NO.")
                else:
                    doDialogText("ADITHYA:# Heck no.")
                doDialogText("         You wish.# The answer's SARBATH.")
                doDialogText("         I should introduce negative marking because of what you just said.")
                print()
                negative = True
                doDialogText("NEGATIVE MARKING HAS BEEN ENABLED.#.#.#?")
                doDialogText("Any wrong answer you make will reduce ONE POINT from your current POINTS.")
            elif q1 == 4:
                doDialogText("ADITHYA:# Come on,# he isn't as miserable as you.")
                doDialogText("         The answer is SARBATH,# his tuition buddy.")
                doDialogText("YOU:# Oh.")
                print()

                doDialogText("ADITHYA:# 0 POINTS!# Better try again on the next question.")
                doDialogText("NO POINTS WERE ADDED TO YOUR POINTS.#.#.##?")
            
            doDialogText("YOU:# Points?# Are you serious?")
            doDialogText("ADITHYA:# Hey,# it makes it better for the both of us.# Now shush and let's move onto the next question.")
            print()

            doDialogText("ADITHYA:# QUESTION 2:")
            q2 = doDialogChoice("What book does ASHISH use the most?", choices=['NCERT','PHYSICS GALAXY', 'CENGAGE'])

            if q2 == 1:
                doDialogText("ADITHYA:# WRONG!# The answer's CENGAGE.")
                if negative:
                    doDialogText("         -1 points for you!")
                    print()
                    doDialogText("ONE POINT WAS DEDUCTED FROM YOUR POINTS.")
                    points -= 1
                    doDialogText(f"YOU NOW HAVE:# {points} points.")
            elif q2 == 2:
                doDialogText("ADITHYA:# That's.#.#.# a good point actually.")
                doDialogText("         I think he recently started using that book more.")
                doDialogText("         I'll let you off the hook on this one.")
                points += 1
                doDialogText(f"YOU NOW HAVE:# {points} POINTS.")
            elif q2 == 3:
                doDialogText("ADITHYA:# Correct!# It's CENGAGE!")
                doDialogText("ONE POINT WAS ADDED TO YOUR POINTS.")
                points += 1
                doDialogText(f"YOU NOW HAVE:# {points} POINTS.")
            print()
            
            doDialogText("ADITHYA:# QUESTION 3:")
            q3 = doDialogChoice("What is ASHISH's shoe size?", choices=['5','6', '7', '8'])

            if q3 in [2, 3]:
                doDialogText("ADITHYA:# I'm not sure about this one either,# I believe it's a six or seven.")
                doDialogText("         I'll give you the point.")

                doDialogText("ONE POINT WAS ADDED TO YOUR POINTS.")
                points += 1
                doDialogText(f"YOU NOW HAVE:# {points} POINTS.")
            else:
                doDialogText("ADITHYA:# INCORRECT.# ASHISH isn't that size for sure.")
                doDialogText("         It's either a six or a seven.")
                if negative:
                    doDialogText("         -1 points for you!")
                    doDialogText("ONE POINT WAS DEDUCTED FROM YOUR POINTS.")
                    points -= 1
                    doDialogText(f"YOU NOW HAVE:# {points} points.")
            
            if points == 3:
                doDialogText("ADITHYA:# Well done,# you flawlessly passed the test.")
                doDialogText("YOU:# How do you have this much info on Ashish?")
                doDialogText("ADITHYA:# Anyways,# despite confirming my suspicions,# I'll give you a reward for clearing my test.")
                
                route5['key'] = True
                print()
                doDialogText("YOU RECEIVED MUSIC ROOM KEY.")
                doDialogText("YOU:# Hey,# you still haven't-", afterdelay=0)
                doDialogText("ADITHYA:# Anyway,# I've ought to head home.### It's getting late after all.", spd=2, afterdelay=0.5)
                doDialogText("         BYE!!")
                doDialogText("YOU:# Suspicious...")
                print()
                doDialogText("You look down at the key he gave you.")
                doDialogText("YOU:# Where does this key lead to anyways?")
                print()
                doDialogText("YOU:# .#.#.#")
                route5['test'] = 'PERFECT'
            elif points >= 0:
                doDialogText("ADITHYA:# Well.#.# not bad.# The situation could've been worse.")
                doDialogText("YOU:# How do you have this much info on Ashish-", afterdelay=0)
                doDialogText("ADITHYA:# Anyway,# I've ought to head home.### It's getting late after all.", spd=2, afterdelay=0.5)
                doDialogText("         BYE!!")
                print()
                doDialogText("YOU:# .#.#.#")
                route5['test'] = "OK"
            elif points < 0:
                doDialogText("ADITHYA:# Well,# this is laughable.# You have like negative points.")
                doDialogText("YOU:# How do you have this much info on Ashish-", afterdelay=0)
                doDialogText("ADITHYA:# Anyway,# I've ought to head home.### It's getting late after all.", spd=2, afterdelay=0.5)
                doDialogText("         BYE!!")
                print()
                doDialogText("YOU:# .#.#.#")
                route5['test'] = "COOKED"
                
            
            doDialogText("YOU:# Guess I'll go home as well then.")
            print()
            doDialogText("From the corner of your eye,# you catch someone staring.")
            doDialogText("A.R RAHMAN quickly looks away.", afterdelay=2)
            print()

        save1 = getPrompt("Save this chapter here?")
        if save1:
            route5["index"] = 1
            saveFile["route5"] = route5
            try:
                saveGame(curSaveName, saveFile)
                doDialogText("The game was saved.")
            except:
                doDialogText("There was an error in saving the game.")
        
        continue1 = getPrompt("Continue your journey?")
        if continue1:
            index = 1 # Second part
            doDialogText("Continuing from LIBRARY.#.#.#")
        
        print()

    if index == 1:
        

        doDialogText("PART TWO:### SATURDAY.", spd=6)
        print()
        doDialogText("Well,# it's saturday.")

        if saveFile['route5']['date']: # YOU'VE GOT YOURSELF A DATE!
            doDialogText("You've got a \"date\" with ASHISH.# Get ready.")
            wear = doDialogChoice('What do I wear?', choices=['Dress Casual', 'Dress Fancy', 'Go Naked', 'Wear a friggin suit and tie'])

            if wear == 3:
                doDialogText("(I'M NOT GOING NAKED.)")
                doDialogText(".#.#.#")
                wear = 1

            if wear == 1:
                doDialogText("(Guess I'll just dress casual.)")
                doDialogText("You pick out a T-shirt from your closet and choose some modest pants.")

            elif wear == 2:
                doDialogText("(Why not put on something fancy?)")
                doDialogText("You pick out your best shirt and ironed pants.")
                doDialogText("You fetch your NIKE Air Force Shoes you got for a steal.")
                doDialogText("There's also a flower pot on top of the shoe rack.")
                doDialogText("(Do I bring a flower?)")
                doDialogText("(No,# that's too weird-)", afterdelay=0)
                doDialogText("MOM:# Woah,# look at you.# Where are you going out dressed like this?")
                doDialogText("YOU:# O-#oh mom.#.# I'm going to hang out with a friend.#.#.#")
                doDialogText("MOM:# Looking at you,# I thought you were going on a date.")
                doDialogText("     Might as well take that flower with you.")
                doDialogText("YOU:# Mom.#.#.#")
                doDialogText("MOM:# Well,# I'll be leaving for work now.# Make sure to tell dad you're \"hanging out\" with your friends.")
                doDialogText("YOU:# I will.#.#.#")
                doDialogText("(What if I just bring the flower anyways.#.#.#)")
                doDialogText("You pick up the flower pot.#.#.# and found 500 Rupees beneath it.")
                doDialogText("(WOAH.# I forgot I left this money here.)")
                doDialogText("(Seems like a sign.)")
                doDialogText("You ultimately decide to bring the flower.")
            
            elif wear == 4:
                doDialogText("(Really?# A Suit and Tie?)")
                doDialogText("(Alright.#.#.#)")
                doDialogText("(Where do I even get a suit and tie tho?)")
                doDialogText("(There's probably some in my dad's closet.)")
                print()
                doDialogText("You prepare to sneak into your dad's room.")
                doDialogText("YOU:# Okay,# my dad should have left for work by now.")
                doDialogText("     Maybe I can borrow his suit for a while.")
                doDialogText("You open dad's closet.")
                doDialogText("YOU:# .#.#.# or suits.#.#.#")
                doDialogText("      There are so many different suits.#.#.#")
                doDialogText("      Theres a black suit,# a dirty white suit which looks like it was worn on a bad party.#.#.#")
                doDialogText("      There's a green suit with polka dots?!?!")
                doDialogText("      WHY DOES HE HAVE TWO RAINBOW COLORED SUITS?!?!")
                print()
                doDialogText("DAD:# What are you looking for?")
                if pgFilter: doDialogText("YOU:# Oh shit-", afterdelay=0)
                else: doDialogText("(Oh no.#.#.#)")
                doDialogText("You turn around so fast you almost snap your neck.")
                doDialogText("DAD:# Why are you going through my suit closet?")
                doDialogText("YOU:# Uh-# Ummm.#.#.#", spd=7)
                doDialogText("DAD:# Wait.#.#.# dont' tell me.#.#.#")
                doDialogText("YOU:# Tell you what?", spd=6)
                doDialogText("DAD:# Ofcourse.#.#.# It's already time.")
                doDialogText("     You have a date,# right?")
                doDialogText("YOU:# W-#WHAT", afterdelay=0.3)
                doDialogText("     NO its nothing like that.")
                doDialogText("DAD:# Say no more ,# son.")
                doDialogText("     I have exactly what you need.")
                doDialogText("YOU:# .#.#.#what?")
                doDialogText("Dad reveals a secret compartment in his closet,# which opens up to a suit.")
                doDialogText("DAD:# It's about time I pass down my secret down to you.")
                doDialogText("YOU:# What secret?")

                doDialogText("DAD:# Son,# I want you to sit down for this one.")
                doDialogText("YOU:# Dad,# what are you talking about-", afterdelay=0)
                print()
                print("DAD: ", end='')
                doDialogText("Son.", spd=6)
                doDialogText("You sit down on a chair.")

                playSong("assets/soundtrack/doubted.ogg", looping=True)
                doDialogText("DAD:# It's about time I tell you about my life.")
                print()
                doDialogText("DAD: ==")
                doDialogText("I was once,# when your age,# a very lovestruck man.")
                doDialogText("I was a very awkward guy,# I bumped into people often.")
                doDialogText("One day,# I bumped into a girl.# Her name was MAYA.")
                doDialogText("She didn't laugh at me,# but she helped me pick up the stuff I dropped.")
                doDialogText("From that day,# we became friends.")
                doDialogText("We would talk sometimes,# and somedays we just waved at each other.")
                doDialogText("Im sure,# that to her,# we were just friends.#.#.#")
                doDialogText("But me.#.#.# I was in LOVE.")
                doDialogText("MAYA was my first love in my whole life,# way before I even met your mother.#.#.#", afterdelay=2)
                print()
                doDialogText("But I was OBSESSED.")
                print()
                doDialogText("I started thinking we were meant for each other,# and that it was upto me to take the right decisions.")
                doDialogText("But I didn't.")
                doDialogText("I fell into a fake vision,# convincing my role was to protect her from any danger.")
                doDialogText("I called myself her savior,# her protector.#")
                doDialogText("I swore I would protect her and never let her get close to harm's way.")
                doDialogText("But as you can probably guess,# she soon started distancing herself from me.")
                print()
                doDialogText("But I didn't back down.")
                print()
                doDialogText("I started following her around,# making sure she was safe.")
                doDialogText("I had intended to do no harm around her.")
                doDialogText("Since she stopped talking to me,# so did I.")
                doDialogText("I never went close to her,# and watched her from a distance.")
                doDialogText("On one particular day,# I noticed a strange man following her.")
                doDialogText("He was slowly following her while she hung out with her friends.")
                doDialogText("He was there,# even when she was alone.")
                doDialogText("Slowly following her.#.#.### with a knife in his hands.")
                doDialogText("I decided that one day,# I must strike.")
                doDialogText("And that day soon came.")
                doDialogText("On that fateful day,# I was prepared.")
                doDialogText("I didn't go empty handed - #I was armed with a metal bat.")
                doDialogText("I jumped at the man,# and hit him on the head.")
                doDialogText("I kept swinging at him,# while yelling to MAYA to run.")
                doDialogText("And run,# she did.")
                print()
                doDialogText("She ran.#.#.# to her father.", afterdelay=2)
                print()
                doDialogText("She seperated me from her father,# and clinged to the very person I thought was protecting MAYA from.")
                doDialogText("This was the worst mistake of my life.", spd=6)
                print()
                doDialogText("Very soon,# I was stabbed,# and jumped by the crowd of people around me.")
                doDialogText("My life became a ruin.# I went to prison for 5 years for aggravated assault,# which left a permanent mark on my life.")
                doDialogText("Colleges wouldn't accept me,# and I could find no job.")
                print()
                doDialogText("I was surely wrecked for life.", afterdelay=2)
                print()
                doDialogText("But then,# one day,# my life changed.")
                doDialogText("Somehow,# I got an interview at a job.")
                doDialogText("I knew first impressions were especially critical in this case,# so I went to look for the best outfit.")
                doDialogText("I tidied up my vocabulary,# my attitude,# everything which I could change.")
                doDialogText("All I needed were proper clothes.")
                print()
                doDialogText(f"Just like you did,# {saveFile['name']}, I looked through my late father's closet,# and found a suit.")
                doDialogText("A Dark Blue suit,# which fitted me perfectly.")
                doDialogText("This would soon become my lucky suit,# as to every interview or important meeting I went to with this suit,# I left the best impression I could.")
                doDialogText("I got my first job very easily,# as an accountant.")
                doDialogText("I used my lucky suit to pick my life back up,# and soon start my own business.")
                doDialogText("After I used up the suit,# it no longer fit me.# But by then,# I was stable enough to no longer need to rely on it.")
                doDialogText("So It's about time I pass it on to you.# Make great use of it.")
                doDialogText("I shall leave for work now.")
                stopSong()
                print()
                doDialogText(".#.#.#")
                if pgFilter: doDialogText("YOU:## DAD,# WHAT THE FUCK-", spd=1)
                print()
                doDialogText("*sigh*")
                doDialogText("You decide to get ready for the \"date\".")
                doDialogText("MOM:# Woah,# look at you.# Looking dapper in your father's old suit.")
                doDialogText("YOU:# O-#oh mom.#.# I'm going to hang out with a friend.#.#.#")
                doDialogText("MOM:# Looking at you,# I thought you were going on a date.")
                doDialogText("     Might as well take that flower with you.")
                doDialogText("YOU:# Mom.#.#.#")
                doDialogText("MOM:# Well,# I'll be leaving for work now.# Make sure to tell dad you're \"hanging out\" with your friends.")
                doDialogText("YOU:# He knows.#.#.#")
                doDialogText("(What if I just bring the flower anyways.#.#.#)")
                doDialogText("You pick up the flower pot.#.#.# and found 500 Rupees beneath it.")
                doDialogText("(WOAH.# I forgot I left this money here.)")
                doDialogText("(Seems like a sign.)")
                doDialogText("You ultimately decide to bring the flower.")


            
            doDialogText(".#.#.#", spd=6)

            playSong("assets/soundtrack/third_meet.ogg", looping=True)
            doDialogText("You're at Johnny's Cafe now.")
            doDialogText(".#.#.# !# You spot ASHISH under a small tree!")
            doDialogText("He's wearing his Atlanta T-Shirt along with a pair of jeans.")
            doDialogText("YOU:# Hey!")
            doDialogText("ASHISH:# Oh,# you're here!")

            if wear == 2:
                doDialogText("ASHISH:# Nice outfit!")
                doDialogText("YOU:# Thanks.")
            elif wear == 4:
                doDialogText("ASHISH:# uhm...#.#.#")
                doDialogText("        interesting outfit choice.", spd=5)
                doDialogText("YOU:# Don't mind it.", spd=5)

            doDialogText("ASHISH:# You got the money and stuff,# right?")
            doDialogText("YOU:# Yeah,# Ofcourse I do.# Lets head in!")
            print()
            doDialogText("You and ASHISH sit down at a table in Johnny's Cafe.")
            doDialogText("As you sit down,# a waiter approaches your table.")
            doDialogText("SIDHARTH:# How may I-", afterdelay=0.6)
            doDialogText("          wait.#.#.#", spd=6, line=False)
            doDialogText(" I know you guys!")
            doDialogText("ASHISH:# Woah,# you work here?")
            doDialogText("YOU:# Aren't you SIDHARTH KRISHANTH from the other class?")
            doDialogText("SIDHARTH:# Yes.#.#.#", spd=5, line=False)
            doDialogText(" please don't tell anyone,# i could get fired.", spd=3)
            doDialogText("          Anyways,# what can I get for you guys?")
            doDialogText("ASHISH:# Lemme look at the menu.#.#.#")

            drinks = ["Johnny's Powerhouse Coffee", "Johnny's Chilled Mint Lime", "Johnny's Neutron Star Milkshake"]
            drinkChoice = doDialogChoice("What will you order? (drinks)", choices=drinks)
            drink = drinks[drinkChoice-1]

            doDialogText("YOU:# .#.#.#what are these names?")
            doDialogText("ASHISH:# I guess it's the theme of the cafe?")
            doDialogText("        I'll have the Milkshake, please!")
            doDialogText(f"YOU:# Uh.#.#.# I'll have the {drink}.")
            doDialogText("SIDHARTH:# Great!# Anything to eat?")

            snacks = ["Johnny's Spiced Pumpkin Pie", "Johnny's Choco Chip Cookies", "Johnny's Savoury Popsicle"]
            snackChoice = doDialogChoice("What will you order? (snacks)", choices=snacks)
            snack = snacks[snackChoice-1]

            doDialogText("YOU: ... these names are really.#.#.#")
            doDialogText("     ...johnny.#.#.#")
            doDialogText(f"     I guess I'll have the {snack} then.")
            doDialogText("ASHISH:# Can I have today's special?")
            doDialogText("SIDHARTH:# The Special.#.#.#", spd=5)
            doDialogText("          The special for today has been the same as it is always.#.#.#")
            doDialogText("          ... Johnny's Love.")
            doDialogText("ASHISH:# Johnny's.#.#.# what?")
            doDialogText("YOU:# what kind of names are these???")
            doDialogText("SIDHARTH:# I'll be right back with your orders.")
            doDialogText("SIDHARTH hurries back into the kitchen.")
            doDialogText("ASHISH:# I guess we wait now.")
            doDialogText("YOU:# yeah.")
            print()
            doDialogText(".#.#.#", spd=5)
            doDialogText("ASHISH:# So,# how's your presentation coming along?")
            doDialogText("YOU:# Oh yeah.#.#.# it's coming along.#.#.# alright,# I guess.")
            doDialogText("     I don't know how good of a leader I am.# Besides,# I can do literally nothing other than motivate others.")
            doDialogText("ASHISH:# Hey,# I'm sure you're not a bad leader.# I've looked at the other teams,# lol.")
            doDialogText("YOU:# lol.# We're just getting the script ready.")
            doDialogText("ASHISH:# That's nice!# We've started rehearsing for our presentation.")
            doDialogText("YOU:# Oh,# damn.# You guys must be pretty ahead.")
            doDialogText("ASHISH:# No way,# the script isn't final and the presentation isn't even done.# We're just rehearsing what we have so far.")
            doDialogText("        Every practice feels awkward,# and I'm pretty sure most of the stuff is gonna change.")
            doDialogText("        But I'd say SARBATH is doing a pretty good job as a leader.")
            doDialogText("YOU:# SARBATH,# huh?")
            doDialogText("ASHISH:# Yeah!# Everyone gets along with him!# He may not be the best at it,# but I'd say he's doing a great job.")
            doDialogText("YOU:# I hope I'm being a good leader.")
            doDialogText("ASHISH:# Don't worry about that.# Just try your best.")
            doDialogText("        By the way,# how's things going on your end?")
            doDialogText("YOU:# Uh.#.#.# we're actually almost done with our presentation.")
            doDialogText("ASHISH:# Woah,# already?# That's really fast!")
            doDialogText("YOU:# Yeah,# I guess we did start SUPER early after all.")
            doDialogText("ASHISH:# What topic are you presenting?")

            topics = {
                'ADITHYA': "SEVEN WONDERS OF THE WORLD",
                'TENMAY': "MOTIVATION AND DETERMINATION",
                "TEJAS": 'THE HISTORY OF TEA',
                'EARWIND': "THEORY OF RELATIVITY",
                'ENAMEL': "RACISM AND DISCRIMINATION"
            }

            topic = 'HOW TO BAKE A CAKE'
            for topicguy in topics:
                if topicguy in route5['team']:
                    topic = topics[topicguy]
                    break
            else:
                topic = 'HOW TO BAKE A CAKE'
            
            doDialogText(f"YOU:# {topic}.")
            if topic == "SEVEN WONDERS OF THE WORLD":
                doDialogText("ASHISH:# Oh,# nice!")
                doDialogText("YOU:# It was ADITHYA's idea.")
                doDialogText("ASHISH:# Oh,# ADITHYA's on your team?")
                doDialogText("YOU:# Yeah,# I figured why not,# maybe try to get on better terms?")
            elif topic == "MOTIVATION AND DETERMINATION":
                doDialogText("ASHISH:# Oh,# that's a very inspirational topic.")
                doDialogText("YOU:# Yeah,# TENMAY came up with it.")
                doDialogText("ASHISH:# Oh,# nice.")
            elif topic == "THE HISTORY OF TEA":
                doDialogText("ASHISH:# Woah,# interesting.")
                doDialogText("YOU:# TEJAS came up with it.# He provided most of the facts.# He knows quite a bit about tea.")
                doDialogText("ASHISH:# That he does.# I see him drinking tea everyday.")
            elif topic == "THEORY OF RELATIVITY":
                doDialogText("ASHISH:# Oh,# that's a pretty advanced topic.")
                doDialogText("YOU:# ARAVIND came up with it.# He's pretty excited about it.")
                doDialogText("     He tried explaining it to us,# but I'm not sure I grasp the entire thing yet.")
                doDialogText("     Let's hope we can present in a way everyone understands it.")
            elif topic == "RACISM AND DISCRIMINATION":
                doDialogText("ASHISH:# Oh,# that's a great topic to present.")
                doDialogText("YOU:# ENAMEL came up with it.")
                doDialogText("     I just hope the presentation's not too.#.#.# one sided.")
            else:
                doDialogText("ASHISH:# that's.#.#.# uh.#.#.#")
                doDialogText("YOU:# I know.# I came up with it.")
                doDialogText("ASHISH:# .#.#.#it's not exactly a bad one.#.#.#")
                doDialogText("YOU:# Well,# no one had any objections,# so we just went with it.")
                doDialogText("ASHISH:# Oh.#.#.# well,# good luck with your topic.")
                doDialogText("YOU:# thanks.")
            print()
            doDialogText(".#.#.#")
            doDialogText("(Awkward silence.#.#.#)", afterdelay=2)
            
            talkChoices = ["Ask about ADITHYA", "Ask about DEBAYAN", "Ask about SARBATH", "Ask about FANTASY GANG", "Wait for the food."]
            while talkChoices:
                talkC = doDialogChoice("Talk about something?", choices = talkChoices)
                print()
                curTalk = talkChoices[talkC-1]
                if curTalk == "Ask about ADITHYA":
                    doDialogText("YOU:# ... What do you think about ADITHYA?")
                    doDialogText("ASHISH:# Uh,# ADITHYA.#.#.# He's a little strange.")
                    doDialogText("        He says he's known me before,# but I can't remember anything about him.#.#.#")
                    doDialogText("        Honestly,# mostly everyone in this class is new to me,# but he does seem to know some things about me.")
                    doDialogText("YOU:# Do you think he could be lying?")
                    doDialogText("ASHISH:# No.#.#.# probably not.")
                    doDialogText("        I think he probably knows me.# I've probably met him before.#.#.#")
                    doDialogText("        ...but I really don't remember him.")
                    print()

                    talkChoices.remove(curTalk)
                if curTalk == "Ask about DEBAYAN":
                    doDialogText("YOU:# .#.# so,# I noticed you have started talking to DEBAYAN a lot more lately.")
                    doDialogText("ASHISH:# Oh yeah!# He's actually a HUGE nerd.# He goes to the same study center as SARBATH and I,# but right now he's in a different class.")
                    doDialogText("        I wish next year,# we all could be in the same class.# Then we could discuss and do questions together!")
                    doDialogText("YOU:# Hmm,# so are you guys best friends?")
                    doDialogText("ASHISH:# Ehh,# it's more like SARBATH and DEBAYAN are best friends.")
                    doDialogText("        But who knows,# he might become my best friend!")
                    print()

                    talkChoices.remove(curTalk)
                if curTalk == "Ask about SARBATH":
                    doDialogText("YOU:# So,# How is SARBATH as a leader?")
                    doDialogText("ASHISH:# I'd say he's a pretty good leader,# but he denies it.")
                    doDialogText("YOU:# Oh.# I haven't really talked to him yet,# what is he like?")
                    doDialogText("ASHISH:# He HAS to be the smartest guy in the class,# atleast when it comes to studying.")
                    doDialogText("        But despite being a nerd,# he's actually quite fun to hang around with!# Hes very nice and funny.")
                    doDialogText("        He's super likeable,# and everyone in our team gets along with him.")
                    doDialogText("YOU:# Woah.#.#.# he seems like a pretty chill guy.")
                    print()

                    talkChoices.remove(curTalk)
                if curTalk == "Ask about FANTASY GANG":
                    doDialogText("YOU:# Hey,# do you know anything about the FANTASY gang?")
                    doDialogText("ASHISH:# I don't know much,# all I know about it is what I've heard from my friends.")
                    doDialogText("        I just know that ADITHYA formed it recently with five other people,# and that they hate you for some reason.")
                    doDialogText("YOU:# wait wait,# five OTHER people?")
                    doDialogText("ASHISH:# Yeah?")
                    doDialogText("YOU:# I was actually introduced to the FANTASY GANG,# but I swear it had like five people in total.")
                    doDialogText("     ADITHYA,# A.R RAHMAN,# SAVAN,# TEJAS,# and EARWIND.")
                    doDialogText("ASHISH:# Oh,# those are the FANTASY GANG members?# I swear I heard it had six members tho.#.#.#")
                    doDialogText("YOU:# Maybe there's a hidden member?")
                    print()

                    talkChoices.remove(curTalk)
                if curTalk == "Wait for the food.":
                    talkChoices = []
            doDialogText("You decide to pull out your phone and watch reels with ASHISH until the food comes.")
            doDialogText(".#.#.#", afterdelay=3)
            print()
            doDialogText("SIDHARTH:# Sorry for the wait!# Here's your food!")
            doDialogText("SIDHARTH arrives at our table with the snacks and drinks on his tray.")
            doDialogText("ASHISH:# Let's eat then!")
            print()
            doDialogText(f"You take a small bite of {snack}.")
            if snackChoice == 3: doDialogText("ASHISH:# Woah,# you BITE your popsicles?")
            doDialogText(".#.#.#")
            doDialogText("YOU:# It's really delicious!")
            doDialogText("ASHISH:# Wait lemme try.#.#.#")
            doDialogText("        .#.#.# Woah,# I love this!")
            doDialogText("YOU:# Yeah,# this is actually really good!")
            doDialogText("SIDHARTH:# I'm glad you like it.")
            doDialogText("          I still haven't brought the special,# so let me get that real quick.")
            doDialogText("SIDHARTH hurries back into the kitchen,# and almost trips on a little kid on the way.")
            doDialogText("You take a sip out of your drink.")
            doDialogText("YOU:# This drink also slaps!")
            doDialogText("ASHISH:# This milkshake is soo good!")
            print()
            doDialogText("You and ASHISH decide to take your time enjoying the food while waiting for SIDHARTH.")
            doDialogText("You look around in the scenery.# It's a nice atmosphere.")
            doDialogText("You can see kids playing in the distant ground from the Cafe.# They remind you of your youth.")
            doDialogText("Well,# technically you're still young,# but you know what you meant.")
            doDialogText("You look around in the cafe.# The place is packed with people.## Probably regulars of this place.")
            doDialogText("You can see a salesman outside the cafe.# He seems to be struggling to advertise his flyer.")
            if route5['COMPLETED']:
                doDialogText("The salesman momentarily stares at you for a brief moment before going back to advertising his flyer.")
                doDialogText("He's advertising more aggressively now.#")
                doDialogText("Soon after,# the owner of the shop scolds him for scaring away his customers.")
            
            doDialogText("You look back into the cafe.# There's all kinds of flowers in beatiful flower pots.")
            if wear in [2, 4]:
                doDialogText("(Oh right,# I have the flower with me.)")
                giveFlower = doDialogChoice("Give the flower to ASHISH?")

                if giveFlower == 1:
                    doDialogText("YOU:# Oh right,# uh,# here.")
                    doDialogText("You hand the flower to ASHISH.")
                    doDialogText("ASHISH:# ..?")
                    doDialogText("YOU:# I got it this morning,# so I figured why not give it to you?")
                    print()

                    if saveFile['route1']['name_choice'] in ['NORMAL', 'RUDE']:
                        doDialogText("ASHISH is blushing.")
                        doDialogText("ASHISH:# O-#oh,# um.#.#.#", spd=6)
                        doDialogText("        ...thanks.# I'll keep it.")
                        route5['flower'] = True
                        doDialogText("YOU:# you're.#.#.# welcome.", spd=5)
                        print()
                        doDialogText("The air of awkwardness returns to the scene.")
                    else:
                        doDialogText("ASHISH:# Oh,# uh...")
                        doDialogText("        Thanks,# I guess?")
                        doDialogText("YOU:# Yeah,# you can just keep it.")
                    doDialogText("You decide to keep looking around.")
                else:
                    doDialogText("You decide to keep the flower with you.")
            doDialogText("You listen to the whirring of the fans above you.")
            doDialogText("The fans here are gold plated.# In fact,# the entire cafe looks pretty expensive.")
            print()
            doDialogText(".#.#.#")
            print()
            doDialogText("SIDHARTH:# Once again,# sorry for the wait!")
            doDialogText("SIDHARTH is walking with a tray that's covered in a red cloth.")
            doDialogText("ASHISH:# Is that the special?")
            doDialogText("SIDHARTH unravels the cloth to reveal a dark,# heart shaped cake.")
            doDialogText("SIDHARTH:# Yes, this cake is the most special item in our cafe.")
            doDialogText("          It represents the love of our all-knowing Father up in the heavens,# watching over us.#.#.#")
            doDialogText("          And Father Johnny's care for the students of one of many generations.")
            doDialogText("          It's a cake that has been baked with love and courtesy,# and has a very special meaning for this cafe.")
            doDialogText("          Please,# try it.")
            doDialogText("You and ASHISH take a slice each.")
            doDialogText("ASHISH slowly takes a bite out of the cake.")
            doDialogText("He eats the slice very carefully,# trying to appreciate each bite.")
            stopSong()
            doDialogText("But the further he chews,# the more his facial expression crumbles.")
            doDialogText("ASHISH:# What.#.#.# is this...#?")
            doDialogText("You take a bite out of the cake.")
            doDialogText("You immediately spit out the cake.")

            if pgFilter: doDialogText("YOU:# W-what the heck?!# It's bitter as HELL!")
            else: doDialogText("YOU:# W-#what the heck?!# It's bitter!")
            playSong('assets/soundtrack/cake_lie.ogg', looping=True)
            doDialogText("SIDHARTH:# That's because I put a large amount of baking soda in it.")
            doDialogText("ASHISH:# W-#What?!")
            doDialogText("SIDHARTH:# You guys deserve to know the truth.# There's something wrong with this institution.")
            doDialogText("          This cafe is under Father Johnny,# PRINCIPAL of Devagiri High.")
            doDialogText("          But this entire area is under his name.# Even the \"owner\" of this cafe doesn't own anything.")
            doDialogText("          There's something wrong with Devagiri High.")
            doDialogText("YOU:# What?# What are you talking about?")
            doDialogText("SIDHARTH:# I'll let you guys in on a secret.# I'm a secret agent of the POLICE,# and I'm currently investigating the Devagiri Institutions.")
            doDialogText("          I'm undercover as a student of Devagiri High,# and have uncovered very suspicious evidence pointing to a massive scheme being pulled by Father Johnny.")
            doDialogText("          I'm also working at this Cafe to investigate more about Devagiri.# Everything about this place is suspicious.")
            doDialogText("          Not only as a member of the POLICE,# but also as a fellow \"Devagirian\".#.#.#")
            doDialogText("          I advise you to be very careful with Devagiri High.", afterdelay=3)
            print()
            doDialogText(".#.#.#")

            stopSong()

            doDialogText("YOU:# Alright man,# say whatever...", afterdelay=0.6)
            doDialogText("     But you didn't have to feed us a bitter cake for that.#.#.#")
            doDialogText("SIDHARTH:# You're very right,# I'm sorry.# I'll have the cake refunded.#")
            doDialogText("          Very sorry for your inconvenience.# Is there anything else you would like?")
            doDialogText("ASHISH:# No.#.#.# I think I'm full.")
            doDialogText("YOU:# Me too.# Shall we go?")
            doDialogText("ASHISH:# Yeah,# let's split the bill.")
            doDialogText("You and ASHISH split the bill and exit the cafe.")
            doDialogText("SIDHARHT:# *sigh*.#.#.#")
            doDialogText("          Well,# one crime for sure is that I'm being paid less than minimum wage.", afterdelay=3)
            print()

            doDialogText("YOU:# Well,# didn't know SIDHARTH was a police agent.")
            doDialogText("ASHISH:# Yeah.#.#.# I feel like he shouldn't have told us that.")

            if not route5['COMPLETED']:
                doDialogText('"YOUNG MEN!!!"', step=3, spd=6)
                doDialogText("There's a salesman calling you.")
                doDialogText("SALESMAN:# YOU TWO LOOK MIGHTY FINE ON SUCH A SATURDAY!", spd=6, step=3)
                doDialogText("YOU:# Uh,# can we help you?")
                doDialogText("SALESMAN:# Oh it's not you doing the helping,# its ME!", step=3, spd=6)
                doDialogText("          YOU SEE,# I'VE GOT THE PERFECT THING EVERY PERSON ON THIS PLANET NEEDS!", step=3, spd=3)
                doDialogText("          YOU HAVE TO GET IT!", spd=6, step=3)
                doDialogText("YOU:# Uh... whatever it is,# I'm not interested.")
                doDialogText("ASHISH:# Yeah,# no thanks.")
                doDialogText("SALESMAN:# .#.#.#", step=3, spd=6)
                doDialogText("You and ASHISH walk away.")
                doDialogText(".#.#.#", afterdelay=3)
                doDialogText("SALESMAN:# SO YOU TWO THINK YOU'RE THE MOST POWERFUL PEOPLE IN THE WORLD,# HUH?!?# IS THAT IT?", spd=6, step=2)
                doDialogText("YOU:# what?")
                doDialogText("SALESMAN:# YOU HAVEN'T EVEN HEARD WHAT I HAVE TO SAY,# YOU HAVEN'T EVEN# LOOKED # AT THE PRODUCT!", spd=6, step=3)
                doDialogText("          YOU TWO THINK YOU'RE SUCH HIGH AND MIGHTY #KINGS# THAT EVEN HELPING A STRUGGLING SALESMAN IS BENEATH YOU.", spd=6, step=3)
                if wear == 4:
                    doDialogText("          ONE OF YOU IS WEARING A FRIGGIN SUIT FOR EXAMPLE!", spd=6, step=3)
                doDialogText("YOU:# what is he talking about?")
                doDialogText("ASHISH:# I have no idea.#.#.#")
                doDialogText("SALESMAN:# YOU KNOW, #I# USED TO OWN THAT CAFE!# THE CAFE YOU JUST WALKED AWAY FROM.", spd=6, step=3)
                if pgFilter:
                    doDialogText("          I HAD THE BUSINESS OF MY LIFE,# UNTIL THAT FUCKING DADDY BASTARD TOOK IT ALL FROM ME!", spd=6, step=3)
                else:
                    doDialogText("          I HAD THE BUSINESS OF MY LIFE,# UNTIL THAT WRETCHED PERSON TOOK IT ALL FROM ME!", spd=6, step=3)
                doDialogText("          DARN HIS LOOPHOLES!", spd=6, step=3)
                doDialogText("YOU:# wait what?")
                doDialogText("SALESMAN:# HEY YOU.# THE ONE IN THE ATLANTA T-SHIRT.", spd=6, step=3)
                doDialogText("ASHISH:# m-#me?")
                doDialogText("SALESMAN:# YOU WANNA KNOW WHAT MOVIE HE'S GONNA TAKE YOU TO?#")
                doDialogText("          WHATEVER MOVIE IT IS,# ITS THE SAME ONE HE WATCHED WITH HIS MOM!")
                doDialogText("YOU:# wait what-# how do you know that?")
                doDialogText("ASHISH:# Do you know this guy?# Or does he know me?")
                doDialogText("SALESMAN:# EVERY PERSON HERE IS THE SAME!# ", afterdelay=0, spd=6, step=3)
                if pgFilter:
                    doDialogText("SELFISH!# WITH THEIR HEAD STUCK UP THEIR ASS!", spd=6, step=3)
                else:
                    doDialogText("SELFISH,# ARROGANT AND IGNORANT!", spd=6, step=3)
                doDialogText("          I HAVE A LIFE CHANGING PRODUCT HERE,# AND ALL YOU ARE DOING IS JUST STANDING,# TALKING AMONG YOUR GODLY SELVES,# JUDGING ME!", spd=6, step=3)
                doDialogText("          YOU PEOPLE THINK YOU'RE SO GREAT YOU CAN'T EVEN FATHOM SOMETHING THAT IS CAPABLE OF HELPING YOU EVEN A LITTLE BIT.", spd=6, step=3)
                doDialogText("ASHISH:# I never-#", afterdelay=0)
                doDialogText("SALESPERSON:# SHUT UP AND LISTEN.# YOU GODS MIGHT THINK THERE'S NOTHING THAT COULD GO WRONG,# BUT I KNOW OF A DANGER THAT WILL SHOW YOU WHAT I KNOW.")
                doDialogText(f"             YOU.# YOU MAY THINK ITS CUTE FOR YOU AND YOUR LITTLE {['TWINK', 'FRIEND'][1 - int(pgFilter)]} TO COME ON THIS DATE.", afterdelay=0)
                doDialogText("             BUT IF YOU DON'T TAKE ACTION SOON,# YOU WILL LOSE HIM FOREVER.", afterdelay=3)
                print()
                doDialogText("ASHISH:## what", afterdelay=2)
                doDialogText('"HEY!!')

                if pgFilter: doDialogText("SALESPERSON:# Oh shit.")
                else: doDialogText("SALESPERSON:# Oh dang it.")
                doDialogText("The SALESPERSON ran away.")
                doDialogText("You see a staff member running towards you.")
                doDialogText("STAFF:# Sorry,# was that guy disturbing you?")
                doDialogText("       It's been a few days,# he comes here and scares our customers away with his terrible ads.")
                doDialogText("       We're so sorry if it has been an inconvenience.")
                doDialogText("ASHISH:# oh.#.#.#")
                doDialogText("STAFF:# .#.#.#")
                doDialogText("YOU:# .#.#.#")
                doDialogText("ASHISH:# .#.#.#")
                print()
                doDialogText("STAFF:# I'll go back to my job now.")
                doDialogText("The staff member walked away.")
                print()


            doDialogText("YOU:# Well,# where do you wanna head next?")
            doDialogText("ASHISH:# Hmm.#.#.# I don't know.#.#")






                

            

            
            

        
        else:
            doDialogText("You have nothing much to do.")
            print()
            doDialogText("Eventually,# you get a message from ADITHYA.")
            doDialogText("\"Hey buddy,# you want a rematch?\"")
            doDialogText("You text back \"Hell no.\"")
            doDialogText("Hell no.")

        save2 = getPrompt("Save this chapter here?")
        if save2:
            route5["index"] = 2
            saveFile["route5"] = route5
            try:
                saveGame(curSaveName, saveFile)
                doDialogText("The game was saved.")
            except:
                doDialogText("There was an error in saving the game.")
        
        continue2 = getPrompt("Continue your journey?")
        if continue2:
            index = 2 # Second part
            doDialogText("Continuing from DATE.#.#.#")
            doDialogText("PRESENTATION DAY APPROACHES.", afterdelay=2)
    
    if index == 2:
        doDialogText("PART THREE:### PROJECTION.", afterdelay=2)
        print()

        doDialogText("It's time.")
        doDialogText("You're standing outside the class,# rehearsing the scripts with your team.")
        doDialogText("Inside,# the other team is presenting.")
        doDialogText("You start to worry if your presentation is good enough.")
        doDialogText(f"{route5['team'][0]}:# Don't worry,# we got this.")
        doDialogText("YOU:# .#.#.#yeah.", afterdelay=3)
        if pgFilter: doDialogText("(Shit,# why am I actually nervous now?)")
        else: doDialogText("(Oh god... why am I actually nervous now?)")
        print()
        doDialogText("It's our turn now.")
        doDialogText("You and your team assemble in front of the whole class.")
        doDialogText("All their eyes on you.#.#.#")
        doDialogText("You take a deep breath.#.#.# and start.", spd=5, afterdelay=3)
        print()

        if soundImportSuccesful:
            initTime = time.time()
            cutsceneIndex = 0

            playSong('assets/soundtrack/projection.ogg')

            while True:
                curTime = time.time() - initTime
                if curTime >= 0 and cutsceneIndex == 0:
                    cutsceneIndex += 1

                    doDialogText(f"{route5['team'][0]} starts with the speech.", spd=5)
                    if route5['team'][0] == 'SAVAN':
                        doDialogText("You can see his legs trembling,# but that doesn't stop him.", spd=5)
                    elif route5['team'][0] == 'ADITHYA':
                        doDialogText("He delivers the introduction flawlessly.", spd=5)
                    elif route5['team'][0] == 'BAPPE':
                        doDialogText("He doesn't sound the most confident,# but that doesn't stop him.", spd=5)
                    doDialogText(f"Seeing {route5['team'][0]} speak to the class.#.#.#", spd=5)
                    doDialogText("It fills you with DETERMINATION.", spd=5)
                    doDialogText(".#.#.#", spd=5)
                    print()
                
                if curTime >= 16 and cutsceneIndex == 1:
                    cutsceneIndex += 1

                    doDialogText(".#.#.# You realize that you should look through your key points.", spd=5)
                    if route5['team'][0] not in ['SAVAN', 'BAPPE']:
                        doDialogText(f"{route5['team'][0]} keeps talking confidently.", spd=5)
                    else:
                        doDialogText(f"Despite stuttering at the start,# you can feel {route5['team'][0]}'s confidence slowly grow.", spd=5)
                    doDialogText("Slowly,# you also start gaining confidence.", spd=5)
                    doDialogText("This is what you had been waiting for.", spd=5)
                    doDialogText(".#.#.#", spd=5)
                    print()

                if curTime >= 36 and cutsceneIndex == 2:
                    cutsceneIndex += 1
                    doDialogText(f".#.#.# {route5['team'][1]}'s design skills really show through the board.", spd=5)
                    if route5['team'][1] == 'DEBAYAN':
                        doDialogText(".#.#.#it's not the best,# but it's not the worst either.", spd=5)
                        doDialogText("This reminds you that you don't have to try to be the best either.", spd=5)
                    elif route5['team'][1] in ['ANNA', 'SAHUR']:
                        doDialogText("You can see a few memes and jokes snuck in here and there.",spd=5)
                        doDialogText("Aside from making the class laugh,# the designs are pretty impressive.")
                        doDialogText("This gives you further confidence for your turn.",spd=5)
                    else:
                        doDialogText("It's pretty modest,# but still better than anything you could've done.",spd=5)
                        doDialogText("You try not to feel useless about yourself.",spd=5)
                    doDialogText(".#.#.#",spd=5)
                    print()
                
                elif curTime >= 52 and cutsceneIndex == 3:
                    cutsceneIndex += 1
                    
                    doDialogText("...You look around at the classroom.", spd=5)
                    doDialogText("Not everyone is listening...# You can see some people talking.", spd=5)
                    doDialogText("You can't help but think you're not good enough.", spd=5)
                    doDialogText("...", spd=5)
                    print()
                
                elif curTime >= 68 and cutsceneIndex == 4:
                    cutsceneIndex += 1

                    doDialogText(f"{route5['team'][0]} finishes his part.# It's {route5['team'][1]}'s turn next.", spd=5)
                    doDialogText("You can see some have lost interest already.", spd=5)
                    doDialogText("You try to ignore them.# Not everyone is attentive, anyways.", spd=5)
                    doDialogText(".#.#.#", spd=5)
                    print()
                
                elif curTime >= 84 and cutsceneIndex == 5:
                    cutsceneIndex += 1

                    doDialogText("The board freezes for a second.", spd=5)
                    doDialogText(f"You can see panic in {route5['team'][1]}'s face.", spd=5)
                    doDialogText("The classroom starts to murmur.")
                    doDialogText(".#.#.# the board soon starts working again.", spd=5)
                    doDialogText(".#.#.#", spd=5)
                    print()
                
                elif curTime >= 100 and cutsceneIndex == 6:
                    cutsceneIndex += 1

                    doDialogText(f"...It's now {route5['team'][2]}'s turn.", spd=5)
                    if route5['team'][2] in ['EARWIND', 'TEJAS']:
                        doDialogText("He explains his facts in great detail.", spd=5)
                        doDialogText("You think you might not speak well.", spd=5)
                    elif route5['team'][2] == 'ASHAK':
                        doDialogText("He speaks differently,# trying to remember his script.", spd=5)
                        doDialogText("You think if your fate will be similar.", spd=5)
                    else:
                        doDialogText("He speaks about his facts in detail.", spd=5)
                        doDialogText("You become afraid that you might not do well.", spd=5)
                    doDialogText(".#.#.#")
                    print()

                elif curTime >= 116 and cutsceneIndex == 7:
                    cutsceneIndex += 1

                    doDialogText(f"You look over to {route5['team'][3]},# controlling the slides on the smartboard.", spd=5)
                    doDialogText("Quietly listening along.#.#.# while also helping the team speak.", spd=5)
                    doDialogText(f"{route5['team'][3]} looks over to you and signals \"YOU GOT THIS\".", spd=5)
                    doDialogText(".#.#.#")
                    print()

                elif curTime >= 132 and cutsceneIndex == 8:
                    cutsceneIndex += 1

                    doDialogText(".#.#.#")
                    doDialogText("The time has come.# It's your turn to speak now.", spd=5)
                    doDialogText("You walk to the front of the class,# your heart beating in a strange manner.", spd=5)
                    doDialogText("No matter who you are,# you're nervous right now.", spd=5)
                    doDialogText("You recollect your words,# getting ready to start.", spd=5)
                    doDialogText("The stares.#.#.#", spd=5)
                    doDialogText("You gather up your words.#.#.#", spd=5, afterdelay=0, line=False)
                    doDialogText(" and start.")
                
                elif curTime >= 164 and cutsceneIndex == 9:
                    cutsceneIndex += 1
                    
                    print()
                    doDialogText("You start speaking with little confidence.", spd=5)
                    doDialogText("Your brain's running at full speed,# trying not to stutter.", spd=5)
                    doDialogText("You were definitely not meant to speak in front of a stage,# but here you are.", spd=5)
                    doDialogText("You try to keep eye contact with the class.# It gets difficult at times.", spd=5)
                    doDialogText("You think if imagining them as pumpkins would help.#.#.###### It does not.", spd=5)
                    doDialogText(".#.#.#", afterdelay=1)
                    doDialogText("Suddenly,# you forget a line.", spd=5)
                    doDialogText("You freeze in front of the entire class.", spd=5)
                    doDialogText(f"You look over to {route5['team'][3]}, who mouths your line to you.", spd=5)
                    doDialogText("You go back to speaking,# trying to pretend nothing happened.", spd=5)
                    doDialogText(".#.#.#")

                elif curTime >= 212 and cutsceneIndex == 10:
                    cutsceneIndex += 1

                    print()
                    doDialogText("Your turn is over now.", spd=5)
                    doDialogText(f"{route5['team'][3]} comes to the stage and wraps up the presentation.")
                    if route5['team'][3] in ['SURYA', 'ENAMEL']:
                        doDialogText("He seems a little off...# Maybe he's also nervous.")
                    else:
                        doDialogText("The presentation gets wrapped up excellently.")
                    doDialogText("You hope you did fine.")

                elif curTime >= 231 and cutsceneIndex == 11:
                    break

                    
        else:

            doDialogText(f"{route5['team'][0]} starts with the speech.")
            if route5['team'][0] == 'SAVAN':
                doDialogText("You can see his legs trembling,# but that doesn't stop him.")
            elif route5['team'][0] == 'ADITHYA':
                doDialogText("He delivers the introduction flawlessly.")
            elif route5['team'][0] == 'BAPPE':
                doDialogText("He doesn't sound the most confident,# but that doesn't stop him.")
            doDialogText(".#.#.#", afterdelay=3)
            print()

            doDialogText(".#.#.# You realize that you should look through your key points.")
            if route5['team'][0] not in ['SAVAN', 'BAPPE']:
                doDialogText(f"{route5['team'][0]} keeps talking confidently.")
            else:
                doDialogText(f"Despite stuttering at the start,# you can feel {route5['team'][0]}'s confidence slowly grow.")
            doDialogText("Slowly,# you also start gaining confidence.")
            doDialogText("This is what you had been waiting for.")
            doDialogText(".#.#.#", afterdelay=3)
            print()

            doDialogText(f".#.#.# {route5['team'][1]}'s design skills really show through the board.")
            if route5['team'][1] == 'DEBAYAN':
                doDialogText(".#.#.#it's not the best,# but it's not the worst either.")
                doDialogText("This reminds you that you don't have to try to be the best either.")
            elif route5['team'][1] in ['ANNA', 'SAHUR']:
                doDialogText("You can see a few memes and jokes snuck in here and there.")
                doDialogText("Aside from making the class laugh,# the designs are pretty impressive.")
                doDialogText("This gives you further confidence for your turn.")
            else:
                doDialogText("It's pretty modest,# but still better than anything you could've done.")
                doDialogText("You try not to feel useless about yourself.")
            doDialogText(".#.#.#", afterdelay=3)
            print()

            doDialogText(".#.#.#You look around at the classroom.")
            doDialogText("Not everyone is listening.#.#.# You can see some people talking.")
            doDialogText("The teacher is still judging everyone's performance.")
            doDialogText("You can't help but think you're not good enough.")
            doDialogText(".#.#.#", afterdelay=3)
            print()

            doDialogText(f"{route5['team'][0]} finishes his part.# It's {route5['team'][1]}'s turn next.")
            doDialogText("You can see some have lost interest already.")
            doDialogText("You try to ignore them.# Not everyone is attentive, anyways.")
            doDialogText(".#.#.#", afterdelay=3)
            print()

            doDialogText("The board freezes for a second.")
            doDialogText(f"You can see panic in {route5['team'][1]}'s face.")
            doDialogText("The classroom starts to murmur.")
            doDialogText(".#.#.# the board soon starts working again.")
            doDialogText(".#.#.#", afterdelay=3)
            print()

            doDialogText(f"...It's now {route5['team'][2]}'s turn.")
            if route5['team'][2] in ['EARWIND', 'TEJAS']:
                doDialogText("He explains his facts in great detail.")
                doDialogText("You think you might not speak well.")
            elif route5['team'][2] == 'ASHAK':
                doDialogText("He speaks differently,# trying to remember his script.")
                doDialogText("You think if your fate will be similar.")
            else:
                doDialogText("He speaks about his facts in detail.")
                doDialogText("You become afraid that you might not do well.")
            doDialogText(".#.#.#", afterdelay=3)

            doDialogText(f"You look over to {route5['team'][3]},# controlling the slides on the smartboard.")
            doDialogText("Quietly listening along.#.#.# while also helping the team speak.")
            doDialogText(f"{route5['team'][3]} looks over to you and signals \"YOU GOT THIS\".")
            doDialogText(".#.#.#")
            print()

            doDialogText(".#.#.#")
            doDialogText("The time has come.# It's your turn to speak now.")
            doDialogText("You walk to the front of the class,# your heart beating in a strange manner.")
            doDialogText("No matter who you are,# you're nervous right now.")
            doDialogText("You recollect your words,# getting ready to start.")
            doDialogText("The stares.#.#.#", spd=5)
            doDialogText("You gather up your words.#.#.#", spd=5, afterdelay=0, line=False)
            doDialogText(" and start.")

            print()
            doDialogText("You start speaking with little confidence.")
            doDialogText("Your brain's running at full speed,# trying not to stutter.")
            doDialogText("You were definitely not meant to speak in front of a stage,# but here you are.")
            doDialogText("You try to keep eye contact with the class.# It gets difficult at times.")
            doDialogText("You think if imagining them as pumpkins would help.#.#.###### It does not.")
            doDialogText(".#.#.#", afterdelay=1)
            doDialogText("Suddenly,# you forget a line.")
            doDialogText("You freeze in front of the entire class.")
            doDialogText(f"You look over to {route5['team'][3]}, who mouths your line to you.")
            doDialogText("You go back to speaking,# trying to pretend nothing happened.")
            doDialogText(".#.#.#")

            print()
            doDialogText("Your turn is over now.", spd=5)
            doDialogText(f"{route5['team'][3]} comes to the stage and wraps up the presentation.")
            if route5['team'][3] in ['SURYA', 'ENAMEL']:
                doDialogText("He seems a little off...# Maybe he's also nervous.")
            else:
                doDialogText("The presentation gets wrapped up excellently.")
                doDialogText("You hope you did fine.")
        




        print()
        doDialogText(".#.#.# it's over.")
        doDialogText("You're not sure about your team's performance.")
        doDialogText("YOU:# We did it guys.")

        # bini mam helped me code this
        for member in route5['team']:
            if member == 'ADITHYA':
                doDialogText("ADITHYA:# You were not half bad yourself.# Good job.")
                doDialogText("YOU:# Thanks,# but you were great as well.")
                print()
            elif member == 'SAVAN':
                doDialogText("SAVAN:# i'm sorry...# did i do bad?", spd=5)
                doDialogText("YOU:# Nonono,# you were alright.# You regained your composure.")
                doDialogText("SAVAN:# thanks.#.#.#")
                print()
            elif member == 'BAPPE':
                doDialogText("BAPPE:# I think I cooked bro.#.#.#")
                doDialogText("YOU:# You weren't that bad,# don't worry.")
                doDialogText("BAPPE:# Thanks..#")
                print()
            elif member in ['SIBI', 'A.R RAHMAN']:
                doDialogText(f"{member}:# Yeah,# we did.")
            
                print()

            if member in ['ANNA', 'SAHUR', 'TENMAY', 'WAYDANT', 'DEBAYAN']:
                doDialogText(f"YOU:# {member},# thanks for your help in design.")
                if member in ['ANNA', 'SAHUR']:
                    doDialogText("     It was really good!")
                doDialogText(f"{member}:# You're welcome.")
                if member in ['WAYDANT', 'DEBAYAN']:
                    doDialogText("         But it can't have been that good tho.#.#.#")
                    doDialogText("YOU:# It wasn't the best,# but I think it was enough.")
                print()

            if member in ['EARWIND', 'TEJAS', 'AWAITH', 'KICHAN', 'ASHAK']:
                doDialogText(f"YOU:# {member},# thank you for your help in doing the research related stuff.")
                if member in ['EARWIND', 'TEJAS']:
                    doDialogText(f"{member}:# No problem bro.# I had fun working with you as well.")
                    doDialogText("YOU:# Thanks.")
                elif member == 'KICHAN':
                    doDialogText("KICHAN:# Thank you,# I tried to help as much as I could.")
                    doDialogText("YOU:# And that you did.")
                elif member == 'AWAITH':
                    doDialogText("AWAITH:# Don't thank me bro,# thank Gemini.")
                    doDialogText("YOU:# I suspected.#.#.#")
                elif member == 'ASHAK':
                    doDialogText("ASHAK:# Don't thank me bro,# thank ChatGPT.")
                    doDialogText("YOU:# I suspected.#.#.#")
                print()

            if member in ['FRIEDEL', 'JANET', 'FARWANA', 'SURYA', 'ENAMEL']:
                doDialogText(f"YOU:# And {member}, thank you for your work on the artwork.")
                if member in ['FRIEDEL', 'JANET']:
                    doDialogText("     It was really good!")
                    doDialogText(f"{member}:# Aw,# thank you.")
                else:
                    doDialogText(f"{member}:# Thank you...# but it really wasn't that great.")
                    doDialogText("YOU:# That's fine,# it was enough for us.")

                    if member != 'FARWANA':
                        doDialogText(f"{member}:# But it was lowkey dogwater...")
                print()




        # LATE EVALUATION (cuz i'm a dumbass)
        presentationPoints = 5

        for member in route5['team']:
            if member in   ['ADITHYA',    'ANNA',    'EARWIND', 'FRIEDEL']:
                presentationPoints += 5
            elif member in ['A.R RAHMAN', "SAHUR",   'TEJAS',   'JANET']:
                presentationPoints += 4
            elif member in ['SIBI',       'TENMAY',  'AWAITH',  'FARWANA']:
                presentationPoints += 3
            elif member in ['SAVAN',      'WAYDANT', 'KICHAN',  'SURYA']:
                presentationPoints += 2
            elif member in ['BAPPE',      'DEBAYAN', 'ASHAK',   'ENAMEL']:
                presentationPoints += 1

        # SYNERGIES + DESYNERGIES
        if 'ADITHYA' in route5['team']:
            if 'EARWIND' in route5['team']:
                presentationPoints += 2
            presentationPoints -= 3

        
        if 'AWAITH' in route5['team'] and 'SIBI' in route5['team']:
            presentationPoints += 4

        if 'BAPPE' in route5['team'] and 'KICHAN' in route5['team']:
            presentationPoints += 3

        if 'EARWIND' in route5['team'] and 'A.R RAHMAN' in route5['team']:
            presentationPoints += 1
        
        if 'SAVAN' in route5['team'] and 'SAHUR' in route5['team']:
            presentationPoints += 2
        
        if 'SIBI' in route5['team'] and 'FARWANA' in route5['team']:
            presentationPoints -= 3
        
        if 'ASHAK' in route5['team']:
            if 'ENAMEL' in route5['team']:
                presentationPoints += 2

        doDialogText("ENGLISH TEACHER:# Okay,# here's my evaluation:")
        doDialogText("                 You get.#.#.#", afterdelay=3)
        playSong('assets/soundtrack/results.ogg', looping=True)
        doDialogText(f"                {presentationPoints}/25 marks!")

        if presentationPoints == 25:
            doDialogText("                 Your presentation was done really well!# I have to give full marks for this.")
            doDialogText("                 Everyone coordinated very well!")
        elif presentationPoints in range(18, 25):
            doDialogText("                 The presentation was well done.")
        elif presentationPoints in range(12, 18):
            doDialogText("                 The presentation could've been better though.#.#.#")
        elif presentationPoints in range(10, 12):
            doDialogText("                 I couldn't really feel any effort put ito the presentation.#.#.#")
            if presentationPoints == 10:
                doDialogText("                 This is the minimum marks I can give you.")
        elif presentationPoints < 10:
            doDialogText("                 But I am REQUIRED to give you atleast 10 marks for internal assessment.")

            if presentationPoints < 9:
                doDialogText("                 Genuinely,# how do you even perform this badly?")
                doDialogText("                 It's like.#.#.#")
                doDialogText("                 It's like you changed reality just to deliberately do awful.")
                doDialogText("                 Like,# it's IMPOSSIBLE to see this screen.# I don't even think you can CHANGE the points in the save file.# I just evaluated the marks right now!")
                doDialogText("                 HOW?# HOW DO YOU DO THIS BAD.")

        if 'ADITHYA' in route5['team']:
            doDialogText("                 ADITHYA spoke very well during the presentation!")
            doDialogText("                 You were able to grab everyone's attention,# and keep them invested.")
            doDialogText("                 I even liked the little remarks you made sometimes.")
        elif 'SAVAN' in route5['team']:
            doDialogText("                 SAVAN,# I could tell you were nervous...")
            doDialogText("                 But still,# you kept talking with confidence.")
            doDialogText("                 I could literally see your legs shiver.")
        elif 'BAPPE' in route5['team']:
            doDialogText("                 BAPPE,# I think you could work on your speech a little more.#.#.")
        else:
            doDialogText(f"                 {route5['team'][0]} did a pretty good job of being the main speaker of the presentation.")

        if 'ANNA' in route5['team']:
            doDialogText("                 Though I liked the presentation a lot!# It even made me laugh sometimes.")
            doDialogText("                 It isn't necessary to always be completely serious,# but you kept your humor moderate.")
        elif 'DEBAYAN' in route5['team']:
            doDialogText("                 And the presentation...")
            doDialogText("                 It could've been better.")
        else:
            doDialogText("                 And the presentation itself was not bad either.")
        
        if 'EARWIND' in route5['team'] or 'TEJAS' in route5['team']:
            doDialogText("                 It was also a very detailed presentation!# Very well researched.")
        elif 'ASHAK' in route5['team']:
            doDialogText("                 I have one criticism about the presentation...# I can tell it's AI generated.")
            doDialogText("                 You could've atleast changed it around.#.#.#")
        else:
            doDialogText("                 The research is well done in my opinion.")
        
        doDialogText("                 And it was also a very unique decision to include artwork in your presentation!")
        if 'FRIEDEL' in route5['team'] or 'JANET' in route5['team']:
            doDialogText("                 Whoever made the artwork is very talented!")
        elif 'ENAMEL' in route5['team']:
            doDialogText("                 Though the art in itself.#.#.#")
            doDialogText("                 i'm not gonna comment on it.")
        
        print()
        stopSong()
        doDialogText("                 And that's it.# That's the last team to do the presentation.")
        doDialogText("                 Everyone,# don't forget:# You have midterms in a month!")
        doDialogText("                 Make sure to study for it.")

        print()
        doDialogText("The presentation,# is thus over.")
        doDialogText("It feels like a weight was lifted off your back.", afterdelay=3)

        if saveFile['route3']['rude_stay'] != "UNFORGIVED":
            doDialogText("You head back to your seat,# and wait for the rest of the day to finish.")
            doDialogText("ASHISH:# Hey,# nice job.# You did pretty well.")
            doDialogText("YOU:# Thanks.# Your team also did pretty well.")
            if presentationPoints == 25:
                doDialogText("ASHISH:# Thanks,# but I think your presentation was the best one so far.")
                doDialogText("YOU:# Really?")
                doDialogText("ASHISH:# Yeah!")
                doDialogText("        It was really fun working with SARBATH.")
            else: doDialogText("ASHISH:# Thanks!# It was really fun working with SARBATH.")
            doDialogText("YOU:# Yeah,# it was fun working on this project.")
            doDialogText("     One last fun project.#.#.#")
            doDialogText("     Let's hope we have more fun things to do in the future.")
            doDialogText("ASHISH:# Yeah,# this school year has been really fun.")
            doDialogText("        But we have exams in a month,# Don't Forget.")
            doDialogText("YOU:# Hmm.#.#.#")
            doDialogText("     I think I'll start studying like a week before it.")
            doDialogText("ASHISH:# Bruh.", afterdelay=3)
        else:
            doDialogText("You had fun working on this presentation.")
            doDialogText("One last fun presentation.#.#.#")
            doDialogText("But you have midterms in a month, so", afterdelay=0.5)
            doDialogText("Don't Forget.", afterdelay=3)
        print()
        doDialogText("And like that,# the school day's over.")

        if route5['key']:
            doDialogText("You think of heading home,# but suddenly you remember-")
            doDialogText("(Wait,# I have this key.)")
            doDialogText("(I think I'll go check it out...)")
            doDialogText("(It says OLD MUSIC ROOM on it.)")
            doDialogText("You head to the old music room of the school.")
            doDialogText("(This place hasn't been used in a long time,# or so I've heard.)") 
            doDialogText("You can hear something from within.")
            doDialogText("(Are there people inside?)")
            doDialogText("You open the door slowly.")
            doDialogText("You are met with a group of girls having tea in a very dark music room.")
            doDialogText("ONE GIRL:# Are you...", spd=5)
            doDialogText("TWO GIRL:# Oh no!# We've been seen!", spd=3)
            doDialogText("ONE GIRL:# Nono,# it's okay.")
            doDialogText("          I see you have the key.")
            doDialogText("YOU:# Yeah.#.#.#")
            doDialogText("     So what are you guys doing in...# here?")
            doDialogText("ONE GIRL:# Oh,# this is just our hiding place.#.#.# heh,# no pun intended.")
            playSong('assets/soundtrack/musicroom.ogg', looping=True)
            doDialogText("TWO GIRL:# We are the original choir group!# Also known as the previous exes of ADITHYA!", spd=3)
            doDialogText("THREE GIRL:# Shush!# He can't know that!")
            doDialogText("YOU:# .#.#.#exes?")
            doDialogText("ONE GIRL:# We are the original choir group of the school.")
            doDialogText("TWO GIRL:# We used to sing the prayer every morning!# It was glorious,# our PRIME!")
            doDialogText("THREE GIRL:# But unfortunately,# it reached that final abode all great things eventually arrive at.")
            doDialogText("            We grew up.")
            doDialogText("FOUR GIRL:# They needed students from younger classes to sing.# We were cast away in name of education.")
            doDialogText("ONE GIRL:# We were known as the school's choir girls.# It was sometimes the only thing we had.")
            doDialogText("          We enjoyed singing as a choir.# Every single song.")
            doDialogText("FIVE GIRL:# But now,# we have no more purpose.# We have moved on.")
            doDialogText("ONE GIRL:# This old little music room is now our hangout spot.")
            doDialogText("          We still practice songs to this day,# remembering our purpose.#.#.#")
            doDialogText("          What we once used to be.")
            doDialogText("SIX GIRL:# *walks in* hey guys,# I found an unusual application for a new-#", afterdelay=0.3)
            doDialogText("          Who is this?")
            doDialogText("ONE GIRL:# He's a friend of ADITHYA,# I assume.")
            doDialogText("YOU:# Uh...# yeah he gave me the key.# Didn't say anything else about this.")
            doDialogText("TWO GIRL:# Wow,# ADITHYA must really trust you!")
            doDialogText("YOU:# Um,## no,# not exactly.")
            doDialogText("THREE GIRL:# He doesn't.#.#.# have a spare key.")
            doDialogText("FIVE GIRL:# Does that mean.#.#.#")
            doDialogText("ONE GIRL:# .#.#.#")
            doDialogText("           He has fully moved on.")
            doDialogText("TWO GIRL:# Oh.#.#.#")
            doDialogText("          Who's his new girlfriend?")
            doDialogText("ONE GIRL:# .#.#.#")
            doDialogText("YOU:# He doesn't have one.")
            doDialogText("ONE GIRL:# Maybe he hasn't decided yet.#.#.#")
            doDialogText("YOU:# I'd say otherwise.# He hasn't made the move yet.")
            doDialogText("THREE GIRL:# That's weird.# He rizzed up all of us with ease.")
            doDialogText("YOU:# So...# are all of you his exes?")
            doDialogText("ONE GIRL:# Yeah.#.#.# he was into girls that could sing,# I suppose.")
            doDialogText("YOU:# .#.#.#but i thought he came from a different school?")
            doDialogText("THREE GIRL:# That doesn't stop him from crossing countries.")
            doDialogText("YOU:# ...wow.")
            doDialogText("      did he have more exes?# Or did he just cycle through the group?")
            doDialogText("ONE GIRL:# We don't know yet,# but it's safe to assume he has more,# probably from his old school.")
            doDialogText("YOU:# That's crazy.")
            doDialogText("TWO GIRL:# What did you mean by you're not exactly friends with him?# He's usually really friendly.")
            doDialogText("ONE GIRL:# Yeah,# how did you get this key?")
            doDialogText("YOU:# He just gave it to me without saying anything about it.# I think he doesn't like me.")
            doDialogText("FOUR GIRL:# Don't forget,# as nice as ADITHYA can be,# he still has his ways.")
            doDialogText("           Maybe you're getting in his way somehow?")
            doDialogText("YOU:# I suppose so.#.#.#")
            doDialogText("     He's convinced I'm gonna do something bad to someone,# I think.")
            doDialogText("SIX GIRL:# Something similar happened to me.")
            doDialogText("          I used to have a best friend - #a guy.")
            doDialogText("          We always used to hang out before I met ADITHYA.")
            doDialogText("          But he always didn't sit right with him.")
            doDialogText("          Ever since we started dating,# he didn't seem to like him as much as anyone else.")
            doDialogText("          One day,# he found incriminating evidence against him,# proving he was trying to use me.")
            doDialogText("          He kept denying,# but ADITHYA's evidence was strong.")
            doDialogText("          Even I couldn't believe he would do something like this.")
            doDialogText("          He had to move schools out of embarrassment.")
            doDialogText("          I was emotionally scarred after that.# I had to break up with ADITHYA a month after.")
            doDialogText("YOU:# Oh.#.#.#")
            doDialogText("FOUR GIRL:# Sound familiar?")
            doDialogText("YOU:# Yes.#.#.# He confronted me with his friend group once.")
            doDialogText("FOUR GIRL:# ...I advise you to be careful.")
            doDialogText("YOU:# Yes,# thank you.")
            doDialogText("ONE GIRL:# So he's found someone.")
            doDialogText("TWO GIRL:# He took so long to find someone!# He's usually back to dating within a week after breakup!")
            doDialogText("THREE GIRL:# Maybe he got tired of finding girls like us,# and finally found someone different?")
            doDialogText("YOU:# I'm not sure when I say this,# but he's found a guy.")
            stopSong()
            doDialogText("ONE GIRL:# .#.#.#")
            doDialogText("TWO GIRL:# .#.#.#")
            doDialogText("The music room suddenly got quiet.")
            doDialogText("ONE GIRL:# Well,# that's.#.#.# surprising.", spd=5)
            doDialogText("TWO GIRL:# HE GOT SO TIRED OF US HE TURNED GAY!# NOOO!")
            doDialogText("THREE GIRL:# I think I saw it coming,# but I didn't expect it to be true.#.#.#")
            doDialogText("YOU:# .#.#.# yeah.# I don't know if hes pursuing a relationship,# but I get the feeling he's been messing with me because I talk to him.")
            doDialogText("FOUR GIRL:# He's pursuing him romantically.# No doubt.")
            doDialogText("YOU:# I see.# Thanks for clarifying.")
            doDialogText("TWO GIRL:# Oh,# my coffee got cold.# Let me reheat it.")
            doDialogText("TWO GIRL grabs her cup of coffee and starts walking towards a microwave.")
            doDialogText("On the way, she trips over what looks like a dusty guitar.")
            doDialogText("TWO GIRL:# MY COFFEE!!", spd=1)
            doDialogText("THREE GIRL:# Oh,# let me help you!")
            doDialogText("YOU:# Is that... a guitar?")
            doDialogText("ONE GIRL:# Yeah.# It's been sitting in this music room for ages.# None of us know how to play guitar.")
            doDialogText("          So it's just been sitting there and collecting dust.")
            doDialogText("YOU:# I know how to play guitar.# Can I see it?")
            doDialogText("ONE GIRL:# You can play guitar?# That's wonderful!# Would you like to play a song with us then?")
            doDialogText("YOU:# Uh,# sure why not?")
            doDialogText("TWO GIRL:# OMG OMG A SONG WITH GUITAR!# I WANNA SING!", spd=2)
            doDialogText("          HERE TAKE A SEAT!", spd=2)
            doDialogText("TWO GIRL brings the guitar to you.")
            doDialogText("YOU:# Let's see.#.#.#")
            doDialogText("The guitar is heavily out of tune.# The strings are almost rusted,# and the frets are really dirty.")
            doDialogText("YOU:# Gonna have to tune it.# Wait a sec.#.#.#")
            doDialogText(".#.#.#")
            doDialogText("You tune the guitar.")
            doDialogText("YOU:# Okay,# I'm ready.")
            doDialogText("ONE GIRL:# Great!# Do you know the song \"Shepherd of my soul\"?")
            doDialogText("YOU:# Uhh, yeah.# Which key are you singing in?")
            doDialogText("ONE GIRL:# Uhh,# I'm not sure.# We just sing along with our pianist.")
            doDialogText("FOUR GIRL:# C sharp major.")
            doDialogText("YOU:# Oh.#.#.# gonna have to work with it.")
            doDialogText("FOUR GIRL:# You need the chords?")
            doDialogText("YOU:# Nope.# I got this.")
            doDialogText("ONE GIRL:# Alright,# GIRLS!# Get in position!")
            doDialogText("The choir girls assemble into position.")
            doDialogText("ONE GIRL:# Let's do our best.")
            doDialogText("YOU:# Yeah.")
            print()

            if soundImportSuccesful:
                lyric = 0
                playSong('assets/soundtrack/shepherd.ogg')
                iTime = time.time()

                while True:
                    curTime = time.time() - iTime

                    if curTime <= 13.7 and lyric == 0:
                        lyric += 1
                        doDialogText("You start strumming the guitar.")
                        doDialogText("Despite it being old,# it sounds nice.")
                        doDialogText("The girls listen along to you.")
                        print()

                    elif curTime > 13.7 and lyric == 1:
                        lyric += 1
                        print()
                        doDialogText('"Shepherd of my SOUL,', spd=5)
                    elif curTime > 16.7 and lyric == 2:
                        lyric += 1
                        doDialogText(' I give you full control.', spd=5)
                    elif curTime > 20.1 and lyric == 3:
                        lyric += 1
                        doDialogText(' Wherever you may lead,', spd=5)
                    elif curTime > 23.1 and lyric == 4:
                        lyric += 1
                        doDialogText(" I will ", afterdelay=0, spd=5, line=False)
                        doDialogText("follow.\"", spd=7)
                    elif curTime > 27.4 and lyric == 5:
                        lyric += 1
                        print()
                        doDialogText('"I have made the choice,', spd=5)
                    elif curTime > 30.4 and lyric == 6:
                        lyric += 1
                        doDialogText(' To listen to your voice.', spd=5)
                    elif curTime > 33.8 and lyric == 7:
                        lyric += 1
                        doDialogText(' Wherever you may lead,', spd=5)
                    elif curTime > 36.8 and lyric == 8:
                        lyric += 1
                        doDialogText(' I will go."', spd=5)      
                    elif curTime > 40.2 and lyric == 9:
                        lyric += 1
                        print()
                        doDialogText('"Be it in a quiet pasture,', spd=5)
                    elif curTime > 44.1 and lyric == 10:
                        lyric += 1
                        doDialogText(' Or by a gentle stream.', spd=5)
                    elif curTime > 47.5 and lyric == 11:
                        lyric += 1
                        doDialogText(' The Shepherd of my Soul is by my side!"', spd=5)
                    elif curTime > 54.0 and lyric == 12:
                        lyric += 1
                        print()
                        doDialogText('"Should I face a mighty mountain,', spd=5)
                    elif curTime > 57.8 and lyric == 13:
                        lyric += 1
                        doDialogText(' Or a valley dark and deep,', spd=5)
                    elif curTime > 61.2 and lyric == 14:
                        lyric += 1
                        doDialogText(' The Shepherd of my Soul will be my guide!"', spd=5)

                    elif curTime > 72 and lyric == 15:
                        print()
                        break
            else:
                doDialogText("You start strumming along with the girls.")
                doDialogText("Due to your hardware limitations,# you were unable to hear the beautiful symphony made together.")
                print()
                doDialogText(".#.#.#")
                doDialogText("You finish the song.")
                print()
            doDialogText("ONE GIRL:# Wow,# that was great!")
            doDialogText("TWO GIRL:# You play so well!# Let's do this again!")
            doDialogText("ONE GIRL:# It's getting late now,# you should probably get going.")
            doDialogText("          But yeah,# let's meet again!")
            doDialogText("FOUR GIRL:# If you need any help,# then just come to us.# We have your back.")
            doDialogText("ONE GIRL:# Yes!# I should introduce you to the rest of the group next time.")
            doDialogText("          Only six girls were here today.# There are 12 of us in total.")
            doDialogText("          We sometimes call ourselves \"THE 12 EXECUTIONERS\".")
            doDialogText("YOU:# It's crazy to think ADITHYA's been through 12 girls.")
            doDialogText("     But yeah,# I'll head home now.# It was nice seeing you all!")
            doDialogText("ONE GIRL:# Goodbye!# Be sure to visit our hiding place next time!")
            print()


        
        doDialogText("You head home from school.")
        doDialogText("As soon as you enter your room,# you plop down on the bed beside your guitar.")
        if saveFile['route1']['name_choice'] == "RUDE" and (saveFile['route3']['rude_stay'] != "UNFORGIVED" or saveFile['route1']['rude_cancel']):
            doDialogText("(It's really been a while since I played guitar, huh.)")
            doDialogText("(I think I'll' practice now.)")
            doDialogText("You take out and scroll through Spotify.")
            doDialogText("At the corner of the screen,# one song sticks out from the rest:")
            doDialogText("AASHISHKAM.", afterdelay=3.6)
            print()

        doDialogText("Meanwhile,# somewhere in a phone call between ASHISH and DEBAYAN:")
        doDialogText("ASHISH:# DEBAYAN.#.#.# I need to let it out.")
        doDialogText("        I.#.#.#")
        doDialogText("        I like someone.", afterdelay=3)
        doDialogText("DEBAYAN:# .#.#.#okay?", spd=5)


        print()

        
        save3 = getPrompt("Save this chapter here?")
        if save3:
            route5["index"] = 2
            route5['COMPLETED'] = True
            saveFile["route5"] = route5
            try:
                saveGame(curSaveName, saveFile)
                doDialogText("The game was saved.")
            except:
                doDialogText("There was an error in saving the game.")

            




        






def start(funcs):

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
    stopSong = funcs['stopSong']
    timeControl = funcs['timeControl']
    pgFilter = funcs['pgFilter']
    saveFile = funcs['saveFile']
    saveGame = funcs['saveGame']
    curSaveName = funcs['curSaveName']
    soundImportSuccesful = funcs['soundImportSuccesful']
    
    chapter_5(funcs)