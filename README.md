
# F1_discord_bot

<ul>
<li>switching over to webhook posting</li>
<li>added color for teams</li>
<li>switched both db's over to mongo</li>
<li>adding google calender functionality so things can be done around racing weekends</li>
<li>adding screenshot functionality with splash, not sure how I will implement this yet</li>
<li>and more...</li>
</ul>

<h2>F1dank_twitter_discord_bot.py</h2>
<br>
<p>
  This is the script you want to get your bot to run. None of these files are standalone but<br>
  it wouldn't take much to make them run independently. All variables to tweak how the bot <br>
  runs can be found in the config.py of which a template is provided in the template folder.<br>
  <b>DON'T</b> forget to change the name of the template files to config.py and praw.ini,<br>
  both of which should be placed in your project folder.
<p>
<br><br>

<h2>reddit_bot.py</h2>
<br>
<p>
  A bot that searches subreddits that you specify in config.py. If the posts meet the provided up-<br>
  vote requirement, it will then send it to F1dank_twitter_discord_bot.py to be posted. This file depends<br>
  on praw.ini which needs the bot1 information filled out. If you don't already have one, create a bot<br>
  on reddit and insert the credntials there. Username and password are the ones for the account you<br>
  used to make the bot with.
<p>
<br><br>

<h2>twitter_scrapy.py</h2>
<p>
  description coming soon...
</p>

