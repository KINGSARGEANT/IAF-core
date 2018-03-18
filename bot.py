import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client() #Initialise Client 

client = commands.Bot(command_prefix = "-") #Initialise client bot



@client.event
async def on_ready():
    online = discord.Status.online
    print("All Systems Check, We are Go.")
    await client.change_presence(game=discord.Game(name="Managing IAF Discord | -help"))


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content == "Hi": 
        await client.send_message(message.channel, "hi you are the bfg
                                  @client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content == "-help": 
        await client.send_message(message.channel, "For support or help Join this discord Here! https://discord.gg/yxSaVGV")
doft/rtt
    if message.content == "-reset": 
        await client.send_message(message.channel, "Reseting Standby.....")
        await client.send_message(message.channel, "Reset Completed")

################################ Auto roles ############################################
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Admissions")
    await client.add_roles(member, role)

###################### K / B #########################
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    if "Administrator" in [role.name for role in ctx.message.author.roles]:
        await client.say("{} Was Kicked from the IAF Discord.".format(user.name))
        await client.kick(user)
    else:
        await client.say("You do not have access to that command. Contact KINGSARGEANT if there are more problems")


@client.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    if "Administrator" in [role.name for role in ctx.message.author.roles]:
        await client.say("{} , was banned from the IAF Discord.".format(user.name))
        await client.ban(user)
    else:
        await client.say("You do not have access to that command. Contact KINGSARGEANT if there are more problems")

@client.command(pass_context=True)
async def on_member_join(ctx, member):
    embed = discord.Embed(title="Welcome Message", description="**Hello {}! Welcome to IAF Discord!**".format(user.name).format(ctx.message.server.name), color=0x00ffff)
    embed.add_field(name="We now have {} members!"(ctx.message.server.members))
    embed.set_thumbnail(url=user.avatar_url)


    











client.run("NDE1NTY2MDE5ODg1NTMxMTM3.DW3yDA.eI0hLgu_bwlZyEFeS-NjtYoiFUc")
