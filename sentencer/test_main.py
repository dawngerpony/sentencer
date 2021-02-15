from sentencer import main

SENTENCES = [
    "This is my rifle.",
    "There are many others like it but this one is mine.",
]


def test_clean_should_return_clean_sentence():
    sentences = [SENTENCES[0].replace(" ", "\n")]
    expected = [SENTENCES[0]]
    assert main.clean(sentences) == expected


def test_clean_no_newlines_should_return_clean_sentence():
    assert main.clean(SENTENCES) == SENTENCES


def test_clean_empty_input_should_return_empty_list():
    assert main.clean([]) == []
