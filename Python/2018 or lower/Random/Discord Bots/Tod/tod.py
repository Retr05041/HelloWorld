#Imports
import random
from discord import Game
from discord.ext.commands import Bot

#Variables
BOT_PREFIX = "*"
TOKEN = "NTQ3ODMyNjE3ODQ0ODY3MDgz.D08gcw.8IK7M2bz277XZWFifHoCM873wgs"
client = Bot(command_prefix=BOT_PREFIX)
#Remove help
client.remove_command("help")

#Main

#New help -- makes a private message(good to look back on)
@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.red())
    embed.set_author(name = "help")
    embed.add_field(name = "*truth", value = "asks a random dare", inline = False)
    embed.add_field(name = "*dare", value = "asks a random dare", inline = False)
    #send to the person
    await client.send_message(author, embed = embed)

#===============================================================================================================================

#Truth
@client.command(name = "truth", pass_context = True) #See's if the string "*truth"
async def truth(context): #If the string "*truth" is typed but is overruled by this ^
    truths = open("truth_list").read().splitlines() #Opens the text file with all the questions and reads them
    random_truths
    await client.say(random_truths + ", " + context.message.author.mention) #Responds with a random answer + person who asked

#Dare
@client.command(name = "dare", pass_context = True) #See's if the string "*dare"
async def dare(context): #If the string "*dare" is typed but is overruled by this ^
    dares = open("dare_list").read().splitlines() #Opens the text file with all the questions and reads them
    random_dare
    await client.say(random_dare + ", " + context.message.author.mention) #Responds with a random answer + person who asked

#=========================================================================================================================

#On bot startup
@client.event
async def on_ready():
    await client.change_presence(game = Game(name = "Truth or Dare")) #Uses game import
    print("Bot is ready!")
    print("Logged in as " + client.user.name)
    print("--------------")


#Run the bot
client.run(TOKEN)
