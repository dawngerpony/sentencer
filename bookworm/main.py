from vocab import vocab_filter, extract_sentences

import argparse
import csv
import functools
import operator

VOCAB_FILENAME: str = "vocabulary.csv"


def clean(sentences: list) -> list:
    """
    Clean up sentences by removing newlines.
    :param sentences:
    :return:
    """
    cleaned = [sentence.replace("\n", " ") for sentence in sentences]
    return cleaned


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

    # pass through the vocabulary filter
    output = vocab_filter(clean(sentences), vocab)
    for sentence in output:
        print(sentence)


if __name__ == "__main__":
    main(VOCAB_FILENAME)
