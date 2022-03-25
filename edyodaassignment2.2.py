keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v' , 'w', 'x', 'y', 'z']
values = [ 97,  98,  99,  100, 101,  102,  103, 104,105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,  117,  118,  119,  120, 121, 122 ]


dict = dict()

for i in range(len(keys)):
    dict.update({keys[i]: values[i]})
print(dict)