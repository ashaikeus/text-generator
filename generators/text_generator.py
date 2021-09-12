import random
from nltk.tokenize import regexp_tokenize
from nltk.util import bigrams


def initialize(filename):
    global tokens, bigram_list, SENTENCE_ENDERS, word
    file = open(filename, "r", encoding="utf-8")
    tokens = []
    for line in file:
        tokens += regexp_tokenize(line, r"\S+")
    bigram_list = list(bigrams(tokens))
    SENTENCE_ENDERS = ".?!"
    word = "."


def start_a_sentence():
    global current_sent_length, word, sentence
    current_sent_length = 0
    while word[0][0] != word[0][0].upper() or word.split()[0][-1] in SENTENCE_ENDERS or word[0][0] == "-":
        word = random.choice(bigram_list)[0]
    sentence = word.split()


def generate():
    global current_sent_length, word, sentence
    start_a_sentence()
    while True:
        current_sent_length += 1
        word_dict = [t[1] for t in bigram_list if t[0] == " ".join(sentence[current_sent_length - 1:current_sent_length + 1])]
        word = "".join(random.choices(word_dict))
        if word[-1] in SENTENCE_ENDERS:
            iters = 0
            if current_sent_length < 5:
                while word[-1] in SENTENCE_ENDERS:
                    word = "".join(random.choices(word_dict))
                    iters += 1
                    if iters > 5:
                        start_a_sentence()
                        break
                if iters > 5:
                    continue
            else:
                sentence.extend(word.split())
                break
        sentence.extend(word.split())
    return " ".join(sentence)
