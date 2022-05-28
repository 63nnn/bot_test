from http import client
import discord as dc
from disnake.ext import commands

client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    print(">> I'm ready <<")

client.run('OTc4NjY5ODIyNjcxOTk4OTc2.Gqo0nc.PFP08I5-ZW1S-spxV16T-F2c7s0eccM1t8IAOo')
