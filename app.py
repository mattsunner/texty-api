from flask import Flask, request, jsonify

from parser_app import tokenizer

app = Flask(__name__)


@app.route('/tokenize', methods=['POST'])
def tokenize_text():
    if request.method == 'POST':
        corpus = request.form['corpus']

        tokens = tokenizer(corpus)

        return jsonify({'Corpus': f'{tokens}'})


if __name__ == '__main__':
    app.run(debug=True)
