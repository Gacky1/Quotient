# for tortoise-orm

TORTOISE = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "localhost",
                "port": "5432",
                "user": "postgres",  # Change this to your PostgreSQL username
                "password": "Hacker01",  # Change this to your PostgreSQL password
                "database": "quotient",  # Change this to your database name
            }
        }
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    }
}


POSTGRESQL = {}

EXTENSIONS = (
    "cogs.events",
    "cogs.mod",
    "cogs.utility",
    "cogs.premium",
    "cogs.esports",
    "cogs.quomisc",
    "cogs.reminder",
)

DISCORD_TOKEN = "MTM3OTkwMTUwMzcxNTgwMzE2Ng.GhcbKi.QjRkUAuE_BKUKW1MxUg7H2tybNuASqIegDWo6s"

COLOR = 0x00FFB3

FOOTER = "In the memory of our dev ROHAN"

PREFIX = "q"

SERVER_LINK = "https://discord.gg/7qmuAKAQ"

BOT_INVITE = "https://discord.gg/7qmuAKAQ"

WEBSITE = "https://gacky.pages.dev"

REPOSITORY = ""

DEVS =(1334572592236855438,)

# LOGS
SHARD_LOG = ""
ERROR_LOG = ""
PUBLIC_LOG = ""

FASTAPI_URL = "http://localhost:8000"  # Set this to your FastAPI server URL if needed

PRIME_EMOJI = "<:prime:123456789012345678>"  # Set this to your actual prime emoji or leave as placeholder
