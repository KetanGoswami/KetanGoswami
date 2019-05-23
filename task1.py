#mylines = []
#with open ('Book1.txt', 'rt') as newfile: # Open Book1.txt for reading text.
#    for line in newfile:
#        mylines.append(line)              # add that line to the list.
#    for content in mylines:
#        print(content)                    # print it.

with open("Book1.txt") as f:
    with open("out.txt", "w") as f1:   # open a old file read it and  created new one with name out.txt
        for line in f:
            f1.write(line)

def leet(text):
    getchar = lambda c: chars[c] if c in chars else c
    chars = {"a":"4","e":"3","l":"1","o":"0","s":"5","A":"4","E":"3","L":"1","O":"0","S":"5"}
    return ''.join(getchar(c) for c in text)

print(leet("Converted leet text!"))
print(leet("CONVERTED  LEET TEXT!"))
