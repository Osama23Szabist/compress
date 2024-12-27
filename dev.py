import wordsll, time#this is step two

prelist = []

with open("list.txt","r",encoding='utf-8') as file:
    while True:
        line = file.readline().strip()
        if line:
            if line[0:1] == "*":
                temphold = "*"
                bit = line[2:]
            else:
                temphold,bit = line.split("*")
            binary_value = int(bit, 2)
            prelist.append((temphold,bit))
        else:
            break

def char_convert_binary(word):
    binary = ''
    for data in word:
        hold = bin(ord(data))[2:]
        hold = hold.zfill(8)
        binary += hold
    return binary

with open ("story.txt","r",encoding='utf-8') as file:#reading text file
    text = file.read()

word = ""
listofwords = wordsll.word()
wordCounter = 0

for i in range(0,len(text)):#breaking it down word by word
    if " " in text[i]:
        if len(word) > 0:
            flag, Thenode = listofwords.search(word)
            if flag:
                listofwords.mod(Thenode,i)
                for data in prelist:
                    if data[0] in Thenode.data:
                        Thenode.worthit = False
                        break
            else:
                listofwords.insert(word,i)
        word = ""
        wordCounter += 1
    else:
        word += text[i]

listofwords.decrese()
listofwords.sort()
lookuptable = wordsll.word()
num = listofwords.size()
print(len(text))
for i in range(0,num):
    tail = listofwords.tail
    while tail != None:
        if len(tail.loc)>0 and tail.loc[0] > 0:
            text = text[0:tail.loc[0]-(len(tail.data))] + text[tail.loc[0]:len(text)]
            flag , thenode = lookuptable.search(tail.data)
            if flag:
                lookuptable.mod(thenode,tail.loc[0])
            else:
                lookuptable.insert(tail.data,tail.loc[0])
            tail.loc.remove(tail.loc[0])
            if len(tail.loc) == 0:
                tail.loc.append(0)
        tail = tail.pre
    listofwords.sort()

#convert to binary and repalce it
