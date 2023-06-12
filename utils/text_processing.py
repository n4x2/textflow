import re 
import json
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory 
from utils.constants import unnecessary_chars, unwanted_words

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

def remove_unwanted_words(text, unwanted_words):
    """
    Removes unwanted words from the given text.
    
    Args:
        text (str): The input text.
        unwanted_words (list): A list of words to be removed from the text.
    
    Returns:
        str: The text with unwanted words removed.
    """
    return ' '.join(word for word in text.split() if word.lower() not in unwanted_words)

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

def remove_links(text):
    """
    Removes links from the given text.

    Args:
        text (str): The input text containing links.

    Returns:
        str: The text with links removed.

    """
    pattern = re.compile(r"(http[s]?://\S+|www\.\S+|pic.twitter.com/\S+)")
    cleaned_text = re.sub(pattern, "", text)
    return cleaned_text

def remove_hashtag(text):
    """
    Removes hashtags from the given text.
    
    Args:
        text (str): The input text containing hashtags.
    
    Returns:
        str: The text with hashtags removed.
    """
    return re.sub(r'#\w+\b', '', text)

def remove_word_after_at(text):
    """
    Removes words that appear after the @ symbol from the given text.
    
    Args:
        text (str): The input text containing mentions.
    
    Returns:
        str: The text with words after @ symbols removed.
    """
    cleaned_text = re.sub(r'@\w+', '', text)
    return cleaned_text


def normalize(text):
    """
    Normalizes the given text if it contains Indonesian words.

    Args:
        text (str): The input text.

    Returns:
        str or bool: The normalized text if it contains Indonesian words, False otherwise.
    """
    text = lowercase_text(text)                                 # Convert text to lowercase
    text = remove_hashtag(text)                                 # Remove hashtags
    text = remove_word_after_at(text)                           # Remove words after @ symbols
    text = remove_links(text)                                   # Remove links
    text = remove_non_alphanumeric(text)                        # Remove non-alphanumeric characters
    text = remove_unnecessary_chars(text)                       # Remove unnecessary characters
    text = remove_unwanted_words(text, unwanted_words)          # Remove unwanted words
    text = normalize_slang(text)                                # Normalize slang words
    text = stem_text(text)                                      # Stemming
    text = remove_stopwords(text)                               # Remove stopwords
    return text
