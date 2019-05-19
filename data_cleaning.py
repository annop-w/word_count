import re
from word_class import list_of_words

def clean_text(text):

    text = text.lower() # convert to lowercase
    text = re.sub(r'(?i)<.*?/>',"",text) # then remove all html tags using regular expression

    words_to_clean = list_of_words()
    words_to_clean.add_words([".",'"',",","!"]) # add these character to the list to be removed 

    # loop through the list and replace them with a space 
    for w in words_to_clean.words:
        text = text.replace(w," ")

    return text 
