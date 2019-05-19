from word_class import list_of_words
import random
import os
import sys

def generate(seed_number):

    random.seed(seed_number) # initialize seed for the random number generator
    
    test_words = list_of_words() # initialize list of test words

    # add words to the list
    test_words.add_words(["This","is","my","list","of","test","words","I","will",\
                          "generate","a","long","text","from","these","randomly","in",\
                          "total","we","have","many","samples","to","work","with","more",\
                          "can","be","added","as","necessary"])

    # generate list of integers storing counts for each word in the list
    counts_each_word = []
    MAX_COUNTS = 100 

    mock_words = list_of_words()
    for i in range(len(test_words.words)):
        cnt = random.randint(1,MAX_COUNTS)
        counts_each_word.append(cnt)
        for n in range(cnt): # put words into the list using known counts
            mock_words.add_words(test_words.words[i])

    random.shuffle(mock_words.words) # shuffle the word list randomly

    text = " ".join(mock_words.words) # join words into long text separated by a space
    solution = [ [test_words.words[i].lower(),counts_each_word[i]] for i in range(len(test_words.words)) ]
    
    return text , solution

if __name__ == "__main__":

    # check command line arguments
    if len(sys.argv) < 2:
        print("# Error : missing an argument for data path")
        sys.exit("# USAGE : python generate_test_data.py {DATA_PATH} {SOLUTION_PATH} {SEED_NUMBER}")
    elif len(sys.argv) < 3:
        print("# Error : missing an argument for solution path")
        sys.exit("# USAGE : python generate_test_data.py {DATA_PATH} {SOLUTION_PATH} {SEED_NUMBER}")
    elif len(sys.argv) < 4:
        print("# Error : missing an argument for seed number")
        sys.exit("# USAGE : python generate_test_data.py {DATA_PATH} {SOLUTION_PATH} {SEED_NUMBER}")

    data_path = sys.argv[1]
    if data_path[-1] != "/": # add slash in case it's not there
        data_path += "/"

    solution_path = sys.argv[2]
    if solution_path[-1] != "/": # add slash in case it's not there
        solution_path += "/"

    seed = int(sys.argv[3])

    text_for_test , test_solution = generate(seed_number=seed)

    # sort the frequency in descending order
    # then sort alphabetically if the frequency is equal
    sorted_solution = [[v[0],v[1]] for v in sorted(test_solution, key=lambda kv: (-kv[1], kv[0]))]

    # write out data to a text file
    f = open(data_path + "test_data_" + str(seed) + ".txt","w")
    f.write(text_for_test)
    f.close()

    # write out solution to a text file
    n_words = 10
    f = open(solution_path + "test_solution_" + str(seed) + ".txt","w")
    for i in range(n_words):
        f.write(sorted_solution[i][0] + " - " + str(sorted_solution[i][1]) + "\n")
    f.close()
    
    exit()
