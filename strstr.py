#!/usr/bin/env python3

# Question:  https://www.shiyanlou.com/courses/492/labs/1624/document
# For a given source string and a target string, you should output
# the first index(from 0) of target string in source string.
# If target does not exist in source, just return -1.
#

def strstr(source, target):

    gap = len(source) - len(target)
    if(gap < 0):
        return -1

    i = 0
    while i <= gap:
        j = i
        for a in target:
            if a == source[j]:
                j += 1
            else:
                break

        # if OK
        if( j == (i + len(target))):
            return i
        else:
            i += 1

    return -1


# test program
if __name__ == '__main__':
    s1 = "source"
    t1 = "target"
    print(strstr(s1, t1))

    s2 = "abcdabcdefg"
    t2 = "bcd"
    print(strstr(s2, t2))
