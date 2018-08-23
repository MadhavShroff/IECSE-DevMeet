import requests
from bs4 import BeautifulSoup

start_at = 1
numberOfComics = 10

url = 'https://xkcd.com/{}'
imgurl = []
for i in range(start_at, start_at + numberOfComics) :
	r = requests.get(url.format(i))
	html = r.content
	soup = BeautifulSoup(html, 'html.parser')
	imgurl.append('https:' + str(soup.find_all('img')[1]['src']))

counter = 1
for url in imgurl:
	print('Getting {}'.format(url))
	response = requests.get(url, stream=True)
	if response.status_code == 200:
		image = response.content
		open('comics/Img{}.png'.format(counter),'wb+').write(image)
		counter += 1