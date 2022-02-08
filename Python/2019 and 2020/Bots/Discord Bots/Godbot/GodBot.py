# ---<{    A God Bot for My High School LC Discord Server   }>---
# ---<{             Started Coded on October 22, 2019        }>---
# ---<{          By: Parker Cranfield | in: Python 3+       }>---
# ---<{     https://discordpy.readthedocs.io/en/latest/     }>---


# REQUIRMENTS
#   - discord.py libary
#   - itertools

# IMPORTS
import discord
from discord.ext import commands, tasks # Easier bot setup | for background tasks
from itertools import cycle # So we can cycle through lists

# VARIABLES
token = "NjM2NDIwODQ0MTgwMjA5NzA0.Xa_XKQ.PiL27NqWTz_PRw_MBil1RFAc5mg"
godbot_prefix = "."
# godbot_status = cycle(["", "", ""]) # Cycles through status's
godbot = commands.Bot(command_prefix = godbot_prefix) # Sets up client | prefix
godbot.remove_command("help") # Removes defult "help" command
security_password = "bXluYW1laXNwYXJrZXJjcmFuZmllbGQ="

#============================================================================

class Events:

    # ON_READY EVENT
    @godbot.event # Notice how it calls client | function decorator
    async def on_ready(): # Async function | when the bot is ready
        print(godbot.user.name + " is ready!")
        print(f"{godbot.user.name}'s initial latency : {round(godbot.latency * 1000)}ms")
        # change_status.start()
        print("---------------------------")
        await godbot.change_presence(activity = discord.Game("the quite game.")) # Changes what godbot is doing

    # ON_MEMBER_JOIN EVENT
    @godbot.event
    async def on_member_join(member): # When someone joins the server
        print(f"{member} has joined the server.") # Async function | Prints this | f"{}" is a good way to insert variables into strings

    # ON_MEMBER_REMOVE EVENT
    @godbot.event
    async def on_member_remove(member): # When someone leaves the server
        print(f"{member} has left the server.") # Async function | Prints this

#============================================================================

class Tasks:
    pass

#============================================================================

class Commands:

    # HELP COMMAND
    @godbot.command()
    async def help(ctx): # ctx = context | always your first arg when you make a command
        author = ctx.message.author # Gets the name of who asked the command
        embed = discord.Embed(colour = discord.Colour.orange()) # Changes the PM's text to orange
        embed.set_author(name="***COMMANDS***") # Changes the placement of where the members name should be on the text to "Help" to better stand out
        # Help list starts here | add another line for each command
        embed.add_field(name = "```KEY```", value = "EVERYTHING = everyone can use | STAFF+ = anyone over staff can use | SECURITY = no one but security can use")
        embed.add_field(name = "```.ping```", value = "Returns 'Pong!', also shows latency of bot (ms) | EVERYONE", inline = False) # Ping command
        embed.add_field(name = "```.clear (int)```", value = "Clears messages, specify how many | STAFF+", inline = False) # Clear command
        embed.add_field(name = "```.mute @member (reason)```", value = "Mutes inputed member, member input is manditory, reason is not manditory | STAFF+", inline = False) # Mute command
        embed.add_field(name = "```.unmute @member```", value = "Umutes inputed member, member input is manditory | STAFF+", inline = False) # Unmute command
        embed.add_field(name = "```.kick @member (reason)```", value = "Kicks inputed member, reason is not manditory | STAFF+", inline = False) # Kick command
        embed.add_field(name = "```.giverole (password) @member (role)```", vlaue = "Gives a role to a certain member | SECURITY", inline = False) # Giverole command
        embed.add_field(name = "```.ban @member (password) (reason)```", value = "Bans inputed member, password is manditory, reason is not manditory | SECURITY", inline = False) # Ban command
        embed.add_field(name = "```.pardon @user_id (password)```", value = "Unbans inputed member_id, password is manditory | SECURITY", inline = False) # Unban command
        embed.add_field(name = "```.banlist (password)```", value = "Prints banlist , password is manditory | SECURITY", inline = False) # Banlist command

        await author.send(embed = embed) # Sends help message to author

    # PING COMMAND
    @godbot.command()
    async def ping(ctx): # Takes ctx
        await ctx.send(f"```Pong! I responded in {round(godbot.latency * 1000)}ms```") # Sends pong back and tells you the latency | latency is in seconds so * 1000 to get ms

    # CLEAR MESSAGES COMMAND
    @godbot.command()
    @commands.has_permissions(manage_messages = True) # Command us only usable if the author has the "manage_messages" permission
    async def clear(ctx, amount : int = 2): # Takes ctx and amount | amount is how many messages, ex. .clear 100, defult is the clear command and the message above it
        await ctx.channel.purge(limit=amount) # Purges the number of messages in the chat you typed the command to

    # MUTE COMMAND
    @godbot.command()
    @commands.has_permissions(manage_messages = True) # Command us only usable if the author has the "manage_messages" permission
    async def mute(ctx, member : discord.Member, *, reason=None): # Takes ctx, the member who your baning, and the reason(s) | member : discord.Member = take the member argument as the discord.Member argument | * = all arguments other than memeber and innitial reason just adds onto reason | reason=None = no reasons right now
        await member.add_roles(discord.utils.get(ctx.guild.roles, name="Muted")) # Puts Member into "Muted" role
        await ctx.send(f"```{member} has been muted```") # Tells everyone the member has be muted

    # UNMUTE COMMAND
    @godbot.command()
    @commands.has_permissions(manage_messages = True) # Command us only usable if the author has the "manage_messages" permission
    async def unmute(ctx, member : discord.Member): # Takes ctx, and the member who your umuting | member : discord.Member = take the member argument as the discord.Member argument
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted")) # Removes "Muted" role
        await ctx.send(f"```{member} has been unmuted```") # Tells everyone the member has been ummuted

    # KICK COMMAND
    @godbot.command()
    @commands.has_permissions(kick_members = True) # Command us only usable if the author has the "kick_members" permission
    async def kick(ctx, member : discord.Member, *, reason=None): # Takes ctx, the member who your kicking, and the reason(s) | member : discord.Member = take the member argument as the discord.Member argument | * = all arguments other than memeber and innitial reason just adds onto reason | reason=None = no reasons right now
        await member.kick(reason=reason) # Kicks member for the reason we submit, if non is provided then it will still kick member

    # GIVEROLE COMMAND
    @godbot.command()
    async def giverole(ctx, password, member : discord.Member, *, role : discord.Role): # takes ctx, pass, member, and the role
            if password == security_password: # Password checks
                await member.add_roles(role) # gives specified member role
                await ctx.send(f"```{member} has gotten {role} role!```") # Tells everyone about it
            else:
                await ctx.send("```Wrong Password.```")

    # BAN COMMAND
    @godbot.command()
    async def ban(ctx, member : discord.Member, password=None, *, reason=None): # Takes ctx, password, the member who your baning, and the reason(s) | member : discord.Member = take the member argument as the discord.Member argument | * = all arguments other than memeber and innitial reason just adds onto reason | reason=None = no reasons right now
        if password == security_password: # Password checks
            await member.ban(reason=reason) # Bans member for the reason we submit, if non is provided then it will still ban member
        else:
            await ctx.send("```Wrong Password.```")

    # UNBAN COMMAND
    @godbot.command()
    async def pardon(ctx, id : int, password=None): # Takes ctx, user id, password | user id = User id instead of actual name and discriminatior
        if password == security_password:
            user = await godbot.fetch_user(id) # Finds user with the ID
            await ctx.guild.unban(user) # Unbans them
            await ctx.send(f"```{id.mention} has been unbanned```")
        else:
            await ctx.send("```Wrong Password.```")

    # BANLIST COMMAND
    @godbot.command()
    async def banlist(ctx, password=None): # Takes ctx, and password
        if password == security_password: # Password checks
             banlist = await ctx.guild.bans() # Gets banlist
             await ctx.send(banlist) # sends banlist
        else:
            await ctx.send("```Wrong Password.```")

#============================================================================

# RUNS CLIENT
godbot.run(token)
