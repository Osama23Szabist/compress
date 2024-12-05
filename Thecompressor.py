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
listofwords.print()


"""listofwords.decrese()
before_size = len(text)
less_size, text = listofwords.removeData(text)
after_size = text
if before_size-less_size == after_size:
    print("All good")
else:
    print("problem")"""



    