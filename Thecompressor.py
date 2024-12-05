import wordsll, time
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
            for j in range(tail.loc[0]-(len(tail.data)),tail.loc[0]):
                hold = text
                text = hold[0:j]
                text += hold[j+1:len(hold)]
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

print(len(text))
listofwords.print()#need to confirm all unwanted data is deleted or not


"""listofwords.decrese()
before_size = len(text)
less_size, text = listofwords.removeData(text)
after_size = text
if before_size-less_size == after_size:
    print("All good")
else:
    print("problem")"""



    