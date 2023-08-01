class Track:
    # Public properties:
    #   title: a string
    #   artist: a string

    def __init__(self, title, artist):
        # Parameters:
        #   title: a string
        #   artist: a string
        # Side-effects:
        #   Sets the title and artist properties
        self.title = title 
        self.artist = artist

    def format(self):
        # Returns:
        #   a string in the format "TITLE by ARTIST"
        pass