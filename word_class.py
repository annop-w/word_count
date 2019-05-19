class list_of_words:

    def __init__(self):
        self.words = []

    def add_words(self, words_to_add):
        if type(words_to_add)==list:
            self.words += words_to_add
        elif type(words_to_add)==str:
            self.words.append(words_to_add)

    def print_words(self):
        print(self.words)

