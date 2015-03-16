import os
import fnmatch
from playlist import Playlist
from song import Song
from mutagen.mp3 import MP3, HeaderNotFoundError
from mutagen.id3 import ID3, TPE1, TPE2, TIT2, TALB
from mutagen.id3 import ID3NoHeaderError, error
from mutagen.easyid3 import EasyID3

#import id3reader
# from mutagen.mp3 import error
# from mutagen.ID3 import HeaderNotFoundError
# from mutagen.ID3 import InvalidMPEGHeader


class MusicCrawler():

    def __init__(self, path):
        self.path = path
        self.new_title = ""
        self.new_artist = ""
        self.new_album = "Unknown album"
        self.folder_files = []

    def import_songs_from_folder(self, track_name, track_path):
        #track_name = self.path + track_name
        try:
            audio = ID3(track_name)
            audio2 = MP3(track_name)
            artist = (audio['TPE1'].text[0])
            title = (audio['TIT2'].text[0])
            album = (audio['TALB'].text[0])
            length = (audio2.info.length)
            bitrate = (audio2.info.bitrate)
            the_song = Song(title, artist, album, Song.MIN_RATING, length, bitrate)
            the_song.file_path = track_path
            return the_song
        except (error, ID3NoHeaderError):
            audio = MP3(track_name, ID3=EasyID3)
            self.generate_tags_from_file_name(track_name)
            #audio = EasyID3(track_name)
            audio["title"] = self.new_title
            audio["artist"] = self.new_artist
            audio["album"] = self.new_album
            #title, artist, album, rating, length, bitrate
            the_song = Song(audio["title"], audio["artist"], audio["album"], Song.MIN_RATING, int(audio.info.length), audio.info.bitrate)
            the_song.file_path = track_path
            return the_song
        #except OSError:
            #print("sorry")

    def generate_tags_from_file_name(self, file_name):
        the_tags = str(file_name.replace(".mp3", ""))
        the_tags = str(the_tags.replace("_", "\n"))
        the_tags = str(the_tags.replace("-", "\n"))
        the_tags = the_tags.split("\n")
        new_artist = (" ".join(the_tags[0:int(len(the_tags)/2)]))
        self.new_artist = "".join(new_artist)
        self.new_title = " ".join(the_tags[int(len(the_tags)/2):])

    def collect_songs_names(self):
        for root, dir, files in os.walk(self.path):
            # DA VNIMAVAM KAKVO PRAVI TUK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #print(root)
            #self.path = root
            #print (root)
            #print(dir)
            for items in fnmatch.filter(files, "*.mp3"):
                if root[-1] == "/":
                    self.folder_files.append(root+items)
                else:
                    self.folder_files.append(root+"/"+items)

    def retrun_folder_name(self):
        playlist_name = self.path.replace("/", "\n")
        playlist_name = playlist_name.split("\n")
        return (playlist_name[-1])

    def generate_playlist(self, playlist_name):
        self.collect_songs_names()
        new_playlist = Playlist("Songs in {} ".format(self.retrun_folder_name()))
        #print(os.getcwd())
        #os.chdir(self.path)
        #print(os.getcwd())
        for song_name in self.folder_files:
            file_name, file_path = MusicCrawler.split_path_and_name(song_name)
            new_playlist.list_all_songs.append(self.import_songs_from_folder(file_name, file_path))
            new_playlist.save(playlist_name)
        return new_playlist

    @staticmethod
    def split_path_and_name(file_path):
        file_name = file_path.split("/")
        file_name = file_name[-1]
        #print(file_name)
        fp = file_path
        #print(fp)
        return file_name, fp

if __name__ == '__main__':
    #a = MusicCrawler("/home/shosho/Music/")
    a = MusicCrawler("/home/shosho/asd/")

    #print(a.folder_files)
    playlist = a.generate_playlist("new_pl.txt")
    #playlist.save("example_playlist.txt")
    #MusicCrawler.split_path_and_name("/home/shosho/Python/HackBulgaria/Programming101/Week2/Foo Fighters-The Pretender (www.myfree.cc).mp3")
    #print(playlist)
