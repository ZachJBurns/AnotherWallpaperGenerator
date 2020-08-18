import praw
import requests
import re
import os
import time
import random
import sys
from PIL import Image
from io import BytesIO
from appscript import app, mactypes

MIN_WIDTH = 2560
MIN_HEIGHT = 1600
CLIENT_ID = ""
CLIENT_SECRET = ""

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     user_agent="Reddit Background Generator")

subreddits = ["Wallpapers", "EarthPorn", "SpacePorn"]
fileExtensions = ["jpg", "png"]
timeFilters = ["hour", "day", "week", "month", "year", "all"]
randomWallpaper = random.choice(subreddits)
downloadList = []


def downloadRandomWallpaper(interactive):
    post = list(reddit.subreddit("Wallpapers").top(time_filter=random.choice(timeFilters)))
    print(len(post))
    randomNumber = random.sample(range(0, len(post)), len(post))
    for rand in randomNumber:
        print(rand)
        url = (post[rand].url)
        file_name = url.split("/")
        if file_name[-1].split(".")[-1] in fileExtensions:
            r = requests.get(url)
            try:
                image = Image.open(BytesIO(r.content))
            except:
                print("Error Opening File")
            width, height = image.size
            if (width >= MIN_WIDTH and height >= MIN_HEIGHT):
                with open(file_name[-1], "wb") as f:
                    f.write(r.content)
                setWallpaper(file_name[-1])
                downloadList.append(file_name[-1])
                if (interactive):
                    choice = input(
                        "Any key to go to next wallpaper, S to save and exit: ")
                    if choice.lower() == "s":
                        deleteWallpapers(downloadList)
                        return
                else:
                    deleteWallpapers(downloadList)
                    return
    deleteWallpapers(downloadList)


def setWallpaper(file_name):
    app('Finder').desktop_picture.set(mactypes.File(file_name))
    time.sleep(1)
    return


def deleteWallpapers(wallpapers):
    for wallpaper in wallpapers:
        try:
            os.remove(wallpaper)
        except:
            print("Could not delete file")


if __name__ == "__main__":
    interactive = sys.argv[-1].lower()
    downloadRandomWallpaper(interactive == "-i")
