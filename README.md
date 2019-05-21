# Project: Word count

### Objective: Find top 10 most frequently used words in text files in a directory

### Usage: 
       make run   - Run an analysis for all text files in a directory under {DATASET_DIR} set in 
                    Makefile. Report files are put under {REPORT_DIR}. In addition, a file 
                    named "report.pdf" is created to visualize 10 most frequent words used in all
                    files using a bar chart.
       make test  - Generate test data under {TESTDATA_DIR}, do analysis, and compare results 
                    to known solutions. Solutions are written out under {TESTSOLUTION_DIR}. 
                    The number of test passes set by {NO_OF_TEST_PASS} in Makefile.
       make clean - Clean test data, report files, and unnecessary files and folders.
       make help  - Print this usage message.

### Requirements: 
       python3, matplotlib (optional)

### Description:

The code is written in Python. It reads in all text files in a directory and counts words used in 
each file in the directory. It then writes out reports files into a separated directory. Report files 
have an extension .rpt. The code also prints out most frequently used words appeared in all text files 
in the directory to standard output. If the matplotlib package is installed, the code plots a bar chart 
of the results and saves the plot as a pdf file named report.pdf. 

#### [run_analysis.py](https://github.com/annop-w/word_count/blob/master/run_analysis.py)
This file contains the main program for performing an analysis. It reads in two command line arguments:
data_path and report_path. It then calls the function `word_count` which performs the analysis and returns
a list of most frequently used words appeared in all files together with the frequencies. It calls the 
function `plot_top_words` to print out the final report.

#### [count.py](https://github.com/annop-w/word_count/blob/master/count.py)
This file contains the main function `word_count`. It first generates a list of all files in the directory 
which we would like to analyse. Then, the function loops over all files in the directory. The function 
currently assumes that the text contained in each file is written in a single line. After reading in 
the data, the text is passed onto the `clean_text` function which does data cleaning. The test is 
then splitted into a list of words using white space as a separator. We use a dictionary object to 
keep track of unique words and count their frequencies. This task is done in the `add_to_dict` function.
Note that we use two dictionaries: one to store analysed data in each file and another that stores 
data from all files. To report on most frequent words we sort the dictionaries using their values (i.e. 
frequency of each word) and return a list of list in the form [[word, frequency]].

#### [data_cleaning.py](https://github.com/annop-w/word_count/blob/master/data_cleaning.py)
This file contains the definition of the `clean_text` function used for cleaning the text data. 
It converts texts to lowercase. When working with the movie review dataset it is necessary to 
remove html tags (e.g. \<br\> and \</br\>). This is done using the regular expression operation `re.sub`.
In addition, it also replaces special characters, e.g. `. " , !`. The list of special characters to 
be removed can be added as necessary. 

#### [word_class.py](https://github.com/annop-w/word_count/blob/master/word_class.py)
This file contains the definition of the class `list_of_words`. The class initializes an empty
list object and contains functions to add a list or a string object to this list.

#### [report.py](https://github.com/annop-w/word_count/blob/master/report.py)
This file contains the definition of the `plot_top_words` function. The function receives the 
list of list `top_words` containing the most frequently used words in all files in the directory 
and their frequencies. It detects whether the `matplotlib` package is installed or not. If 
`matplotlib` is installed, it creates a horizontal bar chart to visualize the final result and 
saves the chart in the file report.pdf. Then, the code prints out the final report to the 
standard output.

### Testing:

We validate the correctness of the main function `word_count` by generating a test dataset with known 
word frequencies. 

#### [generate_test_data.py](https://github.com/annop-w/word_count/blob/master/generate_test_data.py)
This file contains a program to generate data for testing as well as the definition of the data
generation function `generate`. The program reads in 3 command line arguments: data_path, solution_path, 
and seed_number. This seed number is used for initialization of the pseudo random number generator. 
The algorithm in `generate` uses a list of pre-determined words to generate a random text. Each word 
in the list is given a random frequency `cnt`. Then, the code loops over all words in the list and adds 
the word `cnt` times into another list (`mock_words`). This list is then shuffled randomly and all 
words are joined together (separated by a white space) into a string object. The function returns 
the string object and a list of list containing the pre-defined words and their frequencies (`solution`). 
The solution is then sorted and written out into a file.

### Dataset:

For demonstration purposes we analyse a subset of the Large Movie Review Dataset v1.0 available at 
https://ai.stanford.edu/~amaas/data/sentiment/


       @InProceedings{maas-EtAl:2011:ACL-HLT2011,
       author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  
                    Ng, Andrew Y.  and  Potts, Christopher},
       title     = {Learning Word Vectors for Sentiment Analysis},
       booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational 
                    Linguistics: Human Language Technologies},
       month     = {June},
       year      = {2011},
       address   = {Portland, Oregon, USA},
       publisher = {Association for Computational Linguistics},
       pages     = {142--150},
       url       = {http://www.aclweb.org/anthology/P11-1015}
       }

We use only the data of 12500 positive reviews in this project. Here is a plot showing the analysis result. 

![Result from movie reviews dataset](https://github.com/annop-w/word_count/blob/master/report.png)