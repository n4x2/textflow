# TextFlow

TextFlow transform raw Indonesian sentences into a cleaner format for further analysis or modeling. The main preprocessing steps involved in the process are:

- Lowercasing
- Filtering
- Normalizing slang
- Stemming
- Stopword removal

In addition to the mentioned, it also includes the functionality to detect unknown words that are not present in the slang dictionary. These words are captured and stored in the `/data` directory. The purpose behind this feature is to allow manual correction and addition of these words to the slang dictionary, with the goal of improving future normalization.

TextFlow offers the following endpoints:

- `POST /normalize`: Performs normalization on the text.
- `POST /filter`: Filters out unnecessary elements from the text.
- `POST /stem`: Applies stemming to reduce words to their base form.
- `POST /slang`: Normalizes slang words present in the text.
- `POST /tokenize`: Breaks down the text into individual tokens.

Additional endpoint:
- `POST /translate/{source_lang}/{destination_lang}`: Translates text from the source language to the destination language.

## Installation

- Clone the repository: `git clone https://github.com/n4x2/textflow.git`
- Navigate to the project directory: `cd textflow`
- Install the required packages: `pip install -r requirements.txt`
- Run: `uvicorn main:app --reload`

## Usage

Here is an example of how to use the normalization endpoint of TextFlow:

```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/normalize' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "makan apa sekarang ya"
}'
```
The response from the API would be:

```json
{
  "success": true,
  "message": "Text successfully normalized",
  "data": {
    "normalized_text": "makan"
  },
  "error_code": null
}
```
In this example, the input text `"makan apa sekarang ya"` is sent to the `/normalize` endpoint. The API responds with a success message and provides the normalized text as `"makan"`.

## License

TextFlow is licensed under the Simplified BSD License. See the [LICENSE](LICENSE) file for more details.