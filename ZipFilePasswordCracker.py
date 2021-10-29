import argparse
from zipfile import ZipFile


def crack(args):
    try:
        zipfile = ZipFile(args.file)
    except FileNotFoundError:
        print('Zip file not found.')

    try:
        wordlist_read = open(args.wordlist, 'r')
    except FileNotFoundError:
        print('Wordlist file not found.')

    for word in wordlist_read:
        try:
            zipfile.extractall(pwd=word)
            print(f'Zipfile Password is: {word}')
        except RuntimeError:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This tool can help in cracking password')
    parser.add_argument('-w', '--wordlist', 'Name of the Wordlist to be used')
    parser.add_argument('-f', '--file', 'Name of Zip file to crack')

    args = parser.parse_args()

    crack(args)
