import os
import asyncio

import discord
from discord.ext import commands
from dotenv import load_dotenv

from utils.logger import logger
import config

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=config.PREFIX,
            intents=intents,
            help_command=None,
        )

    async def setup_hook(self):
        # load every cog in the cogs/ folder
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                extension = f"cogs.{filename[:-3]}"
                try:
                    await self.load_extension(extension)
                    logger("info", "COGS", f"Loaded {extension}")
                except Exception as e:
                    logger("error", "COGS", f"Failed to load {extension}", str(e))

        # sync slash commands (global sync can take up to 1h to propagate,
        # set config.GUILD_ID for instant sync during development)
        if config.GUILD_ID:
            guild = discord.Object(id=config.GUILD_ID)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            logger("info", "COMMANDS", f"Synced commands to guild {config.GUILD_ID}")
        else:
            await self.tree.sync()
            logger("info", "COMMANDS", "Synced commands globally")

    async def on_ready(self):
        logger("info", "READY", f"Logged in as {self.user} (ID: {self.user.id})")

    async def on_command_error(self, ctx, error):
        logger("warning", "COMMAND", f"Error in command {ctx.command}", str(error))


bot = Bot()


async def main():
    if not TOKEN:
        raise SystemExit("DISCORD_TOKEN is not set. Check your .env file / environment variables.")
    async with bot:
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
