import discord
import json
import requests
#import random
#import re
import os

client = discord.Client()
#msg = message.

def get_quote():
  response = requests.get("https://zenquotes.io/api/today")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
#for now uses the first quote
def get_quote2():
  response2 = requests.get("https://type.fit/api/quotes")
  json_data = json.loads(response2.text)
  quote2 = json_data[0]['text'] + " -" + json_data[0]['author']
  return(quote2)

@client.event
async def on_ready():
  print('The bot is online as {0.user}'
  .format(client))

#Registers the event when a message occurs
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!who'):
   await message.channel.send('I am not a real bot')

  if message.content.startswith('!quote'):
   quote = get_quote()
   await message.channel.send(quote)

  if message.content.startswith('!randomquote'):
   quote2 = get_quote2()
   await message.channel.send(quote2)

#  if in message.content('text'):
#   await message.channel.send('BAD')

client.run(os.getenv('KEY'))

26.53 

https://www.youtube.com/watch?v=SPTfmiYiuok&feature=emb_title