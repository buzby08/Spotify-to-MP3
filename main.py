'''
Name: spotify-to-mp3
Author: busby08 (git and replit)
Date: 25-02-2024
Description: For all songs in a spotify playlist, dowload them to mp3,
    if they have not been downloaded before.
'''

import json
import os
import spotipy
import subprocess

# Import the modules that require pip
try:
    from youtube_search import YoutubeSearch
    from pytube import YouTube
except ImportError:
    subprocess.run(['pip', 'install', 'youtube-search'])
    subprocess.run(['pip', 'install', 'pytube'])
    subprocess.run('clear')
    from youtube_search import YoutubeSearch
    from pytube import YouTube

def main() -> None:
    ''' The main function of the program. '''
    
    import spotipy.util as util
    from spotipy.oauth2 import SpotifyClientCredentials
    from spotipy.oauth2 import SpotifyOAuth
    
    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']
    scope = 'playlist-read-private'

    token = util.prompt_for_user_token('yl5ucbxali83f64suipwp4lsp?si=ade7a354969b4bf1', scope, client_id=client_id, client_secret=client_secret, redirect_uri='https://example.com')
    
    sp = spotipy.Spotify(auth=token)

if __name__ == '__main__':
    main()