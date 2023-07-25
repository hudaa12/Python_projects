
def estimate_reading_time(text):
    if text == "":
        raise Exception("Empty text")
    
    words = text.split()
    word_count = len(words)
    return word_count / 200
    