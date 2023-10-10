import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.artist_repository import *
from lib.album import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['POST'])
def add_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form["artist_id"]
    
    new_album = Album(13, title, release_year, artist_id)
    repository.create(new_album)
    return 'Album Added'


@app.route('/artists', methods=['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    all_artists = repository.all()
    return ', '.join(all_artists)


# ___________________________________________________

@app.route('/artists', methods=['POST'])
def add_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    
    name = request.form["name"]
    genre = request.form["genre"]
    
    new_artist = Artist(0, name, genre)
    repository.create(new_artist)
    return 'Artist added'

# == Example Code Below ==
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

from example_routes import apply_example_routes
apply_example_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))