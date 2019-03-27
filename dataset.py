f = open("movies.csv", encoding="utf-8")
movies_list = []
with f:
    f.readline()
    for line in f:
        line = line.strip().split(",")
        if line[1].startswith("\""):
            line[1] = ",".join(line[1:-1])[1:-1]
            for i in range(2, len(line)-1):
                line[i] = 0
            while 0 in line:
                line.remove(0)
        line = [line[1][:-7], line[1][-5:-1], line[2]]
        if line[0].endswith("The"):
            line[0] = line[0][:-5]
            print(line)
        movies_list.append(line)
print(movies_list)

ratings = open("ratings.list", encoding="utf-8")
ratings_list = []
with ratings:
    for line in ratings:
        try:
            line = line.strip().split()
            if line[-1].endswith("}"):
                continue
            line = [line[1], line[2], " ".join(line[3:-1]), line[-1][1:-1]]
            if line[2].startswith("\""):
                line[2] = line[2][1:-1]
            if int(line[0]) > 1000:
                ratings_list.append(line)
        except:
            continue
print(ratings_list)
print(ratings_list[1000], movies_list[1000])

dataset = []
for movie in movies_list:
    for rating in ratings_list:
        if movie[0] == rating[2] and movie[1] == rating[3]:
            dataset.append(movie + [rating[0], rating[1]])
            break
print(dataset)
dataset_str = ""
for movie in dataset:
    dataset_str += ",".join(movie) + "\n"
with open("movies_dataset.csv", "w+", encoding='utf-8') as file:
    file.write(dataset_str)
