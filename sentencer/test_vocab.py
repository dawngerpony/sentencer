from .vocab import vocab_filter, extract_sentences

SENTENCES = [
    "This is my rifle.",
    "There are many others like it but this one is mine.",
]


def test_vocab_filter_happy_path_should_return_one_sentence():
    vocab = {"this", "be", "my", "rifle"}
    actual = vocab_filter(SENTENCES, vocab)
    expected = [SENTENCES[0]]
    assert actual == expected


def test_vocab_filter_empty_params_should_return_empty_list():
    assert vocab_filter([], {}) == []


def test_vocab_filter_no_match_should_return_empty_list():
    assert vocab_filter(SENTENCES, {"banana"}) == []


def test_vocab_filter_on_no_word_sentence_should_return_empty_list():
    """ Discovered in the Peter Pan text. """
    assert vocab_filter(["1.F.3."], {"test", "vocab"}) == []


def test_vocab_filter_with_proper_noun_should_return_sentence():
    sentences = ["This is John's rifle."]
    vocab = {"this", "be", "rifle"}
    assert vocab_filter(sentences, vocab) == sentences


def test_vocab_filter_with_lemmas():
    sentences = ["These are John's books."]
    vocab = {"these", "be", "book"}
    assert vocab_filter(sentences, vocab) == sentences


def test_extract_sentences_should_return_two_sentences():
    corpus = f"{SENTENCES[0]} {SENTENCES[1]}"
    expected = [SENTENCES[0], SENTENCES[1]]
    assert extract_sentences(corpus) == expected


def test_extract_sentences_empty_params_should_return_empty_list():
    assert extract_sentences("") == []
