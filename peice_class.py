class peice:
    def __init__(self, name, artist, year):
        self.pic = 'images/' + name
        self.name = name
        self.artist = artist
        self.year = year
        self.answers = [self.name, self.artist, self.year]
        self.i = 0