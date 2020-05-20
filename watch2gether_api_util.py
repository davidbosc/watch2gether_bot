import requests
import json

class Watch2getherApiUtil():

    API_KEY = json.load(open('credentials.json'))['w2g_api_key']

    def new_room(self, video_url):
        room_partial_url = 'https://www.watch2gether.com/rooms/'    
        r = requests.post(
            'https://www.watch2gether.com/rooms/create.json',
            data = {
                'share': video_url,
                'api_key': self.API_KEY
            }
        )
        if(r.status_code != 200):
            raise Exception("Request finished with error code: {0}".format(r.status_code))
        return room_partial_url + json.loads(r.text)['streamkey']