import pytube

#다운 받을 동영상 URL 지정
yt = pytube.YouTube("https://www.youtube.com/watch?v=Bwm3dG9lreU")
videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)):
    print(i, ', ', videos[i])


down_dir = "C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section2\\pytube"

videos[1].download(down_dir)
