"""
Random password generator

Generates a random password from the command line.
"""
import argparse
import random
import string


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
    print(password)

if __name__ == '__main__':
    main()
