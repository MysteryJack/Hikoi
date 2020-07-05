from discord.ext import commands
import discord
import random
import time
import os

Hikoi_Prefix = "hikoi "
Hikoi_Token = ""
Hikoi_ban = 0
#for rps
Hikoi_anger = 0
Hikoi_copied = 0
Hikoi_fan = 0

hikoi = commands.Bot(command_prefix=Hikoi_Prefix)

@hikoi.event
async def on_ready():
    print("I guess I\'m ready")
    await hikoi.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
    

@hikoi.event
async def on_message(msg):
    global  Hikoi_ban    
    if msg.author == hikoi.user:
        return

    #unban = sry
    if msg.author.id == Hikoi_ban:
        if msg.content.find("sorry") != -1:
            await msg.channel.send("I don\'t want to forgive you but uhh...fine")
            Hikoi_ban = 0
        return
    elif msg.content.find("sorry") != -1 and Hikoi_ban != 0:
        hikoi_forgive = discord.Client.get_user(hikoi,id = Hikoi_ban)
        await msg.channel.send("You didn\'t do anything wrong.It\'s "+ hikoi_forgive.mention )



    if msg.content.find("hikoi") != -1:
        #if its me
        if msg.author.id == 452756967937540096:
            #HELLO
            if msg.content.find("hello") != -1:
                await msg.channel.send("Hello mmm...master")

            #Bye
            if msg.content.find("bye") != -1:
                await msg.channel.send("no.. I uhh.. dont care if you go but..:disappointed_relieved:")

            #thankyou
            if msg.content.find("thank") != -1:
                await msg.channel.send("I didn\'t meant to do that it just my duty :flushed:")

            #whoisyourmaster
            if msg.content.find("who is your master") != -1:
                await msg.channel.send("yyy...yo..NO ONE!!")

        #Others
        else:
            
            #HELLO
            if msg.content.find("hello") != -1:
                await msg.channel.send("Hello "+ msg.author.mention)

            #Bye
            if msg.content.find("bye") != -1:
                await msg.channel.send("no.. I uhh.. dont care if you go but..:disappointed_relieved:")

            #thankyou
            if msg.content.find("thank") != -1:
                await msg.channel.send("I didn\'t meant to do that I just uhh..:flushed:")

            #whoisyourmaster
            if msg.content.find("who is your master") != -1:
                await msg.channel.send("What do you want me to say? "+ msg.author.mention +"? Baka:weary:")

            
    await hikoi.process_commands(msg)

#Rock Paper Scissirs
@hikoi.command(brief = "Rock Paper Scissors")
async def rps(hikoi, mode, RPC):
    global Hikoi_ban,Hikoi_anger,Hikoi_copied,Hikoi_fan
    Hikoi_RPC = ["Rock :fist:","Scissors :v:","Paper :raised_hand:"]
    Hikoi_rpc = random.randint(1,3)
    if RPC == "rock":
        RPC = 1
    elif RPC == "scissors":
        RPC = 2
    elif RPC == "paper":
        RPC = 3
    else: 
        await hikoi.send("Wait " + hikoi.message.author.mention + " thats cheating")
    #check
    if Hikoi_fan != hikoi.author.id:
        Hikoi_anger = 0
        Hikoi_copied = 0
        Hikoi_fan = 0
    Hikoi_fan = hikoi.author.id
    #1st try
    if Hikoi_anger == 0 and Hikoi_copied == 0:
        if RPC == Hikoi_rpc:
            await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
            await hikoi.send("Why are you copying me!! " + hikoi.message.author.mention)
            Hikoi_copied+=1
        if RPC == 1:
            if Hikoi_rpc == 2:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("I just let you win this time " + hikoi.message.author.mention)
                Hikoi_anger+=1
            elif Hikoi_rpc == 3:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("Haha you noob " + hikoi.message.author.mention)
        if RPC == 2:
            if Hikoi_rpc == 3:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("I just let you win this time " + hikoi.message.author.mention)
                Hikoi_anger+=1
            elif Hikoi_rpc == 1:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("Haha you noob " + hikoi.message.author.mention)
        if RPC == 3:
            if Hikoi_rpc == 1:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("I just let you win this time " + hikoi.message.author.mention)
                Hikoi_anger+=1
            elif Hikoi_rpc == 2:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("Haha you noob " + hikoi.message.author.mention)
    #2nd try(loss)
    elif Hikoi_anger == 1:
        if RPC == Hikoi_rpc:
            await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
            await hikoi.send("Why are you copying me!! " + hikoi.message.author.mention)
            Hikoi_anger = 0
            Hikoi_copied+=1
        if RPC == 1:
            if Hikoi_rpc == 2:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("Next time I will win for sure " + hikoi.message.author.mention)
                Hikoi_anger+=1
            elif Hikoi_rpc == 3:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("See? just like I told you " + hikoi.message.author.mention)
                Hikoi_anger = 0
        if RPC == 2:
            if Hikoi_rpc == 3:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("Next time I will win for sure " + hikoi.message.author.mention)
                Hikoi_anger+=1
            elif Hikoi_rpc == 1:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("See? just like I told you " + hikoi.message.author.mention)
                Hikoi_anger = 0
        if RPC == 3:
            if Hikoi_rpc == 1:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("Next time I will win for sure" + hikoi.message.author.mention)
                Hikoi_anger+=1
            elif Hikoi_rpc == 2:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("See? just like I told you " + hikoi.message.author.mention)
                Hikoi_anger = 0
    #try copying
    elif Hikoi_copied == 1:
        if RPC == Hikoi_rpc:
            await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
            await hikoi.send("Stop copying me!! " + hikoi.message.author.mention)
        if RPC == 1:
            if Hikoi_rpc == 2:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("I just let you win this time " + hikoi.message.author.mention)
                Hikoi_anger+=1
                Hikoi_copied=0
            elif Hikoi_rpc == 3:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("Haha you noob " + hikoi.message.author.mention)
                Hikoi_copied=0
        if RPC == 2:
            if Hikoi_rpc == 3:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("I just let you win this time " + hikoi.message.author.mention)
                Hikoi_anger+=1
                Hikoi_copied=0
            elif Hikoi_rpc == 1:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("Haha you noob " + hikoi.message.author.mention)
                Hikoi_copied=0
        if RPC == 3:
            if Hikoi_rpc == 1:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("I just let you win this time " + hikoi.message.author.mention)
                Hikoi_anger+=1
                Hikoi_copied=0
            elif Hikoi_rpc == 2:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("Haha you noob " + hikoi.message.author.mention)
                Hikoi_copied=0
    #try3(loss)
    elif Hikoi_anger == 2:
        if RPC == Hikoi_rpc:
            await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
            await hikoi.send("Why are you copying me!! " + hikoi.message.author.mention)
            Hikoi_anger = 0
            Hikoi_copied+=1
        if RPC == 1:
            if Hikoi_rpc == 2:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send(hikoi.message.author.mention + " is definitely cheating.I don\'t want play anymore :triumph:")
                Hikoi_ban = hikoi.author.id
                Hikoi_anger=0
            elif Hikoi_rpc == 3:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("See? just like I told you " + hikoi.message.author.mention)
                Hikoi_anger = 0
        if RPC == 2:
            if Hikoi_rpc == 3:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send(hikoi.message.author.mention + " is definitely cheating.I don\'t want play anymore :triumph:")
                Hikoi_ban = hikoi.author.id
                Hikoi_anger=0
            elif Hikoi_rpc == 1:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("See? just like I told you " + hikoi.message.author.mention)
                Hikoi_anger = 0
        if RPC == 3:
            if Hikoi_rpc == 1:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send(hikoi.message.author.mention + " is definitely cheating.I don\'t want play anymore :triumph:")
                Hikoi_ban = hikoi.author.id
                Hikoi_anger=0
            elif Hikoi_rpc == 2:
                await hikoi.send(Hikoi_RPC[Hikoi_rpc-1])
                await hikoi.send("See? just like I told you " + hikoi.message.author.mention)
                Hikoi_anger = 0

#identity check
@hikoi.command(brief = "Check your identity.Just to be sure.",name = "Who-am-I",aliases = ["who-am-I","who-am-i","who_am_i","who_am_I"])
async def who(hikoi):
    #you can be anything
    Anything = ["You are an otaku Baka :stuck_out_tongue_closed_eyes:",
                "You are already dead:skull::skeleton:",
                "You are the chosen one.You will fight for justice protecting innocent and kill the demon lord.:crossed_swords:",
                "You are just a virgin",
                "LOL:joy: You really don\'t know who you are?"
                "You are The Ancient One"
                ]
    if hikoi.author.id == 452756967937540096:
        await hikoi.send("You are nothing my master.Nothing:expressionless:")
    else:
        await hikoi.send(random.choice(Anything))

#cant work with rhthm
@hikoi.command(brief = "Interact or Play an album", name = "Song" , aliases = ["song"])
async def Song(hikoi, mode, album):
    album = album + ".txt"
    if mode == "create":
        calbum = open(album,"w+")
        calbum.close()
        await hikoi.send("Creating album : " + album)
    elif mode == "play":
        calbum = open(album, "r")
        csong = calbum.readlines()
        i = 0
        while csong[i] != '\0':
            await hikoi.send("!p " + csong[i])
            i+=1
        calbum.close()
    elif mode == "show":
        calbum = open(album,"r")
        await hikoi.send(calbum.read())
        calbum.close()

#cant work with rhthm
@hikoi.command(brief = "Add song to an album", name = "Add_song" , aliases = ["add_song"])
async def Add_song(hikoi, album, song):
    album = album + ".txt"
    calbum = open(album,"a")
    calbum.write(song + "\n")
    calbum.close()

@hikoi.command(brief = "Report bug or problem to Hikoi's developer", name = "Report", aliases = ["report"])
async def Report(hikoi, prob):
    report = open("issue.txt", "a")
    report.write(prob + "\n")
    report.close()

hikoi.run(Hikoi_Token)
