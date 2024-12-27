import wordsll , os,linkList, gzip, time, pygame
from bitarray import bitarray

pygame.init()

masterlist = linkList.dll()

print("start time",time.ctime())


listoffiles = os.listdir(os.getcwd())

dellist =[]

for i in range(0,len(listoffiles)):
    flag = True
    if ".txt" not in listoffiles[i] or ".im.txt" in listoffiles[i] or ".gz" in listoffiles[i] or ".zip" in listoffiles[i]:
        dellist.append(listoffiles[i])
        flag = False
    if flag and os.path.isdir(listoffiles[i]):
        dellist.append(listoffiles[i])
    
for data in dellist:
    listoffiles.remove(data)

while True:
    for i in range(0,len(listoffiles)):
        print("Press:",str(i),"For",listoffiles[i])
    op = int(input())
    if op >=0 and op < len(listoffiles):
        break
    else:
        print("please pick from the options above")
        time.sleep(3)


def char_convert_binary(word,prelist):
    binary = ''
    for data in word:
        for info in prelist:
            if data == info[0]:
                binary += info[1]
    return bitarray(binary)


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
            prelist.append((temphold,bit))
        else:
            break
com = []
num = 1

with open (listoffiles[op],"r",encoding='utf-8') as file:#reading text file
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
            masterlist.insert(word)
        word = ""
        wordCounter += 1
    else:
        word += text[i]


temp = listofwords.head
while temp != None:
    for info in prelist:
        if str(temp.data) == str(info[0]):
            temp.inPreList = True
            temp.replace = info[1]           
    temp = temp.next

listofwords.prelistCheck()
listofwords.decrese()

table = listofwords.makeAtable()

temp = masterlist.head


while temp != None:
    ans, node = listofwords.search(temp.data)
    if ans:
        if node.replace != None:
            #print(node.worthit,node.inPreList)
            temp.data = bitarray(node.replace)
        else:
            print("I am screwed")
            quit()
    else:
        temp.data = char_convert_binary(temp.data,prelist)
    temp = temp.next

prediv = char_convert_binary("*",prelist)
prediv = prediv[1:]
preend = char_convert_binary("?",prelist)
preend = preend[1:]

listoffiles[op][0:-4]


with gzip.open(listoffiles[op]+".im.txt", "ab") as file:
    compressed_data = bitarray()
    temp = masterlist.head
    for info in table:
        for data in info:
            compressed_data.extend(data)
        compressed_data.extend(prediv)
    compressed_data.extend(preend)
    while temp != None:
        compressed_data.extend(temp.data)  
        temp = temp.next
    file.write(compressed_data.tobytes())


pygame.mixer.music.load("Super Mario Bros. Level Complete Soundtrack - Sound Effect for editing.mp3")
pygame.mixer.music.play()

print("All done",time.ctime())
time.sleep(20)