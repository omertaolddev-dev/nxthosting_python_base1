import os

# Prefix for legacy text commands (slash commands don't need this, but it's
# kept for the built-in eval/owner commands)
PREFIX = "!"

# Set this to your test server's ID for instant slash command sync while
# developing. Leave empty ("") to sync globally (takes up to 1h to propagate).
GUILD_ID = int(os.getenv("GUILD_ID")) if os.getenv("GUILD_ID") else None

# User IDs allowed to use owner-only commands (eval, shutdown, etc.)
OWNER_IDS = [int(i) for i in os.getenv("OWNER_IDS", "").split(",") if i.strip().isdigit()]

# Embed color used by the EmbedMaker helper (hex, no #)
EMBED_COLOR = 0x5865F2
