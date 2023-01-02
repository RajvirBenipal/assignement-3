a = input(">")                                            #input string
a = " ".join(a.split())                                #remove spaces

#count words in string
if (' ' in a):
    words = set(a.split(' '))
    for b in words: print(b, 'occurs', a.count(b), 'times')

#count letters in a word
else:
    for b in set(a): print(b, 'occurs', a.count(b), 'times')