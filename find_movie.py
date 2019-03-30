from get_poster import *

class NoSuchMovie:
    pass

def find_movie(year, score, popularity, genres):
    f = open("movies_dataset.csv", encoding="utf-8")
    movies = []
    with f:
        for line in f:
            movies.append(line.strip().split(","))

    results = []

    if popularity == "very popular":
        min_votes = 150000
        max_votes = 10000000
    elif popularity == "popular":
        min_votes = 50000
        max_votes = 150000
    elif popularity == "not popular":
        min_votes = 0
        max_votes = 50000

    for movie in movies:
        try:
            same_genres = True
            if int(movie[1]) == year and max_votes >= int(movie[3]) >= min_votes and float(movie[4]) >= score:
                for genre in genres:
                    if genre not in movie[2].split("|"):
                        same_genres = False
                if same_genres:
                    results.append(movie)
        except ValueError:
            continue

    if not results:
        raise NoSuchMovie

    best_movie = results[0]
    for result in results:
        if float(result[4]) > float(best_movie[4]):
            best_movie = result
    return best_movie
