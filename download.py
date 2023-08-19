from pytube import YouTube


def download(url):
    if "https://" in url:
        yt = YouTube(url)
        print("Downloading :", yt.title)
        d_video = yt.streams.get_highest_resolution()
        try:  
            d_video.download() 
        except: 
            print("Error!") 
    else:
        print("This is not a valid url")
    