from flask import Flask, request, jsonify

from parser_app import Tokenizer, Lemmatizer

app = Flask(__name__)


@app.route('/tokenize', methods=['POST'])
def tokenize_text():
    """tokenize_text: API POST route to tokenize text based on token type passed in to the request body.

    Request Body Params:
        corpus: string of text to tokenize
        token_type: 'basic' or 'noStops' are the acceptable token types to pass into the request body. All other entires will yield an error.

    Returns:
        [json]: json REST response
    """
    if request.method == 'POST':
        corpus = request.form['corpus']
        token_type = request.form['token-type']

        token_object = Tokenizer(corpus)

        if token_type == 'basic':
            tokens = token_object.tokenizer_basic()

            return jsonify({'Corpus': f'{tokens}'})
        elif token_type == 'noStops':
            tokens = token_object.tokenizer_no_stops()

            return jsonify({'Corpus': f'{tokens}'})
        else:
            return jsonify({'ERROR': f'{token_type} is not a valid key.'})


@app.route('/lemmatize', methods=['POST'])
def lemmatize_text():
    if request.method == 'POST':
        corpus = request.form['corpus']

        lemma_object = Lemmatizer(corpus)
        lemma_tokens = lemma_object.lemmatize_text()

        return jsonify({'Corpus': f'{lemma_tokens}'})


if __name__ == '__main__':
    app.run(debug=True)
