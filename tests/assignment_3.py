from tester import Test, Input

# Test = namedtuple("Test", ["name", "args", "inputs", "expect"])
# Input = namedtuple("Input", ["prompt", "value"])

q1_tests = [
    Test("SomeInput", "", [Input("Please Enter Values For Matrix 1\r\n", "111"),
                      Input("Please Enter Values For Matrix 2", "000001114400000111119999999999999999")],
     "Please Enter Values For Matrix 1\r\nPlease Enter Values For Matrix 2111\n\n000001114400000111119999999999999999\n"
     "The First Matrix Is :- \n  1  1  1  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n"
     "The Second Matrix Is :- \n  0  0  0  0  0\n  1  1  1  1  1\n  0  0  0  0  0\n  1  1  1  1  1\n  1  1  1  1  1\n"
     "The Resultant Matrix Is :- \n  1  1  1  1  1\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n"),
]

q2_tests = [
    Test("ExtraPoints", "", [Input("Enter the string:", "This is Ashutosh. This is my name.....")],
         "Enter the string:\nThis is Ashutosh. This is my name.....\nNumber of words in given string are: 7\n"),
]

q3_tests = [
    Test("BasicCheck", "", [Input("Please enter the main string..\r\n", "This is the input string"),
                            Input("Please pattern string to find..", "str")],
         "Please enter the main string..\r\nPlease pattern string to find..This is the input string\n\nstr\n> This is the input ing"),
]

tests = [q1_tests, q2_tests, q3_tests]
