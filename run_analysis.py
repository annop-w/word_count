from count import word_count
from report import plot_top_words
import sys

if __name__ == "__main__":

    # check command line arguments
    if len(sys.argv) < 2:
        print("# Error : missing an argument for data path")
        sys.exit("# Usage : python run_analysis.py {DATA_PATH} {REPORT_PATH}")
    elif len(sys.argv) < 3:
        print("# Error : missing an argument for report path")
        sys.exit("# Usage : python run_analysis.py {DATA_PATH} {REPORT_PATH}")

    # get path for dataset from command line
    data_path = sys.argv[1]
    if data_path[-1] != "/": # add slash in case it's not there
        data_path += "/"

    # get path for outputting the report from command line
    report_path = sys.argv[2]
    if report_path[-1] != "/": # add slash in case it's not there
        report_path += "/"

    # do analysis and report on top 10 most frequent words
    n_words = 10
    top_words = word_count(data_path, report_path, n_words)

    plot_top_words(top_words)
    
    exit()

