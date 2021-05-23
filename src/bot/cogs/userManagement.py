import discord
from discord.ext import commands


class userManagement(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Started userMangement cog.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"A new {member} joined")
        embed = discord.Embed(title="Welcome!", description=f"Hello {member.mention}! Welcome to **Hova.finance**! "
                                                            f"We are excited to have you here! ", colour=discord.Color.blue())
        embed.set_author(name="Mayaa")
        embed.set_thumbnail(url=member.avatar_url)
        welcome_channel = self.bot.get_channel(844873592360927252)
        await welcome_channel.send(embed=embed)

    # @commands.command()
    # async def invite(self, ctx, *, args):
    #     try:
    #         args = int(args)
    #         print(type(args))
    #         print(args)
    #         new_user = await self.bot.fetch_user(args)
    #         print(new_user)
    #         invitelink = await ctx.channel.create_invite(max_uses=1, unique=True)
    #         # await self.bot.send_message(new_user, invitelink)
    #         await new_user.send(invitelink)
    #     except Exception as e:
    #         print(e)

def setup(bot):
    bot.add_cog(userManagement(bot))
