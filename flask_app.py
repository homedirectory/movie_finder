from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf import FlaskForm
from get_poster import *
from find_movie import *


app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        try:
            year = int(request.form['year'])
            rating = request.form['radio-group']
            print(rating)
            rating = int(rating[0]) if "+" in rating else -1 * int(rating[0])
            genres = request.form.getlist('genre')
            popularity = request.form['pop']
            print(year, rating, genres, popularity)
            movie_name = find_movie(year, rating, popularity, genres)[0]
            poster = get_poster(movie_name)
            print(movie_name)
            print(poster)
            # return render_template('no_movies.html', movie=movie_name, poster=poster)
        except NoSuchMovie as e:
            print(e)
            print("Mesht no movies")
            error = "Something went wrong. Please try again"
        #     # flash(error)
            return redirect(url_for('goback'))
        except NoPoster as e:
            print(e)
            error = "Something went wrong. Please try again"
            return render_template('homepage.html', error=error)
        except:
            return render_template('homepage.html')
    return render_template('homepage.html')


@app.route("/case1", methods=["GET", "POST"])
def goback():
    if request.method == "POST":
        return redirect(url_for('homepage'))
    return render_template('no_movies.html')








if __name__ == "__main__":
    app.run(debug=True)