# By: Kenny_G_Loggins
# Created on: 8/4/20, 1:17 AM
# File: config_template.py
# Project: F1_discord_bot


# Your bot's Token
token = 'put token here' # can be found in your developer's portal where you created your bot

# Channels to post in
id_channel = 'put number here' # with discord in devmode(Settings/appearances) , right click channel to see copy id

# Subreddits to grab posts from. Make sure to put the list in [ str(sub name), int(upvotes needed)] format
sublist = [['gifs', 8000], ['aww', 9000], ['HQG', 10000]]

# Dictionary for twitter commands. { 'command here': 'link, msg, or w/e here'} format
f1twit_dict = {'!Merc': 'https://twitter.com/MercedesAMGF1', '!RBR': 'https://twitter.com/redbullracing',
               'McL': 'https://twitter.com/McLarenF1', '!RP': 'https://twitter.com/RacingPointF1',
               '!AT': 'https://twitter.com/AlphaTauriF1', '!AR': 'https://twitter.com/AlfaRomeoRacing',
               '!Ren': 'https://twitter.com/RenaultF1Team', 'Hass': 'https://twitter.com/HaasF1team',
               '!Red': 'https://twitter.com/scuderiaferrari', '!WR': 'https://twitter.com/WilliamsRacing',
               '!Fdank': None, '!WTF1': 'https://twitter.com/wtf1official', '!Fia': None,
               '!F1': 'https://twitter.com/F1'}

# More things to search and respond to
addition_commands = { 'Lewis': 'Get in there Lewis!', 'box': 'box box, box, box.',
                      'fiesta': 'https://www.youtube.com/watch?v=3r2OkH7zU_c'}