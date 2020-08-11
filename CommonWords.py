"""
8/11/2020
New Relic Code Challenge
Find 100 most common three-word sequences
"""

import sys
import re

# Get the command line arguments
number_of_args = len(sys.argv)
print("The number of arguments passed:", number_of_args)
arg_list = str(sys.argv)
print("The Arguments List: ", arg_list)

for count in range(1, number_of_args):  # If you desire to parse multiple files

    print("Reading file:", sys.argv[count])
    cur_file = open(sys.argv[count], "r", )

    sequence_one = []
    sequence_two = []
    sequence_three = []

    first_word = ""
    second_word = ""

    line_num = 0
    for line in cur_file:
        word_num = 0
        for word in line.split():
            if word_num > 1:
                continue
            elif word_num == 0:
                first_word = word
            elif word_num == 1:
                second_word = word
            word_num += 1
        line_num += 1

        line_minus_first = line.replace(first_word,"",1)
        line_minus_second = line_minus_first.replace(second_word,"",1)


        #removePuncAndSplit(line)

        # Remove the punctuation from the line
        no_punc_line = re.sub(r'[^\w\s]', '', line.lower())
        no_punc_line_mf = re.sub(r'[^\w\s]', '', line_minus_first.lower())
        no_punc_line_ms = re.sub(r'[^\w\s]', '', line_minus_second.lower())
        #print(no_punc_line)

        # Split every three words using regular expressions
        word_seg_list = re.split('((?:\w+(?:\s)){3})', no_punc_line)
        word_seg_list_mf = re.split('((?:\w+(?:\s)){3})', no_punc_line_mf)
        word_seg_list_ms = re.split('((?:\w+(?:\s)){3})', no_punc_line_ms)
        #print(word_seg_list)


        # Filter out the blank lines from the list
        results = list(filter(None, word_seg_list))
        results_mf = list(filter(None, word_seg_list_mf))
        results_ms = list(filter(None, word_seg_list_ms))
        #print(results)

        list_length = len(results)
        list_length_mf = len(results_mf)
        list_length_ms = len(results_ms)

        for seg_num in range(0, list_length):
            #print(results[seg_num].rstrip())
            sequence_one.append(results[seg_num].rstrip())

        for seg_num in range(0, list_length_mf):
            #print(results[seg_num].rstrip())
            sequence_two.append(results_mf[seg_num].rstrip())

        for seg_num in range(0, list_length_ms):
            #print(results[seg_num].rstrip())
            sequence_three.append(results_ms[seg_num].rstrip())



    # Make a dictionary for all 3 word sequences
    final_results = {}
    for phrase_index in range(0, len(sequence_one)):
        #print("looking at", phrase_index, "for:", sequence_one[phrase_index])
        if sequence_one[phrase_index] not in final_results:
            # Count how many times each phrase is used
            occurrences = sequence_one.count(sequence_one[phrase_index])
            #print(occurrences)
            final_results[sequence_one[phrase_index]] = occurrences

    for phrase_index in range(0, len(sequence_two)):
        if sequence_two[phrase_index] not in final_results:
            # Count how many times each phrase is used
            occurrences = sequence_two.count(sequence_two[phrase_index])
            #print(occurrences)
            final_results[sequence_two[phrase_index]] = occurrences

    for phrase_index in range(0, len(sequence_three)):
        if sequence_three[phrase_index] not in final_results:
            # Count how many times each phrase is used
            occurrences = sequence_three.count(sequence_three[phrase_index])
            #print(occurrences)
            final_results[sequence_three[phrase_index]] = occurrences


    # Sort the dictionary by value
    sorted_phrases = sorted(final_results.items(), key=lambda x: x[1], reverse=True)

    # Print the phrases and their occurrences
    for i in sorted_phrases:
        print(i[0], "\t->\t" ,i[1])






    cur_file.close()






"""
[X] The program accepts as arguments a list of one or more file paths (e.g. ./solution.rb file1.txt file2.txt ...).
[] The program also accepts input on stdin (e.g. cat file1.txt | ./solution.rb).
[] The program outputs a list of the 100 most common three-word sequences in the text, along with a count of how many times each occurred in the text. For example: 231 - i will not, 116 - i do not, 105 - there is no, 54 - i know not, 37 - i am not …
[X] The program ignores punctuation, line endings, and is case insensitive (e.g. “I love\nsandwiches.” should be treated the same as "(I LOVE SANDWICHES!!)")
[X] The program is capable of processing large files and runs as fast as possible.
[] The program should be tested. Provide a test file for your solution.
"""
