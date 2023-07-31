import pytest
from lib.music_track import *

"""
initially, there are two tracks
"""
def test_init_music_track():
    tracker = MusicTrack()
    assert tracker.() == []