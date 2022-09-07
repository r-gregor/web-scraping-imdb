import random
import requests
from bs4 import BeautifulSoup

url= 'https://www.imdb.com/chart/top'

def main():
    response = requests.get(url, headers = {"Accept-Language": "en-US, en;q=0.5"})
    # response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    ''' TESTS:
    movietag0 = movietags[0]
    # print(movietag0)

    innermovietag0 = inner_movietags[0]
    # print(innermovietag0)

    rating0 = rating_tags[0]
    print(rating0)
    print(rating0['data-value'])

    actors = innermovietag0['title']  # inside the <a tag as title=
    title = innermovietag0.text       # between <a> </a> tags
    # print(f'Actors: {actors}')
    # print(f'Title: {title}')

    moviesplit = movietag0.text.split()
    # print(moviesplit)

    year = moviesplit[-1]
    # print(year)
    '''

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year

    years = [get_year(tag) for tag in movietags]
    actors = [tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in rating_tags]

    n_movies = len(titles)

    ''' print ALL
    for i in range(n_movies):
        print(f" Title: {titles[i]} {years[i]}")
        print(f" Actors: {actors[i]}")
        print(f" rating: {ratings[i]:.2f}")
        print(f" ---")
    '''

    def print_movie_info(idx):
        print(f" Title: {titles[idx]} {years[idx]}")
        print(f" Actors: {actors[idx]}")
        print(f" rating: {ratings[idx]:.1f}")
        print(f" ---")

    ''' pick random '''
    while(True):
        idx = random.randrange(0,n_movies)
        print_movie_info(idx)

        user_input = input('Do you want another one (y/[n]) ?')
        if user_input != 'y':
            break


if __name__ == '__main__':
    main()

