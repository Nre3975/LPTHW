def break_words(stuff): 
    # Using """ Comment """ instead of # means it shows up 
    # in a help command (Documentation comments)
    """This function will break up words. """ 
    words = stuff.split(' ')
    return words

def sort_words(words): 
    """Sorts the words""" 
    return sorted(words)

def print_first_word(words): 
    """ prints first word after popping it off """
    word = words.pop(0) 
    print(word)

def print_last_word(words):
    # prints last word after popping it off 
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence): 
    # Take sentence and return sorted words. 
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence): 
    # Print first and last words of then sentence 
    # Take a sentence, break it into a list of words
    # then print the first and last. 
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):  
    # Take a sentance sort it (which breaks words up and returns 
    # a sorted list), Then prints first and last words.
    words = sort_sentence(sentence) 
    print_first_word(words)
    print_last_word(words)