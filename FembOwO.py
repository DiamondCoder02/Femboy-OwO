import discord
import json
import os
import requests
from discord.ext import commands

os.system('cls')

from dotenv import load_dotenv
load_dotenv()
secret_token = os.getenv("TOKEN")

#json config load
with open('config.json', 'r') as json_config:
    config = json.load(json_config)
json_config.close

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix='+')

@client.command()
async def facts(ctx, number):
    print(number)
    response = requests.get(f'http://numbersapi.com/{number}')
    await ctx.channel.send(response.text)

# Homework for school:
@client.command()
async def calculate_numbers_file(ctx):
    for attachment in ctx.message.attachments:
        await attachment.save(attachment.filename)
    
    print("\n1.feladat")
    with open(attachment.filename) as ff:
        codes=[code.strip() for code in ff]
        print(codes)












@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
    if message.content[0] == '.':
        return
    await message.channel.send('Hello!')

if(config["token"] == "token"): client.run(secret_token)
else: client.run(config["token"])