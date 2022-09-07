import requests
from bs4 import BeautifulSoup

URL= 'https://www.imdb.com/chart/top'
NUMLINES = 5

def main():
    # response = requests.get(URL)
    response = requests.get(URL, headers = {"Accept-Language": "en-US, en;q=0.5"})
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')

    # test
    # """
    print(f'movietags[0]: {movietags[0]}')
    movietag0 = movietags[0].text.split('\n')
    print(f"list of contents: {movietag0}")

    # """
    # end of test

    def print_movie_info(num):
        for i in range(num):
            movietag = movietags[i]
            moviesplit = movietag.text.split('\n')

            movieTitle = moviesplit[2].lstrip()
            movieYear = moviesplit[3].replace('(','').replace(')','')

            print(f"Movie: {movieTitle}\nyear: {movieYear}\n---")
        print("\n")

    # print_movie_info(NUMLINES)


if __name__ == '__main__':
    main()

