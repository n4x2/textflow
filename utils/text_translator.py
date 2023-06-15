from googletrans import Translator


def translate_text(text: str, src_lang: str, dest_lang: str) -> str:
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text.lower()
