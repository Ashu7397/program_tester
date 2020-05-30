import os
from tester import Tester

import sys
sys.path.append('tests')
from assignment_3 import tests


SRC_DIR = "src_files"
CSV_FILE_NAME = "results_final.csv"

def main():
    tester = Tester(tests)
    for student in sorted(os.listdir(SRC_DIR)):
        print("Testing student {}: ".format(student), end='')
        tester.test(student, os.path.join(SRC_DIR, student))

    print("Creating report")
    tester.report_results(CSV_FILE_NAME)


if __name__ == "__main__":
    main()