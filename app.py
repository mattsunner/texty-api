from flask import Flask, request, jsonify

from parser_app import Tokenizer, Lemmatizer

app = Flask(__name__)


@app.route('/tokenize', methods=['POST'])
def tokenize_text():
    if request.method == 'POST':
        corpus = request.form['corpus']

        token_object = Tokenizer(corpus)
        tokens = token_object.tokenizer_no_stops()

        return jsonify({'Corpus': f'{tokens}'})


@app.route('/lemmatize', methods=['POST'])
def lemmatize_text():
    if request.method == 'POST':
        corpus = request.form['corpus']

        lemma_object = Lemmatizer(corpus)
        lemma_tokens = lemma_object.lemmatize_text()

        return jsonify({'Corpus': f'{lemma_tokens}'})


if __name__ == '__main__':
    app.run(debug=True)
