import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    words = words.split()


# TODO: analyze which words can follow other words
# Your code here
following = {}

for word in words:
    words[word] = []

for word in words:
    if words[word+1]:
        words[word] = words[words].append(words[word+1])

print(words)


# TODO: construct 5 random sentences
# Your code here

