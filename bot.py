import os
from threading import Thread
from flask import Flask
import discord
from discord.ext import commands

app = Flask("")


@app.route("/")
def home():
    return "I am alive!"


def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)


def keep_alive():
    t = Thread(target=run)
    t.start()


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user.name}")


@bot.event
async def on_member_join(member):
    guild = member.guild
    target_channel = None  # ここも綺麗に直しといたよ！
    if target_channel is None:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                target_channel = channel
                break

    if target_channel:
        await target_channel.send("ようこそ！")


keep_alive()
bot.run(token)
