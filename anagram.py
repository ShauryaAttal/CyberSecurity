# string1 = "listen"
# string2 = "silent"

# string1 = sorted(string1.lower())
# string2 = sorted(string2.lower())

# print("s1: ",string1)
# print("s2: ",string2)

# if string1 == string2:
#     print("Strings are anagrams")
# else:
#     print("Strings are not anagrams")


# counter
# from collections import Counter
# def check(s1,s2):
#     print(Counter(s1))
#     print(Counter(s2))

#     if Counter(s1) == Counter(s2):
#         print("Strings are anagrams")
#     else:
#         print("Strings arent anagrams")

# string1 = "elbow"
# string2 = "below"

# check(string1.lower(),string2.lower())

from collections import defaultdict
words = ["cat","dog","tac","god","act","z"]

anagrams = defaultdict(list)

for word in words:
    anagrams[''.join(sorted(word))].append(word)

for a in anagrams.values():
    print(' '.join(a))