import collections
import os

import requests
import slacker


channel = os.environ.get('AOTD_CHANNEL_ID')
list_name = os.environ.get('LIST_NAME', 'Albumlist')
random_url = os.environ.get('AOTD_RANDOM_URL')
slack_token = os.environ.get('SLACK_OAUTH_TOKEN')

slack = slacker.Slacker(slack_token)


def build_attachment(album_details, list_name):
    attachment = {
        'fallback': f'{album_details["album"]} by {album_details["artist"]}',
        'color': '#36a64f',
        'pretext': f'{album_details["album"]} by {album_details["artist"]}',
        'author_name': album_details['artist'],
        'image_url': album_details['img'],
        'title': album_details['album'],
        'title_link': album_details['url'],
        'callback_id': 'album_results_random',
        'fields': [
            {
                'title': 'Tags',
                'value': ', '.join(album_details['tags']),
                'short': 'false',
            },
        ],
        'footer': list_name,
    }
    return attachment


def get_random_album():
    response = requests.get(random_url)
    if response.ok:
        return response.json()['album']


def post_random_album():
    if not channel or not slack_token:
        print('[random]: missing environment variables', channel, slack_token)
        return
    album = get_random_album()
    if album is None:
        print('[random]: no random album found')
        return
    attachment = build_attachment(album, list_name)
    print(f'[random]: posting random album to {channel}')
    text = f":new_moon_with_face: Today's album of the day is:"
    slack.chat.post_message(channel, text, attachments=[attachment])


if __name__ == '__main__':
    post_random_album()
