from linkList import dll
#we will have a new look up table for comman words

text = "hello!word"

find = text.find("!")
hold = text
text = hold[0:find]
text += hold[find+1:len(hold)]
print(text)