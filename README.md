# Another Wallpaper Generator

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Another Simple wallpaper generator for MacOS where you can pull images from your favorite subreddits.
## Getting Started <a name = "getting_started"></a>

Clone the repository by typing
```
git clone "https://github.com/ZachJBurns/AnotherWallpaperGenerator"
```
### Prerequisites
Mac OS Catalina or higher

Head over to https://www.reddit.com/prefs/apps and create an app to receive your API information to pull posts from Reddit.

### Installing

After cloning you can install the required modules with:


```
pip install -r requirements.txt
```

You can import your API ID and Secret key with one of two ways.

Replace the CLIENT_ID and CLIENT_SECRET variables with their respective values.

OR

In terminal:

```
touch .env
vi .env

CLIENT_ID = "your client id"
CLIENT_SECRET = "your client secret key"
SAVE_DIR = "directory to where you would like to save wallpaper"
```

## Usage <a name = "usage"></a>

You can generate a random wallpaper by typing:
```
python Wallpaper.py
```

You can also run it in interactive mode by typing:
```
python Wallpaper.py -i
```
When running in interactive mode, you can keep generating wallpapers until you find the right one. Unlike running in random generation, interactive mode will save the wallpaper you pick to a defined directory.

You can add or remove information to the subreddits and fileExtensions variables to restrict or increase the scope for file types and subreddits to pull from.