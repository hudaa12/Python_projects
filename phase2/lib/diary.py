# File: lib/diary.py

import math
class Diary:
    def __init__(self):
        self.log = []

    def add(self, entry):
        
        self.log.append(entry)

    def all(self):
        return self.log
        

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total = 0
        for entry in self.log:
            total += entry.count_words()
            return total

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        word_count = self.count_words()
        return math.ceil(word_count / wpm)
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        words_the_user_could_read = wpm * minutes
        readable_entries = []
        for entry in self.log:
            if entry.count_words() >= words_the_user_could_read:
                readable_entries.append(entry)
            return readable_entries[0]

