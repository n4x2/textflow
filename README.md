# textflow
Text Preprocessing

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [API Endpoint](#api-endpoint)

## Introduction

Textflow transform raw text data into a format suitable for further analysis or modeling.

The main features of this project include:
- Lowercasing of text to ensure consistency and remove case sensitivity.
- Filtering of non-alphanumeric characters and unnecessary characters.
- Normalization of slang words to their standard forms.
- Stemming to reduce words to their base or root form.
- Stopword removal to eliminate common words that do not carry significant meaning.


## Installation
1. Clone the repository: `git clone https://github.com/n4x2/textflow.git`
2. Navigate to the project directory: `cd textflow`
3. Install the required packages: `pip install -r requirements.txt`
4. Run: `uvicorn main:app --reload`

## API Endpoint

This project provide API endpoints:

### Normalize Text

**Endpoint:** `/normalize`

**Method:** POST

**Request:**

```json
{
  "text": "raw text"
}
```

