import re 
import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory 
from utils.constants import unnecessary_chars 

def lowercase_text(text):
    """
    Converts the text to lowercase.

    Args:
        text (str): The input text.

    Returns:
        str: The text converted to lowercase.
    """
    return text.lower()

def stem_text(text):
    """
    Stems the text using the Sastrawi stemmer.

    Args:
        text (str): The input text.

    Returns:
        str: The stemmed text.
    """
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()  
    return stemmer.stem(text)

def remove_stopwords(text):
    """
    Removes stopwords from the text.

    Args:
        text (str): The input text.

    Returns:
        str: The text with stopwords removed.
    """
    with open('./data/stopwords.json', 'r') as file:
        stop_words = json.load(file)
    return ' '.join(word for word in text.split() if word.lower() not in stop_words)

def remove_non_alphanumeric(text):
    """
    Removes non-alphanumeric characters from the text.

    Args:
        text (str): The input text.

    Returns:
        str: The text with non-alphanumeric characters removed.
    """
    return re.sub(r'\W+|\d+', ' ', text)

def remove_unnecessary_chars(text):
    """
    Removes unnecessary characters from the text.

    Args:
        text (str): The input text.

    Returns:
        str: The text with unnecessary characters removed.
    """
    return ''.join(char for char in text if char not in unnecessary_chars)

def normalize_slang(text):
    """
    Normalizes slang words in the text.

    Args:
        text (str): The input text.

    Returns:
        str: The text with slang words normalized.
    """
    with open('./data/kamus_alay.json', 'r') as file:
        slang_dict = json.load(file)
        
    normalized_text = []
    words = text.split()
    
    for word in words:
        normalized_word = slang_dict.get(word.lower(), word)
        normalized_text.append(normalized_word)
    
    return ' '.join(normalized_text)

def normalize(text):
    """
    Normalizes the given text if it contains Indonesian words.

    Args:
        text (str): The input text.

    Returns:
        str or bool: The normalized text if it contains Indonesian words, False otherwise.
    """
    text = lowercase_text(text)               # Convert text to lowercase
    text = remove_unnecessary_chars(text)     # Remove unnecessary characters
    text = remove_non_alphanumeric(text)      # Remove non-alphanumeric characters
    text = normalize_slang(text)              # Normalize slang words
    text = stem_text(text)                    # Stemming
    text = remove_stopwords(text)             # Remove stopwords
    return text
