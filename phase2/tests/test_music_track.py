import pytest
from lib.music_track import *

"""
initially, there are two tracks
"""

def test_add_and_view_artists():
    library = MusicTracker()
    library.add_track('Tupac','Hail Mairy')
    answer = library.view_artists()
    assert answer == 'Tupac'
    library.add_track('Tupac','Hail Mairy')
    library.add_track('Nipsey Hussle','Ocean Blues')
    answer1 = library.view_artists()
    assert answer1 == 'Tupac\nNipsey Hussle'
    library.add_track('Tupac','Hail Mairy')
    library.add_track('Nipsey Hussle','Ocean Blues')
    library.add_track('Young Dolph','Hold Up')
    library.add_track('King Von','I am')
    answer1 = library.view_artists()
    assert answer1 == 'Tupac\nNipsey Hussle\nYoung Dolph\nKing Von'


def test_view_tracks_by_artist():
    library = MusicTracker()
    library.add_track('Tupac','Hail Mairy')
    library.add_track('Nipsey Hussle','Ocean Blues')
    library.add_track('Young Dolph','Hold Up')
    library.add_track('Young Dolph','Crashin Out')
    library.add_track('King Von','I am')
    answer = library.view_tracks_by_artist('Young Dolph')
    assert answer == 'Hold Up\nCrashin Out'

def test_view_library():
    library = MusicTracker()
    library.add_track('Tupac','Hail Mairy')
    library.add_track('Nipsey Hussle','Ocean Blues')
    library.add_track('Young Dolph','Hold Up')
    library.add_track('Young Dolph','Crashin Out')
    library.add_track('King Von','I am')
    answer = library.view_library()
    assert answer == [('Tupac', ['Hail Mairy']), ('Nipsey Hussle', ['Ocean Blues']), ('Young Dolph', ['Hold Up', 'Crashin Out']), ('King Von', ['I am'])]

def test_remove_track():
    library = MusicTracker()
    library.add_track('Tupac', 'Uppercut')
    library.add_track('Tupac', 'Starin Through My Rearview')
    ans = library.remove_track('Tupac', 'Uppercut')
    assert ans == f'Track Uppercut has been removed'
    answer = library.view_tracks_by_artist('Tupac')
    assert answer == 'Starin Through My Rearview'

def test_remove_artist():
    library = MusicTracker()
    library.add_track('Tupac', 'Uppercut')
    library.add_track('Tupac', 'Starin Through My Rearview')
    ans = library.remove_artist('Tupac')
    assert ans == f'Artist Tupac has been removed'

#def test_favourite_artist():
    # library = MusicTracker()
    # library.add_track('Tupac', 'Uppercut')
    # library.add_track('Tupac', 'Starin Through My Rearview')
    # library.add_track('Tupac','Hail Mairy')
    # library.add_track('Nipsey Hussle','Ocean Blues')
    # library.add_track('Young Dolph','Hold Up')
    # library.add_track('Young Dolph','Crashin Out')
    # library.add_track('King Von','I am')
    # ans = library.favourite_artist()
    # assert ans == f"Your favourite artist is Tupac with 3 songs."