# Sentencer

A program to extract translatable sentences from a corpus,
based on a known vocabulary.

The vocabulary is stored in a CSV file.

## Corpus resources

- [Project Gutenberg](https://www.gutenberg.org/)
- [Lingua](https://lingua.com/english/reading/my-day/)

## Getting started

(NB. You might want to set up a virtualenv first)

    pip install -r requirements.txt
    pip install -r requirements_dev.txt
    python scripts/nltk_download.py

Run the tests:

    pytest

Run the program:

    python sentencer/main.py my-day

