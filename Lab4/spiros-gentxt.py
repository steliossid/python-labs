import numpy as np
import time
import sys
import collections
import text_stats


def main():
    with open(sys.argv[1], "r", encoding="utf8") as file:
        doc = text_stats.data_processing(file)
    sentence = generate_random_sentence(doc)
    print(sentence)


def give_next_word(possible_words):
    """argument: a counter/dictionary that has the possible words
    return: the chosen"""
    possible_words = collections.OrderedDict(possible_words)  # keep the order of the dictionary
    word_occ = np.fromiter(possible_words.values(),
                           dtype=float)  # maybe give double weight no most freq words by mupliplying by 2
    prob_occ = word_occ / sum(word_occ)  # the probabilities of each word to be after
    ref_dict = dict(
        zip(range(1, len(possible_words) + 1), possible_words.keys()))  # dict(zip(cntr.keys(), range(1,len(cntr)+1)))
    indx = np.random.choice(a=np.array(range(1, len(possible_words) + 1)), p=prob_occ)  # get a weigted random next word
    nxt_word = ref_dict[indx]
    return nxt_word


def generate_random_sentence(doc):
    ith_word = 1
    max_wrds = int(sys.argv[3])
    current_word = sys.argv[2]
    gen_text = current_word
    possible_words = [0, 0]
    words = doc.split()

    if current_word in words:
        while len(possible_words) >= 1 and ith_word < max_wrds:
            possible_words = text_stats.find_successors(doc, current_word)
            nxt = give_next_word(possible_words)
            gen_text = gen_text + " " + nxt[:-1]
            current_word = nxt[:-1]
            ith_word += 1

    return gen_text


if __name__ == '__main__':
    start_time = time.time()
    main()
    passed_time = round(time.time() - start_time)
    print(f"{passed_time} seconds")
