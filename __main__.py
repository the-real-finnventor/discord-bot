import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(f"Online as {client.user}")


client.run(os.getenv('TOKEN'))
