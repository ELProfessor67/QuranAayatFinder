from requests import get
from bs4 import BeautifulSoup
from json import dumps

r = get("https://www.quranmualim.com/a-list-of-114-quran-surahs-quranmualim/")
r = r.content

soup = BeautifulSoup(r,'html.parser')
ol = soup.find('ol')
li = ol.find_all('li')
obj = {}
for i,name in enumerate(li):
	em = name.find('em')
	# print(em.string)
	obj[i] = em.string
obj = dumps(obj,indent=4)

with open("surah.json","a") as f:
	f.write(obj)
