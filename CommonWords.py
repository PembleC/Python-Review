"""
8/11/2020
New Relic Code Challenge
Find 100 most common three-word sequences
"""

# Program Imports
import sys
import re


# Helper Functions
def removePuncAndSplit(line):
    # Remove the punctuation from the line
    no_punc_line = re.sub(r'[^\w\s]', '', line)
    # Split every three words using regular expressions
    word_seg_list = re.split('((?:\w+(?:\s)){3})', no_punc_line)
    return word_seg_list

def appendToLists(seg_list, sequence):
    # Filter out the blank lines from the list
    results = list(filter(None, seg_list))
    #print("This is results ", results)
    list_length = len(results)
    for seg_num in range(0, list_length):
        # Remove the whitespace
        seq = results[seg_num].strip()
        if seq != '':
            # Append it to my sequences
            sequence.append(seq)
    return

def dictionaryOccurances(results, sequence):
    for phrase_index in range(0, len(sequence)):
        key = sequence[phrase_index]
        if key in results:
            # Increase the counter for that 3-word phrase
            results[key] += 1
        else:
            # Add it to my dictionary
            results[key] = 1
    return


# Main Function
def main():
    # Get the command line arguments
    number_of_args = len(sys.argv)
    print("The number of arguments passed:", number_of_args)
    arg_list = str(sys.argv)
    print("The Arguments List: ", arg_list)

    # If you desire to parse multiple files from command line
    for count in range(1, number_of_args):
        # Create Variables
        sequence_one = []
        sequence_two = []
        sequence_three = []
        first_word = ""
        second_word = ""

        print("Reading file:", sys.argv[count], "\n")
        cur_file = open(sys.argv[count], "r", )

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

            # Gives me all possible 3 word combinations
            line_minus_first = line.replace(first_word,"",1)
            line_minus_second = line_minus_first.replace(second_word,"",1)

            word_seg_list = removePuncAndSplit(line.lower())
            word_seg_list_mf = removePuncAndSplit(line_minus_first.lower())
            word_seg_list_ms = removePuncAndSplit(line_minus_second.lower())

            appendToLists(word_seg_list, sequence_one)
            appendToLists(word_seg_list_mf, sequence_two)
            appendToLists(word_seg_list_ms, sequence_three)


        # Make a dictionary for all 3 word sequences
        final_results = {}

        # Fill from all the possible sequences
        dictionaryOccurances(final_results, sequence_one)
        dictionaryOccurances(final_results, sequence_two)
        dictionaryOccurances(final_results, sequence_three)

        # Sort the dictionary by value
        sorted_phrases = sorted(final_results.items(), key=lambda x: x[1], reverse=True)
        #print(sorted_phrases)

        # Print the phrases and their occurrences
        counter = 0
        for i in sorted_phrases:
            if i[0].count(' ') == 2:
                counter += 1
                print(i[0], " -> ", i[1])
                if counter == 100:
                    break
        print("\n")

        cur_file.close()



if __name__ == "__main__":
    main()


"""
[X] The program accepts as arguments a list of one or more file paths (e.g. ./solution.rb file1.txt file2.txt ...).
[X] The program also accepts input on stdin (e.g. cat file1.txt | ./solution.rb).
[X] The program outputs a list of the 100 most common three-word sequences in the text, along with a count of how many times each occurred in the text. For example: 231 - i will not, 116 - i do not, 105 - there is no, 54 - i know not, 37 - i am not …
[X] The program ignores punctuation, line endings, and is case insensitive (e.g. “I love\nsandwiches.” should be treated the same as "(I LOVE SANDWICHES!!)")
[X] The program is capable of processing large files and runs as fast as possible.
[X] The program should be tested. Provide a test file for your solution.
"""
