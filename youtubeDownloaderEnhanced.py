from pytube import YouTube
# misc
import os
import shutil
import math
import datetime
import json

from youtube_search import YoutubeSearch

downloadPath = 'Z:\Python Video test'

def searchAndDownload(search,avChoice):

        results = YoutubeSearch(search, max_results=1).to_json()

        python_obj = json.loads(results)

        for url in python_obj["videos"]:
                value = url["id"]

        video = YouTube('https://www.youtube.com/watch?v={0}'.format(value))
        video.streams.get_by_itag(avChoice).download(downloadPath)

        print("Download Complete")


userChoice = 'y'
while userChoice == 'y':
        avChoice = int(input("MP3 (1) or MP4 (2): "))
        if avChoice == 1:
            search = input("Enter search term: ")
            searchAndDownload(search,140)
            userChoice = input("download another? (y/n): ")
        elif avChoice == 2:
            search = input("Enter search term: ")
            searchAndDownload(search,18)
            userChoice = input("download another? (y/n): ")
        else:
            print('nice try.')
