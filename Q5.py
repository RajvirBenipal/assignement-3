from math import ceil
a = "ABCDEFGHIJK"

for i in range(ceil(len(a)/2)):
    print(' '*i + a[0:(len(a)-i*2)])