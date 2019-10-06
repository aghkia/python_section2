import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1256/1256211/ac4496dc0de216395fbf_20190906151141531.png"
mp3Url = "https://tvetamovie.pstatic.net/libs/1256/1256375/1f49f754038145bab294_20190909164826517.mp4-pBASE-v0-f91144-20190909165235076.mp4"

savePath1 = "C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section2\\img\\test1.jpg"
savePath2 = "C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section2\\img\\test2.mp4"

f1 = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(mp3Url).read()

with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(f1)

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료")
