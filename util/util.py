#coding=utf-8
import jieba
from gensim.models import KeyedVectors


def get_tokens(text):
    '''jieba分词'''
    tokens=jieba.cut(text)
    return tokens

def load_model(path):
    '''加载word2vec模型'''
    word2vec_model=KeyedVectors.load_word2vec_format(path,binary=True)
    return word2vec_model
