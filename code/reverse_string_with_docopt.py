"""
Reverse String
Reverses any input string.

Usage:
    reverse_string.py [reverse] [options]
    reverse_string.py -h | --help
    reverse_string.py -v | --verbose

Options:
    -h --help      Show this
    -v --verbose   Verbose mode
    -q --quiet     Quiet mode

"""
from docopt import docopt

def reverse(string_to_reverse):
    reversed_str = string_to_reverse[::-1]
    print(reversed_str)

if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments['reverse']:
        string_to_reverse = input('Enter the string to be reversed: ')
        reverse(string_to_reverse)
    else:
        print(arguments)
