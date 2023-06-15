import json
import csv
import os
import re


def _init_kbbi() -> list:
    keywords = []
    with open("./data/kbbi/katakunci.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            keyword = row[0].strip()
            keywords.append(keyword)
    return keywords


def _extract_non_matching_words(sentence: str, keywords: list) -> list:
    words = sentence.split()
    non_matching_words = [word for word in words if word not in keywords]
    return non_matching_words


def _remove_words(sentence: str, words: list) -> str:
    return re.sub(r'\b(?:{})\b'.format('|'.join(map(re.escape, words))), '', sentence)


def filter_and_remove(text: str) -> str:
    non_matching_words = _extract_non_matching_words(text, _init_kbbi())
    if non_matching_words:
        json_file_path = './data/dump/unknown_words.json'
        existing_words = []
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as json_file:
                existing_words = json.load(json_file)
        unique_words = list(set(existing_words + non_matching_words))
        with open(json_file_path, 'w') as json_file:
            json.dump(unique_words, json_file, ensure_ascii=False, indent=4)
    return _remove_words(text, non_matching_words)
