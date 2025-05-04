import discord
from discord.ext import commands, tasks
import asyncio
import random
import youtube_dl
import os
import requests
from dotenv import load_dotenv



intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 1. Özellik - Mesafe hesaplama
@bot.command()
async def evemesafe(ctx):
    await ctx.send("Rotterdam ile Mersin arası yaklaşık 3,000 km'dir.")

# 2. Özellik - Her dakika "mert" yazdırma
@tasks.loop(minutes=1)
async def yaz_mert():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send("mert")
                break
            except:
                continue

# 3. Özellik - Favori takım
@bot.command()
async def favoritakım(ctx):
    await ctx.send("Galatasaray")
# 4. Özellik - Rastgele hayvan fotoğrafı
@bot.command()
async def foto(ctx):
    urls = [
        "https://random.dog/woof.json",
        "https://api.thecatapi.com/v1/images/search",
        "https://randomfox.ca/floof/"
    ]
    url = random.choice(urls)

    try:
        if "dog" in url:
            res = requests.get(url).json()
            await ctx.send(res["url"])
        elif "cat" in url:
            res = requests.get(url).json()
            await ctx.send(res[0]["url"])
        elif "fox" in url:
            res = requests.get(url).json()
            await ctx.send(res["image"])
    except:
        await ctx.send("Resim alınamadı :(")
