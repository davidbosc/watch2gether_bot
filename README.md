# watch2gether_bot
A discord bot for facilitating creating rooms and sharing invite links for Watch2gether.


## Setup:
To run on your server, you'll need a watch2gether API key, as well as a discord bot token.  Once you have both, create a file in the same directory as the repo called `credentials.json`, with 2 properties: `w2g_api_key` and `bot_token`. Then, simply run the `watch2gether_bot.py` script.

## Commands:

`!wtg [video_url]`

-video_url: URL to an online video, ex)

Creates a watch2gether room with the provided video URL. Note: Watch2gether will make a room regardless if a typo is made or if the video host is unsupported.

---

*More commands will be added as Watch2gether adds more API endpoints*
