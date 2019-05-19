from data_cleaning import clean_text
import os

def add_to_dict(word_dict, word):
    for w in word:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1

def word_count(data_path, report_path, n_words):
    
    # get a list of all files in directory
    data_files = [files for files in os.listdir(data_path) if os.path.join(data_path, files)] 

    all_word_frequency = {} # initialize empty dictionary for word counts in all files

    # loop over files, analyse, and make reports
    for files in data_files:
        review_text = open(data_path+files,"r").read()

        review_text = clean_text(review_text) # pass text for cleaning

        review_words = review_text.split() # split text into words using space
        
        word_frequency = {} # initialize empty dictionary for word counts in each file

        # add words to both dictionaries and count
        add_to_dict(word_frequency, review_words)
        add_to_dict(all_word_frequency, review_words)

        # sort the frequency in descending order
        # then sort alphabetically if the frequency is equal
        sorted_word = [[v[0],v[1]] for v in sorted(word_frequency.items(), key=lambda kv: (-kv[1], kv[0]))]

        # check if report directory exists. if not create it
        if not os.path.exists(report_path):
            os.makedirs(report_path)
        
        # write out a report for each file
        f = open(report_path + os.path.splitext(files)[0] + ".rpt","w")
        n = min(len(sorted_word),n_words) # in case there are less unique words we report frequency of all words
        for i in range(n):
            f.write(sorted_word[i][0] + " - " + str(sorted_word[i][1]) + "\n")
        f.close()

    # sort the frequency in descending order
    # then sort alphabetically if the frequency is equal
    sorted_all_word = [[v[0],v[1]] for v in sorted(all_word_frequency.items(), key=lambda kv: (-kv[1], kv[0]))]

    # visualize most frequent words in all reviews
    return sorted_all_word[:n_words]
