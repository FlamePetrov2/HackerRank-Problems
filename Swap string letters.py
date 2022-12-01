s = 'HackerRank.com presents "Pythonist 2".'
s1=''
for letter in s:
    if letter.isupper():
        letter = letter.lower()
        s1+=letter
    else:
        letter = letter.upper()
        s1+=letter
print(s1)