import discord
from discord.ext import commands
import os

# 環境変数からDiscordトークンを取得
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容へのアクセス権を許可
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user}')

@bot.event
async def on_ready():
    activity = discord.Game(name="起動中 | オンライン")
    await bot.change_presence(status=discord.Status.online, activity=activity)

# ボットの実行
bot.run(DISCORD_TOKEN)  # 環境変数からトークンを取得して使用
