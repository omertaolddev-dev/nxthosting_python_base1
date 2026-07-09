import discord
import config


class EmbedMaker(discord.Embed):
    """
    Same idea as discord.Embed but with sensible defaults already applied.

    embed = EmbedMaker(title="Title", description="Description")
    await ctx.send(embed=embed)
    """

    def __init__(self, *, color=None, timestamp=None, **kwargs):
        super().__init__(
            color=color if color is not None else config.EMBED_COLOR,
            timestamp=timestamp if timestamp is not None else discord.utils.utcnow(),
            **kwargs,
        )
