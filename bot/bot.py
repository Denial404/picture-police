from server import ping
import os

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='pp ', case_insensitive=True, help_command=None)


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='protecting the people'))
    print('Logged on as {0}!'.format(client.user))


@client.event
async def on_message(message):
    content = message.content

    # log bot output
    if message.author == client.user:
        print(message.content)
        return

    # await message.channel.send("don't send bad stuff ;) ;)")

    # resume bot (DO NOT DELETE)
    await client.process_commands(message)


@client.command(name='test')
async def test(ctx):
    await ctx.send('test')


# run
ping()

client.run(os.getenv('BOT_TOKEN'))
