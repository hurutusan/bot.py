import discord
from discord.ext import commands
from flask import Flask
import threading

# Flaskアプリケーションの設定
app = Flask(__name__)

@app.route('/keep-alive', methods=['GET'])
def keep_alive():
    return 'OK'  # 定期的にリクエストを送ることで、ボットが動作し続ける

# Discordボットの設定
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="起動中 | オンライン"))

@bot.tree.command(name="comment", description="指定したサーバーまたはチャンネルにメッセージを送信")
async def comment(interaction: discord.Interaction, content: str, server: str = None):
    if server:
        guild = discord.utils.get(bot.guilds, name=server)
        if guild:
            channel = guild.text_channels[0]
            await channel.send(content)
            await interaction.response.send_message(f"メッセージはサーバー「{server}」に送信されました。")
        else:
            await interaction.response.send_message(f"サーバー「{server}」が見つかりませんでした。")
    else:
        await interaction.response.send_message(content)

# Flaskアプリをバックグラウンドで実行
def run_flask():
    app.run(debug=True, host='0.0.0.0', port=5000)

# Flaskアプリをバックグラウンドスレッドで実行
threading.Thread(target=run_flask).start()

# Discordボットを実行
bot.run('YOUR_DISCORD_BOT_TOKEN')  # トークンはGitHub Secretsに設定してください
