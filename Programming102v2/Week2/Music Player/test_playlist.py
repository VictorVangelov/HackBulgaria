import unittest
from playlist import Playlist
from song import Song
import json
import mutagen


class Test_Playlist(unittest.TestCase):

    def setUp(self):
        self.some_playlist = Playlist("my playlist")
        self.some_song = Song("title", "artist1", "album", 1, 250, 32)
        self.some_song2 = Song("title2", "artist1", "album2", 2, 250, 32)
        self.some_song3 = Song("title3", "artist3", "album3", 3, 250, 16)
        self.some_playlist.add_song(self.some_song)

    def test_init(self):
        self.assertEqual(self.some_playlist.name, "my playlist")

    def test_total_length(self):
        self.assertEqual(0, self.some_playlist.total_length)

    def test_show_artist(self):
        self.some_playlist.add_song(self.some_song2)
        self.some_playlist.show_artists()
        self.assertEqual(1, len(self.some_playlist.set_of_artists))
        self.some_playlist.add_song(self.some_song3)
        self.some_playlist.show_artists()
        self.assertEqual(2, len(self.some_playlist.set_of_artists))

    def test_remove_disrated(self):
        self.some_playlist.remove_disrated(1)
        self.assertEqual(1, len(self.some_playlist.list_all_songs))
        self.some_playlist.add_song(self.some_song3)
        self.assertEqual(2, len(self.some_playlist.list_all_songs))
        self.assertRaises(IndexError, self.some_playlist.remove_disrated(6))

    def test_remove_bad_quality(self):
        self.some_playlist.add_song(self.some_song2)
        self.some_playlist.remove_bad_quality()
        self.assertEqual(2, len(self.some_playlist.list_all_songs))

    def test_remove_song(self):
        self.assertEqual(1, len(self.some_playlist.list_all_songs))
        self.some_playlist.remove_song("title")
        self.assertEqual(0, len(self.some_playlist.list_all_songs))



if __name__ == '__main__':
    unittest.main()
    print(self.some_song.__dict__)

