class MusicTracker:

    def __init__(self):
        self.music_dict = {}

    def add_track(self, artist, track):
        self.music_dict.setdefault(artist, []).extend([track])
        return f'Your track: {track} has been added.'

    def view_artists(self):
        artist = self.music_dict.keys()
        return '\n'.join(artist)

    def view_tracks_by_artist(self, artist):
        for k,v in self.music_dict.items():
            if k == artist:
                tracks = v
         
        return'\n'.join(tracks)

    def view_library(self):

        print((list(self.music_dict.items())))
        return((list(self.music_dict.items())))

    def remove_track(self, artist, track):
        self.music_dict[artist].remove(track)
        #self.music_dict[artist] = [value for value in self.music_dict[artist] if value != track]]
        return  f'Track {track} has been removed'

    def remove_artist(self, artist):
        del self.music_dict[artist]
        return f'Artist {artist} has been removed'

    #def favourite_artist(self):
        # for k,v in self.music_dict.items():
        #     loop Throughfind len of v 
            
        #return f'Your favourite artist is {Tucpa} with {3} songs.'

        # two variables to keep track of result: one is counter, one is artist name
        # counter is 0 and artist name is empty string 
        # music_dict => {artist : [songs,  songs ]}
        # goal of the function: return the artist with the most number of songs
        # loop through list of items with key value
        # check number of entries in value 
        # if current_num_songs > counter
        #       set the counter to current_num_songs
        #       set artist name to current key 