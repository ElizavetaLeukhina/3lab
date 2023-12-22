string = str(input("Введите строку: "))
words = []
wordsnew = []
maxw = 0
string = string.split(' ')
for j in range(len(string)):
    words.append(string[j])
for d in range(len(words)):
    words[d] = words[d].split('\t')
    for k in range(len(words[d])):
        wordsnew.append(words[d][k])
for i in range(len(wordsnew)):
    if maxw <= len(wordsnew[i]):
        maxw = len(wordsnew[i])
        maxword = wordsnew[i]
print("Самое длинное слово из вашей строки:", maxword)