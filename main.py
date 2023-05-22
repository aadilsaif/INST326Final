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
genres = []
decades = []
ratings = []

class Movie:
    def __init__(self, id):
        url = f"https://api.themoviedb.org/3/{id}/550?api_key={config.key}"
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
        genres.append(self.genres)
        ratings.append(self.rating)
        decades.append(self.year[:4])
        self.language = loadData['original_language']
        
def plots():
    fig1, ax1 = plot.subplot()
    ax1.hist(ratings, bins = 'auto')
    ax1.xlabel("Ratings")
    ax1.ylabel("Frequency")
    ax1.title("Frequency of Ratings")

    fig2, ax2 = plot.subplot()
    ax2.hist(genres, bins = 'auto')
    ax2.xlabel("Genres")
    ax2.ylabel("Frequency")
    ax2.title("Frequency of Genres")

    for year in decades:
        year += '0'

    fig3, ax3 = plot.subplot()
    ax3.hist(decades, bins = 'auto')
    ax3.xlabel("Decades")
    ax3.ylabel("Frequency")
    ax3.title("Frequency of Decades")

    canvas1 = FigureCanvasAgg(fig1)
    ratingsHist = canvas1.print_to_buffer()

    canvas2 = FigureCanvasAgg(fig2)
    genresHist = canvas2.print_to_buffer()

    canvas3 = FigureCanvasAgg(fig3)
    yearsHist = canvas3.print_to_buffer()

    return [ratingsHist, genresHist, yearsHist]





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
        string = (f"""\n\n{i+1}. Movie Name: {movies[i].name}     Year: {movies[i].year}       TMDB Rating: {movies[i].rating}\n
              Description: {movies[i].description}\nRuntime: {movies[i].runtime}       Languages: {movies[i].language}\nGenres: {genrestr}""")
        print(textwrap.fill(string, 35))

    print("\n\n\nNow Here is some cool data about the movies you were recommended")
    plotList = plots()
    for plt in plotList:
        plot.figure()
        plot.imshow(plt)
        plot.show()




