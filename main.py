from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:dodo123.@localhost:3306/movies'
db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    imdb_id = db.Column(db.String(255), nullable=False)
    uri = db.Column(db.String(255), nullable=False)
    year = db.Column(db.String(255), nullable=False)
    def __repr__(self):
        return f"<Movie(title='{self.title}', imdb_id='{self.imdb_id}', year='{self.year}, uri='{self.uri}')>"

@app.route('/')
def home():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run()