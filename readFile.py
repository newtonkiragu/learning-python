handle = open('test.txt','r')
handle1 = open('test.txt','r')
handle2 = open('test.txt','r')

data = handle.read() #reads the entire document
data1 = handle1.readline() #returns the first line in the keyboard
data2 = handle2.readlines() #reads multiple lines

print(data)
print('\n' + ('-*' * 30 ) + '\n')
print(data1)
print('\n' + ('-*' * 30) + '\n')
print(data2)
handle.close()