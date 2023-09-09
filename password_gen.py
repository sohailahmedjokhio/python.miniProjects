"""
Random password generator

Generates a random password from the command line.
"""
import argparse
import random
import string


class InvalidPasswordLengthError(Exception):
    pass


def get_one_each_password(length, required_lower, required_upper, required_digits, required_punctuation):
    total_required_length = required_lower + required_upper + required_digits + required_punctuation
    if total_required_length > length:
        raise InvalidPasswordLengthError(f'total_required_length {total_required_length} exceeds length {length}')
    # Create required material list
    required_material = []
    if required_lower > 0: 
        required_material.extend(random.choices(string.ascii_lowercase, k=required_lower))
    if required_upper > 0:
        required_material.extend(random.choices(string.ascii_uppercase, k=required_upper))
    if required_digits > 0:
        required_material.extend(random.choices(string.digits, k=required_digits))
    if required_punctuation > 0:
        required_material.extend(random.choices(string.punctuation, k=required_punctuation))
    # Create random list
    random_material = []
    if required_lower >= 0: 
        random_material.extend(random.choices(string.ascii_lowercase, k=required_lower))
    if required_upper >= 0:
        random_material.extend(random.choices(string.ascii_uppercase, k=required_upper))
    if required_digits >= 0:
        random_material.extend(random.choices(string.digits, k=required_digits))
    if required_punctuation >= 0:
        random_material.extend(random.choices(string.punctuation, k=required_lower))
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
