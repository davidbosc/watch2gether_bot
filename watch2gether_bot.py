import discord
import json
import watch2gether_api_util

WAKE_COMMNAND = "!wtg"
ERROR_MESSAGE = "No video url provided!"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logs for {0}'.format(self.user))

    async def on_message(self, message):
        if(message.content.lower().startswith(WAKE_COMMNAND)):
            print('{0.author}: {0.content}'.format(message))
            if(len(message.content.strip().split()) <= 1):
                await message.channel.send(ERROR_MESSAGE)
                print('{0}: {1}'.format(self.user, ERROR_MESSAGE))
            else:
                video_url = message.content.strip().split()[1]
                room_url = watch2gether_api_util.Watch2getherApiUtil().new_room(video_url)
                await message.channel.send(room_url)
                print('{0}: {1}'.format(self.user, room_url))

client = MyClient()
bot_token = json.load(open('credentials.json'))['bot_token']
client.run(bot_token)