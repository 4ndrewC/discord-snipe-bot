import discord
from discord import Interaction
from discord.ext import commands
from discord.utils import get
import random


TOKEN = "MTAxNTk4MTM4NzM4OTU5OTc3NA.GXrNSp.Eiym1T9VdVTcRmXPeNx5a2owtiPFEcX0Ah6ndE"

intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print("Bot {0.user} online".format(bot))
    print("")

beemoviescript = open('beemovie.txt', 'r')
beemovie = beemoviescript.readline()

thebeastcopypasta = open('thebeast.txt', 'r')
beast = thebeastcopypasta.readline()

NNID = '885473624927109170'

RefugeeCampID = '960348217067843584'

##NN commands
@bot.slash_command(guild_ids=[NNID]) 
async def whogay(interaction: Interaction):
    await interaction.response.send_message("scp")

@bot.slash_command(guild_ids=[NNID, RefugeeCampID]) 
async def bee(interaction: Interaction):
    await interaction.response.send_message(beemovie)

@bot.slash_command(guild_ids=[NNID, RefugeeCampID]) 
async def thebeast(interaction: Interaction):
    await interaction.response.send_message(beast)

@bot.slash_command(guild_ids=[NNID])
async def rape(ctx):
    await ctx.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\sus\scp\rape eren.png"))

@bot.slash_command(guild_ids=[NNID])
async def hashira(ctx):
    await ctx.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\sus\misc\tryout.jpg"))

#Refugee camp commands
@bot.slash_command(guild_ids=[RefugeeCampID])
async def jamesfuck(interaction: Interaction):
    await interaction.response.send_message('fuck you james')

@bot.slash_command(guild_ids=[RefugeeCampID])
async def jamesbeta(ctx):
    await ctx.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\sus\james\rape me.png"))

@bot.slash_command(guild_ids=[RefugeeCampID])
async def emlook(ctx):
    await ctx.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\sus\emy\emlookistillloveyou.png"))

@bot.slash_command(guild_ids=[RefugeeCampID])
async def impregnate(ctx):
    await ctx.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\sus\misc\iwillimpregnateyou.jpg"))

@bot.slash_command(guild_ids=[RefugeeCampID])
async def waifu(ctx):
    await ctx.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\sus\waifu\waifuracist.png"))

#vc

@bot.slash_command(guild_ids=[NNID])
async def join(ctx):
    # if ctx.author.voice:
    #     channel = ctx.message.author.voice.channel
    #     await channel.connect()
    # else:
    #     await ctx.send("Connect to a voice channel first")
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.slash_command(guild_ids=[NNID])
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("{0.user} has left the voice channel")
    else:
        await ctx.send("I am not in a voice channel")


#pinging
@bot.slash_command(guilds_id=[RefugeeCampID])
async def unleash(ctx):
    jit = get(ctx.guild.members, id=534091306348052480)
    for i in range(10):
        await ctx.send(f"{jit.mention}")

@bot.slash_command(guilds_id=[RefugeeCampID])
async def summon_bitches(ctx):
    female = get(ctx.guild.roles, name='female')
    for i in range(10):
        await ctx.send(f"{female.mention}")


#send messages


#master function
@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {message.content} ({channel})')

    if user_message.lower() =='!fuck':
        await message.channel.send('fuck you')
    
    elif user_message.lower() == 'caca':
        caca = get(message.channel.members, id=256040925715890187)
        await message.channel.send(f"{caca.mention}")

    elif message.channel.id == 960348217713774615 and user_message.lower() == '!rape':
        await message.channel.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\sus\james\rape me.png"))
    
    elif message.channel.id == 885473624927109172 and 'scp' in user_message.lower():
        await message.channel.send('is gay')
    
    elif message.channel.id == 995931017389027341 and user_message.lower() == '!xunn':
        await message.channel.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\sus\xunn\mommy.png"))

    elif message.channel.id == 995931017389027341 and user_message.lower() == '!beta':
        await message.channel.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\sus\xunn\knees.png"))

    elif '@everyone' in user_message.lower() and 'vc' in user_message.lower():
        await message.channel.send('average vc ping')

    elif message.channel.id == 960348217713774615 and '@everyone' in user_message.lower():
        await message.channel.send('fuck off')

    elif message.channel.id == 995931017389027341 and '@everyone' in user_message.lower() and message.author.id == 906729715107258398:
        await message.channel.send('stfu')
    
    elif message.channel.id == 995931017389027341 and user_message.lower() == '!unleash':
        for i in range(10):
            await message.channel.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\shu\squirt.png"))
    
    elif message.channel.id == 995931017389027341 and user_message.lower() == '!thankslukie':
        await message.channel.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\shu\thankslukie.png"))

    elif message.channel.id == 995931017389027341 and user_message.lower() == '!cf':
        c = random.random()
        if c>0.5: 
            await message.channel.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\shu\squirt.png"))
        else:
            await message.channel.send(file=discord.File(r"C:\Users\andre\randomstuff\raot\sus\xunn\knees.png"))
#logging
# @bot.event
# async def on_message(message):
#     username = str(message.author).split('#')[0]
#     user_message = str(message.content)
#     channel = str(message.channel.name)
#     print(f'{username}:{message.content} ({channel})')


bot.run(TOKEN)