import random
from typing import List

from discord.ext import commands, tasks


class TasksCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.insult_task.start()

    @tasks.loop(seconds=3600)
    async def insult_task(self) -> None:
        await self.bot.wait_until_ready()
        if self.bot.conf_options["APP"]["USER_TO_INSULT"] != "":
            async with self.bot.session.get("https://insult.mattbas.org/api/insult.json") as r:
                json_data = await r.json(content_type="text/json")
            insult_list: List[str] = self.bot.conf_options["APP"]["INSULTS_LIST"]
            actual_insult: str = random.choice([random.choice(insult_list), json_data["insult"]])
            channel = await self.bot.fetch_channel(944109932989530162)
            await channel.send(
                f"Hey <@{self.bot.conf_options['APP']['USER_TO_INSULT']}>, {actual_insult}"
            )
        else:
            return


def setup(bot: commands.Bot) -> None:
    bot.add_cog(TasksCog(bot))
