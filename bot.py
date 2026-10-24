import discord
from discord.ext import commands
import config
import random

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('Press Ctrl+C to exit')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def hi(ctx):
    await ctx.send('yo what is up')

@client.command()
async def info(ctx):
    await ctx.send('i am discowd\n uhh and als-\n did you see that:eyes:')

@client.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right) # adds two number together and sends the result

@client.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices)) # chooses a random choice from the provided options and sends it

@client.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # says when a member joined the server

client.run(config.token)