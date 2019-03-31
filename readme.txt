# "Movie Finder" Web App

main code is written on python3 using Flask

to run the website:
1. install python3 https://www.python.org/downloads/
2. install Flask
    if you are using macOS -> open terminal and type: pip3 install flask
    if you are using Windows -> open terminal and type: pip install flask
3. run flask_app.py
4. go to the link
5. enjoy our website :)


PROJECT STRUCTURE:
1. find_modules - package containing python modules:
    1. find_movie.py ----- finds a movie in the database 'movies_dataset.csv'
    2. get_poster.py ----- finds a poster using omdb API
2. static -- contains css and pictures
3. templates -- contains html files
4. flask_app.py -- main module for running a website
5. movies_dataset.csv -- database with movies
6. readme.txt -- you are currently reading it