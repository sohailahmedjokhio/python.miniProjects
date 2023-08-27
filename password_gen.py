"""
Random password generator

Generates a random password from the command line.
"""
import argparse
import random
import string


def get_one_each_password(length, num_ascii_letters, num_digits, num_punctuation):
    material = string.ascii_letters + string.digits + string.punctuation
    one_letter = random.choice(string.ascii_letters)
    one_digit = random.choice(string.digits)
    one_punctuation = random.choice(string.punctuation)
    password = ''.join(random.choices(material, k=length-3)) + one_letter + one_digit + one_punctuation
    return ''.join(random.sample(password, k=len(password)))


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
