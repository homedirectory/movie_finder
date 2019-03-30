from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf import FlaskForm
from find_movie import *
from get_poster import *


app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        try:
            year = int(request.form['year'])
            rating = request.form['radio-group']
            genres = request.form.getlist('genre')
            rating = int(rating[0]) if "+" in rating else -1 * int(rating[0])
            print(year, rating, genres)
            movie = find_movie(year, rating, genres)[0]
            poster = get_poster(movie)
            print(movie)
            print(poster)
        except NoSuchMovie as e:
            print(e)
            print("Mesht")
            error = "Something went wrong. Please try again"
        #     # flash(error)
            return render_template('homepage.html', error=error)
        except NoPoster as e:
            print(e)
            error = "Something went wrong. Please try again"
            return render_template('homepage.html', error=error)




    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(debug=True)