"""Fetch words from given file

Usage:
    python app.py <filepath>
    import app
    app.main(<filepath>)

"""

import sys


def fetch_words(filepath):
    """
    Fetch words from given file
    :param filepath: path to file
    :type filepath: str
    :return collection of words from given file
    :rtype list[str]
    """
    with open(filepath, 'r') as file:
        return [word for line in file for word in line.split()]


def print_items(items):
    """
    Show elements from iterable
    :param items: collection of items
    :type items: iterable
    :return: Nothing
    :rtype: None
    """
    for item in items:
        print(item)


def main(filepath):
    # TODO add documentation for this function
    words = fetch_words(filepath)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # Zero-index is module name
