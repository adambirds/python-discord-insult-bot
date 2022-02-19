from discord.ext import commands


class EventsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Ready!")
        print("Logged in as ---->", self.bot.user)
        print("ID:", self.bot.user.id)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(EventsCog(bot))
