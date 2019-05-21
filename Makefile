DATASET_DIR      = "./dataset/data"
TESTDATA_DIR     = "./dataset/mockdata"
REPORT_DIR       = "./report"
TESTSOLUTION_DIR = "./solution"
NO_OF_TEST_PASS = 10
SHELL := /bin/bash

.PHONY: test run clean

help:
	@echo "USAGE: make run   - Run an analysis for all text files in a directory under {DATASET_DIR} set in"
	@echo "                    Makefile. Report files are put under {REPORT_DIR}. In addition, a file"
	@echo "                    named \"report.pdf\" is created to visualize 10 most frequent words used in all"
	@echo "                    files using a bar chart."
	@echo "       make test  - Generate test data under {TESTDATA_DIR}, do analysis, and compare results"
	@echo "                    to known solutions. Solutions are written out under {TESTSOLUTION_DIR}."
	@echo "                    The number of test passes set by {NO_OF_TEST_PASS} in Makefile."
	@echo "       make clean - Clean test data, report files, and unnecessary files and folders."
	@echo "       make help  - Print this usage message."

run:
	@echo "Do text analysis for directory ${DATASET_DIR}"
#set LANG environment variable to en_GB.UTF-8 in case it's not set
#this is for handling non-ascii characters in the review data
	@export LANG=en_GB.UTF-8 ; python3 run_analysis.py ${DATASET_DIR} ${REPORT_DIR}
	@echo "Analysis ... DONE"
	@echo "Report files are in ${REPORT_DIR}"

test:
	@echo "Generating test dataset in ${TESTDATA_DIR}"
	@if [ ! -d ${TESTDATA_DIR} ]; then mkdir -p ${TESTDATA_DIR}; fi
	@if [ ! -d ${TESTSOLUTION_DIR} ]; then mkdir -p ${TESTSOLUTION_DIR}; fi
	@for n in `seq 1 ${NO_OF_TEST_PASS}`; do \
	    python3 generate_test_data.py ${TESTDATA_DIR} ${TESTSOLUTION_DIR} $${n} ; \
	 done
	@echo "Generating test dataset ... done"
	@echo "Do text analysis for directory ${TESTDATA_DIR}"
	@python3 run_analysis.py ${TESTDATA_DIR} ${REPORT_DIR}
	@for n in `seq 1 ${NO_OF_TEST_PASS}`; do \
	    cmp -s ${REPORT_DIR}/test_data_$${n}.rpt ${TESTSOLUTION_DIR}/test_solution_$${n}.txt ; \
	    DIFF=$$? ; \
	    if [ $${DIFF} -eq 0 ]; then \
	       echo "Testing PASS$${n} ... PASSED" ; \
	    else \
	       echo "Testing PASS$${n} ... FAILED" ; \
	    fi ; \
	 done

clean:
	@rm -rf ${TESTDATA_DIR} ${TESTSOLUTION_DIR} ${REPORT_DIR} *~ *.pyc __pycache__ #report.pdf 



