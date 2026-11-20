import string

def remove_punctuation(s):
    return ''.join(c for c in s if c not in string.punctuation)

print(remove_punctuation("Hi, world!"))
print(remove_punctuation(""))
print(remove_punctuation("a,b,c,d"))
print(remove_punctuation("..."))
