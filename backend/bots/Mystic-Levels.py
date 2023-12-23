import discord
import json
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents)
tree = bot.tree
fp = open("../settings.json")
SETTINGS = json.load(fp)

@bot.command()
async def syncCommand(ctx):
    if ctx.author.id != 973834864853909525: return # if not me, Kai, exit
    msg = await ctx.send("syncing...")             # Send sync message
    await tree.sync()                              # sync / commands
    await msg.edit(content="done!")                # edit the sync message to notify we are done


@tree.command(name="rank")
async def rankCommand(interaction:discord.Interaction):
    pass # send pil image here




bot.run(SETTINGS["token"])