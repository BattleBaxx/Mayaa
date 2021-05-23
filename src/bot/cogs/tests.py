import discord
from discord.ext import commands


class test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx, *, arg):
        await ctx.send(arg)

    @commands.command()
    async def log_avatar_url(self, ctx):
        await ctx.send(ctx.message.author.avatar_url)

    @commands.command()
    async def embed(self, ctx, *, arg):
        embed = discord.Embed(title="Test Embed", description=arg, colour=0xFF5733)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(test(bot))
