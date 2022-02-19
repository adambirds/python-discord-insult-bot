from discord.ext import commands


class CommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def insult(self, ctx: commands.Context, user: str) -> None:
        """>insult command"""
        async with self.bot.session.get("https://insult.mattbas.org/api/insult.json") as r:
            json_data = await r.json(content_type="text/json")
        await ctx.send(f"Hey @{user}, {json_data['insult']}")


def setup(bot: commands.Bot) -> None:
    bot.add_cog(CommandsCog(bot))
