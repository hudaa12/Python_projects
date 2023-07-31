import math
class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        words = wpm.split()
        word_count = len(words)
        return word_count / 200

    # def reading_chunk(self, wpm, minutes):
    #     words_user_can_read = wpm * minutes
    #     words = self.contents.split()
    #     chunk_start = self.read_so_far
    #     chunk_end = self.read_so_far + words_user_can_read
    #     chunk_words = words[:chunk_start:chunk_end]
    #     self.read_so_far = chunk_end
    #     return " ".join(chunk_words)
