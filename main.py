from argparse import ArgumentParser
import sys
import textwrap
import WebInteract
import requests
import json
import matplotlib.pyplot as plot
from matplotlib.backends.backend_agg import FigureCanvasAgg
import config


movies = []
genresL = []
decades = []
ratings = []

class Movie:
    def __init__(self, id):
        url = f"https://api.themoviedb.org/3/movie/{id}?api_key={config.key}"
        response = requests.get(url)
        data = response.json()
        loadData = json.loads(data)
        self.title = loadData['title']
        self.description = loadData['overview']
        self.year = (loadData['release_date'])[:5]
        self.runtime = loadData['runtime']
        self.rating = loadData['vote_average']
        self.genres = []
        for genres in loadData['genres']:
            self.genres.append(genres['name'])
            genresL.append(genres['name'])
        ratings.append(self.rating)
        decades.append(self.year[:4])
        self.language = loadData['original_language']
        
def plots():
   plot.subplot(3, 1, 1)
   plot.hist(ratings, bins = 'auto')
   plot.xlabel("Ratings")
   plot.ylabel("Frequency")
   plot.title("Frequency of Ratings")

   plot.subplot(3, 1, 2)
   plot.hist(genresL, bins='auto')
   plot.xlabel("Genres")
   plot.ylabel("Frequency")
   plot.title("Frequency of Genres")

   decadeInt = [int(x) * 10 for x in decades]

   plot.subplot(3, 1, 3)
   plot.hist(decadeInt, bins = 'auto')
   plot.xlabel("Decades")
   plot.ylabel("Frequency")
   plot.title("Frequency of Decades")

   plot.tight_layout()
   plot.show()


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser(arglist)
    parser.add_argument("username", help="your letterboxd username")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    username = args.username
    movieIdList = WebInteract.webinteraction(username)
    for id in movieIdList:
        movie = Movie(id)
        movies.append(movie)
    
    print("Welcome to the Movie Recommender, here are the 20 best movies for you to watch based on your current watch history")

    for i in range(min(20, len(movies))):
        genrestr = ', '.join(str(genre) for genre in movies[i].genres)
        string = (f"""\n\n{i+1}. Movie Name: {movies[i].title}     Year: {movies[i].year}       TMDB Rating: {movies[i].rating}
                \nDescription: {movies[i].description}\nRuntime: {movies[i].runtime}       Languages: {movies[i].language}\nGenres: {genrestr}""")
        print(string)

    print("\n\n\nNow Here is some cool data about the movies you were recommended")
    plots()




