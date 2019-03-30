f = open("movies_dataset.csv", encoding="utf-8")
movies = []
with f:
    for line in f:
        movies.append(line.strip().split(","))

genres_list = []
for movie in movies:
    genres = movie[2].split("|")
    for genre in genres:
        genres_list.append(genre)

genres_list = list(set(genres_list))

for genre in genres_list:
    if genre.isdigit():
        print(genre)
        genres_list.remove(genre)

print(genres_list)
