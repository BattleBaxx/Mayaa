import discord
from discord.ext import commands
import math

from dependencies.database.models.count import Count

def is_power(x, y):
    if x == 1:
        return y == 1
    power = 1
    while power < y:
        power = power * x
    return power == y


class Level(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.db.base.metadata.create_all(self.bot.db.engine)
        self.session = self.bot.db.session()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Started level cog.")

        # data =
        # for row in data:
        #     print(row.id, row.count)
        # print(data)
        # row = Count(123, 0)
        # self.session.add(row)
        # self.session.commit()
        # self.session.close()

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            try:
                if self.session.query(Count).filter(Count.id == str(message.author.id)).first() is None:
                    new_user = Count(str(message.author.id), 1)
                    self.session.add(new_user)
                    self.session.commit()
                    self.session.close()
                    # print("In 1")
                else:
                    user_details = self.session.query(Count).filter(Count.id == str(message.author.id)).first()
                    user_details.count += 1
                    if is_power(10, user_details.count-1):
                        if user_details.count % 10 == 1:
                            await message.channel.send(
                                f"Congratulations, you have leveled up to level {int(math.log10(user_details.count))}!!!")
                    self.session.commit()
                    # print("In 2")
            except Exception as e:
                print(e)
        # print(f"{message.author.id} has messaged.")


def setup(bot):
    bot.add_cog(Level(bot))
