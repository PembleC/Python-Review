"""

8/10/2020
New Relic Code Challenge
Find 100 most common three-word sequences
"""
import sys

number_of_args = len(sys.argv)
print("The number of arguments passed:", number_of_args)
arg_list = str(sys.argv)
print("Argument List: ", arg_list)

file_number = 1
for file_number in range(1,number_of_args):
    print("Reading file:", arg_list[file_number])
    cur_file = open(arg_list[file_number], "r", )

    print(cur_file.readline)

    cur_file.close()






"""
The program accepts as arguments a list of one or more file paths (e.g. ./solution.rb file1.txt file2.txt ...).
The program also accepts input on stdin (e.g. cat file1.txt | ./solution.rb).
The program outputs a list of the 100 most common three-word sequences in the text, along with a count of how many times each occurred in the text. For example: 231 - i will not, 116 - i do not, 105 - there is no, 54 - i know not, 37 - i am not …
The program ignores punctuation, line endings, and is case insensitive (e.g. “I love\nsandwiches.” should be treated the same as "(I LOVE SANDWICHES!!)")
The program is capable of processing large files and runs as fast as possible.
The program should be tested. Provide a test file for your solution.
"""