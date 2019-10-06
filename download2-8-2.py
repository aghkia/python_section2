from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("")
url = base + quote

res = req.urlopen(url)
savePath = "C:\\Users\\aghki\\Desktop\\Python\\Crawling\\section2\\imgdown\\"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.columns.is-mobile.courses_card_list_body")[0]

for i, e in enumerate(img_list, 1):
    with open(savePath+"text_"+str(i)+".txt", "wt") as f:
        f.write(e.select_one("div.card-content > div").string)
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    print(fullFileName)
    req.urlretrieve(e.select_one("div.card-image > figure > img")['src'], fullFileName)

print("다운로드 완료")
