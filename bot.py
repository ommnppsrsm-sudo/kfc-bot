import discord
from discord.ext import commands

# Включаем все доступы (Intents), которые вы настроили на портале
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_line_prefix="!", intents=intents)

# Событие: когда бот успешно включается
@bot.event
async def on_ready():
    print(f"Бот {bot.user} успешно запустился и готов к работе!")

# Простая тестовая команда. Если написать на сервере !привет, бот ответит
@bot.command()
async def привет(ctx):
    await ctx.send(f"Привет, {ctx.author.mention}! Я бот KFC Kombat!")

# Сюда вставьте ваш секретный токен, который вы скопировали ранее
bot.run("MTUzMzE1Nzc4ODg4MzM1MzcyMg.Gv94uO.8blobFJA7pNrjtIzkNFjvIxQIvEU-FoD2xYxa0")
