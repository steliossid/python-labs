#!/usr/bin/env python3
import sys
import re
import os.path
from collections import Counter


def main():
    if len(sys.argv[1:]) >= 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], "r", encoding="utf8") as file:
                doc = data_processing(file)
            print_letter_frequency(doc)
            print("\n")
            print_number_of_words(doc)
            print("\n")
            print_number_of_unique_words(doc)
            print("\n")
            print_common_words(doc)
        else:
            print("The file does not exist!")
            sys.exit(1)
    else:
        print("No argument provided. Please provide at least the shakespeare.txt.")
        sys.exit(1)


def output_log(line):
    """
    Print a line and if output file argument is given, write that line to the file

    Arguments:
    line: A type string variable
    """
    print(line)
    if len(sys.argv[1:]) == 2:
        with open(sys.argv[2], "a", encoding="utf8") as output:
            output.write(line + "\n")


def data_processing(file):
    """Clean a txt and keep only words seperated by commas

    Arguments:
    file : the file that will clean

    Returns:
    doc (str): The cleaned text in a string
    """
    doc = file.read()
    doc = doc.replace('\n', ' ')
    doc = re.sub(r"\d", " ", doc)  # remove all digits
    doc = re.sub(r"[^\w\s]", " ", doc)  # remove punctuations

    doc = re.sub(r"[_]", " ", doc)
    doc = re.sub(r"\sd\s", " ", doc)
    doc = re.sub(r"\ss\s", " ", doc)
    doc = re.sub(r"\so\s", " ", doc)

    doc = re.sub(r"\s+", " ", doc)  # substitute all spaces with a single space
    doc = doc.lower()
    doc = doc.strip()
    return doc


def print_letter_frequency(doc):
    """
    Calculates how many times each letter appears in the text

    Arguments:
    doc (str): The cleaned text in a string
    """
    doc2 = tuple(re.sub(r'\s+', "", doc))
    c = Counter(doc2)
    title = "Frequency table for alphabetic letters:"
    output_log(title)
    for letter in c.most_common():
        content = f"{letter[0]} ({letter[1]} occurrences)"
        output_log(content)


def print_number_of_words(doc):
    """
    Calculates how many words there are in the text in total

    Arguments:
    doc (str): The cleaned text in a string
    """
    words = doc.split()
    c = Counter(words)
    content = f"The total number of words is {sum(c.values())}"
    output_log(content)


def print_number_of_unique_words(doc):
    """
    Calculates how many unique words there are in the text

    Arguments:
    doc (str): The cleaned text in a string
    """
    words = doc.split()
    c = Counter(words)
    content = f"The number of unique words is {len(c)}"
    output_log(content)


def find_successors(text, word):
    """Find the successors

    Arguments:
    text (str): the text that will search in
    word (str): a word of the text to find the next possible words

    Returns:
    possible_words (dict): The next possible words with their frequency in a dictionary
    """
    rx = r'%s (\w+ ){1}' % word
    prog = re.compile(rx)
    possible_words = Counter(prog.findall(text))
    return possible_words

def print_common_words(doc):
    """
    Finds the five most common words and the three most common successors of these five words.

    Arguments:
    doc (str): The cleaned text in a string
    """
    words = doc.split()
    c = Counter(words)
    five_most_common = dict(c.most_common(5))
    title = "The five most common words are: "
    output_log(title)
    for key, value in five_most_common.items():
        c2 = find_successors(doc, key)
        three_most_common = dict(c2.most_common(3))
        content = f"{key} ({value} occurrences)"
        output_log(content)
        for key, value in three_most_common.items():
            content2 = f"-- {key}, {value}"
            output_log(content2)


if __name__ == '__main__':
    main()
