import linkList
with open ("story.txt","r",encoding='utf-8') as file:#reading text file
    text = file.read()

word = ""
listofwords = []
wordCounter = 0

for i in range(0,len(text)):#breaking it down word by word
    if " " in text[i]:
        if len(word) > 0:
            flag = True
            for info in listofwords:
                if info[1] in word:
                    flag = False
                    break
            if flag:
                listofwords.append((1,word,i))
            else:
                for k in range(0,len(listofwords)):
                    if listofwords[k][1] in word:
                        num = listofwords[k][0] +1
                        locs = listofwords[k][2]
                        if isinstance(locs, list):
                            locs.append(i)
                        else:
                            locs = locs , i
                        listofwords.remove(listofwords[k])
                        listofwords.append((num,word,locs))
        word = ""
        wordCounter += 1
    else:
        word += text[i]


newlist = linkList.sll()
listofwords.sort(reverse=True)

for i in range(0,len(listofwords)):#calci=ualting to see which word needs to be removed 
    if ((len(listofwords[i][1])*8) * listofwords[i][0]) >(len(listofwords[i][1])*8)+10:#need to refine this here
        newlist.insert(listofwords[i])

newlist.print()
print(len(listofwords))

for i in range(3102-len("Python,"),3102):#error unable to recontruct
    print(text[i])
    