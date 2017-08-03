#!/usr/bin/env python

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    print(Colors.HEADER + 'Header....' + Colors.ENDC)
    print(Colors.OKBLUE + 'OK...' + Colors.ENDC)
    print(Colors.OKGREEN + 'OK...'+ Colors.ENDC)
    print(Colors.WARNING + 'Warning...' + Colors.ENDC)
    print(Colors.FAIL + 'Fail...' + Colors.ENDC)
    print(Colors.BOLD + 'Bold....' + Colors.ENDC)
    print(Colors.UNDERLINE + 'Underline....' + Colors.ENDC)
