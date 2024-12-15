"""
Problem : Given two strings, needle and haystack, identify the starting position of the first instance where needle appears within haystack. If needle does not exist in haystack, return -1.
"""
def strStr( haystack: str, needle: str) -> int:
    return haystack.find( needle )
