import discord
from discord import app_commands
from discord.ext import commands

from utils.embed import EmbedMaker


class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Replies with the bot's latency")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        embed = EmbedMaker(title="🏓 Pong!", description=f"Latency: `{latency}ms`")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="help", description="Shows the list of available commands")
    async def help(self, interaction: discord.Interaction):
        embed = EmbedMaker(title="Help")
        for command in self.bot.tree.get_commands():
            embed.add_field(
                name=f"/{command.name}",
                value=command.description or "No description",
                inline=False,
            )
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))
