"""
Random password generator

Generates a random password from the command line.
"""
import argparse
import random
import string


class InvalidPasswordLengthError(Exception):
    pass


class InvalidCharClassRequired(Exception):
    pass


class CharClass:
    def __init__(self, num_required, char_class):
        self.num_required = num_required
        self.char_class = char_class


def get_password_with_classes(length, char_classes):
    total_required_length = 0
    required_material = []
    random_material = []
    for char_class in char_classes:
        char_class_required = char_class.num_required
        total_required_length += char_class_required
        if total_required_length > length:
            raise InvalidPasswordLengthError(f'total_required_length {total_required_length} exceeds length {length}')
        if char_class_required > 0:
            required_material.extend(random.choices(char_class.char_class, k=char_class_required))
        if char_class_required >= 0:
            random_material.extend(char_class.char_class)
        else:
            raise(InvalidCharClassRequired(f'Number of required character class characters ({char_class_required}) is less than zero.'))
    required_material.extend(random.choices(random_material, k=length-total_required_length))
    print(required_material)
    password = ''.join(random.sample(required_material, length))
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
