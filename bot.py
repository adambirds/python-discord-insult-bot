import os
import sys
import traceback
from typing import Any

import discord
import yaml
from aiohttp import ClientSession
from discord.ext import commands


# Define function to process yaml config file
def process_config_file() -> Any:
    with open("config.yaml", "r") as stream:
        config_options = yaml.safe_load(stream)

    return config_options


class PythonInsultBot(commands.Bot):
    async def start(self, *args: str, **kwargs: str) -> None:
        async with ClientSession() as self.session:
            await super().start(*args, **kwargs)


def main() -> None:
    intents = discord.Intents.default()
    intents.guilds = True

    bot = PythonInsultBot(
        command_prefix=">", description="Python Discord Insult Bot", intents=intents
    )
    bot.conf_options = process_config_file()

    for filename in os.listdir("./modules/cogs/"):
        if filename.endswith(".py"):
            try:
                bot.load_extension(f"modules.cogs.{filename}".strip(".py"))
            except Exception:
                print(f"Failed to load extension modules.cogs.{filename}.", file=sys.stderr)
                traceback.print_exc()

    @bot.event
    async def on_message(message: discord.Message) -> None:
        """
        on_message event.
        """
        if message.author.bot:
            return

        print(f"{message.author}: {message.content}")

        await bot.process_commands(message)

    bot.run(bot.conf_options["APP"]["ACCESS_TOKEN"], bot=True)


if __name__ == "__main__":
    main()
