from lib.music_library import MusicLibrary

"""
inintially there are no tracks.
"""
def test_init_there_are_no_tracks():
    music_library = MusicLibrary()
    assert music_library.all() == []