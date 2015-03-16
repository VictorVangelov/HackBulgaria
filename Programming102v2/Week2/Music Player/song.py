class Song():
    MAX_RATING = 5
    MIN_RATING = 0


    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate
        self.file_path = ""

    def rate(self, num):number_of_programmers
        if num >= MIN_RATING or num <= MAX_RATING:
            self.rating = num
        else:
            error_message = "The rating must be between {} and {}".format(MIN_RATING, MAX_RATING)
            raise IndexError
