import linkList
with open ("story.txt","r",encoding='utf-8') as file:
    text = file.read()

word = ""
listofwords = []
wordCounter = 0

for data in text:
    if " " in data:
        if len(word) > 0:
            flag = True
            for info in listofwords:
                if info[1] in word:
                    flag = False
                    break
            if flag == True:
                listofwords.append((1,word))
            else:
                for i in range(0,len(listofwords)):
                    if listofwords[i][1] in word:
                        num = listofwords[i][0] +1
                        listofwords.remove(listofwords[i])
                        listofwords.append((num,word))
        word = ""
        wordCounter += 1
    else:
        word += data
listofwords.sort(reverse=True)


newlist = linkList.sll()

for i in range(0,len(listofwords)):
    if ((len(listofwords[i][1])*8) * listofwords[i][0]) >(len(listofwords[i][1])*8)+10:
        newlist.insert(listofwords[i])

newlist.print()
print(len(listofwords))
    