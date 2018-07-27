### range example ###
# looping through each element in the array
for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1,10,2):
    print(i)

# creating a list with range:
newList = [i for i in range(10)]
print(newList)

# do something to each element in the list(or enumerable data type instance)
stringList = ['我', '今天', '在電機營', '學', 'python']
stringList2 = ['好', '潮']
string = ''
for element in stringList:
    string += element     
print(string)

### practice 2  Find the 20th Fibonacci Number f(20) using a for loop. Note that f(1) = f(2) = 1 ###
F_1 = 1
F_2 = 1
tmp = -1024

for i in range(18):
    tmp = F_1
    # print(tmp)
    F_1 = F_2
    print(F_1)
    F_2 = tmp + F_1
    print(F_2)

if tmp < 0:
    raise ValueError 
    
print('The 20th Fibonacci Number is {}'.format(F_2))
# using array:
fibonacciList = [1, 1]
for i in range(2, 20):
    newElement = fibonacciList[i-2] + fibonacciList[i-1]
    fibonacciList.append(newElement)
    print('New element is: {}'.format(newElement))
    print('length is:', len(fibonacciList))

### While ###
while True:
    print('我在電機營')
### practice 3 ###
operationCount = 0
x = 100
while (x != 1):
    if(x%2 == 0):
        x /= 2
    else:
        x = 3*x + 1
    operationCount += 1



###     More Python     ###

###     Dictionary      ###
d = {}
print('This is an empty dictionary {}'.format(d))
n = 123
d = {'EECAMP': 2018, 'name': '鄭人豪', 'height': 187, n: 456}
s = 'name'
d[s] = '趙崇皓'
d[height] = 183
d.setdefault('weight', '祕密不跟你說')
d['性向'] = '男性'
del d['性向'] 
d['性別'] = '男性'
d.keys()
d.values()
d.pop(123)
d[123] # an error raised here

###     Basic I/O and string      ###
print('歡迎大家參加電機營')
s = 'EEcamp 2018'
print(len(s))
for i in range(len(s)):
    print(s[i])
print(s[1:3])
s[-1] = '9' # an error raised here
print(2* s)
s = s + ' gogog!'
print(s)
print('I am {}, and I {} EEcamp so much.'.format('Andy', 'love'))
print('hello', end='-->'); print('hi', '~~~')

###     practice 4 Print a 10-level pyramid on the console.     ###

# divide each row into three parts
c1, c2, c3 = '', '*', ''
for i in range(0, 10, 1):
    c1, c3 = '', ''
    j = 10 - i
    for index in range(j):
        c1 += ' '
    for index in range(i):
        c1 += '*'
        c3 += '*' 
    print('{}{}{}'.format(c1, c2, c3))

###     Function    ###

# example: FizzBuzz     #
def FizzBuzz(x):
    if (x%3 == 0):
        if (x%15 == 0):
            print('fizzbuz')
        else:
        print('fizz')            
    elif (x%5 == 0):
        if (x%15 == 0):
            print('fizzbuz')
        else:
            print('buzz')        
    else:
        print(x)
FizzBuzz(30)

###     practice 5      ###

def reverseTheString(stringWillBeReversed):
    stringWasRversed = stringWillBeReversed[::-1]
    return stringWasRversed

def reverseTheString_stack(stringWillBeReversed):
    stringWasReversed = ''
    stringStack = []
    stringStack = list(stringWillBeReversed)
    print('initial stack state:', stringStack)
    for i in range(len(stringStack)):
        stringWasReversed += stringStack.pop()
        print('new stack state', stringStack)
    return stringWasReversed

reversedString = reverseTheString('EEcamp2018')
print(reversedString)

###     time module     ###

import time
print('Time from 1970 to now are {} seconds.'.format(time.time()))
print('Today is {}'.format(time.ctime()))
print('now: {}'.format(time.ctime())); print('after 5 seconds'); time.sleep(5); print('now: {}'.format(time.ctime()))