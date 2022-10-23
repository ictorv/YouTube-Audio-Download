from pytube import YouTube
# from sys import argv
#will receive link from terminal
getlink="https://www.youtube.com/watch?v=CGLmYdFRErg"
yut=YouTube(getlink)

print("Title :", yut.title)
print("Views :", yut.views)
dwn=yut.streams.filter(only_audio=True)
videos=list(enumerate(dwn,1))
for i in videos:
    print(i)
stream=int(input("Choose:"))
dwn[stream-1].download()
print("Downloaded")
