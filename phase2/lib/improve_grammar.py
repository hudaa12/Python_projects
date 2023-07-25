def improve_grammar(text):
    first_letter = text[0]
    last_letter = text[-1]
    punctuation = ['!', '.', '?']

    if first_letter != first_letter.upper():
        return False
    
    if last_letter not in punctuation:
        return False
    
    return True
