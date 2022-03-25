letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v' , 'w', 'x', 'y', 'z']
print (letters)

values = [ord(x) for x in letters]
dic = dict()
for i in range (len(letters)):
    dic[letters[i]]= values[i]
print(dic)




