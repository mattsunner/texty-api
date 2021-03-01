import nltk
nltk.download('punkt')


def tokenizer(corpus: str):
    """tokenizer: Simple text tokenizer method

    Args:
        corpus (str): Text corpus to be tokenized

    Returns:
        List: List of corpus tokens with no other edits.
    """
    tokens = nltk.word_tokenize(corpus)

    return tokens


if __name__ == '__main__':
    print(tokenizer('Hello there, how are you?'))
