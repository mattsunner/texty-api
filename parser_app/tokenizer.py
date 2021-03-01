import nltk
from nltk.corpus import stopwords

nltk.download('punkt')


class Tokenizer:
    def __init__(self, corpus: str):
        self.corpus = corpus

    def tokenizer_basic(self):
        """tokenizer: Simple text tokenizer method

        Args:
            corpus (str): Text corpus to be tokenized

        Returns:
            List: List of corpus tokens with no other edits.
        """
        tokens = nltk.word_tokenize(self.corpus)

        return tokens


if __name__ == '__main__':
    string = 'Hello there, how are you doing?'
    token = Tokenizer(string)
    print(token.tokenizer_basic())
