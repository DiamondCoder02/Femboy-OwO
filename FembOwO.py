import discord
import json

#json config load
with open('config.json', 'r') as json_config:
    config = json.load(json_config)
json_config.close
# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTk3MTkxMDg1MTQxMDEyNTYx.GBHqkU.glenMF01WdtFPOqg1Umsxa5ovqRZGQtdxTB6vI')
