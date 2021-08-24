import discord
import os
import requests
import json


#Retrieve secret bot token
bkey = os.environ['bkey']

#Initialise bot client
client = discord.Client()

def kanye_quote():
  '''
  Description: Uses REST API to fetch Kanye Quotes
  '''
  response = requests.get("https://api.kanye.rest").json()
  #json_data = json.loads(response)
  #quote = json
  return(response)

#Successful login confirmation (in console)
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#Bot messges
@client.event
async def on_message(message):
  if message.author == client.user:
      return
  if message.content.startswith('$kanye'):
      quote = kanye_quote()['quote']
      await message.channel.send(f"*\"{quote}\" - Kanye*")

#Run bot (go online)
client.run(bkey)