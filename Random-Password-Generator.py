import random
letterAndNumber = 'qwertyuiopasdfghjkl;zxcvbnm,./QWERTYUIOPASDFGHKJKL:K><NCZNBMVC'

def randomCodeGenerator(length):
    if length > len(letterAndNumber):
        length = len(letterAndNumber)
    
    i = 0;
    newCode = '';
    while length > i:
        newCode += letterAndNumber[random.randrange(0,len(letterAndNumber))]
        i += 1
    return newCode
    
print(randomCodeGenerator(10));
