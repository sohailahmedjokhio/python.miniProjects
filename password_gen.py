"""
Random password generator

Generates a random password from the command line.
"""
import argparse
import random
import string


class InvalidPasswordLengthError(Exception):
    pass


def get_one_each_password(length, num_ascii_letters, num_digits, num_punctuation):
    total_required_length = num_ascii_letters + num_digits + num_punctuation
    if total_required_length > length:
        raise InvalidPasswordLengthError(f'total_required_length {total_required_length} exceeds length {length}')
    required_ascii_letters = random.choices(string.ascii_letters, k=num_ascii_letters)
    required_digits = random.choices(string.digits, k=num_digits)
    required_punctuation = random.choices(string.punctuation, k=num_punctuation)
    material = (
        random.choices(string.ascii_letters+string.digits+string.punctuation, k=length-total_required_length)
        + required_ascii_letters + required_digits + required_punctuation)
    print(material)
    password = ''.join(random.sample(material, length))
    return password


def get_password(length, use_punctuation=True):
    material = string.ascii_letters + string.digits
    if use_punctuation is True:
        material += string.punctuation
    password = ''.join(random.choice(material) for _ in range(length))
    return password


def main():
    parse = argparse.ArgumentParser(description='Random Password Generator')
    parse.add_argument('--length', type=int, default=8, help='Default value of length (8)')
    parse.add_argument('--use_punctuation', action='store_true', help='Using punctuation')
    args = parse.parse_args()
    password = get_password(args.length, args.use_punctuation)
    print('Generated password will be: ', password)


if __name__ == '__main__':
    main()
