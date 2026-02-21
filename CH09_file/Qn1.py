f= open("poem.txt")
c= f.read()
if("twinkle" in c):
    print("the word twinkle is here")
else:
    print("the word twinkle isnot present")
f.close()