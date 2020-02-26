
import sys
import re
import os.path
from collections import Counter
from string import ascii_lowercase, punctuation, digits


def main():
    if len(sys.argv[1:]) >= 1:
        if os.path.isfile(sys.argv[1]):
            # print("**************************************************")
            # print("*** Welcome to a simple text extraction script ***")
            # print("**************************************************")
            # print("1) Frequency table for alphabetic letters")
            # print("2) Number of words")
            # print("3) Number of unique words")
            # print("4) Most common words")
            # choice = input("Enter the number you want (or the letter 'q' to quit):")
            # print("\n")
            # while choice != "q":
            #     with open(sys.argv[1], "r", encoding="utf8") as file:
            #         call_function(choice, file)
            #     print("\n1) Frequency table for alphabetic letters")
            #     print("2) Number of words")
            #     print("3) Number of unique words")
            #     print("4) Most common words")
            #     choice = input("Enter the number you want (or the letter 'q' to quit):")
            #     print("\n")
            # print("\nThank you for choosing the text extraction script.")
            with open(sys.argv[1], "r", encoding="utf8") as file:
                letter_frequency(file)
                number_of_words(file)
                number_of_unique_words(file)
                common_words(file)
        else:
            print("The file does not exist!")
            sys.exit(1)
    else:
        print("No argument provided. Please provide at least the shakespeare.txt.")
        sys.exit(1)


# def call_function(choice, file):
#     if choice == "1":
#         frequency_alphabetic(file)
#     elif choice == "2":
#         number_of_words(file)
#     elif choice == "3":
#         number_of_unique_words(file)
#     elif choice == "4":
#         common_words(file)
#     else:
#         print("Non valid number! Choose another one.\n")


# print frequency table for alphabetic letters, ordered from the most common to the least
def letter_frequency(file):
    c = Counter(letter for line in file for letter in line.lower() if letter in ascii_lowercase)
    print("Frequency table for alphabetic letters:")
    for letter in c.most_common():
        print(f"{letter[0]} ({letter[1]} occurrences)")


# print the number of words that the text contains, according to some definition of words (884.421)
def number_of_words(file):
    # 1st Implementation
    # c = 0
    # with open("english-words.txt", "r") as word_file:
    #     english_words = set(word.strip().lower() for word in word_file)
    #     for line in file:
    #         for word in line.lower().split():
    #             if word in english_words:
    #                 c += 1
    #
    # 2nd Implementation
    # digits_punct = digits + punctuation + "‘’“”—"
    # remove_digits_punct = str.maketrans('', '', digits_punct)
    # c = Counter(word.translate(remove_digits_punct) for line in file for word in line.lower().split()
    #             if word.startswith("www") != True and word.startswith("http") != True)
    #
    # for key, value in c.items():
    #     print(f"{key} ({value} occurrences)")
    #
    # print(f"The total number of words is {sum(c.values())}")
    shakespeare = file.read()
    doc = shakespeare.replace('\n', ' ')
    doc = re.sub(r"\d", " ", doc)  # remove all digits
    doc = re.sub(r"[^\w\s]", " ", doc)  # remove punctuations

    doc = re.sub(r"\sd\s"," ",doc)
    doc = re.sub(r"\ss\s"," ",doc)
    doc = re.sub(r"\so\s"," ",doc)

    doc = re.sub(r"\s+", " ", doc)  # substitute all spaces with a single space
    doc = doc.lower()
    doc = doc.strip()
    words = doc.split()

    c = Counter(words)
    #print(f"The total number of words is {sum(c.values())}")
    print(f"The number of words that the text contains: {len(words)}")


# print the number of unique words that the text contains, according to this definition (28.829)
def number_of_unique_words(file):
    # 1st Implementation
    # with open("english-words.txt", "r") as word_file:
    #     english_words = set(word.strip().lower() for word in word_file)
    #     c = Counter(word for line in file for word in line.lower().split() if word in english_words)
    #     print(f"The number of unique words is {len(c)}")
    # 2nd Implementation
    # digits_punct = digits + punctuation + "’“”—"
    # remove_digits_punct = str.maketrans('', '', digits_punct)
    # c = Counter(word.translate(remove_digits_punct) for line in file for word in line.lower().split())
    # print(f"The number of unique words is {len(c)}")
    shakespeare = file.read()
    doc = shakespeare.replace('\n', ' ')
    doc = re.sub(r"\d", " ", doc)  # remove all digits
    doc = re.sub(r"[^\w\s]", " ", doc)  # remove punctuations

    doc = re.sub(r"\sd\s", " ", doc)
    doc = re.sub(r"\ss\s", " ", doc)
    doc = re.sub(r"\so\s", " ", doc)

    doc = re.sub(r"\s+", " ", doc)  # substitute all spaces with a single space
    doc = doc.lower()
    doc = doc.strip()
    words = doc.split()

    c = Counter(words)
    print(f"The number of unique words is {len(c)}")
    # print(f"The number of unique words that the text contains: {len(set(words))}")


# print five most common words with their frequency + words that commonly follow them
# (3 per word, ordered, number of occurrences)
# Should be the following table:
# the : 28.944
# and : 27.317
# i : 21.120
# to : 20.136
# of : 17.181
def common_words(file):
    # 1st Implementation
    # with open("english-words.txt", "r") as word_file:
    #     english_words = set(word.strip().lower() for word in word_file)
    #     c = Counter(word for line in file for word in line.lower().split() if word in english_words)
    #     print("The five most common words are: ")
    #     sorted_most_common = c.most_common()
    #     for i in range(5):
    #         print(f"{sorted_most_common[i][0]} ({sorted_most_common[i][1]} occurrences)")
    #
    # 2nd Implementation
    # digits_punct = digits + punctuation + "’“”—"
    # remove_digits_punct = str.maketrans('', '', digits_punct)
    # c = Counter(word.translate(remove_digits_punct) for line in file for word in line.lower().split())
    # print("The five most common words are: ")
    # sorted_most_common = c.most_common()
    # for i in range(5):
    #     print(f"{sorted_most_common[i][0]} ({sorted_most_common[i][1]} occurrences)")
    shakespeare = file.read()
    doc = shakespeare.replace('\n', ' ')
    doc = re.sub(r"\d", " ", doc)  # remove all digits
    doc = re.sub(r"[^\w\s]", " ", doc)  # remove punctuations

    doc = re.sub(r"\sd\s", " ", doc)
    doc = re.sub(r"\ss\s", " ", doc)
    doc = re.sub(r"\so\s", " ", doc)

    doc = re.sub(r"\s+", " ", doc)  # substitute all spaces with a single space
    doc = doc.lower()
    doc = doc.strip()
    words = doc.split()

    c = Counter(words)
    five_most_common = dict(c.most_common(5))

    for key, value in five_most_common.items():
        rx = r'%s (\w+ ){1}' % key
        prog = re.compile(rx)
        c2 = Counter(prog.findall(doc))
        three_most_common = dict(c2.most_common(3))
        print(f"{key} ({value} occurrences)")
        for key, value in three_most_common.items():
            print(f"-- {key}, {value}")


if __name__ == '__main__':
    main()
