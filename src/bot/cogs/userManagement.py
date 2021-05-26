import discord
from discord.ext import commands
from AntiSpam import AntiSpamHandler


class userManagement(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.handler = AntiSpamHandler(self.bot, warn_only=True)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Started userMangement cog.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"A new {member} joined")
        embed = discord.Embed(title="Welcome!", description=f"Hello {member.mention}! Welcome to **Hova.finance**! "
                                                            f"We are excited to have you here! ",
                              colour=discord.Color.blue())
        embed.set_author(name="Mayaa")
        embed.set_thumbnail(url=member.avatar_url)
        welcome_channel = self.bot.get_channel(844873592360927252)
        await welcome_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if  message.channel.id != 846328332224430090:
            try:
                await self.bot.handler.propagate(message)
            except Exception as e:
                print(e)


def setup(bot):
    bot.add_cog(userManagement(bot))
