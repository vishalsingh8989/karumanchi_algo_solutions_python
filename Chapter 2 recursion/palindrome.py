#!/usr/bin/python
__author__ = "Vishal Jasrotia. Stony Brook University"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = ""
__problem__ = 'NA'

import sys


def ispalindrome(string  = ""):
    if len(string) == 1 or len(string) == 0:
        return True
    else:
        return string[0] == string[-1] and ispalindrome(string[1:-1])

if __name__ == "__main__":
    print("ABC is palindrome %s"%ispalindrome("ABC"))
    print("abcba is palindrome %s"%ispalindrome("abcba"))
    print("abccba is palindrome %s"%ispalindrome("abccba"))

