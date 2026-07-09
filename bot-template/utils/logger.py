from datetime import datetime

COLORS = {
    "info": "\033[36m",     # cyan
    "success": "\033[32m",  # green
    "warning": "\033[33m",  # yellow
    "error": "\033[31m",    # red
}
RESET = "\033[0m"
BOLD = "\033[1m"


def logger(level: str, title: str, *messages: str):
    """
    Simple colored console logger.

    logger("info", "COGS", "Loaded cogs.general")
    logger("error", "COMMAND", "eval failed", str(exception))
    """
    color = COLORS.get(level, "")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    joined = " ".join(str(m) for m in messages)
    print(f"{color}[{timestamp}] [{level.upper()}] [{title}]{RESET} {joined}")
