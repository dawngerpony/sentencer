# Sentencer

A program to extract translatable sentences from a corpus,
based on a known vocabulary.

The vocabulary is stored in a CSV file.

## Corpus resources

- [Project Gutenberg](https://www.gutenberg.org/) - a great place for public domain works
- [Lingua](https://lingua.com/english/reading/my-day/) - simple short English paragraphs for people learning English. The source of some of the texts in [corpus](./corpus).
- [1000 most common words in English](https://www.ef.co.uk/english-resources/english-vocabulary/top-1000-words/) - a good starting point for a vocabulary, perhaps. The source of [vocabulary-1000.csv](./vocabulary-1000.csv).

## Getting started

(NB. You might want to set up a virtualenv first)

    pip install -r requirements.txt
    pip install -r requirements_dev.txt
    python scripts/nltk_download.py

Run the tests:

    flake8
    pytest

Run the program on a sample corpus:

    python sentencer/main.py my-day

