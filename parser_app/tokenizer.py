import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

nltk.download('punkt')
nltk.download('stopwords')


class Tokenizer:
    def __init__(self, corpus: str):
        self.corpus = corpus

    def tokenizer_basic(self):
        """tokenizer: Simple text tokenizer method

        Returns:
            List: List of corpus tokens with no other edits.
        """
        tokens = nltk.word_tokenize(self.corpus)

        return tokens

    def tokenizer_no_stops(self):
        """tokenizer_no_stops: Method to return a list of tokens without stopwords included

        Returns:
            List: List of corpus tokens with no other edits.
        """
        stop_word_lib = set(stopwords.words('english'))
        tokens = nltk.word_tokenize(self.corpus)

        filtered_tokens = []

        for t in tokens:
            if t not in stop_word_lib:
                filtered_tokens.append(t)

        return filtered_tokens

    def tokenize_no_punc(self):
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(self.corpus)

        return tokens
