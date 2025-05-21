from discord import app_commands, Interaction
from scraper import get_usdtwd_rate

def register_commands(tree: app_commands.CommandTree):
    @tree.command(name="get", description="取得美金對台幣匯率")
    async def get_exchange(interaction: Interaction):
        await interaction.response.defer()
        rate = get_usdtwd_rate()
        await interaction.followup.send(f"目前美金兌台幣匯率為：{rate}")
