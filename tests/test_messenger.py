import pytest
import messenger

def test_bodyformer():
    expected = 'Hi there Alex!'
    try:
        file = open('./messenger_tests/valid_bodytest.txt')
    except IOError as e:
        print(str(e))
        assert False
    result = messenger.body_former.generate_message()
    assert expected == result