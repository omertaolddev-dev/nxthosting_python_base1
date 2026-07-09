# discord.py Bot Template

A very simple bot template for the `discord.py` library. Slash commands, cogs, custom logger, custom embeds.

## Features

| Feature |
|---|
| ✅ Very easy and simple |
| ✅ Slash commands (`app_commands`) |
| ✅ Cog / extension auto-loader |
| ✅ Built-in commands (`ping`, `help`, `eval`) |
| ✅ Owner-only command protection |
| ✅ Custom logger |
| ✅ Custom embeds |

## Setup

1. `pip install -r requirements.txt`
2. Rename `.env.example` to `.env` and fill in `DISCORD_TOKEN`.
3. (Optional) Set `GUILD_ID` in `.env` for instant slash command sync while developing.
4. (Optional) Set `OWNER_IDS` (comma separated) for the `eval` command.
5. `python bot.py`

## Adding a command

Create a new file in `cogs/` (or add a method to an existing cog):

```python
import discord
from discord import app_commands
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Says hello")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello, world!")

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

It gets auto-loaded and auto-synced on the next restart.

## Embeds

```python
from utils.embed import EmbedMaker

embed = EmbedMaker(title="Title", description="Description")
await interaction.response.send_message(embed=embed)
```

## Logger

```python
from utils.logger import logger

logger("warning", "COMMAND", "eval blocked for", "someuser", "not an owner")
```
