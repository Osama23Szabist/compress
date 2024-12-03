import linkList
with open ("story.txt","r",encoding='utf-8') as file:#reading text file
    text = file.read()

word = ""
listofwords = linkList.sll()
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


listofwords.print()

    