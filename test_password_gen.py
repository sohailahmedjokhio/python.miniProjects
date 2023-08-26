import string

from password_gen import get_password

def test_password():
    passwd = get_password(10)
    assert len(passwd) == 10


def test_no_punctuation():
    passwd = get_password(10, False)
    for c in passwd:
        assert c not in string.punctuation

