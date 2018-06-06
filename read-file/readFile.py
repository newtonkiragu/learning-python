handle = open('test.txt','r')
handle1 = open('test.txt','r')
handle2 = open('test.txt','r')
handle3 = open('test.txt','r')

data = handle.read() #reads the entire document
data1 = handle1.readline() #returns the first line in the keyboard
data2 = handle2.readlines() #reads multiple lines
data3 = handle.read() #reads the entire document
counter = 0

print(data)
print('\n' + ('-*' * 30 ) + '\n')
print(data1)
print('\n' + ('-*' * 30) + '\n')
print(data2)
for word in data.split(): 
    if word == 'python':
        counter += 1
        print(counter)

handle.close()