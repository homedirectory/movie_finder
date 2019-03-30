from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf import FlaskForm


app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        try:
            year = request.form['year']
            rating = request.form['radio-group']
            genre = request.form.getlist('genre')
        except:
            print("Mesht")
            error = "Something went wrong. Please try again"
            # flash(error)
            return render_template('homepage.html', error=error)


        print(year, rating, genre)
        print(type(year), type(rating), type(genre))

    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(debug=True)