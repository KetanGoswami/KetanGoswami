def leet(text):
    getchar = lambda c: chars[c] if c in chars else c
    chars = {"a":"4","e":"3","l":"1","o":"0","s":"5","A":"4","E":"3","L":"1","O":"0","S":"5"}
    return ''.join(getchar(c) for c in text)

print(leet("Converted leet text!"))
print(leet("CONVERTED  LEET TEXT!"))
