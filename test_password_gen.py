import string

from password_gen import get_password_with_classes, CharClass


def test_one_each():
    char_classes = [
        CharClass(5, string.ascii_lowercase),
        CharClass(6, string.ascii_uppercase),
        CharClass(6, string.digits),
        CharClass(3, string.punctuation),
    ]
    get_password_with_classes(20, char_classes)
