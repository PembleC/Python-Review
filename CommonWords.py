"""

8/10/2020
New Relic Code Challenge
Find 100 most common three-word sequences
"""
import sys
import re

number_of_args = len(sys.argv)
print("The number of arguments passed:", number_of_args)
arg_list = str(sys.argv)
print("The Arguments List: ", arg_list)

for count in range(1, number_of_args):  # If you desire to parse multiple files
    # if count == 0:
    #     print("nothing to do for THIS file")
    #     continue

    print("Reading file:", sys.argv[count])
    cur_file = open(sys.argv[count], "r", )

    sequence_one = []
    sequence_two = []
    sequence_zero = []

    line_num = 0
    for line in cur_file:
        #print("Line: ", line_num)
        line_num += 1
        word_num = 0

        # Remove the punctuation from the line
        no_punc_line = re.sub(r'[^\w\s]', '', line.lower())
        #print(no_punc_line)

        # Split every three words
        word_seg_list = re.split('((?:\w+(?:\s)){3})', no_punc_line)

        # Filter out the blank lines
        results = list(filter(None, word_seg_list))
        #print(results)
        list_length = len(results)

        for seg_num in range(0, list_length):
            #print(results[seg_num].rstrip())
            sequence_one.append(results[seg_num].rstrip())






        #print("\n")



    #     for word in line.split():
    #         #print("Word: ", word_num)
    #         word_num += 1
    #         #print(word_num % 3)
    #         if (word_num % 3 == 1):
    #             sequence_one.append(word.lower())
    #         elif (word_num % 3 == 2):
    #             sequence_two.append(word.lower())
    #         elif (word_num % 3 == 0):
    #             sequence_zero.append(word.lower())
    #
    #         print(word)


    print("\n")
    print("Sequence one is: ", sequence_one)
    print("\n")
    # print(sequence_two)
    # print("\n")
    # print(sequence_zero)
    # print("\n")




    # Make a dictionary for all 3 word sequences
    final_results = {}
    for phrase_index in range(0, len(sequence_one)):
        #print("looking at", phrase_index, "for:", sequence_one[phrase_index])
        if sequence_one[phrase_index] not in final_results:
            # Count how many times each phrase is used
            occurrences = sequence_one.count(sequence_one[phrase_index])
            #print(occurrences)
            final_results[sequence_one[phrase_index]] = occurrences

    print(final_results)

    # sort the keys according to the values:
    #sorted_names = sorted(scores, key=scores.__getitem__)
    #for k in sorted_names:
    #print("{} : {}".format(k, scores[k]))






    cur_file.close()






"""
[X] The program accepts as arguments a list of one or more file paths (e.g. ./solution.rb file1.txt file2.txt ...).
[] The program also accepts input on stdin (e.g. cat file1.txt | ./solution.rb).
[] The program outputs a list of the 100 most common three-word sequences in the text, along with a count of how many times each occurred in the text. For example: 231 - i will not, 116 - i do not, 105 - there is no, 54 - i know not, 37 - i am not …
[X] The program ignores punctuation, line endings, and is case insensitive (e.g. “I love\nsandwiches.” should be treated the same as "(I LOVE SANDWICHES!!)")
[X] The program is capable of processing large files and runs as fast as possible.
[] The program should be tested. Provide a test file for your solution.
"""
