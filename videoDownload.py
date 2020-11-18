from pytube import YouTube
# misc
import os
import shutil
import math
import datetime
import json

from youtube_search import YoutubeSearch

userChoice = 'y'
def searchAndDownload(search):

        results = YoutubeSearch(search, max_results=10).to_json()

        #print(results)

        python_obj = json.loads(results)

        for url in python_obj["videos"]:
                value = url["id"]
                break

        video = YouTube('https://www.youtube.com/watch?v={0}'.format(value))
        video.streams.get_by_itag(140).download('Z:\Python Video test')

        print("Download Complete")

while userChoice == 'y':
        search = input("Enter search term: ")
        searchAndDownload(search)
        userChoice = input("download another?")
