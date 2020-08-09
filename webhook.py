from discord import Webhook, RequestsWebhookAdapter, Embed, Color
from config import webhook_id_reddit, webhook_token_reddit, team_colors
import re
import discord


def reddit_webhook(title, post, name):
    img = ['.jpeg', '.png', '.gif', '.bmp']
    try:
        color = team_colors[name]
    except KeyError:
        color = 0
    for x in img:
        if re.search(x, post):
            data = Embed(title=title, color=Color(
                color), url=post).set_image(url=post)
            return data

    data = Embed(title=title, color=Color(color), url=post)
    return data
