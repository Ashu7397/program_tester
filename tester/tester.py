from program import Program
from collections import defaultdict
from collections import namedtuple
import csv


Test = namedtuple("Test", ["name", "args", "inputs", "expect"])
Input = namedtuple("Input", ["prompt", "value"])

class Tester:
    def __init__(self, tests):
        self.tests = tests
        self.results = defaultdict(lambda : defaultdict(list))

    def test(self, student, path):
        for q_num, tests in enumerate(self.tests):
            try:
                q_name = "/q{}".format(q_num+1)
                print("\nQ", q_num + 1, end="")
                with Program(path+q_name) as prog:
                    try:
                        prog.compile()
                    except RuntimeWarning as e:
                        print("[\033[93m{}\033[0m] ".format(str(e)), end="")

                    for _, args, inputs, expect in tests:
                        res = self._run_test(prog, args, inputs, expect)
                        print(
                            "\033[92m.\033[0m" if res else "\033[91mX\033[0m", end="")
                        self.results[student][q_name].append("PASS" if res else "FAIL")
            except RuntimeError as e:
                print("\033[91m{}\033[0m".format(str(e)), end="")
                self.results[student][q_name].append(str(e))
                #break
        print()

    @staticmethod
    def _run_test(prog, args, inputs, expect):
        prog.log_file.write("-"*40+"\n")
        try:
            output = prog.run(args, inputs)
        except RuntimeError as e:
            output = str(e)

        res = expect == output
        prog.log_file.write("output:\n{}\n".format(output))
        prog.log_file.write("expected:\n{}\n".format(expect))
        prog.log_file.write("result: {}\n".format("PASS" if res else "FAIL"))
        return res

    def report_results(self, file_name):
        with open(file_name, "w") as fd:
            handle = csv.writer(fd, dialect='excel')
            test_names = ["q{}_{}".format(index+1, test.name)
             for index, tests in enumerate(self.tests)
                 for test in tests]
            handle.writerow(["student", "student_id", "grade"] + test_names)
            for student, question in sorted(self.results.items()):
                # results = [res for _, test in question.items() for res in test]
                total_list = []
                for item in sorted(question.items()):
                    val = item[1]
                    if val[0] == "Failed to compile":
                        val = item[1] * int(len(test_names)/len(item[0]))
                    total_list = total_list + val
                # grade = 100*sum(1.0 for res in results if res == "PASS")/len(test_names)
                total_grade = 0
                for grade in total_list:
                    if grade == "PASS":
                        grade_points = 7
                    elif grade == "FAIL":
                        grade_points = 3
                    else:
                        grade_points = 0
                    total_grade += grade_points
                total_grade = total_grade if total_grade < 100 else 100
                student_name, student_id = student.split('_')
                handle.writerow([student_name, student_id, total_grade] + total_list)
