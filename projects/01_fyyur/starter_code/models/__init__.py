from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


artist_genre_table = db.Table('artist_genre_table', 
    db.Column('genre_id',db.Integer,db.ForeignKey('Genre.id'),primary_key=True),
    db.Column('artist_id',db.Integer,db.ForeignKey('Artist.id'),primary_key=True))

venue_genre_table = db.Table('venue_genre_table',
    db.Column('genre_id', db.Integer, db.ForeignKey('Genre.id'), primary_key=True),
    db.Column('venue_id',db.Integer, db.ForeignKey('Venue.id'),primary_key=True))

class Genre(db.Model):
    __tablename__='Genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    #genres = db.Column(db.String(120))
    genres = db.relationship('Genre', secondary=artist_genre_table, backref=db.backref('artists'))
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120), nullable=True)
    seeking_venue = db.Column(db.Boolean, default=False, nullable=False)
    seeking_description = db.Column(db.String(120),nullable=True)
    shows = db.relationship('Show', backref='artist',lazy=True)
    def __repr__(self):
        return f'Artist: {self.id} {self.name}'

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # --Third Normal Form-- stick to the scope
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    #city_id = db.Column(db.Integer, db.ForeignKey('City.id'),nullable=False)
    #state_id = db.Column(db.Integer, db.ForeignKey('State.id'),nullable=False)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500),nullable=True)
    facebook_link = db.Column(db.String(120),nullable=True)
    website = db.Column(db.String(120), nullable=True)
    # This should be another model, searching for an artist, Artist_Search
    seeking_talent = db.Column(db.Boolean, nullable = False, default=False)
    seeking_description = db.Column(db.Text, nullable = True)
    # Lol, I might be getting into something more than the course wants...
    # https://stackoverflow.com/questions/24612395/how-do-i-execute-inserts-and-updates-in-an-alembic-upgrade-script/24623979
    # https://docs.sqlalchemy.org/en/14/orm/examples.html#module-examples.generic_associations
    #links = db.Column(db.String(),backref='creator')
    genres = db.relationship('Genre', secondary=venue_genre_table, backref=db.backref('venues'))
    shows = db.relationship('Show', backref='venue', lazy=True)
    def __repr__(self):
        return f'Venue: {self.id} {self.name}'

class Show(db.Model):
    __tablename__="Show"
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column('artist_id',db.Integer,db.ForeignKey(Artist.id))
    venue_id = db.Column('venue_id',db.Integer,db.ForeignKey(Venue.id))
    start_time = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return f'Show: {self.id} {self.start_time} Artist={artist_id} Venue={venue_id}'
