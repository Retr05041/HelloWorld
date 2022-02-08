#Imports
import random
import discord
from discord import Game
from discord.ext.commands import has_permissions, Bot

#Variables
BOT_PREFIX = "."
TOKEN = "NTQ2OTI2NjI1MTE2MjU4MzA0.D0vY5g.qfv3H3gZCYgKlDqztNYpLga0RSc"
client = Bot(command_prefix=BOT_PREFIX)
#Remove help
client.remove_command("help")


#Main

#New help -- makes a private message(good to look back on)
@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.orange())
    embed.set_author(name = "help")
    embed.add_field(name = ".8ball", value = "Answers yes/no questions form the beyond", inline = False)
    embed.add_field(name = ".gender", value = "The gender of the bot", inline = False)
    embed.add_field(name = ".ping", value = "You should know what this does", inline = False)
    embed.add_field(name = ".hobbies", value = "asks what dotty is into", inline = False)
    embed.add_field(name = ".joke", value = "tells you a random joke, There are 50, I have no life", inline = False)
    embed.add_field(name = ".purgechat", value = "clears chat - Only for Admins", inline = False)
    #send to the person
    await client.send_message(author, embed = embed)


#===============================================================================================================================

#8ball
@client.command(name = "8ball", pass_context = True) #See's if the string ".8ball"
async def eight_ball(context): #If the string ".eight_ball" is typed but is overruled by this ^
    possible_8ball_responses = [
        "That is a resounding no",
        "It is not likely",
        "It is quite possible",
        "Definitely",
        "You will just have to wait and see",
        "HA... Like that will ever happen"
    ]
    await client.say(random.choice(possible_8ball_responses) + ", " + context.message.author.mention) #Responds with a random answer + person who asked

#Bot gender
@client.command(name = "gender") #See's if the string ".gender"
async def gender(): #If the string ".gender" is typed but is overruled by this ^
    possible_gender_answers = [
    "I am an intergalactical assassi..... I am a discord bot, I dont have a gender ;)"
    ]
    await client.say(random.choice(possible_gender_answers)) #Responds with a random answer

#ping pong
@client.command(pass_context = True)
async def ping(context):
    await client.say("pong, " + context.message.author.mention)

#Hobbies
@client.command(name = "hobbies") #See's if the string ".hobbies"
async def hobbies(): #If the string "?gender" is typed but is overruled by this ^
    possible_hobby_answers = [
    "I sometimes plan on taking over the planet someday",
    "Being drastically anoying to code is always fun",
    "Hobbies? Why? You lookin for a date....... ;)"
    ]
    await client.say(random.choice(possible_hobby_answers)) #Responds with a random answer

#Jokes
@client.command(name = "joke") #See's if the string ".joke"
async def joke(): #If the string ".joke" is typed but is overruled by this ^
    pja = open("possible_joke_answers").read().splitlines() #Opens the text file with all the jokes and reads them
    myline = random.choice(pja) #Randomly chooses one
    await client.say(myline) #Says the one that was chosen

#=========================================================================================================================


#clears chat -- 100 messages at one time -- dangerous
@client.command(name = "purgechat", pass_context = True)
@has_permissions(administrator = True) #First checks if the person asking has the administrator privilages
async def clear(ctx, amount = 100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit = int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("Messages deleted.")


#On bot startup
@client.event
async def on_ready():
    await client.change_presence(game = Game(name = "with death"))
    print("Bot is ready!")
    print("Logged in as " + client.user.name)
    print("--------------")


#Run the bot
client.run(TOKEN)
