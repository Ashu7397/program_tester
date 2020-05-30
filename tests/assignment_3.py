from tester import Test, Input

# Test = namedtuple("Test", ["name", "args", "inputs", "expect"])
# Input = namedtuple("Input", ["prompt", "value"])

q1_tests = [
    Test("BasicTest", "", [Input("Please Enter Values For Matrix 1\r\n", "111"),
                      Input("Please Enter Values For Matrix 2", "000001114400000111119999999999999999")],
     "Please Enter Values For Matrix 1\r\nPlease Enter Values For Matrix 2111\n\n000001114400000111119999999999999999\n"
     "The First Matrix Is :- \n  1  1  1  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n"
     "The Second Matrix Is :- \n  0  0  0  0  0\n  1  1  1  1  1\n  0  0  0  0  0\n  1  1  1  1  1\n  1  1  1  1  1\n"
     "The Resultant Matrix Is :- \n  1  1  1  1  1\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n"),
    Test("NoInput", "", [Input("Please Enter Values For Matrix 1\r\n", "     "),
                      Input("Please Enter Values For Matrix 2", "")],
     "Please Enter Values For Matrix 1\r\nPlease Enter Values For Matrix 2     \n\n\n"
     "The First Matrix Is :- \n  1  1  1  1  1\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n"
     "The Second Matrix Is :- \n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n"
     "The Resultant Matrix Is :- \n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n"),
    Test("ExcessInput", "", [Input("Please Enter Values For Matrix 1\r\n", "888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888"),
                      Input("Please Enter Values For Matrix 2", "   ")],
     "Please Enter Values For Matrix 1\r\nPlease Enter Values For Matrix 2888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888\n\n   \n"
     "The First Matrix Is :- \n  1  1  1  1  1\n  1  1  1  1  1\n  1  1  1  1  1\n  1  1  1  1  1\n  1  1  1  1  1\n"
     "The Second Matrix Is :- \n  1  1  1  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n"
     "The Resultant Matrix Is :- \n  1  1  1  0  0\n  1  1  1  0  0\n  1  1  1  0  0\n  1  1  1  0  0\n  1  1  1  0  0\n"),
    Test("SomeInput", "", [Input("Please Enter Values For Matrix 1\r\n", "01010 25454 87878 91010 00"),
                      Input("Please Enter Values For Matrix 2", "*-+00000000000000000")],
     "Please Enter Values For Matrix 1\r\nPlease Enter Values For Matrix 201010 25454 87878 91010 00\n\n*-+00000000000000000\n"
     "The First Matrix Is :- \n  0  1  0  1  0\n  1  1  1  1  1\n  1  1  1  1  1\n  1  1  1  1  1\n  0  1  0  1  0\n"
     "The Second Matrix Is :- \n  1  1  1  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n"
     "The Resultant Matrix Is :- \n  0  0  0  0  0\n  1  1  1  0  0\n  1  1  1  0  0\n  1  1  1  0  0\n  0  0  0  0  0\n"),
    Test("BasicTest", "", [Input("Please Enter Values For Matrix 1\r\n", "111000654987010"),
                           Input("Please Enter Values For Matrix 2", "11  53")],
         "Please Enter Values For Matrix 1\r\nPlease Enter Values For Matrix 2111000654987010\n\n11  53\n"
         "The First Matrix Is :- \n  1  1  1  0  0\n  0  1  1  1  1\n  1  1  0  1  0\n  0  0  0  0  0\n  0  0  0  0  0\n"
         "The Second Matrix Is :- \n  1  1  1  1  1\n  1  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n  0  0  0  0  0\n"
         "The Resultant Matrix Is :- \n  1  1  1  1  1\n  1  0  0  0  0\n  1  1  1  1  1\n  0  0  0  0  0\n  0  0  0  0  0\n"),
]

q2_tests = [
    Test("BasicSent", "", [Input("Enter the string:", "Basic sentence with number of words. Lets say 16 for now. Lets see if this works  ")],
         "Enter the string:\nBasic sentence with number of words. Lets say 16 for now. Lets see if this works  \nNumber of words in given string are: 16\n"),
    Test("TabsSpaces", "", [Input("Enter the string:", "     This Something asdkjh Something 	asdfj,,,	  ")],
         "Enter the string:\n     This Something asdkjh Something 	asdfj,,,	  \nNumber of words in given string are: 5\n"),
    Test("Altogether", "", [Input("Enter the string:", ",This is,a sentence  :bla,,bla  bla@robot? and3@3banana e")],
         "Enter the string:\n,This is,a sentence  :bla,,bla  bla@robot? and3@3banana e\nNumber of words in given string are: 11\n"),
    Test("SimpleSpace", "", [Input("Enter the string:", "  This is the       input     .    ")],
         "Enter the string:\n  This is the       input     .    \nNumber of words in given string are: 4\n"),
    Test("SimpleTabs", "", [Input("Enter the string:", "This        is the input        123  * * 654    ")],
         "Enter the string:\nThis        is the input        123  * * 654    \nNumber of words in given string are: 6\n"),
]

q3_tests = [
    Test("BasicCheck", "", [Input("Please enter the main string..\r\n", "a ab abc abcd abcde abcdef"),
                            Input("Please enter the pattern string to find..", "abc")],
         "Please enter the main string..\r\nPlease enter the pattern string to find..a ab abc abcd abcde abcdef\n\nabc\n> a ab  d de def"),
    Test("Empty", "", [Input("Please enter the main string..\r\n", ""),
                            Input("Please enter the pattern string to find..", "")],
         "Please enter the main string..\r\nPlease enter the pattern string to find..\n\n\n> Cannot find the pattern in the string!"),
    Test("Whitespace", "", [Input("Please enter the main string..\r\n", "Whitespace Check Text With Some 	Tabs	Too"),
                            Input("Please enter the pattern string to find..", " ")],
         "Please enter the main string..\r\nPlease enter the pattern string to find..Whitespace Check Text With Some 	Tabs	Too\n\n \n> WhitespaceCheckTextWithSome	Tabs	Too"),
    Test("Multiple", "", [Input("Please enter the main string..\r\n", "This string is free. This stringis with a word. This is String. sstrtr.."),
                            Input("Please enter the pattern string to find..", "str")],
         "Please enter the main string..\r\nPlease enter the pattern string to find..This string is free. This stringis with a word. This is String. sstrtr..\n\nstr\n> This ing is free. This ingis with a word. This is String. str.."),
    Test("BasicFailure", "", [Input("Please enter the main string..\r\n", "This is my input string."),
                            Input("Please enter the pattern string to find..", "123")],
         "Please enter the main string..\r\nPlease enter the pattern string to find..This is my input string.\n\n123\n> Cannot find the pattern in the string!"),

]

tests = [q1_tests, q2_tests, q3_tests]
