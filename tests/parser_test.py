from parser_app import Lemmatizer, Tokenizer

corpus = 'This is a corpus.'

tokenizer = Tokenizer(corpus)
lemmatizer = Lemmatizer(corpus)


def test_tokenizer_basic():
    assert tokenizer.tokenizer_basic() == ['This', 'is', 'a', 'corpus', '.']


def test_tokenizer_no_stops():
    assert tokenizer.tokenizer_no_stops() == ['This', 'corpus', '.']


def test_lemmatize_text():
    assert lemmatizer.lemmatize_text() == ['corpus', '.']
