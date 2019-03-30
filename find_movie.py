from get_poster import *

class NoSuchMovie(Exception):
    pass


def find_movie(year, score, genres, votes=0):
    f = open("movies_dataset.csv", encoding="utf-8")
    movies = []
    with f:
        for line in f:
            movies.append(line.strip().split(","))

    results = []

    for movie in movies:
        try:
            same_genres = True
            score_check = float(movie[4]) >= score if score > 0 else float(movie[4]) <= score
            if int(movie[1]) == year and int(movie[3]) >= votes and score_check:
                for genre in genres:
                    if genre not in movie[2].split("|"):
                        same_genres = False
                if same_genres:
                    results.append(movie)
        except ValueError:
            continue
    # print(results)
    if len(results) == 0:
        raise NoSuchMovie
    best_movie = results[0]
    for result in results:
        if float(result[4]) > float(best_movie[4]):
            best_movie = result
    return best_movie

print(find_movie(2017, 5, ['Drama']))
