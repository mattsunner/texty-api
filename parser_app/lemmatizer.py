import nltk
from nltk.stem import WordNetLemmatizer

from .tokenizer import Tokenizer

nltk.download('wordnet')


class Lemmatizer:
    def __init__(self, corpus: str):
        self.corpus = corpus

    def lemmatize_text(self):
        lemmatizer = WordNetLemmatizer()
        corpus_text = self.corpus.lower()
        tokens = Tokenizer(corpus_text).tokenizer_no_stops()

        lemma_tokens = []

        for l in tokens:
            result = lemmatizer.lemmatize(l)
            lemma_tokens.append(result)

        return lemma_tokens


if __name__ == '__main__':
    tokens = 'Rocks and Rolls are running the town'
    lemms = Lemmatizer(tokens)
    print(lemms.lemmatize_text())
