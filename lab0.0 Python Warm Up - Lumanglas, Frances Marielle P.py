# Problem 0: Warm-Up Stretch

def cube(x):
    raise NotImplementedError
num=int(input("Enter num:"))
cube = num*num*num
print("The cube of is",cube,".")

def factorial(x):
    raise NotImplementedError
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
   print("Factorial:input must not be negative!")
elif num == 0:
   print("The factorial of 0 is 1.")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial,".")

def count_pattern(string, sub):

    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

pattern1 = ['a', 'b', 'c', 'e', 'b', 'a', 'b', 'f']
patternN = ['a','b']

text = ''.join(str(x) for x in pattern1)
print("Pattern 1:", text)
patternN = ''.join(str(x) for x in patternN)
print("Count the pattern:",patternN)
print("counts of pattern a,b:",text.count(patternN),"No overlapping") #for no overlappingial)
print("Total counts:",count_pattern(text, patternN))

pattern2 = ['g', 'a', 'b', 'a', 'b', 'a', 'b', 'a']
patternNN = ['a','b','a']

text = ''.join(str(x) for x in pattern2)
print("Pattern 2:", text)
patternNN = ''.join(str(x) for x in patternNN)
print("Count the pattern:",patternNN)
print("counts of pattern a,b:",text.count(patternNN),"No overlapping") #for no overlappingial)
print("Total counts:",count_pattern(text, patternNN))