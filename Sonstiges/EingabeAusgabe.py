f = open("c:/temp/test.txt", "r")

text = f.read(-1)

f.close()

print(text)

