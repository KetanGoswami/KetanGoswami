choice = input("enter choice(1/2/0):")
#input1= int(input("enter 1 to copy file in to new file: else 0:"))
#inupt2= int (input("enter 2 if you want to converted text to LEET code: else 0:"))


if  choice =='1':
 with open("Book1.txt") as f:
    with open("out.txt", "w") as f1:   # open a old file read it and  created new one with name out.txt
        for line in f:
            f1.write(line)
elif choice =='2':
 
 def leet(text):
    getchar = lambda c: chars[c] if c in chars else c
    chars = {"a":"4","e":"3","l":"1","o":"0","s":"5","A":"4","E":"3","L":"1","O":"0","S":"5"}
    return ''.join(getchar(c) for c in text)
 print(leet("Converted leet text!"))
#print(leet("CONVERTED  LEET TEXT!"))

elif choice =='0':
   print(" Thank you for your responce")
else :
   print("enter valid number for task")

