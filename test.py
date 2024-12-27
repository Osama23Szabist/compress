from bitarray import bitarray
ans = "0110111001100101011101100110010101110010"
word = ""
words = []
for data in ans:
    word += data
    if len(word) >= 8:
        words.append(word)
        word = ""
print(word)
for data in words :
    num =  int(data, 2)
    print(num)
    word += chr(num)
print(word)