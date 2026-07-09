import discord
from discord import app_commands
from discord.ext import commands

import config
from utils.logger import logger


class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_owner_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id in config.OWNER_IDS

    @app_commands.command(name="eval", description="Evaluates Python code (owner only)")
    async def eval_command(self, interaction: discord.Interaction, code: str):
        if not self.is_owner_check(interaction):
            logger("warning", "COMMAND", "eval blocked for", str(interaction.user), "not an owner")
            await interaction.response.send_message("You are not allowed to use this command.", ephemeral=True)
            return

        try:
            result = eval(code)
            await interaction.response.send_message(f"```py\n{result}\n```")
        except Exception as e:
            await interaction.response.send_message(f"```py\n{e}\n```")


async def setup(bot: commands.Bot):
    await bot.add_cog(Owner(bot))
