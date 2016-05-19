# coding=utf-8
text = open("c:/temp/test.txt", "w")
zeile = raw_input('Bitte etwas reinschreiben: ')

print("Zeile hinzugefügt.")

text.read(zeile)
text.close()
