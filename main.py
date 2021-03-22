from discord.ext import commands
import discord

intents = discord.Intents.default()
bot = commands.Bot(command_prefix = ".", intents = intents)
cogs = ["events.on_message"]

@bot.event
async def on_ready():
	print("The bot is ready!")
	for cog in cogs:
		try:
			bot.load_extension(cog)
			print(f"{cog} was loaded.")
		except Exception as e:
			print(e)

bot.run("ODIzNDM3ODYzMjM5NjgwMDIx.YFg0RQ.a0b4Qin78QOWSYWikdfX1_KAops")
