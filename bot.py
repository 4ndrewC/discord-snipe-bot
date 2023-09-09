import discord

TOKEN = 'MTEzODQxNTMwNzA2OTg1Mzc5Nw.G9ObzL.PdoPgZK-gsxWjlaa3lhuUh40GIXA7INYHSDq8E'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

snipes = []
names = []


@client.event
async def on_ready():
  print("Bot online")


#master function
@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{username}: {message.content} ({channel})')
  stripped = user_message.lower().replace(" ", "")

  if '!snipe' in stripped:
    if message.author.id != client.user.id:
      index = -1
      try:
        index = int(stripped[-1]) - 1
      except:
        await message.channel.send('add a number between 1 and 5 after !snipe')
        return
      await message.channel.send(f'{names[index]}: {snipes[index]}')


@client.event
async def on_message_delete(message):
  user_message = str(message.content)
  username = str(message.author).split('#')[0]
  stripped = user_message.lower().replace(" ", "")
  snipes.append(stripped)
  names.append(username)
  if (len(snipes) >= 5):
    snipes.pop(0)
    names.pop(0)


client.run(TOKEN)
