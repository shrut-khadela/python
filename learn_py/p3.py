'''
f1 = input("enter fruit number 1:")
f2 = input("enter fruit number 2:")
f3 = input("enter fruit number 3:")
f4 = input("enter fruit number 4:")
f5 = input("enter fruit number 5:")
f6 = input("enter fruit number 6:")
f7 = input("enter fruit number 7:")

fruits = [f1,f2,f3,f4,f5,f6,f7]
print(fruits)

m1 = int(input("enter marks of subject 1:"))
m2 = int(input("enter marks of subject 2:"))
m3 = int(input("enter marks of subject 3:"))
m4 = int(input("enter marks of subject 4:"))
m5 = int(input("enter marks of subject 5:"))
m6 = int(input("enter marks of subject 6:"))

marks = [m1,m2,m3,m4,m5,m6] 
marks.sort()
print(marks)

a = [1,2,4,6]
print(a[0]+a[1]+a[2]+a[3])
print(sum(a))

A = (91,0,3,2,0,4,0)
print(A.count(0))

dict = {"hu":"me",
        "tu":"you",
        "tya":"there"}
#print(dict["hu"])
#print(dict["tya"])
print("options are:",dict.keys())
a = input("enter gujarati word:\n")
print("-->the meaning of your word is:",dict.get(a))

a = set()
a.add(1)
a.add(1.0)
a.add('1')
print(len(a))

age = int(input("enter your age:"))
if(age>=18):
    print("yes")
else:
    print("no")

n1 = int(input("enter a number:"))
n2 = int(input("enter a number:"))
n3 = int(input("enter a number:"))
n4 = int(input("enter a number:"))

if(n1>n2):
    a1=n1
else:
    a1=n2

if(n3>n4):
    a2=n3
else:
    a2=n4

if(a1>a2):
    print(a1,"is greast number")
else:
    print(a2,"is greast number")

i=1
while i<=50:
    print(i)
    i=i+1

fruit = ['mango','banana','melon','apple','orange']
i = 0
while i<len(fruit):
    print(fruit[i])
    i=i+1

for i in range(10):
    if i == 3:
        continue
    print(i)

    
# write a multplication table of given number
num = int(input("enter a number:"))
i=1
while i<11:
    # print(str(num) + "X" + str(i) + "=" +str(num*i))
    print(f"{num}X{i}={num*i}")
    i=i+1


    
# greatting to them whose name start with "s"
l1=["rahul","shrut","priyansh","shriishty"]
for names in l1:
    if names.startswith("s"):
        print("hello  " + names)


# number is prime or not
num=int(input("enter a number:"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False

if prime:
    print(num," is prime number")
else:
    print(num," is not prime number")


# factorial of given number using for loop
factorial=int(input("Enter the number"))
i = 1

for j in range(1,factorial+1):
    i *= j
print(i)

# sum of first n natural number
n = int(input("enter a number:"))
i=0
total=0
while i<=n:
    total=total + i
    i=i+1

print(total)


# miultplication table of n in reverse ordered using for loop

n=int(input("enter n:"))
for i in range(10,0,-1):
    print(f"{n}X{i}={n*i}")

# greet user using function 
def greet(name):
    print("good day, "+name)

greet("shrut")


# find greatest number using function
# n1=int(input("enter number 1:"))
# n2=int(input("enter number 2:"))
# n3=int(input("enter number 3:"))

def great(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    else:
        if n2>n3:
            return n2  
        else:
            return n3
        
m=great(2,3,1)
print("maximum number is:",+m)


# calculate sum of first n natural number using function 
def calc(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

a=calc(5)
print("sum of n is:",+a)
        #    OR 
        # using recursion function method
def s(n):
    if n==0:
        return 0
    else:
        return n+s(n-1)

a=s(0)
print("sum=",+a)


# convert inches to cm using function 
def con(inc):
    return(inc*2.54)
a=con(5)
print(a)


# open a txt file 
o=open('demo.txt','r')
data=o.read( )
print(data)
o.close()


# write in a text file  
f=open("demo.txt","w")
f.write("i am writing")
f.close()
# f=open("demo.txt","r")
# data=f.read()
# print(data)
# f.close()

def game():
    return 886
score=game()

with open("hiscore.txt","r") as a:
    hiscore=a.read()
if hiscore=='':
    with open("hiscore.txt","w") as a:
        a.write(str(score)) 
elif score>int(hiscore):
    with open("hiscore.txt","w") as a:
        a.write(str(score))


# write mul.. table of 1-20 in different files 
for i in range(2,21):
    with open(f"table/multplication of {i}","w")as f:
        for j in range(1,11): 
            f.write(f"{i} X {j} = {i*j}\n")


# replace word with another word 
with open ("sample.txt") as f:
    content = f.read()
    content = content.replace("donkey","%$#@#%@^")

with open ("sample.txt","w") as f:
    f.write(content)



# __init__ constructor 
class employee:
    def __init__(self):
        print("employee is created")
    
shrut=employee()


# class number:
#     def __init__(self,num1):
#         self.num = num1
        
#     def __add__(self,num2):
#         print("lets add")
#         return number(self.num+num2)

# num1 = number(10)
# num2 = number(20)
# A = num1 + num2
# sum(A)
# print(sum)

class number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num2):
        print("lets add")
        return self.num + num2.num 

n1=number(10)
n2=number(20)
sum=n1+n2
print(sum) 

class employee:
    salary = 10000
    increment = 1.5
    
    @property
    def salaryafter(self):
        return self.salary * self.increment

    @salaryafter.setter
    def salaryafter(self,sai):
        self.increment = sai/self.salary

e = employee()
print(e.salaryafter)

print(e.increment)
e.salaryafter = 20000
print(e.increment)




dict1 = {
    "a":"hello",
    2:"kuku2323"
}
print("this is my dictionary:",dict1.get("b","default"))

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)
print(type([1, 2, 3]) is type([1, 2, 3]))


picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]
# pixel == 1

for row in picture:  # name as readable/rememberable as possible
    for i in row: 
        # if pixel == 0:  #you can clean it
        if not i:
            print(
                " ", end=""
            )  # we need this to override the default end='\n' from the print
        else:
            print("*", end="")
    print("\n")
    

def call_me(name, age):  # <-this is parameter
    print(f"\nYou have called me {name}! of {age} age")

call_me(name='shrut',age=19)



def some_fn(*args):  # -> args stored as tuple
    return sum(args)



print("\n'args' gets stored as a tuple, Sum :", some_fn(1, 2, 3, 4, 5))
=

def some_fn(i):
    print(i)
    print(i["item1"])
    return sum(i.values())


print("\n'kwargs' contains a dictionary, Sum :", some_fn(item1=5, item2=10))


import time

time.sleep(5)
print("Printing after 5 seconds, count 1 missisiipie, 2missisipie, ...5missisipie")
time.time()  # for computer people
time.ctime()  # for non computer people


import requests
from bs4 import BeautifulSoup

url = "https://www.allsides.com/media-bias/media-bias-ratings"

headers = {
    "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

rows = soup.select("tbody tr")

# Safety check
if not rows:
    print("No rows found — website blocked or structure changed.")
    print("Preview (first 300 chars):")
    print(r.text[:300])
    exit()

row = rows[0]
print("\nRow:", row)

print("\nRetriving the data")
# $Get <td> element of '.source-title' class and get the text part from it
name = row.select_one(
    ".source-title"
).text.strip()  # .text gets all the text from the code(not the actual html code)
print("\nName (td) : ", name)

# Get the same '.source-title' 'text' html link
allsides_page = row.select_one(".source-title a")["href"]
allsides_page = "https://www.allsides.com" + allsides_page
print("It's html url : ", allsides_page)

# $Get another 'td's 'image' html link
bias = row.select_one(".views-field-field-bias-image a")["href"]
print("Bias Image link : ", bias)
bias = bias.split("/")[-1]
print("Bias Image end loc(inside server) : ", bias)





pages = [
    "https://www.allsides.com/media-bias/media-bias-ratings",
    "https://www.allsides.com/media-bias/media-bias-ratings?page=1",
]
from time import sleep
import requests
from bs4 import BeautifulSoup

all_data = []
i = 0
for page in pages:
    print("\n\nIter : ", i)
    i += 1
    r = requests.get(page)
    soup = BeautifulSoup(r.content, "html.parser")

    rows = soup.select("tbody tr")

    for row in rows:
        d = dict()

        d["name"] = row.select_one(".source-title").text.strip()
        d["allsides_page"] = (
            "https://www.allsides.com" + row.select_one(".source-title a")["href"]
        )
        d["bias"] = row.select_one(".views-field-field-bias-image a")["href"].split(
            "/"
        )[-1]
        d["agree"] = int(row.select_one(".agree").text)
        d["disagree"] = int(row.select_one(".disagree").text)
        d["agree_ratio"] = d["agree"] / d["disagree"]
        d["agreeance_text"] = get_agreeance_text(d["agree_ratio"])

        all_data.append(d)

    sleep(10)

    
all_data = []

import json

with open("allsides.json", "w") as f:
    json.dump(all_data, f)

with open("allsides.json", "r") as f:
    data2 = json.load(f)

import pandas as pd

df = pd.read_json(open("allsides.json", "r"))
df.set_index("name", inplace=True)
df.head()

df[df["agreeance_text"] == "strongly disagrees"]


# $Error handeling
while True:
    try:
        age = input("\nEnter your age : ")
        print(int(age))
    except ValueError:
        print("Please enter a number!")
        continue
    except TypeError:
        print("Please enter a correct type!")
        continue
    else:
        print("Thank you !")
        break
    finally:
        print("Ok, i'm done here")


def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print("\nProgram error : ", err)


print(sum(1, "2"))



import re

string = "this search inside of this text please!"
print(f"Search present : {'search' in string}")

# $Search using pattern
print("\nSearch using pattern")
pattern = re.compile("this")
a = pattern.search(string)  # <-returns an 'match' object
print("a : ", a)
print("a start index : ", a.start())
print("a end index : ", a.end())

print("\nFind all instances :", pattern.findall(string))
print("\n Simple match : ", pattern.match(string))
print("\n Full match : ", pattern.fullmatch(string))


# $Another common  security concern preservation with simple strings reserving the addition of tokens and its style
s = "the quick"
t = "brown fox"
print(s + t)  # combining tokens to login in the website

# hacker can know the final string and combine it any ways
s = "the "
t = "quick brown fox"
print((s + t))  # since the hacker can also reach the final point from anywhere, security is vulnerable

# quick fix -> make a tuple repr of tokkens
s = "the quick"
t = "brown fox"
print(repr((s, t))) 

# now if a hacker got all tokkens and tries to combine them to access login
s = "the "
t = "quick brown fox"
print(repr((s, t))) # he obtains a different object from before although he has all the tokens



import os

print(os.listdir("./"))  # returns list of directory names only

import glob

print(
    glob.glob("./*.py")
)  # returns all files of type specified but with it's format/path specified in the search string, just replacing the *

print()


my_file = open("text.txt")

'''
my_file = open("text.txt")
# $Analysing the cursor position
print("\nAnalysing the cursor position")
print(my_file.read())
print(my_file.read())  # <-returns nothing as the cursor has moved to the end of the file
print(my_file.read())  # <-returns nothing as the cursor has moved to the end of the file

print("\nRedirecting the cursor position")
my_file = open("text.txt")
print(my_file.read())
my_file.seek(0)
print(my_file.read())  # <-returns nothing as the cursor has moved to the end of the file

print(my_file.readline())
print(my_file.readline())

my_file.close()