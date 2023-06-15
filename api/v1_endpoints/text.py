from fastapi import APIRouter, Path
from schemas.text import TextRequest
from schemas.response import StandardResponse
from utils.text_translator import translate_text
from utils.text_processing import stem_text, normalize_text, filter_text, normalize_slang_word

router = APIRouter()


@router.post('/tokenize', response_model=StandardResponse)
def tokenize_sentence(payload: TextRequest):
    try:
        if not payload.text:
            raise ValueError("Empty request. Please provide a text.")

        tokenized_text = payload.text.split()
        return StandardResponse(success=True, message="Text tokenized successfully", data={"tokenized": tokenized_text})

    except ValueError as ve:
        return StandardResponse(success=False, message=str(ve), error_code=400)

    except Exception as e:
        return StandardResponse(success=False, message=str(e), error_code=500)


@router.post('/translate/{src_lang}/{dest_lang}', response_model=StandardResponse)
def translate_sentence(payload: TextRequest, src_lang: str = Path(...), dest_lang: str = Path(...)):
    try:
        if not payload.text:
            raise ValueError("Empty request. Please provide a text.")

        translation = translate_text(payload.text, src_lang, dest_lang)
        return StandardResponse(success=True, message="Text successfully translated", data={"translation": translation})

    except ValueError as ve:
        return StandardResponse(success=False, message=str(ve), error_code=400)

    except Exception as e:
        return StandardResponse(success=False, message=str(e), error_code=500)


@router.post('/stem', response_model=StandardResponse)
def stem_sentence(payload: TextRequest):
    try:
        if not payload.text:
            raise ValueError("Empty request. Please provide a text.")

        stemmed_text = stem_text(payload.text)
        return StandardResponse(success=True, message="Text successfully stemmed", data={"stemmed_text": stemmed_text})

    except ValueError as ve:
        return StandardResponse(success=False, message=str(ve), error_code=400)

    except Exception as e:
        return StandardResponse(success=False, message=str(e), error_code=500)


@router.post('/filter', response_model=StandardResponse)
def filter_sentence(payload: TextRequest):
    try:
        if not payload.text:
            raise ValueError("Empty request. Please provide a text.")

        clean_text = filter_text(payload.text)
        return StandardResponse(success=True, message="Text successfully cleaned", data={"clean_text": clean_text})

    except ValueError as ve:
        return StandardResponse(success=False, message=str(ve), error_code=400)

    except Exception as e:
        return StandardResponse(success=False, message=str(e), error_code=500)


@router.post('/slang', response_model=StandardResponse)
def filter_sentence(payload: TextRequest):
    try:
        if not payload.text:
            raise ValueError("Empty request. Please provide a text.")

        normalized_text = normalize_slang_word(payload.text)
        return StandardResponse(success=True, message="Text successfully cleaned", data={"normalized_text": normalized_text})

    except ValueError as ve:
        return StandardResponse(success=False, message=str(ve), error_code=400)

    except Exception as e:
        return StandardResponse(success=False, message=str(e), error_code=500)


@router.post('/normalize', response_model=StandardResponse)
def normalize_sentence(payload: TextRequest):
    try:
        if not payload.text:
            raise ValueError("Empty request. Please provide a text.")

        normalized_text = normalize_text(payload.text)
        return StandardResponse(success=True, message="Text successfully normalized", data={"normalized_text": normalized_text})

    except ValueError as ve:
        return StandardResponse(success=False, message=str(ve), error_code=400)

    except Exception as e:
        return StandardResponse(success=False, message=str(e), error_code=500)
