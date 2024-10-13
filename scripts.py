#I was extremely stuck on some of the RegEx problems, particularly lookahead/lookbehind, so I did look up a specific solution for one of them, to try to understand how it works. I think it was Regex Substitution.

# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2:
        print("Weird")
    elif n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    else:
        print ("Not Weird")

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i)

# Write a function
def is_leap(year):
    leap = False
    
    if (year%4):
        leap=False
    elif not (year%4):
        if not (year%100):
            if not (year%400):
                leap = True
            else:
                leap = False
        else:
            leap = True
    
    return leap

# Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end='')

# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    x = tuple((integer_list))
    print(hash(x))

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    solutions = [[i,j,k] for i in range(0,x+1) for j in range (0,y+1) for k in range (0,z+1) if (i+j+k != n)]
    print(solutions)

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = list(arr)
    x = sorted(x)
    first = x[-1]
    runnerup = -1000
    for i in x[::-1]:
        if i < first:
            runnerup = i
            break
    
    print(runnerup)
            

# Nested Lists
if __name__ == '__main__':
    students_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_grades.append([name, score])
    
    second_lowest = sorted(list(set([x[1] for x in students_grades])))[1]
    names = sorted([x[0] for x in students_grades if x[1]==second_lowest])
    for n in names:
        print(n)
    
    

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    print(format(sum(marks)/len(marks), ".2f"))

# Lists
if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(0,N):
        command = input().split(" ")
        func = command[0]
        if func == "sort":
            l = sorted(l)
        elif func == "pop":
            l.pop()
        elif func == "reverse":
            l.reverse()
        elif func == "print":
            print(l)
        elif func == "append":
            l.append(int(command[1]))
        elif func == "insert":
            l.insert(int(command[1]), int(command[2]))
        elif func == "remove":
            l.remove(int(command[1]))

# sWAP cASE
def swap_case(s):
    return s.swapcase()

# String Split and Join

def split_and_join(line):
    new = "-".join(line.split(" "))
    return new
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")

# Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

# Find a string
def count_substring(string, sub_string):
    n_occ = 0
    for i in range(0, len(string)):
        x = string[i:i+len(sub_string)]
        if x == sub_string:
            n_occ += 1
    return n_occ

# String Validators
if __name__ == '__main__':
    s = input()
    alphanum, digit, alpha, lower, upper = False, False, False, False, False
    for i in s:
        if i.isdigit():
            digit = True
            alphanum = True
        if i.isalpha():
            alpha = True
            alphanum = True
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
    print(("False", "True") [alphanum])
    print(("False", "True") [alpha])
    print(("False", "True") [digit])
    print(("False", "True") [lower])
    print(("False", "True") [upper])

# Text Wrap

def wrap(string, max_width):
    whole, remainder = divmod(len(string), max_width)
    parts = []
    counter = 0
    for i in range(0, len(string), max_width):
        counter += 1
        if counter > whole:
            break
        part =''.join([string[j] for j in range(i, i+max_width)])
        parts.append(part)
        
    part=''.join([string[i] for i in range(whole*max_width, len(string))])
    parts.append(part)
    final='\n'.join(parts)
    
    return final

# String Formatting
def print_formatted(number):
    #to account for '0b' and also for the single space
    padding=len(bin(number)) - 1
    for i in range(1, number+1):
      n = str(i)
      #stripping the leading character indicating the number format
      n_oct = oct(i)[2:]
      n_hex = hex(i)[2:]
      n_bin = bin(i)[2:]
      #to know the appropriate amount of padding for each number given the amount of characters, taking into account that the last digit has to be in a fixed position
      padding_deca = ''.join([" " for i in range(0,padding - len(n) - 1)])
      padding_oct =''.join([" " for i in range (0, padding - len(n_oct))])
      padding_hex =''.join([" " for i in range (0, padding - len(n_hex))])
      padding_bin =''.join([" " for i in range (0, padding - len(n_bin))])
      
      print (padding_deca + n + padding_oct + n_oct + padding_hex + n_hex.upper() + padding_bin+n_bin)
      
      
      

# Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = [int(n) for n in input().split(" ")]
n = int(input())
b = [int(n) for n in input().split(" ")]
setA, setB = set(a), set(b)
symDiff = sorted(setA.difference(setB).union(setB.difference(setA)))
for nr in symDiff:
    print (nr)

# No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
mn = [int(i) for i in input().split(" ")]
#Technically not needed
m, n = mn[0], mn[1]
#However, the array might contain duplicate elements - very sneaky hint, I was initially making this a set as well
inSet = [int(i) for i in input().split(" ")]
a = set([int(i) for i in input().split(" ")])
b = set([int(i) for i in input().split(" ")])
happiness = 0
for nr in inSet:
    if nr in a:
        happiness += 1
    elif nr in b:
        happiness -= 1
print (happiness)

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
countries = []
for i in range(0,n):
    countries.append(input())
countrySet = set(countries)
print(len(countrySet))

# Set .discard(), .remove() & .pop()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
mySet = set()
#The pop() command does not actually remove an arbitrary element in this case, it removes them from left to right. This is consistent with what the test cases expect it to do, but not with the description and the documentation. Initially, I was solving this in PyPy 3, where pop() instead removes elements from right to left in the set, making the problem unsolvable.
inputList = input().split(" ")
for i in range(0,n):
    mySet.add(int(inputList[i]))
nrCommands = int(input())
for i in range(0, nrCommands):
    command = input().split(" ")
    if command[0] == "pop":
        x = mySet.pop()
    if command[0] == "remove":
        mySet.remove(int(command[1]))
    if command[0] == "discard":
        mySet.discard(int(command[1]))
print(sum(mySet))

# Introduction to Sets
def average(array):
    distinct = set(array)
    n = len(distinct)
    return sum(distinct) / n

# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set1, set2 = set(), set()
arr1 = [int(i) for i in input().split(" ")]
for i in range(0,len(arr1)):
    set1.add(arr1[i])
m=int(input())
arr2 = [int(i) for i in input().split(" ")]
for i in range(0,len(arr2)):
    set2.add(arr2[i])
print(len(set1.union(set2)))
#n and m are not used in the for loops because the lengths of the input being passed does not actually match them in many of the text cases, causing index out of bound-exceptions

# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set1, set2 = set(), set()
arr1 = [int(i) for i in input().split(" ")]
for i in range(0,len(arr1)):
    set1.add(arr1[i])
m=int(input())
arr2 = [int(i) for i in input().split(" ")]
for i in range(0,len(arr2)):
    set2.add(arr2[i])
print(len(set1.intersection(set2)))
#n and m are not used in the for loops because the lengths of the input being passed does not actually match them in many of the text cases, causing index out of bound-exceptions

# Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set1, set2 = set(), set()
arr1 = [int(i) for i in input().split(" ")]
for i in range(0,len(arr1)):
    set1.add(arr1[i])
m=int(input())
arr2 = [int(i) for i in input().split(" ")]
for i in range(0,len(arr2)):
    set2.add(arr2[i])
print(len(set1.difference(set2)))
#n and m are not used in the for loops because the lengths of the input being passed does not actually match them in many of the text cases, causing index out of bound-exceptions

# Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set1, set2 = set(), set()
arr1 = [int(i) for i in input().split(" ")]
for i in range(0,len(arr1)):
    set1.add(arr1[i])
m=int(input())
arr2 = [int(i) for i in input().split(" ")]
for i in range(0,len(arr2)):
    set2.add(arr2[i])
print(len(set1.symmetric_difference(set2)))
#n and m are not used in the for loops because the lengths of the input being passed does not actually match them in many of the text cases, causing index out of bound-exceptions

# Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
testcases = int(input())
for i in range(0, testcases):
    n1 = int(input())
    set1 = set()
    arr1 = [int(j) for j in input().split(" ")]
    for i in range(0, n1):
        set1.add(arr1[i])
    n2 = int(input())
    set2 = set()
    arr2 = [int(j) for j in input().split(" ")]
    for i in range(0, n2):
        set2.add(arr2[i])
    
    if set1.issubset(set2):
        print("True")
    else:
        print("False")

# Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set([int(i) for i in input().split(" ")])
n = int(input())
flag = True
for i in range(0,n):
    compset = set([int(i) for i in input().split(" ")])
    if not(A > compset):
        flag = False
        break
print(flag)

# Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
numA = int(input())
A = set([int(i) for i in input().split(" ")])
numOtherSets = int(input())
for i in range(0, numOtherSets):
    line = input().split(" ")
    command = line[0]
    n_elements = int(line[1])
    B = set([int(i) for i in input().split(" ")])
    if command == "intersection_update":
        A.intersection_update(B)
    if command == "update":
        A.update(B)
    if command == "difference_update":
        A.difference_update(B)
    if command == "symmetric_difference_update":
        A.symmetric_difference_update(B)
print(sum(A))

# The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
allRoommates = [int(i) for i in input().split(" ")]
allRoomNumbers = set(allRoommates)
counts = dict()
for room in allRoomNumbers:
    counts[room] = 0
for room in allRoommates:
    counts[room] += 1
keyToPop = -9999
for key in counts.keys():
    if counts[key] == 1:
        keyToPop = key
        
counts.pop(keyToPop)
duplicates = set(counts.keys())
captain = allRoomNumbers - duplicates
print (captain.pop())

# Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
testCases = int(input())
for i in range (0, testCases):
    a, b = input().split(" ")
    try:
        print(int(a)//int(b))
        #explicit integer division because I was getting floats otherwise
    except ZeroDivisionError as z:
        #I manualy wrote the error code as it seems to have changed since the test case was written - it's now 'division by zero'
        print ("Error Code: integer division or modulo by zero")
    except ValueError as v:
        print ("Error Code:", v)

# Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar as c
date = [int(d) for d in input().split(" ")]
month, day, year = date
dayOfWeek = c.weekday(year, month, day)
match dayOfWeek:
    case 0:
        print("MONDAY")
    case 1:
        print("TUESDAY")
    case 2:
        print("WEDNESDAY")
    case 3:
        print("THURSDAY")
    case 4:
        print("FRIDAY")
    case 5:
        print("SATURDAY")
    case 6:
        print("SUNDAY")

# Time Delta
#!/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    #t1_parts = t1.split(" ")[1:]
    #t2_parts = t2.split(" ")[1:]
    #months = {"Jan" : 1, "Feb": 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug": 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
    #t1_parts[1] = months[t1_parts[1]]
    #t2_parts[1] = months[t2_parts[1]]
    #print(t1_parts, t2_parts)
    
    #abs1, abs2 = 0, 0
    #if t1_parts[-1][0] == "-":
    #    abs1 += float(t1_parts[-1][0])/60.00 * 3600
    #else:
    #    abs1 -= float(t1_parts[-1][0])/60.00 * 3600
    #if t2_parts[-1][0] == "-":
    #    abs2 += float(t2_parts[-1][0])/60.00 * 3600
    #else:
    #    abs2 -= float(t2_parts[-1][0])/60.00 * 3600
    
    #hhmmss1 = t1_parts[-2].split(":")
    #hhmmss2 = t2_parts[-2].split(":")
    
    #abs1 += int(hhmmss1[-1]) + int(hhmmss1[-2]) * 60 + int(hhmmss1[-3]) * 3600
    #abs2 += int(hhmmss2[-1]) + int(hhmmss2[-2]) * 60 + int(hhmmss2[-3]) * 3600
    
    #abs1 += (int(t1_parts[0]) - 1) * 24 * 3600
    #abs2 += (int(t2_parts[0]) - 1) * 24 * 3600
    
    ...
    #At first I was trying to do this completely by hand, but I gave up thinking there must be a much more elegant way, and luckily there is
    #I found the format codes here: https://www.programiz.com/python-programming/datetime/strptime
    #I was unfamiliar with most of the date-time specific ones until now
    date_format = '%a %d %b %Y %H:%M:%S %z'
    t1, t2 = datetime.strptime(t1, date_format), datetime.strptime(t2, date_format)
    return str(int(abs((t1-t2).total_seconds())))    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

# Map and Lambda Function
cube = lambda x: x ** 3 # complete the lambda function 
def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    fib = [0,1,1]
    for i in range(3, n):
        fib.append(fib[i-1] + fib[i-2]) 
    
    return fib[:n]
        

# Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
args = input().split(" ")
n, x = int(args[0]), int(args[1])
grades = []
for i in range(0,x):
    grades.append([float(grade) for grade in input().split(" ")])
zipped = list(zip(*grades))
for zipling in zipped:
    print(sum(zipling) / len(zipling))

# Athlete Sort
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
for athlete in (sorted(arr, key = lambda arr: arr[k])):
    athlete = list(map(str, athlete))
    print(" ".join(athlete))

# ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
ginorts = input()
lowers, uppers, evens, odds = [],[],[],[]
for i in ginorts:
    if i.islower():
        lowers.append(i)
    if i.isupper():
        uppers.append(i)
    if i.isdigit():
        if int(i) %2:
            odds.append(i)
        else:
            evens.append(i)
finalstring = sorted(lowers) + sorted(uppers) + sorted(odds) + sorted(evens)
print(''.join(finalstring))

# Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
columns = input()
Student = namedtuple('Student', columns)
students, total = [], 0
for i in range(0,n):
    line = [l for l in input().split()]
    arg0, arg1, arg2, arg3 = line[0], line[1], line[2], line[3]
    student = Student(arg0, arg1, arg2, arg3)
    total += float(student.MARKS)
print("{:.2f}".format(total/n))

# Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
supermarket = OrderedDict()
n_items = int(input())
for i in range(0,n_items):
    name, price = input().rsplit(" ", 1)
    currentKeys = list(supermarket.keys())
    if name in currentKeys:
        supermarket[name] += int(price)
    else:
        supermarket[name] = int(price)
for key, value in supermarket.items():
    print(key, value)

# Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
dq = deque()
for i in range(0,n):
    command = input().split()
    if command[0] == "append":
        dq.append(command[1])
    if command[0] == "appendleft":
        dq.appendleft(command[1])
    if command[0] == "pop":
        dq.pop() 
    if command[0] == "popleft":
        dq.popleft()
print(" ".join(list(dq)))

# collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
sizes = [int(s) for s in input().split()]
counts = Counter(sizes)
total = 0
n = int(input())
for i in range(0,n):
    size, price = map(int, input().split())
    if counts[size] > 0:
        total += price
        counts[size] -= 1
print(total)

# DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
a = defaultdict(list)
b = []
n,m = map(int, input().split())
for i in range(0,n):
    a[input()].append(str(i+1))
for i in range(0,m):
    word = input()
    b.append(word)
    #if word not in b:
        #b.append(word)
#print(b)
for word in b:
    if not a[word]:
        print(-1)
    else:
        print(" ".join(a[word]))

# Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
words = OrderedDict()
n = int(input())
for i in range(0,n):
    word = input()
    currentKeys = words.keys()
    if word not in currentKeys:
        words[word] = 1
    else:
        words[word] += 1
print(len(words.keys()))
vals = [str(v) for v in words.values()]
print(" ".join(vals))

# Company Logo
#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    counts = dict(Counter(s))
    listItems = []
    for key,value in counts.items():
        listItems.append([key,value])
    s = sorted(listItems, key= lambda x: (-x[1], x[0]))
    for i in range(0,3):
        print(s[i][0], s[i][1])
    

# Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
t = int(input())
for i in range(0,t):
    n = int(input())
    blocks = deque([int(i) for i in input().split()])
    vertical, left, right = [], blocks.popleft(), blocks.pop()
    if len(blocks) == 0:
        if len(vertical) == 0:
            print("Yes")
            continue
        else:
            if (left <= right <= vertical[-1]) or (right <= left <= vertical[-1]):
                print("Yes")
                continue
            else:
                print("No")
                continue
    if left > right:
        vertical.append(left)
        left = blocks.popleft()
    else:
        vertical.append(right)
        right = blocks.pop()
    for j in range(0, n-1):
        if left > right:
            vertical.append(left)
            if vertical[-1] > vertical[-2]:
                print("No")
                break
            if len(blocks) > 0:
                left = blocks.popleft()
        else:
            vertical.append(right)
            if vertical[-1] > vertical[-2]:
                print("No")
                break
            if len(blocks) > 0:
                right = blocks.pop()
    if len(blocks) == 1:
         block = blocks.pop()
         vertical.append(block)
    if vertical[-1] <= vertical[-2]:
        print("Yes")
    
         
     
    
    
    

# Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr, float)
    a = numpy.flip(a)
    return a

# Shape and Reshape
import numpy
_1d_array = numpy.array(list(map(int, input().split())))
_2d_array = numpy.reshape(_1d_array, (3,3))
print(_2d_array)


# Transpose and Flatten
import numpy
n, m = list(map(int, input().split()))
bigArr = []
for i in range(0,n):
    row = list(map(int, input().split()))
    bigArr.append(row)
my_array = numpy.array(bigArr)
print (numpy.transpose(my_array))
print(my_array.flatten())
        

# Concatenate
import numpy
n,m,p = list(map(int, input().split()))
top, bottom = [], []
for i in range(0,n):
    line = list(map(int, input().split()))
    top.append(line)
for i in range (0,m):
    line = list(map(int, input().split()))
    bottom.append(line)
top_array, bottom_array = numpy.array(top), numpy.array(bottom)
print (numpy.concatenate((top_array, bottom_array), axis=0))

# Zeros and Ones
import numpy
axes = list(map(int, input().split()))
print(numpy.zeros((axes), dtype = int))
print(numpy.ones((axes), dtype = int))


# Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')
n, m = list(map(int, input().split()))
print (numpy.eye(n, m, 0))


# Array Mathematics
import numpy
n, m = list(map(int, input().split()))
arrA, arrB = [], []
for i in range (0, n):
    line = list(map(int, input().split()))
    arrA.append(line)
for i in range (0, n):
    line = list(map(int, input().split()))
    arrB.append(line)
npA, npB = numpy.array(arrA, int), numpy.array(arrB, int)
print(npA + npB)
print(npA - npB)
print(npA * npB)
print(numpy.floor_divide(npA, npB))
print(npA % npB)
print(npA ** npB)

# Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy='1.13')
line = list(map(float, input().split()))
arr = numpy.array(line)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))


# Sum and Prod
import numpy
n, m = list(map(int, input().split()))
arr = []
for i in range(0,n):
    line = list(map(int, input().split()))
    arr.append(line)
a = numpy.array(arr)
a_sum = numpy.sum(a, axis=0)
print(numpy.prod(a_sum))

# Min and Max
import numpy
n, m = list(map(int, input().split()))
arr = []
for i in range(0, n):
    line = list(map(int, input().split()))
    arr.append(line)
a = numpy.min(numpy.array(arr), axis = 1)
print(numpy.max(a))


# Mean, Var, and Std
import numpy
n, m = list(map(int, input().split()))
arr = []
for i in range(0,n):
    line = list(map(int, input().split()))
    arr.append(line)
a = numpy.array(arr)
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(round(numpy.std(a, axis=None), 11))

# Dot and Cross
import numpy
n = int(input())
arr=[]
arr2=[]
for i in range(0, n):
    line = list(map(int, input().split()))
    arr.append(line)
for i in range(0, n):
    line = list(map(int, input().split()))
    arr2.append(line)
a = numpy.array(arr)
a2 = numpy.array(arr2)
print(numpy.dot(a, a2))

# Inner and Outer
import numpy
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(numpy.inner(a,b))
print(numpy.outer(a,b))

# Polynomials
import numpy
coefs = list(map(float, input().split()))
x = float(input())
poly = numpy.array(coefs)
print(numpy.polyval(poly, x))

# Linear Algebra
import numpy
n = int(input())
arr = []
for i in range(0,n):
    line = list(map(float, input().split()))
    arr.append(line)
a = numpy.array(arr)
print(round(numpy.linalg.det(a),2))

# Re.split()
regex_pattern = r"[.]|[,]"	# Do not delete 'r'.

# Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
        return [f(someone) for someone in sorted(people, key=lambda person: int(person[2]))]
    return inner

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        no_prefix = [number[-10:] for number in l]
        with_format = ["+91 " + number[0:5] + " " + number[5:10] for number in no_prefix]
        return f(with_format)
    return fun

# Birthday Cake Candles
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    # Write your code here
    occurrences, tallest = 0, 0
    for candle in candles:
        if candle == tallest:
            occurrences += 1
        if candle > tallest:
            occurrences = 1
            tallest = candle
            
    return occurrences
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

# Viral Advertising
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def viralAdvertising(n):
    # Write your code here
    received = 5
    cumulative = 0
    for i in range(0,n):
        liked = math.floor(received/2)
        received = liked*3
        cumulative += liked
    return cumulative
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Number Line Jumps
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 == v2:
        return "NO"
    if (x1-x2) % (v1-v2) == 0:
        if v1>v2:
            return "YES"
        else:
            return "NO"
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# XML 1 - Find the Score

def get_attr_number(node):
    elements = node.findall('.//')
    attributes = len(node.attrib)
    for element in elements:
        attributes += len(element.attrib)
    return attributes

# XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1
    for e in elem:
        depth(e, level+1)

# Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils
n = int(input())
emails = []
pattern = re.compile(r'[a-zA-Z]{1}[a-zA-Z0-9_.-]+@[a-zA-Z]+\.[a-z]{,3}$')
for i in range(0,n):
    emails.append([m for m in input().split()])
for mail in emails:
    mail[1] = mail[1][1:-1]
    if re.match(pattern, mail[1]):
        print (email.utils.formataddr((mail[0], mail[1])))

# Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = re.compile(r'[789][0-9]{9}$')
n = int(input())
for i in range(0,n):
    number = input()
    if re.fullmatch(pattern, number):
        print("YES")
    else:
        print("NO")

# Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = int(input())
pattern = re.compile(r'^[+.-]?[0-9]*\.[0-9]+$')
for i in range(0,t):
    line = input()
    try:
        conv = float(line)
        if re.fullmatch(pattern, line):
            print("True")
        else:
            print("False")
    except Exception:
        print("False")

# Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
line = input()
pattern1 = r'[aoeiuAOEIU]{2,}'
pattern2 = r'^[aoeiuAOEIU]{2,}'
pattern3 = r'[aoeiuAOEIU]{2,}$'
matches1 = re.findall(pattern1, line)
matches2 = re.findall(pattern2, line)
matches3 = re.findall(pattern3, line)
if len(matches1) == 0:
    print(-1)
for match in matches1:
    if match not in matches2 and match not in matches3:
        print (match)

# Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
lines = []
matches = []
for i in range(0,n):
    lines.append(input())
pattern = re.compile(r'#[0-9a-fA-F]{3,6}')
for line in lines:
    if line.endswith(";"):
        match = re.findall(pattern, line) 
        if len(match) > 0:
            for m in match:
                print(m)
        #if match is not None:
            #matches.append(match.group())
#for match in matches:
    #print(match)

# Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
result = []
def func(match):
    logical = str(match.group(0))
    if logical.startswith("&&"):
        return "and"
    else:
        return "or"
for i in range(0,n):
    line = input()
    newline = re.sub(r'(?<= )(\|\||&&)(?= )', func, line)
    print(newline)
    

# Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
creditcards = []
pattern = re.compile(r'[456][0-9]{3}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}$')
consecutive = re.compile(r'.*(\d)\1{3}.*')
for i in range(0,n):
    creditcards.append(input())
for card in creditcards:
    m1 = re.match(pattern, card)
    stripped = card.replace("-", "")
    stripped = stripped.replace(" ","")
    m2 = re.match(consecutive, stripped)
    if m1 and not m2:
        print("Valid")
    else:
        print("Invalid")

# Capitalize!

# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    out = ""
    for word in words:
        word = word.capitalize()
        out += (word + " ")
    out = out.rstrip()
    return out

# Reduce Function

def product(fracs):
    t = reduce(lambda x,y : x*y, fracs)
    return t.numerator, t.denominator

# Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    size=len(string) / k
    parts = [string[i:i+k] for i in range(0, len(string), k)]
    for part in parts:
        helper = ""
        for p in part:
            if p not in helper:
                helper += p
        print(helper)

# Text Alignment
#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = [int(a) for a in input().split()]
for i in range(0,n//2):
    j = (2*i)+1
    print(('.|.'*j).center(k,'-'))
print(('WELCOME').center(k,'-'))
for i in range(n//2 - 1, -1, -1):
    j = (2*i) + 1
    print(('.|.'*j).center(k,'-'))        

# Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
pattern = re.compile(r'([a-zA-Z0-9])\1{1}')
m = re.search(pattern, s)
if m is None:
    print (-1)
else:
    print(m.group(1))

# Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = int(input())
pattern_alphanum_10 = re.compile(r'^[a-zA-Z0-9]{10}$')
pattern_digits = re.compile(r'.*[0-9]+.*[0-9]+.*[0-9]+.*')
pattern_uppercase = re.compile(r'.*[A-Z]+.*[A-Z]+.*')
pattern_unique = re.compile(r'^(?!.*(.).*\1).+$')
patterns = [pattern_alphanum_10, pattern_digits, pattern_unique, pattern_uppercase]
for i in range(0,t):
    line = input()
    flag_valid = True
    a = pattern_alphanum_10.match(line) 
    b = pattern_digits.match(line) 
    c = pattern_uppercase.match(line) 
    d = pattern_unique.match(line) 
    if a and b and c and d:
        print("Valid")
    else:
        print("Invalid")

# Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
k = input()
raw_k = r'{}'.format(k)
pattern = re.compile(raw_k)
match = re.search(pattern, s)
if match:
    newS = s
    offset = 0
    all_finds = []
    while match and len(newS) >= len(k):
        #print('({}, {})'.format(match.start() + offset, match.end() -1 + offset))
        start_end = (match.start() + offset, match.end() -1 + offset)
        if start_end not in all_finds:
            all_finds.append(start_end)
        #print (len(newS), len(k))
        newS = newS[1:]
        offset += 1
        #print(newS)
        match = re.search(pattern, newS)
    for find in all_finds:
        print(find)
else:
    print('(-1, -1)')

# Validating Roman Numerals
regex_pattern = r"^(M{0,3})?(CD|DC{1,3}|CM|C{1,3})?(XC|XL|X{1,3}|LX{1,3})?(I{1,3}|IV|VI{1,3}|IX)?$"	# Do not delete 'r'.

# Recursive Digit Sum
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    # Write your code here
    supernumber = 0
    n = str(n)
    for i in range(1,len(n)+1):
        supernumber += int(n[-i])
    supernumber*=k
    if supernumber <= 9:
        return supernumber
    return superDigit(supernumber, 1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    # Write your code here
    newstr = [d for d in arr]
    char = arr[-1]
    for i in range(n-2,-1,-1):
        comp = arr[i]
        if char < comp:
            newstr[i+1] = comp
            print(" ".join(str(p) for p in newstr))
        elif char > comp:
            newstr[i+1] = char
            print(" ".join(str(p) for p in newstr))
            break
        if i==0 and char < comp:
            newstr[0] = char
            print(" ".join(str(p) for p in newstr))
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort2(n, arr):
    # Write your code here
    newarr = arr
    for i in range(1, n):
        for j in range(0, i, 1):
            left, right = newarr[j], newarr[i]
            if right < left:
                newarr.remove(right)
                newarr.insert(j, right)
        print(" ".join(str(p) for p in newarr))
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

# The Minion Game
def minion_game(string):
    # your code goes here
    # I solved this initially in an exhaustive brute force way that I think was functional, but got timeout errors because it had a huge execution time
    vowels, consonants  = "AOEIU", "BCDFGHJKLMNPQRSTVWXYZ"
    kevin, stuart = 0, 0
    winner = ""
    points = 0
    #if a string has length 1, it has one occurrence of all substrings, then if it has a length of 2, the second character is either a new substring or a 2nd occurrence of the first, then the 3rd character is either a new substring or belongs to a new occurrence of an existing one etc. I assume it holds true for strings of any length via induction
    for i in range(len(string) - 1, -1, -1):
        char = string[i]
        points += 1
        if char in vowels:
            kevin += points
        if char in consonants:
            stuart += points
    
    if kevin == stuart:
        print("Draw")
    
    else:
        winner = "Kevin" if kevin > stuart else "Stuart"
        print(winner, max(kevin, stuart))
    
        
    
        

# Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

# Matrix Script
#!/bin/python3
import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
def formatter(m):
    pattern = str(m.group(0))
    result = pattern[0] + " " + pattern[-1]
    return result  
transposed = ""
for j in range(0,m):
    for i in range(0,n):
        transposed += matrix[i][j]
        
pattern = re.compile(r'[a-zA-Z0-9]{1}[!@#$%& ]+[a-zA-Z0-9]{1}')
print(re.sub(pattern, formatter, transposed))

# HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        if attrs:
            for name, value in attrs:
                print("->", name, ">", value)
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        if attrs:
            for name, value in attrs:
                print("->", name, ">", value)

parser = MyHTMLParser()
n = int(input())
code = ""
for i in range (0,n):
    code += input()
parser.feed(code)

# HTML Parser - Part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print (">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    def handle_data(self, data):
        if not data == '\n':
            print (">>> Data")
            print(data)  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Detect HTML Tags, Attributes and Attribute Values
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for name, value in attrs:
                print("->", name, ">", value)
    def handle_endtag(self, tag):
        return
    def handle_data(self, data):
        return
        
    def handle_comment(self, data):
        return
parser = MyHTMLParser()
n = int(input())
code = ""
for i in range(0,n):
    code += input()
parser.feed(code)

# Alphabet Rangoli
alphabet = "abcdefghijklmnopqrstuvwxyz"
def print_rangoli(size):
    # your code goes here
    start_index = size - 1
    rangoli_list = []
    width = 4*(size-1) + 1
    for i in range(0, size):
        rangoli = ""
        end_index = start_index - i
        if start_index == end_index:
            rangoli = alphabet[start_index]
        else:
            for j in range(start_index, end_index, -1):
                rangoli+= alphabet[j]
                rangoli+= "-"
                if j - 1 == end_index:
                    rangoli += alphabet[j-1]
            reversed_part = rangoli[::-1][1:]
            rangoli += reversed_part
        rangoli_list.append(rangoli)
    for rangoli in rangoli_list:
        print((rangoli).center(width, '-'))
    rangoli_list.reverse()
    rangoli_list = rangoli_list[1:]
    for rangoli in rangoli_list:
        print((rangoli).center(width, '-'))

# Validating Email Addresses With a Filter
def fun(s):
    # return True if s is a valid email, else return False
    if "@" not in s:
        return False
    before_and_after_ = [part for part in s.split("@")]
    if len(before_and_after_) != 2:
        return False
    before, after = before_and_after_
    if before == "" or after == "":
        return False
    for c in before:
        if not (c.isalnum() or c in ["-", "_"]):
            return False
    if "." not in after:
        return False
    after_split = [part for part in after.split(".")]
    if len(after_split) != 2:
        return False
    for c in after_split[0]:
        if not c.isalnum():
            return False
    for c in after_split[1]:
        if not c.isalpha():
            return False
    if len(after_split[1]) > 3:
        return False
    return True    
    

