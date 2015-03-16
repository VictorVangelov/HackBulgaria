import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.some_song = Song("title", "artist", "album", 0, 333, 32)

    def test_init(self):
        self.assertEqual("title", self.some_song.title)
        self.assertEqual("artist", self.some_song.artist)
        self.assertEqual("album", self.some_song.album)
        self.assertEqual(0, self.some_song.rating)
        self.assertEqual(333, self.some_song.length)
        self.assertEqual(32, self.some_song.bitrate)

    def test_rate(self):
        self.some_song.rate(6)
        self.assertEqual(self.some_song.rating, 5)

if __name__ == '__main__':
    unittest.main()
