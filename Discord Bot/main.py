import discord
from discord import app_commands
import asyncio

# 設定 intents
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

GUILD_ID = 000000000000000000000

# 當機器人準備好時觸發
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id = GUILD_ID))  # 同步 Slash command
    print(f'Bot connected: {client.user.name}')

# 範例 Slash command: /hello
@tree.command(name="hello", description="回應一個問候訊息")
@app_commands.guilds(discord.Object(id = GUILD_ID))
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'你好，{interaction.user.mention}！')

# 啟動機器人
async def main():
    try:
        await client.start('YOUR_BOT_TOKEN')
    except Exception as e:
        print(f'啟動失敗：{e}')

if __name__ == "__main__":
    asyncio.run(main())