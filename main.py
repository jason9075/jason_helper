import discord
from discord import app_commands
import requests
from bs4 import BeautifulSoup
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced.")

client = MyClient()

@client.tree.command(name="get", description="取得美金對台幣匯率")
async def get_exchange(interaction: discord.Interaction):
    await interaction.response.defer()  # 回應稍後回傳，避免 timeout

    try:
        r = requests.get("https://www.bing.com/search?q=usdtwd")
        soup = BeautifulSoup(r.text, "html.parser")
        result = soup.select_one("div.b_focusTextLarge")
        price = result.text.strip() if result else "無法找到匯率資訊"
    except Exception as e:
        price = f"發生錯誤: {str(e)}"

    await interaction.followup.send(f"目前美金兌台幣匯率為：{price}")

client.run(TOKEN)
