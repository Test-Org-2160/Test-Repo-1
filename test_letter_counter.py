import pytest
from letter_counter import count_letters

def test_for_words_pass():
    assert isinstance(count_letters("Hello"), int)  == True

def test_for_words_fail():
    assert isinstance(count_letters("Hello1234"), int)  == True

def test_for_counts():
    assert count_letters("Hello") == 5

 