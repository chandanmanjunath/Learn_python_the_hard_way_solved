from nose.tools import *
from ex48 import parser
def test_sentence_class():
    sen=parser.Sentence(('direction','north'),('verb', 'stop'),('noun','door'))
    assert_equal(sen.subject,'north')
    assert_equal(sen.verb,'stop')
    assert_equal(sen.object,'door')

def test_peek():
    assert_equal(parser.peek([('verb','stop')]),'verb')

def test_match():
    assert_equal(parser.match([('verb','stop')],'verb'),('verb','stop'))

def test_skip():
    assert_equal(parser.skip([('verb','stop')],'verb'),('verb','stop'))

def test_parse_verb():
    assert_equal(parser.parse_verb([('verb','stop')]),('verb','stop'))

def test_parse_object():
    assert_equal(parser.parse_object([('noun','bear')]),('noun','bear'))

def test_parse_subject():
    assert_equal(parser.parse_subject([('verb','stop')]), ('noun', 'player'))

def test_parse_sentence():
    assert_equal(parser.parse_sentence([('noun','bear')]),None)
