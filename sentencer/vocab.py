from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()


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
        words_no_proper_nouns = [(word, tag) for (word, tag) in tagged_sentence if tag != "NNP"]
        words = [(word.lower(), tag) for (word, tag) in words_no_proper_nouns if word.isalpha()]
        lemmas = set()
        for word, tag in words:
            pos = "n"
            if tag[0] == "V":
                pos = "v"
            lemma = lemmatizer.lemmatize(word, pos=pos)
            lemmas.add(lemma)
        if len(lemmas) > 0 and all(lemma in vocab for lemma in lemmas):
            filtered_list.append(sentence)
    return filtered_list


def extract_sentences(text: str) -> list:
    """
    Extract the sentences from a text string.
    :param text:
    :return:
    """
    return sent_tokenize(text)
