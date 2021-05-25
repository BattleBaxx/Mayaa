import sys
import traceback
import os

import discord
from discord.ext import commands

from bot.environment import BOT_TOKEN, COMMAND_PREFIX, DESCRIPTION, DB_HOST, DB_PASSWORD, DB_NAME, DB_USER
from dependencies.database.base import Database


class Bot(commands.AutoShardedBot):

    def __init__(self):

        intents = discord.Intents.default()
        intents.members = True
        super().__init__(command_prefix=COMMAND_PREFIX,
                         description=DESCRIPTION, pm_help=None, help_attrs=dict(hidden=True),
                         fetch_offline_members=False, heartbeat_timeout=150.0, intents=intents)
        self.bot_token = BOT_TOKEN
        self.db = Database.getInstance(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

        for filename in os.listdir('./bot/cogs'):
            if filename.endswith(".py"):
                self.load_extension(f"bot.cogs.{filename[:-3]}")

    async def on_ready(self):
        print("Mayaa is online")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f"What you are attempting to do isn't implemented by the lazy devs 😱 | error: {error}")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('Sorry. This command is disabled and cannot be used.')
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send('This command cannot be used in private messages.')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You are missing required arguments in the command. :frowning:")
        elif isinstance(error, commands.CommandInvokeError):
            original = error.original
            if not isinstance(original, discord.HTTPException):
                print(f'In {ctx.command.qualified_name}:', file=sys.stderr)
                traceback.print_tb(original.__traceback__)
                print(f'{original.__class__.__name__}: {original}', file=sys.stderr)
        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.send(error)

    def run(self):
        try:
            super().run(self.bot_token, reconnect=True)
        except Exception as e:
            print(f"Startup Error: {type(e)}: {e}")










