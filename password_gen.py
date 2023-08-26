"""Random password generator

Generates a random password from the command line.
"""
import argparse
import random
import string

def get_password(length):
    material = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(material) for _ in range(length))
    return password


def main():
    parser = argparse.ArgumentParser('Random Password Generator')
    parser.add_argument('--length', type=int, default=8, help='random password default value (8)')
    args = parser.parse_args()

    password = get_password(args.length)

    print('Generated Password Will be:', password)

if __name__ == '__main__':
    main()

