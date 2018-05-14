# practicing pytube. for documentation, see https://github.com/nficano/pytube

from pytube import YouTube, Playlist

# some example video link
videoLink = 'https://www.youtube.com/watch?v=-EKxzId_Sj4'

# creating youtube instances
youtube = YouTube(videoLink)

# to download the highest progressive download stream available
# youtube.streams.first().download()

# to download the lowest progressive download stream available
# youtube.streams.last().download()

# to download playlist
playlist = Playlist('https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU')
# playlist.download_all()
# playlist.download_all('../downloaded)
# playlist.download_all(filename_prefix = 'ehe')

# get video title
videoTitle = youtube.title
print(videoTitle)

# get thumbnail url
videoThumbnailUrl = youtube.thumbnail_url
print(videoThumbnailUrl)

# check stream channels
# allStreams = youtube.streams.all()
# progressiveStreams = youtube.streams.filter(progressive = True).all()
# print('all stream')
# for element in allStreams:
#     print(element)
# print('progressive stream')
# for element in progressiveStreams:
#     print(element)

# download a video and save it to a certain folder
allStream = youtube.streams.all()
pickedVideoStream = allStream.first()
pickedVideoStream.download('/tmp')