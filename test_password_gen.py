from password_gen import get_password


def test_password():
    passwd = get_password()
    assert len(passwd) == 8
