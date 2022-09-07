import requests
from bs4 import BeautifulSoup

URL= 'https://www.imdb.com/chart/top'
response = requests.get(URL, headers = {"Accept-Language": "en-US, en;q=0.5"})
# response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
movietags = soup.select('td.titleColumn')

def main():
	numOfTitles = int(input("Enter the number of titles to be displayed: "))
	print_movie_info(numOfTitles)

def print_movie_info(num):
	for i in range(num):
		movietag = movietags[i]
		moviesplit = movietag.text.split('\n')
		movieTitle = moviesplit[2].lstrip()
		movieYear = moviesplit[3].replace('(','').replace(')','')
		print(f"Movie: {movieTitle}\nyear: {movieYear}\n---")
	print("\n")

if __name__ == '__main__':
	main()

