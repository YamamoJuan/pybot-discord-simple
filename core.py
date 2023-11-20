import discord
import pytz
from discord.ext import commands
from datetime import *
from apis import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)
timezone = pytz.timezone('Asia/Jakarta')
current_time = datetime.now(timezone)

welcome_send_user_dm = False
welcome_message = "Selamat datang di PPWL, {message.mention}! \n Semoga betah ya bro! 😘😘😘"
welcome_channel_id = 1174160265097531482

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    
    if "siapa aku?" in msg.content.lower():
        await msg.channel.send("???")

    if "whoami" == msg.content.lower():
        await msg.channel.send("???")
   
    await bot.process_commands(msg)

@bot.event
async def on_member_join(member):

    greeting = welcome_message.format(member=member)

    welcome_channel = bot.get_channel(welcome_channel_id)

    await welcome_channel.send(greeting)

@bot.command()
async def  set_welcome_message(ctx, *, message: str):
    global welcome_message
    welcome_message = message

    await ctx.send(f"Custom pesan welcome sudah terubah\n, {message}")

@bot.command()
async def  set_welcome_channel(ctx, *, channel_id: int):
    global welcome_channel_id
    welcome_channel_id = channel_id

    await ctx.send(f"Welcome channel sudah diubah: {channel_id}")

@bot.command()
async def bjir(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

@bot.command()
async def react(ctx):
    await ctx.send("Im feeling excited")
    await ctx.message.add_reaction("😘")

@bot.command()
async def embed_biasa(ctx):
    embed = discord.Embed(title= "Ini embed", description="Ini embed basic", color=discord.Color.orange())
    await ctx.send(embed=embed)
    
@bot.command()
async def embed_keren(ctx):
    embed = discord.Embed(title= "Ini embed", description="Ini embed advanced", color=discord.Color.orange())
    embed.set_author(name="juan", icon_url="https://i.cbc.ca/1.4382287.1509558031!/fileImage/httpImage/ac-origins-pyramids.jpg")
    embed.add_field(name="field 1", value="Ini field pertama", inline=False)
    embed.add_field(name="field 2", value="Ini field pertama", inline=False)
    embed.add_field(name="field 3", value="Ini field pertama", inline=False)
    embed.add_field(name="field 4", value="Ini field pertama", inline=False)
    embed.set_thumbnail(url="https://i.cbc.ca/1.4382287.1509558031!/fileImage/httpImage/ac-origins-pyramids.jpg")
    
    embed.add_field(name="field 5", value="Ini field pertama")
    embed.add_field(name="field 6", value="Ini field pertama")
    embed.add_field(name="field 7", value="Ini field pertama")
    embed.add_field(name="field 8", value="Ini field pertama")

    embed.set_footer(text="Ini embed advanced footer")
    embed.timestamp = datetime.utcnow()
    await ctx.send(embed=embed)

@bot.command()
async def waktu_sekarang(ctx):
    embed = discord.Embed(title="Waktu sekarang")
    embed.set_footer(text="juankeren")
    embed.timestamp = datetime.now(timezone)
    await ctx.send(embed=embed)

@bot.command()
async def waktusekarang(ctx):
    current_time = datetime.now(timezone)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f"Waktu sekarang: {formatted_time}")


bot.run(TOKEN)