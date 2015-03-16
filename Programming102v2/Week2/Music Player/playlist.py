from song import Song
import json
from mutagen.mp3 import MP3
import os



class Playlist():
    MIN_BITRATE = 32

    def __init__(self, name):
        self.name = name
        self.list_all_songs = []
        self.total_length = 0
        self.set_of_artists = set([])
        self.dict = {}
        self.m3u_format = "#EXTM3U \n"

    def save(self, filename):
        dict_for_file = {}
        list_of_songs = []
        dict_for_file["playlist_name"] = self.name
        for song in self.list_all_songs:
            list_of_songs.append(song.__dict__)
        dict_for_file["Songs"] = list_of_songs
        file = open(filename, "w")
        file.write(json.dumps(dict_for_file))
        file.close()
        self.save_m3u_playlist(filename)

    def generate_m3u_content(self):
        for song in self.list_all_songs:
            length = int(song.length)
            current_row = "#EXTINF:{}, {} - {} {}\n{}\n".format(length, song.artist, song.title, song.album, song.file_path)
            self.m3u_format += (current_row)

    def save_m3u_playlist(self, filename):
        playlist_name = filename.split(".")
        playlist_name = "{}.m3u".format(playlist_name[0])
        self.generate_m3u_content()
        #os.chdir("/home/shosho/generated_playlists/")
        file = open("/home/shosho/generated_playlists/"+playlist_name, "w")
        file.write(self.m3u_format)
        file.close()

    def load(self, filename):
        file = open(filename, "r")
        content = json.load(file)
        self.name = content["playlist_name"]
        for song in content["Songs"]:
            self.list_all_songs.append(self.decode_song(song))

    def decode_song(self, one_song):
        title = one_song["title"]
        artist = one_song["artist"]
        album = one_song["album"]
        rating = one_song["rating"]
        length = one_song["length"]
        bitrate = one_song["bitrate"]
        file_path = one_song["file_path"]
        created_song = Song(title, artist, album, rating, length, bitrate)
        created_song.file_path = file_path
        return created_song

    def add_song(self, song):
        if isinstance(song, Song):
            self.list_all_songs.append(song)
            self.total_length += song.length
        else:
            print("This is not a song, please try agian")

    def remove_song(self, name):
        songs = []
        for num_song, song in enumerate(self.list_all_songs):
            if song.title != name:
                songs.append(song)
        self.list_all_songs = []
        self.list_all_songs = songs

    def format_soconds(self, length):
        sec = length
        hrs = int(sec / 3600)
        sec -= int(3600*hrs)
        mins = int(sec / 60)
        sec -= 60*mins
        return "%02d:%02d:%02d" % (hrs, mins, sec)

    def __str__(self):
        somelist = []
        print(self.name)
        for song in self.list_all_songs:
            current_length = self.format_soconds(song.length)
            somelist.append("{} {} - {}".format(song.artist, song.title, current_length))
        return "\n".join(somelist)

    def total_length(self):
        self.total_length = 0
        for song in self.list_all_songs:
            self.total_length += song.length

    def remove_disrated(self, num):
        if num >= Song.MIN_RATING or num <= Song.MAX_RATING:
            for song_num, song in enumerate(self.list_all_songs):
                if song.rating < num:
                    del self.list_all_songs[song_num]
                    song_num -= 1
        else:
            error_message = "The rating must be between {} and {}".format(MIN_RATING, MAX_RATING)
            raise IndexError

    def show_artists(self):
        for song in self.list_all_songs:
            self.set_of_artists.add(song.artist)
        artists = "\n".join(self.set_of_artists)
        #print(artists)

    def remove_bad_quality(self):
        new_list_of_songs = []
        for song in self.list_all_songs:
            if not song.bitrate < self.MIN_BITRATE:
                new_list_of_songs.append(song)
        self.list_all_songs = []
        self.list_all_songs = new_list_of_songs

    def test_import_mp3(self):
        audio = MP3('/home/shosho/Python/HackBulgaria/Programming101/Week2/a2.mp3')
        print (audio.info.bitrate, audio.info.length)

if __name__ == '__main__':
    pass
    #some_playlist = Playlist("Disturbed and DC")
    # some_song = Song("Highway to hell", "AC/DC", "Highway to Hell", 1, 208, 32)
    # some_song2 = Song("Decadance", "Disturbed", "Ten Thousand Fists", 2, 208, 32)
    # some_song3 = Song("Striken", "Disturbed", "Ten Thousand Fists", 3, 247, 16)
    # some_playlist.add_song(some_song)
    # some_playlist.add_song(some_song2)
    # some_playlist.add_song(some_song3)
    # some_playlist.save("save.txt")
    #some_playlist.load("save.txt")
    #some_playlist.test_import_mp3()
    #print (some_playlist)
