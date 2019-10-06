import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://cafefiles.naver.net/20151126_112/gunwoo0423_1448535959729YfC2I_JPEG/740_47d4878a3e974.jpeg"
htmlURL = "http://google.com"

savePath1 = "C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section2\\img\\test1.jpg"
savePath2 = "C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section2\\img\\index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1, 'wb') # w: write, r: read, a: add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료")
