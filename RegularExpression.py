import string
s = "Hello there! How are you ? @jhon"
for char in string.punctuation:
    s = s.replace(char, ' ')
print(s)


import re 
s = "Hello there! How are you ? @jhon"
re.sub(r'[^\w]', ' ', s)
print(s)


a = "Hello there! How are you ? @jhon"
dir(a)
[ (....) 'partition', 'replace' (....)]
a.replace("'", " ")
print(a)