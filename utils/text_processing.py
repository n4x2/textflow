import re
import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


def _remove_hashtag(text: str) -> str:
    return re.sub(r'#\w+\b', '', text)


def _remove_mentions(text: str) -> str:
    return re.sub(r'@\w+', '', text)


def _remove_number(text: str) -> str:
    return re.sub(r'\d+', '', text)


def _remove_links(text: str) -> str:
    return re.sub(re.compile(r"(http[s]?://\S+|www\.\S+|pic.twitter.com/\S+)"), "", text)


def _remove_non_alphanumeric(text: str) -> str:
    return re.sub(r'\W+', ' ', text)


def _lowercase_text(text: str) -> str:
    return text.lower()

def _remove_leading_trailing_space(text: str)->str:
    text = re.sub(r'^[\s\n]*([^.]+)[\s\n]*\.', r'\1.', text)
    text = re.sub(r'\.[\s\n]*([^.]+)[\s\n]*$', r'.\1', text)
    return text

def _remove_consecutive_spaces(text: str) -> str:
    return re.sub(r'\s{2,}', ' ', text)


def _remove_stopwords(text: str) -> str:
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()

    return stopword.remove(text)


def normalize_slang_word(text: str) -> str:
    with open('./data/slang.json', 'r') as file:
        slang_dict = json.load(file)

    with open('./data/custom_slang_words.json', 'r') as file:
        additional_slang_dict = json.load(file)

    slangs = {**slang_dict, **additional_slang_dict}

    normalized_text = []
    words = text.split()

    for word in words:
        normalized_word = slangs.get(word.lower(), word)
        normalized_text.append(normalized_word)

    return ' '.join(normalized_text)


def filter_text(text: str) -> str:
    text = _lowercase_text(text)
    text = _remove_hashtag(text)
    text = _remove_mentions(text)
    text = _remove_links(text)
    text = _remove_number(text)
    text = _remove_non_alphanumeric(text)
    text = _remove_consecutive_spaces(text)
    text = _remove_leading_trailing_space(text)
    return text


def stem_text(text: str) -> str:
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    return stemmer.stem(_lowercase_text(text))


def normalize_text(text: str) -> str:
    text = filter_text(text)
    text = normalize_slang_word(text)
    text = _remove_stopwords(text)
    text = stem_text(text)
    return text
