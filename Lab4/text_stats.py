# If second argument (a file name), output should be written to that file

import sys
import os.path
from collections import Counter
from string import ascii_lowercase, punctuation, digits


def main():
    if len(sys.argv[1:]) >= 1:
        if os.path.isfile(sys.argv[1]):
            print("**************************************************")
            print("*** Welcome to a simple text extraction script ***")
            print("**************************************************")
            print("1) Frequency table for alphabetic letters")
            print("2) Number of words")
            print("3) Number of unique words")
            print("4) Most common words")
            choice = input("Enter the number you want (or the letter 'q' to quit):")
            print("\n")
            while choice != "q":
                with open(sys.argv[1], "r", encoding="utf8") as file:
                    call_function(choice, file)
                print("\n1) Frequency table for alphabetic letters")
                print("2) Number of words")
                print("3) Number of unique words")
                print("4) Most common words")
                choice = input("Enter the number you want (or the letter 'q' to quit):")
                print("\n")
            print("\nThank you for choosing the text extraction script.")
        else:
            print("The file does not exist!")
            sys.exit(1)
    else:
        print("No argument provided. Please provide at least the shakespeare.txt.")
        sys.exit(1)


def call_function(choice, file):
    if choice == "1":
        frequency_alphabetic(file)
    elif choice == "2":
        number_of_words(file)
    elif choice == "3":
        number_of_unique_words(file)
    elif choice == "4":
        common_words(file)
    else:
        print("Non valid number! Choose another one.\n")


# print frequency table for alphabetic letters, ordered from the most common to the least
def frequency_alphabetic(file):
    c = Counter(letter for line in file for letter in line.lower() if letter in ascii_lowercase)
    print("Frequency table for alphabetic letters:")
    for letter in c.most_common():
        print(f"{letter[0]} ({letter[1]} occurrences)")


# print the number of words that the text contains, according to some definition of words
# Should be 884.421 total words
def number_of_words(file):
    # c = 0
    # with open("english-words.txt", "r") as word_file:
    #     english_words = set(word.strip().lower() for word in word_file)
    #     for line in file:
    #         for word in line.lower().split():
    #             if word in english_words:
    #                 c += 1
    digits_punct = digits + punctuation + "‘’“”—"
    remove_digits_punct = str.maketrans('', '', digits_punct)
    c = Counter(word.translate(remove_digits_punct) for line in file for word in line.lower().split())

    # for key, value in c.items():
    #     print(f"{key} ({value} occurrences)")

    print(f"The total number of words is {sum(c.values())}")


# print the number of unique words that the text contains, according to this definition
# Should be 28.829 unique word forms
def number_of_unique_words(file):
    # with open("english-words.txt", "r") as word_file:
    #     english_words = set(word.strip().lower() for word in word_file)
    #     c = Counter(word for line in file for word in line.lower().split() if word in english_words)
    #     print(f"The number of unique words is {len(c)}")
    digits_punct = digits + punctuation + "’“”—"
    remove_digits_punct = str.maketrans('', '', digits_punct)
    c = Counter(word.translate(remove_digits_punct) for line in file for word in line.lower().split())

    print(f"The number of unique words is {len(c)}")


# print five most common words with their frequency + words that commonly follow them
# (3 per word, ordered, number of occurrences)
# Should be the following table:
# the : 28.944
# and : 27,317
# i : 21,120
# to : 20,136
# of : 17,181
def common_words(file):
    # with open("english-words.txt", "r") as word_file:
    #     english_words = set(word.strip().lower() for word in word_file)
    #     c = Counter(word for line in file for word in line.lower().split() if word in english_words)
    #     print("The five most common words are: ")
    #     sorted_most_common = c.most_common()
    #     for i in range(5):
    #         print(f"{sorted_most_common[i][0]} ({sorted_most_common[i][1]} occurrences)")
    digits_punct = digits + punctuation + "’“”—"
    remove_digits_punct = str.maketrans('', '', digits_punct)
    c = Counter(word.translate(remove_digits_punct) for line in file for word in line.lower().split())
    print("The five most common words are: ")
    sorted_most_common = c.most_common()
    for i in range(5):
        print(f"{sorted_most_common[i][0]} ({sorted_most_common[i][1]} occurrences)")


if __name__ == '__main__':
    main()
