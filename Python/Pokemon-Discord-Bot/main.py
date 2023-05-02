import discord
from discord.ext import commands
from discord import embeds
import requests

import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
  print("im alive and ready to go!")


@client.command()
async def hello(message):
  await message.channel.send("hello!")


@client.command()
async def info(ctx, message):
  pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{message}"
  data = requests.get(pokemon_url).json()
  name = data['species']['name']
  poketype = data['types'][0]['type']['name']
  image = data['sprites']['front_default']
  await ctx.send(image)
  await ctx.send('Name: ' + name)
  await ctx.send('Type: ' + poketype)

  #description
  description = requests.get(
    f"https://pokeapi.co/api/v2/pokemon-species/{message}").json()
  entry = description['flavor_text_entries'][0]['flavor_text']

  #returns our info in an embed
  result = discord.Embed(title=name, description=entry)
  result.add_field(name="Type: ", value=poketype, inline=False)
  result.set_image(url=image)
  await ctx.send(embed=result)


client.run(
  "Key-goes-here")
