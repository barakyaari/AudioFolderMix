import os
folder = r'H:\\'
counter = 1
for i in os.listdir(unicode(folder)):
    print i
    counter+=1
print counter
numbers = list(range(1, counter + 1))
from random import shuffle
print numbers
shuffle(numbers)
print numbers
counter = 0
os.chdir(folder)
for i in os.listdir(unicode(folder)):
    while i[0].isdigit() | (i[0]=='.'):
        os.rename(i, i[1:])
        i = i[1:]
    newName = str(numbers[counter]) + "." + i
    os.rename(i, newName)
    counter+=1

