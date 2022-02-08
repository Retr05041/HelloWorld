# ---<{    A Teacher Verifirer Bot for My High School LC Discord Server   }>---
# ---<{                  Started Coded on October 28, 2019                }>---
# ---<{                 By: Parker Cranfield | in: Python 3+              }>---
# ---<{             https://discordpy.readthedocs.io/en/latest/           }>---


# REQUIRMENTS
#   - discord.py libary
#   - tinydb

# IMPORTS
import discord
from discord.ext import commands, tasks # Easier bot setup | for background tasks
import discord.utils

# VARIABLES
token = "NjM4NDA3MjE4ODIzMjk5MDcz.XbcRFg.GmPrL3EPXRATtV4xbNcBglPB3Qo"
teacherbot_prefix = "_!"
# teacherbot_status = cycle(["", "", ""]) # Cycles through status's
teacherbot = commands.Bot(command_prefix = teacherbot_prefix) # Sets up client | prefix
teacherbot.remove_command("help") # Removes defult "help" command

#============================================================================

class Events:

    # ON_READY EVENT
    @teacherbot.event # Notice how it calls client | function decorator
    async def on_ready(): # Async function | when the bot is ready
        print(teacherbot.user.name + " is ready!")
        print(f"{teacherbot.user.name}'s initial latency : {round(teacherbot.latency * 1000)}ms")
        # change_status.start()
        print("---------------------------")
        await teacherbot.change_presence(activity = discord.Game("the sleeping game.")) # Changes what teacherbot is doing

#============================================================================

class Tasks:
    pass

#============================================================================

class Commands:

    # HELP COMMAND
    @teacherbot.command()
    async def help(ctx): # ctx = context | always your first arg when you make a command
        author = ctx.message.author # Gets the name of who asked the command
        embed = discord.Embed(colour = discord.Colour.green()) # Changes the PM's text to orange
        embed.set_author(name="***COMMANDS***") # Changes the placement of where the members name should be on the text to "Help" to better stand out
        # Help list starts here | add another line for each command
        embed.add_field(name = "```.ping```", value = "Returns 'Pong!', also shows latency of bot (ms)", inline = False) # Ping command
        await author.send(embed = embed) # Sends help message to author

    # PING COMMAND
    @teacherbot.command()
    async def ping(ctx): # Takes ctx
        await ctx.send(f"```Pong! I responded in {round(teacherbot.latency * 1000)}ms```") # Sends pong back and tells you the latency | latency is in seconds so * 1000 to get ms

    # VERIFY COMMAND
    @teacherbot.command()
    async def verify(ctx, role : discord.Role, password):
        author = ctx.message.author
        await author.add_roles(role)
        await ctx.send(f"```{author} has become a teacher!```")





#============================================================================

# RUNS CLIENT
teacherbot.run(token)
