import string

from password_gen import get_password, get_one_each_password

def test_password():
    passwd = get_password(10)
    assert len(passwd) == 10


def test_no_punctuation():
    passwd = get_password(10, False)
    for c in passwd:
        assert c not in string.punctuation


def test_one_each():
    ascii_letter_count = 0
    digits_count = 0
    punctuation_count = 0
    passwd = get_one_each_password(10)
    for c in passwd:
        if c in string.ascii_letters:
            ascii_letter_count += 1
        elif c in string.digits:
            digits_count += 1
        elif c in string.punctuation:
            punctuation_count += 1
    assert ascii_letter_count >= 1
    assert digits_count >= 1
    assert punctuation_count >= 1
