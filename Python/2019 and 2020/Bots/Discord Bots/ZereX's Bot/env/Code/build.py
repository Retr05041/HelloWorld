# ---<{                A Bot for ZereX's Server             }>---
# ---<{                     March 1, 2020                   }>---
# ---<{          By: Parker Cranfield | in: Python 3+       }>---
# ---<{     https://discordpy.readthedocs.io/en/latest/     }>---


# REQUIRMENTS
#   - discord.py libary
#   - itertools

# IMPORTS
import discord
from discord.ext import commands, tasks # Easier bot setup | for background tasks
# from itertools import cycle # So we can cycle through lists

# VARIABLES
token = "NjgzODQwNTk0OTI1MTkxMjU5.XlxaYw.ip8C2AxoE2mntht0Ff5lOKZ_o6w" # secret bot token
zerexBot_prefix = "-" # prefix
# zerexBot_status = cycle(["", "", ""]) # Cycles through status's
zerexBot = commands.Bot(command_prefix = zerexBot_prefix) # Sets up client | prefix
zerexBot.remove_command("help") # Removes defult "help" command
security_password = "bWFzdGVybXl0aGljYWxpc2FoYWlyeW5vb2RsZQ==" # for special commnds

#============================================================================

class Events:

    # ON_READY EVENT
    @zerexBot.event # Notice how it calls client | function decorator
    async def on_ready(): # Async function | when the bot is ready
        print(zerexBot.user.name + " is ready!")
        print(f"{zerexBot.user.name}'s initial latency : {round(zerexBot.latency * 1000)}ms")
        # change_status.start()
        print("---------------------------")
        await zerexBot.change_presence(activity = discord.Game("the quite game.")) # Changes what zerexBot is doing

    # ON_MEMBER_JOIN EVENT
    @zerexBot.event
    async def on_member_join(member): # When someone joins the server
        print(f"{member} has joined the server.") # Async function | Prints this | f"{}" is a good way to insert variables into strings

    # ON_MEMBER_REMOVE EVENT
    @zerexBot.event
    async def on_member_remove(member): # When someone leaves the server
        print(f"{member} has left the server.") # Async function | Prints this

#============================================================================

class Tasks:
    pass

#============================================================================

class Commands:

    # HELP COMMAND
    @zerexBot.command()
    async def help(ctx): # ctx = context | always your first arg when you make a command
        author = ctx.message.author # Gets the name of who asked the command
        embed = discord.Embed(colour = discord.Colour.orange()) # Changes the PM's text to orange
        embed.set_author(name="***COMMANDS***") # Changes the placement of where the members name should be on the text to "Help" to better stand out
        # Help list starts here | add another line for each command
        embed.add_field(name = "```-ping```", value = "Returns 'Pong!', also shows latency of bot (ms)", inline = False) # Ping command
        embed.add_field(name = "```-clear (password) (int)```", value = "Clears messages, specify how many", inline = False) # Clear command
        embed.add_field(name = "```-staffhelp```", value = "Alerts Staff that theres a noob in need of assistance", inline = False) # Staffhelp
        embed.add_field(name = "```-twitch```", value = "Mythicals Twitch link", inline = False) # Twitch command
        embed.add_field(name = "```-mixer```", value = "Mythicals mixer link", inline = False) # Mixer command
        embed.add_field(name = "```-instagram```", value = "Mythicals Instagram link", inline = False) # Instagram command
        embed.add_field(name = "```-twitter```", value = "Mythicals Twitter link", inline = False) # Twitter command

        await author.send(embed = embed) # Sends help message to author

    # PING COMMAND
    @zerexBot.command()
    async def ping(ctx): # Takes ctx
        await ctx.send(f"```Pong! I responded in {round(zerexBot.latency * 1000)}ms```") # Sends pong back and tells you the latency | latency is in seconds so * 1000 to get ms

    # CLEAR MESSAGES COMMAND
    @zerexBot.command()
    @commands.has_permissions(manage_messages = True) # Command us only usable if the author has the "manage_messages" permission
    async def clear(ctx, password, amount : int = 2): # Takes ctx and amount | amount is how many messages, ex. .clear 100, defult is the clear command and the message above it
        if password == security_password:
            await ctx.channel.purge(limit=amount) # Purges the number of messages in the chat you typed the command to
        else:
            await ctx.send(f"```F off you little shit```")

    # STAFF HELP
    @zerexBot.command()
    async def staffhelp(ctx):
        role = discord.utils.get(ctx.message.guild.members, name="Staff")
        await ctx.channel.send(f"{role}, there is a noob in need of assistance!")

    # Twitch
    @zerexBot.command()
    async def twitch(ctx):
        author = ctx.message.author  # Gets the name of who asked the command
        await author.send("https://www.twitch.tv/zerexstv/")

    # Mixer
    @zerexBot.command()
    async def mixer(ctx):
        author = ctx.message.author  # Gets the name of who asked the command
        await author.send("https://mixer.com/TeamZereX")

    # Instagram
    @zerexBot.command()
    async def instagram(ctx):
        author = ctx.message.author  # Gets the name of who asked the command
        await author.send("https://www.instagram.com/zerexs.tv/")

    # Twitter
    @zerexBot.command()
    async def twitter(ctx):
        author = ctx.message.author  # Gets the name of who asked the command
        await author.send("https://twitter.com/TeamZereX")

#============================================================================

# RUNS CLIENT
zerexBot.run(token)
