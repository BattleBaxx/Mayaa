import discord
from discord.ext import commands


class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        # print(reaction.message.channel.id)
        if reaction.message.channel.id == 844826625274019860:
            # print("Inside")
            role = discord.utils.get(user.guild.roles, name="member")
            await user.add_roles(role)

    @commands.command(hwlp="Add roles to members (Only the CEO can run this command)", brief="Add roles")
    @commands.has_role("CEO")
    async def addrole(self, ctx, role_name, user: discord.Member):
        # print(user.id)
        role = discord.utils.get(user.guild.roles, name=role_name)
        await user.add_roles(role)
        # await self.bot.add_roles(user, role)

    @commands.command(hwlp="Remove roles to members (Only the CEO can run this command)", brief="Remove roles")
    @commands.has_role("CEO")
    async def removerole(self, ctx, role_name, user: discord.Member):
        print(user.id)
        role = discord.utils.get(user.guild.roles, name=role_name)
        await user.remove_roles(role)


def setup(bot):
    bot.add_cog(Role(bot))
