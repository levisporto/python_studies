#remember to pip install pytubefix 
from pytubefix import YouTube

def Download(link):
    youtube_video = YouTube(link)
    youtube_video = youtube_video.streams.get_highest_resolution();
    youtube_video.download()
    print("Success!")

link = input("Enter the link to the video:")
Download(link)

"lmao that did not work, lets try again"

