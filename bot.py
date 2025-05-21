import discord
import os
from discord import app_commands
from commands import register_commands

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        register_commands(self.tree)
        await self.tree.sync()
        print("Slash commands synced.")

def main():
    client = MyClient()
    client.run(TOKEN)

if __name__ == "__main__":
    main()
