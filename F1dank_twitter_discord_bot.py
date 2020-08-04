# By: Kenny_G_Loggins
# Created on: 8/2/20, 6:48 PM
# File: F1dank_twitter_discord_bot.py
# Project: pythonProject

# imports subreddit query function
from reddit_bot import forumal_dank
import discord
import asyncio
# Check config.py and change these values
from config import token, id_channel, f1twit_dict, addition_commands, sublist, post_frequency


client = discord.Client()

# Print's the bot's information to console when on and ready.
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Loop for posting reddit feed using formual_dank('subreddit name', #of upvotes needed)
async def my_background_task():
    await client.wait_until_ready()
    channel = await client.fetch_channel(int(id_channel))
    while not client.is_closed():
        for item in sublist:
            sub, title = forumal_dank(item[0], item[1])
            [await channel.send(post_title + '\n' + post) for post, post_title in zip(sub, title)]
        await asyncio.sleep(post_frequency) # task runs every x seconds

# listens for commands in chat so it can respond with tweets
@client.event
async def on_message(message):
    # Ignore bots own input
    if message.author == client.user: return
    if message.author.bot: return
    # !help command
    if message.content.find('!help') != -1:
        await message.channel.send('```List of available commands:\n-!Merc,!RBR, !McL !RP, !AT, !AR, !Ren, !Hass,'
                                       '!Red, !WR\n-!WTF1, !Fdank, !Fia, !F1```')
    # F1 twitter commands
    [await message.channel.send(f1twit_dict[command]) for command in f1twit_dict if message.content.find(command) != -1]
    # Addition commands
    [await message.channel.send(addition_commands[command]) for command in addition_commands if
     message.content.find(command) != -1]


client.loop.create_task(my_background_task())
client.run(str(token))