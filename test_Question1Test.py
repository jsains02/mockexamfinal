from Question1 import *
import pytest

def test_search():
    assert search('y',['r','t'],2) == -1

def test_search():
    assert search('y',['r','y'],2) == 1

