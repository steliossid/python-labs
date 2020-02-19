# If no such argument, print error message (not just an exception raised)
# If second argument (a file name), output should be written to that file
# If file does not exist, print "The file does not exist!" (ie not just crash)

from collections import Counter
from string import ascii_lowercase


def main():
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
        with open("shakespeare.txt", "r", encoding="utf8") as file:
            call_function(choice, file)
        print("\n1) Frequency table for alphabetic letters")
        print("2) Number of words")
        print("3) Number of unique words")
        print("4) Most common words")
        choice = input("Enter the number you want (or the letter 'q' to quit):")
        print("\n")
    print("\nThank you for choosing the text extraction script.")


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
        print(f"{letter[0]} : {letter[1]}")


# print the number of words that the text contains, according to some definition of words
def number_of_words(file):
    c = 0
    for line in file:
        line = line.lower()
        for word in line.split():
            c += 1
    print(f"The total number of words is {c}")


# print the number of unique words that the text contains, according to this definition
def number_of_unique_words(file):
    pass


# print five most common words with their frequency + words that commonly follow them
# (3 per word, ordered, number of occurrences)
def common_words(file):
    pass


if __name__ == '__main__':
    main()
