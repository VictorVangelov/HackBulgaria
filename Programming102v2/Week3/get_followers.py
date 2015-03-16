import requests
from directed_graph import DirectedGraph

TOKEN = "02e3593880205eae6e68d16b048201228985fb95"


class GetFollowers():

    def __init__(self):
        self.dict_of_following = {}
        self.list_of_follwoers_names = []
        self.dg = DirectedGraph()

    def folling(self, user_name):
        git_user_url = "https://api.github.com/users/{}/following".format(user_name)
        my_request = requests.get(git_user_url, auth=(TOKEN, ''))
        #print(my_request.encoding)
        if my_request.status_code == 200:
            self.dict_of_following = my_request.json()
            #print(self.dict_of_following)
            self.list_of_follwoers_names = []
            for user in self.dict_of_following:
                self.list_of_follwoers_names.append(user["login"])
            return self.list_of_follwoers_names
        else:
            print("fuck you")

    def metoda(self, user):

        for follower in self.folling(user):
            self.dg.add_edge(user, follower)
            for follower2 in self.folling(follower):
                self.dg.add_edge(follower, follower2)
                for follower3 in self.folling(follower2):
                    self.dg.add_edge(follower2, follower3)
                    for follower4 in self.folling(follower3):
                        self.dg.add_edge(follower3, follower4)

    def print_following(self):
        for person in self.dict_of_following:
            print(person["login"])

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

if __name__ == '__main__':
    gf = GetFollowers()

    gf.metoda("Ivaylo-Bachvarov")
    if gf.dg.path_between("Ivaylo-Bachvarov", "robneu"):
        print("yeah")
    else:
        print("nope")
