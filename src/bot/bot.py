import discord
from discord.ext import commands
import os
from environment import BOT_TOKEN

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():
    print("Mayaa is online")


for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(BOT_TOKEN)
