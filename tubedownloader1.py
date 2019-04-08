import pytube
url=input("enter the url which u want to download:")
yt=pytube.YouTube(url)
#Streams are high-level async/await-ready primitives to work with network connections.
#Streams allow sending and receiving data without using callbacks or low-level protocols and transports.
stream=yt.streams.first()
stream.download()
print("download competed")
#the downloaded video will be placed in the source code loaction
