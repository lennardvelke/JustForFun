
while(True):
    f = open("spam.txt", "r")
    a= f.read()
    f.close()
    f = open("spam.txt", "a")
    f.write(a)
    f.close()
