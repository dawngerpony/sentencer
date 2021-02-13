from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

import argparse
import csv
import functools
import operator

VOCAB_FILENAME: str = "vocabulary.csv"


def vocab_filter(sentences: list, vocab: set) -> list:
    """
    Only return sentences that contain at least one word from the vocabulary.
    :param sentences:
    :param vocab:
    :return: a list of sentences filtered by words in the dictionary
    """
    filtered_list = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        tagged_sentence = pos_tag(words)
        words_no_proper_nouns = [word for (word, tag) in tagged_sentence if tag != "NNP"]
        words = [word.lower() for word in words_no_proper_nouns if word.isalpha()]
        # words = [word.lower() for word in words if word.isalpha()]
        if len(words) > 0 and all(word in vocab for word in words):
            filtered_list.append(sentence)
    return filtered_list


def clean(sentences: list) -> list:
    """
    Clean up sentences by removing newlines.
    :param sentences:
    :return:
    """
    cleaned = [sentence.replace("\n", " ") for sentence in sentences]
    return cleaned


def extract_sentences(text: str) -> list:
    """
    Extract the sentences from a text string.
    :param text:
    :return:
    """
    sentences = sent_tokenize(text)
    return sentences


def load_corpus(filename: str) -> str:
    """
    Read the text from a file into a string.
    :type filename: str
    :param filename:
    :return:
    """
    with open(filename) as f:
        text = f.read()
    return text


def load_vocab(filename: str) -> set:
    """
    Load CSV vocabulary from file.
    :param filename:
    :return:
    """
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    # flatten 2D vocab list into a single list of words
    words = functools.reduce(operator.iconcat, rows, [])
    # convert each word to lowercase
    words = set(map(str.lower, words))
    return words


def main(vocab_filename: str) -> None:
    # Get the name of the desired corpus from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus")
    args = parser.parse_args()
    text_filename = f"corpus/{args.corpus}.txt"

    # Load the desired corpus and vocabulary from disk
    corpus = load_corpus(text_filename)
    vocab = load_vocab(vocab_filename)

    # Extract sentences from the corpus
    sentences = extract_sentences(corpus)
    # print(f"{len(sentences)} sentences were extracted from the text.", file=sys.stderr)
    output = vocab_filter(clean(sentences), vocab)
    # print(f"{len(output)} matching sentence(s) were discovered:", file=sys.stderr)
    # print()
    for i, sentence in enumerate(output):
        # print(f"{i+1}: {sentence}")
        print(sentence)


if __name__ == "__main__":
    main(VOCAB_FILENAME)
