class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.passed_texts = 0 
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if not text:
            return False
        if text[0].isupper():
            last_char = text[-1]
            sentence_enders = {'.', '!', '?'}
            if last_char in sentence_enders:
                self.passed_texts += 1
                self.total_texts += 1
                return True
            self.total_texts += 1
            return False
  
    def percentage_good(self):
        if self.total_texts == 0:
            return 0
        percentage =  (self.passed_texts / self.total_texts) * 100.0
        return int(percentage)
    # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.